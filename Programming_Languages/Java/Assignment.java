import java.util.Scanner;              //why i am getting orange line i don't know...

public class Assignment {
    //Average & Sum of Cube of three numbers method:
    public static void avgCube(float a, float b, float c){
        float cubeSum = (a*a*a) + (b*b*b) + (c*c*c);
        float avg = (a + b + c)/3;
        System.out.println("Average of the numbers is " + avg);
        System.out.println("Sum of cube of the numbers is " + cubeSum);
        System.out.println();
    }
    //Right_Triangle Star Pattern print method:
    public static void RightTriangle() {
        for (int i = 1; i <= 5; i++){
            for (int j = 1; j <= i; j++){
                System.out.print("* ");
            }
            System.out.println();
        }
        System.out.println();
    }
    //Invert_Right_Triangle Star Pattern print method:
    public static void invRightTriangle() {
        for (int i = 5; i >= 1; i--){
            for (int j = i; j >= 1; j--){
                System.out.print("* ");
            }
            System.out.println();
        }
        System.out.println();
    }
    //Mirrored_Right_Triangle Star Pattern print method:
    public static void mirroredRightTriangle() {
        for (int i = 1; i <= 5; i++){
            for (int j = 5; j >= i; j--){
                System.out.print("  ");
            }
            for (int k = 1; k <= i; k++){
                System.out.print("* ");
            }
            System.out.println();
        }
        System.out.println();
    }
    //Hour_Glass Star Pattern print method:
    public static void hourGlassPattern() {
        for (int i = 3; i > 1; i--){
            for (int j = i; j <= 3; j++){
                System.out.print("  ");
            }
            for (int k = i; k > 1; k-- ){
                System.out.print("* ");
            }
            for (int l = i; l >= 1; l-- ){
                System.out.print("* ");
            }
            System.out.println();
        }
        for (int i = 1; i <= 3; i++){
            for (int j = 3; j >= i; j--){
                System.out.print("  ");
            }
            for (int k = 1; k < i; k++ ){
                System.out.print("* ");
            }
            for (int l = 1; l <= i; l++ ){
                System.out.print("* ");
            }
            System.out.println();
        }
        System.out.println();
    }
    //Right_Arrow Star Pattern print method:
    public static void rightArrowPattern() {
        for (int i = 5; i > 1; i--){
            for (int j = i; j <= 5; j++){
                System.out.print("  ");
            }
            for (int k = i; k >= 1; k--){
                System.out.print("* ");
            }
            System.out.println();
        }
        for (int i = 1; i <= 5; i++){
            for (int j = 5; j >= i; j--){
                System.out.print("  ");
            }
            for (int k = 1; k <= i; k++){
                System.out.print("* ");
            }
            System.out.println();
        }
        System.out.println();
    }
    //Inverted_Right_Triangle Number pattern method:
    public static void invNumTriangle(){
        for (int i = 5; i >= 1; i--) {
            for (int j = i; j <= 5; j++){
                System.out.print("  ");
            }
            for (int k = i; k >= 1; k--){
                System.out.print(k + " ");
            }
            System.out.println();
        }
        System.out.println();
    }
    //Right Arrow Number pattern method:
    public static void numArrowPattern(){
        for (int i = 5; i > 1; i--){
            for (int j = i; j <= 5; j++){
                System.out.print("  ");
            }
            for (int k = i; k >= 1; k--){
                System.out.print(k + " ");
            }
            System.out.println();
        }
        for (int i = 1; i <= 5; i++){
            for (int j = 5; j >= i; j--){
                System.out.print("  ");
            }
            for (int k = i; k >= 1; k--){
                System.out.print(k + " ");
            }
            System.out.println();
        }
        System.out.println();
    }
    //Prime number checking method: 
    //Main Function:-
    public static void main(String[] args) {
        while (true) {
            System.out.println("\n>> List of Operations :-");
            System.out.println("1.Calculate average & sum of cube of numbers.");
            System.out.println("2.Print right triangle star pattern.");
            System.out.println("3.Print inverted right triangle star pattern.");
            System.out.println("4.Print mirrored right triangle star pattern");
            System.out.println("5.Print hour glass star pattern");
            System.out.println("6.Print right arrow star pattern");
            System.out.println("7.Print inverted right triangle number pattern.");
            System.out.println("8.Print right arrow number pattern.");
            Scanner userInput = new Scanner(System.in);
            System.out.print(">Enter between 1 to 9 to perform an operation: ");
            int key = userInput.nextInt();
            System.out.println();
            switch(key){
                case 1:
                    System.out.println(">>Average & Sum of Cube calculation of three numbers:-");
                    System.out.print("Enter the first number: ");
                    float num1 = userInput.nextFloat();
                    System.out.print("Enter the second number: ");
                    float num2 = userInput.nextFloat();
                    System.out.print("Enter the third number: ");
                    float num3 = userInput.nextFloat();
                    avgCube(num1, num2, num3);
                    break;
                case 2:
                    System.out.println(">>Right Triangle pattern of stars:-");
                    RightTriangle();
                    break;
                case 3:
                    System.out.println(">>Inverted Right Triangle pattern of stars:-");
                    invRightTriangle();
                    break;
                case 4:
                    System.out.println(">>Mirrored Right Triangle pattern of stars:-");
                    mirroredRightTriangle();
                    break;
                case 5:
                    System.out.println(">>Hour Glass pattern of stars:-");
                    hourGlassPattern();
                    break;
                case 6:
                    System.out.println(">>Right Arrow pattern of stars:-");
                    rightArrowPattern();
                    break;
                case 7:
                    System.out.println(">>Inverted Right Triangle pattern of numbers:-");
                    invNumTriangle();
                    break;
                case 8:
                    System.out.println(">>Right Arrow pattern of numbers:-");
                    numArrowPattern();
                    break;
                default:
                    System.out.println("Please enter a valid input next time.");
                    System.exit(0);
            }
            System.out.print("Do you want to perform more operation (y/n)? ");
            String answer = userInput.next();
            if (answer.equals("n")) {
                userInput.close();
                System.exit(0);
            }
        }
    }
}
