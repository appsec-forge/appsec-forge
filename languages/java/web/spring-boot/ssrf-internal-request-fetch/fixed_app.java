import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.*;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.URI;
import java.net.URL;

@SpringBootApplication
@RestController
public class SecureApp {

    public static void main(String[] args) {
        SpringApplication.run(SecureApp.class, args);
    }

    @GetMapping("/fetch")
    public String fetchUrl(@RequestParam String url) {
        try {
            URI uri = new URI(url);

            // FIX: allow only http/https and block localhost/internal addresses
            if (!uri.getScheme().matches("http|https") ||
                uri.getHost().equals("localhost") ||
                uri.getHost().startsWith("127.")) {
                return "Blocked URL";
            }

            URL target = uri.toURL();
            BufferedReader reader = new BufferedReader(
                    new InputStreamReader(target.openStream())
            );

            StringBuilder result = new StringBuilder();
            String line;
            while ((line = reader.readLine()) != null) {
                result.append(line).append("\n");
            }

            reader.close();
            return result.toString();

        } catch (Exception e) {
            return "Error";
        }
    }
}