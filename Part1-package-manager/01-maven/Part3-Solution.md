## Part 3: Challenge Step

### Challenge
Enhance the `maven-java-lab` project to:

1. Add a new dependency for JSON processing (e.g., `com.fasterxml.jackson.core:jackson-databind`).
2. Create a new class `JsonParser` that uses the library to parse a JSON string.
3. Write a unit test for `JsonParser`.

### Solution

1. **Update `pom.xml`**:
   ```xml
   <dependency>
       <groupId>com.fasterxml.jackson.core</groupId>
       <artifactId>jackson-databind</artifactId>
       <version>2.15.0</version>
   </dependency>
   ```

2. **Create `JsonParser.java`**:
   ```java
   package com.example;

   import com.fasterxml.jackson.databind.ObjectMapper;
   import java.io.IOException;

   public class JsonParser {
       public static String parse(String json) throws IOException {
           ObjectMapper mapper = new ObjectMapper();
           return mapper.readTree(json).toString();
       }
   }
   ```

3. **Write `JsonParserTest.java`**:
   ```java
   package com.example;

   import org.junit.jupiter.api.Test;
   import static org.junit.jupiter.api.Assertions.*;

   public class JsonParserTest {
       @Test
       void testParse() throws Exception {
           String json = "{\"key\":\"value\"}";
           assertEquals("{\"key\":\"value\"}", JsonParser.parse(json));
       }
   }
   ```

4. **Run the tests**:
   ```bash
   mvn test
   ```