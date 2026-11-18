import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.*;

public class Main {
    public static void main(String[] args) throws Exception {
        System.setProperty("jdk.http.auth.tunneling.disabledSchemes", "");
        Authenticator.setDefault(new Authenticator() {
            protected PasswordAuthentication getPasswordAuthentication() {
                return new PasswordAuthentication("USERNAME", "PASSWORD".toCharArray());
            }
        });
        Proxy proxy = new Proxy(Proxy.Type.HTTP, new InetSocketAddress("proxies.proxiesfood.com", 81));
        HttpURLConnection con = (HttpURLConnection) new URL("https://icanhazip.com").openConnection(proxy);
        try (BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()))) {
            System.out.println(in.readLine());
        }
    }
}
