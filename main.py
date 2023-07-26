import asyncio
import aioxmpp

class XMPPClient(aioxmpp.Client):
    def __init__(self, jid, password):
        super().__init__(jid, aioxmpp.make_security_layer(password, no_verify=True))
        self.account = aioxmpp.Account(jid, password)
        self.client = None

    async def start(self):
        async with self.connected() as stream:
            print(f"Bienvenido, has iniciado sesión como {self.account.jid}")
            await stream.send(aioxmpp.Message(
                to=aioxmpp.JID.fromstr("amigo@alumchat.xyz"),
                body="¡Hola! Esto es un mensaje de prueba desde mi cliente XMPP."
            ))

    async def register_account(self, new_jid, new_password):
        try:
            new_jid_obj = aioxmpp.JID.fromstr(new_jid)
            self.account = aioxmpp.Account(new_jid_obj, new_password)
            register_client = aioxmpp.AccountClient(self.account)
            await register_client.register()
            print("¡Cuenta creada exitosamente!")
        except aioxmpp.errors.XMPPError as e:
            print(f"Error al crear la cuenta: {e}")

    async def login(self):
        try:
            await self.account.connect()
            print("Conexión exitosa.")
            self.client = aioxmpp.Client(self.account)
            self.client.on_stream_established.connect(self.on_stream_established)
            self.client.on_stanza_received.connect(self.on_stanza_received)
        except aioxmpp.errors.XMPPError as e:
            print(f"Error al iniciar sesión: {e}")

    async def on_stream_established(self, stream):
        await self.start()

    def on_stanza_received(self, stream, stanza):
        if isinstance(stanza, aioxmpp.Message):
            print(f"Mensaje recibido de {stanza.from_}: {stanza.body}")

if __name__ == "__main__":
    print("¡Bienvenido a la consola de chat XMPP!")
    while True:
        print("\nSelecciona una opción:")
        print("1 - Crear usuario")
        print("2 - Iniciar sesión")
        print("3 - Salir")
        option = input(">> ")

        if option == "1":
            new_jid = input("Ingresa el nuevo nombre de usuario (sin @alumchat.xyz): ")
            new_password = input("Ingresa la contraseña: ")
            xmpp_client = XMPPClient("alumchat.xyz", "")
            asyncio.run(xmpp_client.register_account(f"{new_jid}@alumchat.xyz", new_password))

        elif option == "2":
            jid = input("Ingresa tu nombre de usuario (sin @alumchat.xyz): ")
            password = input("Ingresa tu contraseña: ")
            xmpp_client = XMPPClient(f"{jid}@alumchat.xyz", password)
            asyncio.run(xmpp_client.login())

        elif option == "3":
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intenta nuevamente.")
