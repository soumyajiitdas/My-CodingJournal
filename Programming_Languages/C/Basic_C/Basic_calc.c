#include <stdio.h>
#include <math.h>

int main() {
    float num1, num2, result;
    char operator;

    // Get the user's first number
    printf("Enter a number: ");
    scanf("%f", &num1);

    // Get the user's operator
    printf("Enter an operator (+, -, *, /, ^): ");
    scanf(" %c", &operator);

    // Get the user's second number
    printf("Enter another number: ");
    scanf("%f", &num2);


    // Perform the appropriate calculation and print the result
    if (operator == '+') {
        result = num1 + num2;
        printf("%.2f %c %.2f = %.2f", num1, operator, num2, result);
    } else if (operator == '-') {
        result = num1 - num2;
        printf("%.2f %c %.2f = %.2f", num1, operator, num2, result);
    } else if (operator == '*') {
        result = num1 * num2;
        printf("%.2f %c %.2f = %.2f", num1, operator, num2, result);
    } else if (operator == '/') {
        result = num1 / num2;
        printf("%.2f %c %.2f = %.2f", num1, operator, num2, result);
    } else if (operator == '^') {
        result = pow(num1,(num2));
        printf("%.2f %c %.2f = %.2f", num1, operator, num2, result);
    } else {
        printf("Invalid operator");
    }
    return 0;
}