public class Example {
    int x; // No access modifier (Should be private)
    
    // Constructor without validation
    public Example(int x) {
        this.x = x;
    }

    // Method with potential division by zero error
    public int divide(int a, int b) {
        return a / b; // No check for division by zero
    }

    // Inefficient string concatenation in a loop
    public String repeatString(String str, int times) {
        String result = "";
        for (int i = 0; i < times; i++) {
            result += str; // Inefficient: uses immutable Strings instead of StringBuilder
        }
        return result;
    }

    // Unused method (Dead code)
    public void unusedMethod() {
        System.out.println("This method is never used");
    }

    public static void main(String[] args) {
        Example ex = new Example(10);
        System.out.println(ex.divide(10, 0)); // Runtime error: Division by zero
        
        System.out.println(ex.repeatString("Hello", 3));
    }
}
