package com.example.library;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.HashMap;
import java.util.Optional;

/**
 * A sample library management system to test code analysis
 */
public class LibraryManagementSystem {
    // This constant doesn't follow proper naming convention
    private static final String defaultStatus = "AVAILABLE";
    
    private Map<String, Book> bookInventory;
    private List<Member> members;
    
    // Constructor with overly complex initialization
    public LibraryManagementSystem() {
        this.bookInventory = new HashMap<>();
        this.members = new ArrayList<>();
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 5; j++) {
                String id = "BOOK" + i + j;
                Book book = new Book(id, "Sample Book " + (i * 5 + j));
                this.bookInventory.put(id, book);
            }
        }
    }
    
    // Method with high cyclomatic complexity
    public boolean ProcessBookReturn(String bookId, String memberId) {
        if (bookId == null || memberId == null) {
            return false;
        }
        
        Book book = bookInventory.get(bookId);
        if (book == null) {
            return false;
        }
        
        Member member = findMember(memberId);
        if (member == null) {
            return false;
        }
        
        if (!book.isCheckedOut()) {
            return false;
        }
        
        if (!book.getCurrentBorrower().equals(memberId)) {
            return false;
        }
        
        if (book.hasLateFees()) {
            if (!member.hasSufficientBalance()) {
                return false;
            }
            member.deductLateFees(book.calculateLateFees());
        }
        
        book.returnBook();
        return true;
    }
    
    // Method with poor exception handling
    public void addNewBook(Book book) {
        try {
            validateBook(book);
            bookInventory.put(book.getId(), book);
        } catch (Exception e) {
            // Bad practice: catching generic exception
            System.out.println("Error adding book: " + e.getMessage());
        }
    }
    
    // Duplicate code block
    private Member findMember(String memberId) {
        for (Member member : members) {
            if (member.getId().equals(memberId)) {
                return member;
            }
        }
        return null;
    }
    
    // Another method with similar duplicate code
    private Book findBook(String bookId) {
        for (Book book : bookInventory.values()) {
            if (book.getId().equals(bookId)) {
                return book;
            }
        }
        return null;
    }
    
    // Class with too many public methods
    public class Book {
        private String id;
        private String title;
        private String status;
        private String currentBorrower;
        private double lateFees;
        
        public Book(String id, String title) {
            this.id = id;
            this.title = title;
            this.status = defaultStatus;
        }
        
        public String getId() { return id; }
        public String getTitle() { return title; }
        public String getStatus() { return status; }
        public String getCurrentBorrower() { return currentBorrower; }
        public double getLateFees() { return lateFees; }
        public void setId(String id) { this.id = id; }
        public void setTitle(String title) { this.title = title; }
        public void setStatus(String status) { this.status = status; }
        public void setCurrentBorrower(String borrower) { this.currentBorrower = borrower; }
        public void setLateFees(double fees) { this.lateFees = fees; }
        public boolean isCheckedOut() { return status.equals("CHECKED_OUT"); }
        public boolean hasLateFees() { return lateFees > 0; }
        public double calculateLateFees() { return lateFees; }
        public void returnBook() { 
            this.status = defaultStatus;
            this.currentBorrower = null;
        }
    }
    
    private class Member {
        private String id;
        private double balance;
        
        public String getId() { return id; }
        public boolean hasSufficientBalance() { return balance > 0; }
        public void deductLateFees(double fees) { balance -= fees; }
    }
}
