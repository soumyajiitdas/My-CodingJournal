import java.util.Scanner;

class rectangle {
    double length;
    double breadth;

    // Method to display length and breadth
    public static void displayDimensions(double length, double breadth) {
        System.out.println("Length: " + length);
        System.out.println("Breadth: " + breadth);
    }

    // Method to calculate the perimeter of the rectangle
    public static double calculatePerimeter(double length, double breadth) {
        return 2 * (length + breadth);
    }

    // Method to calculate the area of the rectangle
    public static double calculateArea(double length, double breadth) {
        return length * breadth;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Taking input from the user
        System.out.print("Enter the length of the rectangle: ");
        double length = scanner.nextDouble();
        System.out.print("Enter the breadth of the rectangle: ");
        double breadth = scanner.nextDouble();

        // Displaying the dimensions
        displayDimensions(length, breadth);

        // Calculating and displaying the perimeter
        double perimeter = calculatePerimeter(length, breadth);
        System.out.println("Perimeter: " + perimeter);

        // Calculating and displaying the area
        double area = calculateArea(length, breadth);
        System.out.println("Area: " + area);

        scanner.close();
    }
}
