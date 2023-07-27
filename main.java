import org.jivesoftware.smack.AbstractXMPPConnection;
import org.jivesoftware.smack.ConnectionConfiguration;
import org.jivesoftware.smack.SmackException;
import org.jivesoftware.smack.XMPPException;
import org.jivesoftware.smack.tcp.XMPPTCPConnection;
import org.jivesoftware.smack.tcp.XMPPTCPConnectionConfiguration;
import java.io.IOException;

public class XMPPClient {
    public static void main(String[] args) {
        String username = "par20117";
        String password = "Park20000721";
        String domain = "alumchat.xyz";

        // Configuración de la conexión
        XMPPTCPConnectionConfiguration config = XMPPTCPConnectionConfiguration.builder()
                .setUsernameAndPassword(username, password)
                .setXmppDomain(domain)
                .setHost("alumchat.xyz")
                .setPort(5222) // Puerto por defecto para XMPP
                .setSecurityMode(ConnectionConfiguration.SecurityMode.disabled) // Desactivar SSL/TLS para este ejemplo
                .setCompressionEnabled(false)
                .build();

        AbstractXMPPConnection connection = new XMPPTCPConnection(config);

        try {
            // Conexión al servidor
            connection.connect();
            connection.login();

            // Si todo va bien, se mostrará este mensaje de conexión exitosa
            System.out.println("Conexión exitosa al servidor XMPP");

            // Realizar las operaciones adicionales aquí después de la conexión exitosa.

            // Cerrar la conexión cuando hayas terminado de utilizarla
            connection.disconnect();
        } catch (SmackException | IOException | XMPPException e) {
            // Si hay algún error en la conexión o autenticación, se mostrará el mensaje de error
            System.out.println("Error al conectar o autenticar: " + e.getMessage());
        }
    }
}
