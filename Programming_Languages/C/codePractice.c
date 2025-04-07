//Description: uncommentout the section you want to then comment it out again. Don't uncomment all together.

//Check Even or Odd using ternary operator:
/*#include <stdio.h>
int main() {

int a;
printf("Entre a number: ");
scanf("%d", &a);
(a%2==0)? printf("%d is an even number",a) : printf("%d is a odd number.", a);

    return 0;
}*/



//Check Even or Odd using if else:
/*#include <stdio.h>
int main() {
    int a;

    printf("Entre a number: ");
    scanf("%d", &a);

    if (a%2==0) {
        printf("%d is an even number.", a);
    } else {
        printf("%d is a odd number.", a);
    }
    return 0;
}*/



/*//even odd using goto statement:
#include <stdio.h>
#include <stdlib.h>        //for execution of exit().

int main() {
    int num;

    printf("Enter a number\n");
    scanf("%d", &num);

    if (num % 2 == 0)
        goto even;
    else
        goto odd;

even:
    printf("%d is even\n", num);
    exit(0);
odd:
    printf("%d is odd\n", num);

    return 0;
}*/



//Roots of a quadratic equation:
/*#include <stdio.h>
#include <math.h>

int main() {
    float a, b, c, d, r1, r2;

    printf("Enter the coefficients of x², x & constant term: ");
    scanf("%f %f %f", &a, &b, &c);

    if (b*b>=4*a*c) {
        d=sqrt(b*b-4*a*c);
        r1=(-b+d)/(2*a);
        r2=(-b-d)/(2*a);
        printf("Values of x are %.2f & %.2f.", r1,r2);
    } else {
        printf("Values of x are imaginary.");
    }

    return 0;
}*/



//find grade by calculating avg marks:
/*#include <stdio.h>
int main() {
    float a, b, c, d, e, f, avg = (a+b+c+d+e+f)/6;

    printf("Enter your marks: ");
    scanf("%f, %f, %f, %f, %f, %f", &a, &b, &c, &d, &e, &f);

    if (a>35 && b>35 && c>35 && d>35 && e>35 && f>35) {
        if (avg>34 && avg<50) {
            printf("your marks is %.1f and you got 3rd division.", avg);
        } else if (avg>49 && avg<60) {
            printf("your marks is %.1f and you got 2nd division.", avg);
        } else if (avg>59 && avg<75) {
            printf("your marks is %.1f and you got 1st division.", avg);
        } else if (avg>74 && avg<=100) {
            printf("your marks is %.1f and you got distinction.", avg);
        }
    } else {
        printf("You got %.1f but unfortunately you failed one(or more) subject(s), better luck next time.", avg);
    }

    return 0;
}*/



//largest num among 3 nums:
/*#include <stdio.h>

int main() {
    int a, b, c;

    printf("Enter 3 numbers: ");
    scanf("%d %d %d", &a, &b, &c);

    if (a>b && a>c) {
        printf("%d is the greater number than %d, %d", a, b, c);
    } else if (b>a && b>c) {
        printf("%d is the greater number than %d, %d", b, c, a);
    } else {
        printf("%d is the greater number than %d, %d", c, a, b);
    }

    return 0;

}*/



//Alternate Method:
/*#include <stdio.h> 
int main() {
    int a, b, c;

    printf("Enter three numbers: ");
    scanf("%d %d %d", &a, &b, &c);

    if (a>b) {
        if (a>c) {
            printf("%d is the greater number than %d, %d", a, b, c);
        } else {
            printf("%d is the greater number than %d, %d", c, a, b);
        }
    } else {
        if (b>c) {
            printf("%d is the greater number than %d, %d", b, a, c);
        } else {
            printf("%d is the greater number than %d, %d", c, a, b);
        }
    }

    return 0;
}*/



//Swap 2 numbers with using other variables:
/*#include <stdio.h>
int main() {
    int a, b;

    printf("Choose  Values of A and B: ");
    scanf("%d %d", &a, &b);

    a = a+b;
    b = a-b;
    a = a-b;
    printf("\nThe new values of A and B are: %d & %d", a, b);

    return 0;
}*/



//Print only odd numbers between a range:
/*#include <stdio.h>
int main() {
    int i, a, count = 0;

    printf("Enter the closing range (from 1 to ?): ");
    scanf("%d", &a);

    for (i=1; i<=a; i++) {
        if (i%2 == 1) {
            printf("%d\t ", i);
            count++;
        }
    }

    printf("\nTotal odd numbers between 1 to %d are %d.", a, count);
    return 0;
}*/



//calculate factorial of a number using for loop:
/*#include <stdio.h>
int main() {

    int i, n, fact = 1;
    printf("Enter the number: ");
    scanf("%d", &n);

    for (i=1; i<=n; i++)
        fact= fact*i;
    printf("Factorial of %d is %d", n,fact);

    return 0;
}*/



// Wap to print Factorial sum:
/*#include <stdio.h>
#include <math.h>
int main() {
int n, fact=1, sum=0;

printf("Enter the number of terms: ");
scanf("%d", &n);
for (int i = 1; i <= n; i++) {
    
    fact*=i;
    sum += fact;
    printf("%d\t", fact);
    }
    
    printf("\ntotal sum= %d\n", sum);
    return 0;
}*/



