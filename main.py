import asyncio
import aioxmpp

async def on_connected(stream):
    print("Conectado correctamente.")
    await stream.close()

async def on_failure(stream, error):
    print("Error de autenticación:", error)
    await stream.close()

async def main():
    jid = aioxmpp.JID.fromstr("par20117@alumchat.xyz")
    password = "Park20000721"

    client = aioxmpp.PresenceManagedClient(jid, password)
    client.on_stream_established.connect(on_connected)
    client.on_failure.connect(on_failure)

    try:
        async with client.connected():
            await asyncio.Event().wait()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    asyncio.run(main())
