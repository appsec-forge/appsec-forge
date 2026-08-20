// Run: mvn spring-boot:run (or compile manually)

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.*;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.URL;

@SpringBootApplication
@RestController
public class VulnerableApp {

    public static void main(String[] args) {
        SpringApplication.run(VulnerableApp.class, args);
    }

    @GetMapping("/fetch")
    public String fetchUrl(@RequestParam String url) {
        StringBuilder result = new StringBuilder();
        try {
            // VULNERABLE: user-controlled URL is used directly without validation
            URL target = new URL(url);
            BufferedReader reader = new BufferedReader(
                    new InputStreamReader(target.openStream())
            );

            String line;
            while ((line = reader.readLine()) != null) {
                result.append(line).append("\n");
            }

            reader.close();
        } catch (Exception e) {
            return "Error: " + e.getMessage();
        }
        return result.toString();
    }

    // Simulated internal endpoint
    @GetMapping("/internal")
    public String internal() {
        return "SECRET_INTERNAL_DATA";
    }
}