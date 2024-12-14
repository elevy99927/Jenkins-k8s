package com.example;

public class App {
    public static void main(String[] args) {
        App app = new App();
        int number = 5;
        int result = app.factorial(number);
        System.out.println("Factorial of " + number + " is: " + result);
    }

    public static void printHello() {
        System.out.println("Hello, Maven Lab!");
    }
    
    public int factorial(int n) {
        if (n < 0) {
            throw new IllegalArgumentException("Number must be non-negative");
        }
        if (n == 0 || n == 1) {
            return 1;
        }
        return n * factorial(n - 1);
    }
}
