package com.example;

public class App {
    public static void main(String[] args) throws InterruptedException {
        System.out.println("Starting application...");
        for (int i = 0; i < 50; i++) {
            System.out.println("Count: " + i);
            Thread.sleep(1000);
        }
        System.out.println("Application completed.");
    }
}