//print even numbers between two intervals:
/*#include <stdio.h>
int main(){

    int i, a, b;
    printf("Enter lower and upper limit: ");
    scanf("%d %d", &a, &b);

    printf("Even numbers between %d to %d are:\n", a, b);
    for (i=a; i<=b; i++) {
        if (i%2==0) {
            printf("%d\t", i);
        }
    }

    return 0;
}*/



//Print prime numbers between range:
/*#include <stdio.h>
int main() {

    int num, i, n, count;
    printf("Enter max range: ");
    scanf("%d", &n);

    for(num=1; num<=n; num++) {
        count=0;

        for(i=2;i<=num/2; i++) {
            if (num%i==0) {
                count++;
            }
        }

        if (count==0 && num!=1)
        printf("%d, ", num);
    }
    return 0;
}*/



//Calculate area of a Circle from radius:
/*#include <stdio.h>
#include<math.h>
#define PI 3.14
int main() {

    float r, area;
    printf("Enter the radius of the Circle: ");
    scanf("%f", &r);

    area = PI*r*r;
    printf("The area of the circle is %.2f", area);

    return 0;
}*/



//Temperature Conversion degree f to degree C:
/*#include <stdio.h>
int main() {

    float f, c;
    printf("Enter the temperature (in Degree F): ");
    scanf("%f", &f);

    c = 5*(f-32)/9;
    printf("%.2f degree F is equal to %.2f degree C.", f, c);

    return 0;
}*/



//Temperature Conversion with user input
/*#include <stdio.h>
int main() {
    float a, b;
    char operator;

    printf("Enter unit ('f' or 'c'): ");
    scanf("%c", &operator);

    if (operator!='f' && operator!='c') {
        printf("invalid operator");
    } else {
        printf("Enter temperature: ");
        scanf("%f", &a);
        if (operator=='f') {
            b = 5*(a-32)/9;
            printf("%f degree fahrenheit = %.2f degree centigrade.", a, b);
        } else if (operator=='c') {
            b = (9*a/5)+32;
            printf("%f degree centigrade = %.2f degree fahrenheit.", a, b);
        } else  {
            printf("invalid input.");
        }
    }

    return 0;
}*/



/*//Check Leap Year or not:
#include <stdio.h>
int main() {

    int year;
    printf("Enter year: ");
    scanf("%d", &year);

    if (year%4==0 || year%400==0 && year%100!=0)
        printf("The year %d is a Leap Year.", year);
    else
        printf("The year %d is not an Leap Year", year);

    return 0;
}*/



//Sum of digits of a number:
/*#include <stdio.h>
int main() {

    int num, sum = 0;
    printf("Enter a number: ");
    scanf("%d", &num);

    while (num > 0) {
        sum = sum + num % 10;
        num = num/10;
    }
    printf("%d", sum);

    return 0;
}*/



//Reverse the number:
/*#include <stdio.h>
int main() {

    int num, reverse_num = 0;
    printf("Enter a number: ");
    scanf("%d", &num);

    while (num > 0) {
        reverse_num = (reverse_num * 10) + num % 10;
        num = num / 10;
    }

    printf("The reversed number is: %d", reverse_num);

    return 0;
}*/



//Armstrong number:
/*#include <stdio.h>
int main() {
int z, y, x, a_sum=0;

printf("Enter a number: "); 
scanf("%d", &z);

for (y = 1; y<=z; y++) {
    x = z%10;
    a_sum += x*x*x;
    z/=10;
    
}

if (a_sum == z) {

printf("%d is a armstrong number", a_sum);

} else {
    printf("%d is a armstrong number", a_sum);
}
}*/



//WAP to print fibonacci numbers
/*#include <stdio.h>
int main() {

    int n, a=0, b=1, c=a+b, i;
    printf("Enter the number of terms:");
    scanf("%d", &n);

    printf("Fibonacci Series: %d, %d, ", a, b);
    for (i=1; i<=n; i++) {
        printf("%d, ", c);
        a=b;
        b=c;
        c=a+b;
    }

    return 0;
}*/



//find nth root of a number:
/*#include <stdio.h>
#include <math.h>
int main() {

    float n, p, q, r;
    printf("Enter a number: ");
    scanf("%f", &n);

    printf("Enter power: ");
    scanf("%f/%f", &p, &q);

    r=pow(n,(p/q));
    printf("The %.0f/%.0fth root of the number %.2f is %.3f", p, q, n, r);

    return 0;
}*/



//complex series 1
/*#include <stdio.h>
int main() {
    int n, a, sum= 0;

    printf("Choose a number: ");
    scanf("%d", &n);

    for (int i=0; i<=n; i++) {
    a = pow(n, i);
    printf("%d\t", a);
    sum += a;
    }

    // printf("\ntotal sum= %d\n", sum);
}*/


//complex series 2
/*#include <stdio.h>
int main() {
    float n, sum=0, a, b;

    printf("Choose a number: ");
    scanf("%f", &n);

    for(float i=1; i<=n; i++) {
    b= pow(n, i);
    a= b/i;
    printf("%f ", a);
    sum += a;
    }

    printf("\ntotal sum= %f\n", sum);
}*/



//pyramid pattern
/*#include <stdio.h>
int main() {
    int i,j, rows;
    printf("Enter number of rows: ");
    scanf("%d",&rows);
    for(i=0; i<=rows; i++) {
        for(j=0; j<=i; j++) {
        printf("* ");
        }
    printf("\n");
    }
    return 0;
}*/

