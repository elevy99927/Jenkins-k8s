package com.example;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;


public class AppTest {
    @Test
    void testFactorial() {
        App app = new App();
        assertEquals(1, app.factorial(0));
        assertEquals(1, app.factorial(1));
        assertEquals(2, app.factorial(2));
        assertEquals(6, app.factorial(3));
        assertEquals(120, app.factorial(5));
    }

    @Test
    void testFactorialNegative() {
        App app = new App();
        Exception exception = assertThrows(IllegalArgumentException.class, () -> {
            app.factorial(-1);
        });
        assertEquals("Number must be non-negative", exception.getMessage());
    }
}
