// Description: This file contains printing hello world to c functions including variables, data types, operators, loops, conditional statements etc. in C Language 
// Disclaimer: Do not run this file directly. First study the file properly.

#include <stdio.h> //include standered input output header file (".h")

// create a function:
void myFunction1()
{
    printf("This is a function declared in my own function named 'myFunction()'.\n");
}

void myFunction2(char personName[], int personAge)
{
    printf("%s is %d years old.\n", personName, personAge);
}

int myFunction3(int fun1, int fun2)
{
    return fun1 + fun2;
}

int main()
{
    printf("Hello World!");
    printf("I am learning C. It's quite fun.\n");
    // to start with a new line add "\n". "\n" escape character.
    printf("C language created by \'Dennis Ritchie\' in 1972.\n\n");
    // to add horizontal tab(\t), backslash(\\) & double quote(\"  \"):
    printf("The \"back slash\" is denoted by\t\"\\\".\n");

    /*Forward slash (/) is used to write a comment in C language.
    For single line comment use "//" and for multiline comment
    use "/*".*/

    // Variables:
    printf(">>Variables & Data types:\n");
    int myVer1 = 3;         // Integer. Range -32768 to +32768.
    float myVer2 = 76.879;  // Float number.
    char myVer3 = 'A';      // Character.
    myVer3 = 'B';           // over write letter 'A'.
    printf("%i\n", myVer1); // instead "%d" can be use.
    printf("%f\n", myVer2);
    printf("%c\n", myVer3);
    printf("Roll No. %d, who got %f marks, get %c grade.\n", myVer1, myVer2, myVer3);
    // First declare then assign :
    int myVer4;
    myVer4 = 42;
    myVer1 = myVer4;
    printf("%d\n", myVer1); // will give 42 instead 24.
    // copy value to empty variables :
    float myVer5;
    myVer5 = myVer2;
    printf("%f\n", myVer5); // will give 76.879

    // Sum of integers :
    int num1 = 5, num2 = 8, num3 = 9;
    printf("Sum of the integers = %d\n", num1 + num2 + num3);

    // Conversion :
    float sum1 = 5 / 2;        // Implicit (auto) conversion.
    printf("%.1f\n", sum1);    // gives 2.0
    float sum2 = (float)5 / 2; // Explicit (manual) conversion.
    printf("%.1f\n", sum2);    // gives 2.5

    // Data Type :
    // except %i or %d, %f, %c
    double verDouble = 12.999; //%lf shows upto 15 decimals. Where %f 6 to 7.
    printf("%lf\n", verDouble);
    printf("%.3lf\n", verDouble); // shows 3 digits after decimal.
    printf("%.2f\n", myVer2);     // shows 2 digits after decimal.
    char sentence[] = "I'm Soumyajit.";
    printf("%s\n", sentence); //%s used for strings.

    // Constants :
    printf(">>Constant Variables:\n");
    const int YEAR = 2003; // value can't be changed.
    // YEAR = 2004;                           //will give an error.
    printf("%d\n", YEAR); // for const variables use uppercase names.
    //'const' must be assign with a value :
    /*const int MONTH;
    MONTH = 7;
    printf("%i", MONTH)*/               // will give an Error.

    //Operators :
    //1.arithmetic operators:
    printf(">>Outputs of \'Arithmetic\'Operators:\n");
    int a=11, b=22;
    printf("%d\n", a+b);
    printf("%d\n", b-a);
    printf("%d\n", a*b);                  //Multiplication.
    printf("%d\n", b/a);                 //Division.
    printf("%d\n", b%a);                //Modulus.
    printf("%d\n", ++a);               //increment (add +1).
    printf("%d\n", --a);              //decrement (add -1).

    //2.assignment operators:
    printf(">>Outputs of \'Assignment\'Operators:\n");
    int c=10, d=20, e=30, f=40, g=45, h=50, i=60, j=70;
    printf("%d\n", c);                            //use to assign values.
    printf("%d\n", c+=10);                       //returns c = c+10.
    printf("%d\n", d-=10);                      //returns d = d-10.
    printf("%d\n", e*=10);                     //returns e = e*10.
    printf("%d\n", f/=10);                    //returns f = f/10.
    printf("%d\n", g%=10);                   //returns g = g%10.
    printf("%d\n", h&=10);                  //returns h = h&10.
    printf("%d\n", i|=10);                 //returns i = i|10.
    printf("%d\n", j^=2);                 //returns j = j^2.
    int k=80, l=90;
    printf("%d\n", k>>=l);          //returns...
    printf("%d\n", l<<=k);         //returns ...

    //3.comparison operators:
    printf(">>Outputs of \'Comparison\'Operators:\n");
    int m, n, o;
    m = n = 20, o = 40;           //assign & declare simultaneously doesn't work.
    printf("%d\n", m==n);        //returns 1 for true & 0 for false.
    printf("%d\n", m!=o);
    printf("%d\n", m>o);
    printf("%d\n", m<n);
    printf("%d\n", m<=o);
    printf("%d\n", m>=n);

    //4.logical operators:
    printf(">>Outputs of \'Logical\'Operators:\n");
    int p=6, q=9;
    printf("%d\n", p<8 && q<8);         //returns 1 if both are true.
    printf("%d\n", p!=5 || p>q);       //returns 1 if one of them is true.
    printf("%d\n", !(p<8 && q>8));    //reverse the result.

    //5.sizeof operators:    //returns memory size (in bytes) of a data type or variable.
    printf(">>Outputs of \'Sizeof\'Operators:\n");
    int myInt;
    float myFloat;
    double myDouble;
    char myChar;
    printf("%lu\n", sizeof(myInt));
    printf("%lu\n", sizeof(myFloat));
    printf("%lu\n", sizeof(myDouble));
    printf("%lu\n", sizeof(myChar));


    //If...Else Statement:
    int myNum = 10;             //the curly braces are not mandatory but recommended.
    if (myNum > 0) {
        printf("The value is a positive number.\n");
    } else if (myNum < 0) {
        printf("The value is a negative number.\n");
    } else {
        printf("The value is 0.\n");
    }
    //Short Hand If...Else (Ternary Operator):
    int time = 20;
    (time < 18) ? printf("Good day.\n") : printf("Good evening.\n");

    //'switch' statement:
    int day = 4;
    switch (day) {
    case 6:
        printf("Today is Saturday\n");
        break;                           //'break' keyword breaks out of the switch block.
    case 7:
        printf("Today is Sunday\n");
        break;
    default:                                          //'default' statement is optional.
        printf("Looking forward to the Weekend.\n");
    }

    //While loop:
    printf(">>Print 0 to 3 using while loop:\n");
    int a1 = 0;
    while (a1 < 4) {
        printf(" %d, ", a1);
        a1++;
    }
    //Do/while loop:
    printf("\n>>Print 4 to 9 using do/while loop:\n");
    int a2 = 4;
    do {
        printf(" %d, ", a2);
        a2++;
    }
    while (a2 < 10);

    //For loop:
    printf(">>Even numbers from 0 to 10:\n");
    int a3;
    for (a3 = 0; a3 <= 10; a3 = a3 + 2) {
        printf(" %d, ", a3);
    }

    //Break & Continue:
    //'break' statement can also be used to jump out of a loop:
    printf("\n>>This only prints from 0 to 5:\n");
    int a4;
    for (a4 = 0; a4 < 10; a4++) {
        if (a4 == 5) {
        break;
        }
        printf(" %d, ", a4);            //break at a4=5.
    }
    //'continue' statement breaks one iteration in the loop.
    printf("\n>>This prints from 0 to 10 except 5:\n");
    int a5;
    for (a5 = 0; a5 < 10; a5++) {
        if (a5 == 5) {
        continue;
        }
        printf(" %d, ", a5);           //skip a5=5.
    }
    //Break and Continue in While Loop:
    printf("\n>>'break' output in while loop:\n");
    int a6 = 0;
    while (a6 < 10) {
        if (a6 == 5) {
        break;
        }
        printf(" %d, ", a6);            //break at a6=5.
        a6++;
    }
    printf("\n>>'continue' output in while loop:\n");
    int a7 = 0;
    while (a7 < 10) {
        if (a7 == 5) {
        a7++;
        continue;
        }
        printf(" %d, ", a7);            //skip a7=5.
        a7++;
    }


    //Arrays:
    printf("\n>>Arrays Operations:\n");
    int myYears[] = {2003, 2019, 2021, 2023};
    printf("%d\n", myYears[1]);                      //access element.
    myYears[0] = 2002;
    printf("%d\n", myYears[0]);                      //returns 2002 instead 2003.
    //loop through array:
    printf(">>loop through array:\n");
    int b1;
    for (b1 = 0; b1 < 4; b1++) {
        printf(" %d, ", myYears[b1]);
    }
    //Set array size:
    // Declare an array of four integers:
    printf("\n>>Array setting: ");
    int myWeeks[4];
    // Add elements to it
    myWeeks[0] = 5;
    myWeeks[1] = 4;
    myWeeks[2] = 3;
    myWeeks[3] = 2;
    printf("%d\n", myWeeks[0]);


    //Strings:
    printf(">>String operations:\n");
    char greetings1[] = "My name is Soumyajit.";
    printf("%s\n", greetings1);                       //print string.
    printf("%c\n", greetings1[11]);                  //first character is 0 in a string.
    //modify strings:                               //'%c' prints letter & '%s' entire string.
    greetings1[16] = 'o';
    printf("%s\n", greetings1);                   //replace 'a' of 'Soumyajit' with 'o'.
    //Creat string in alternate way:
    printf(">>Another Way Of Creating Strings:\n");
    char greetings2[] = {'H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '!', '\0'};
    printf("%s", greetings2);           //'\0' is 'null terminating character'. It declares end of a string.
    //Difference:
    printf("\n>>The memory size of two ways of creating strings:\n");
    char greetings3[] = "Hello World!";
    printf("%lu\n", sizeof(greetings2));
    printf("%lu\n", sizeof(greetings3));                                //both output same.



    //User input:
    printf(">>To get user input use 'scanf()' function:\n");
    float userNum1, userNum2, sumResult;                                //create int variable.
    printf("Type a number: ");                                         //ask user for input.
    scanf("%f", &userNum1);                                           //get & save the user input.
    printf("Type another number: ");
    scanf("%f", &userNum2);                   //'&VariableName' is the reference operator, which stores the memory address.
    sumResult = userNum1 + userNum2;
    printf("Output - The sum of %.2f & %.2f is : %.2f\n", userNum1, userNum2, sumResult);        //output the result.

    //User input String:
    printf(">>String as a user input:");
    char userStr1[20], userStr2[10];        //create char variable. Values (after variable name) indicates the size of the String.
    printf("Enter your first name: ");          //ask user for input.
    scanf("%s", &userStr1);                    //get & save the text.
    printf("District: ");
    scanf("%s", &userStr2);
    printf("Output - %s is a good person, he lives in %s.\n", userStr1, userStr2);            //output the text.


    //Memory Address:
    printf(">>The memory address is the location of where the variable is stored on the computer. When we assign a value to the variable, it is stored in this memory address. This address prints in 'hexadecimal form'.\n>Example:- ");
    printf("%p is the memory address of your entered name.\n", &userStr1);

    //Pointers:
    printf(">>A pointer is a variable that stores the memory address of another variable as its value. A pointer variable points to a data type (like int) of the same type, and is created with the '* operator'.\n");
    int myAge = 20;                                               // An int variable
    int* ptr = &myAge;                                           // A pointer variable, with the name ptr, that stores the address of myAge. '*' is called dereference operator.
    //Output the value of myAge:
    printf("%d\n", myAge);
    //Output the memory address of myAge:
    printf("%p\n", &myAge);                                  //In this example '&myAge' is a pointer & '&' is a reference operator.
    //Reference: Output the memory address of myAge with the pointer:
    printf("%p\n", ptr);

    //Dereference:
    printf(">>We can also get the value of the variable the pointer points to, by using the 'dereference ('*') operator':\n");
    // Dereference: Output the value of myAge with the pointer:
    printf("%d\n", *ptr);

    // Functions:
    printf(">>A function is a block of code which only runs when it is called.");
    // Predefine Functions:
    printf("\'main()\', \'printf()\' these are the predefine functions.\n");
    printf(">>A function was previously created. The output of the function is:\n");
    myFunction1(); // call the function.
    printf(">>A function can be called multiple times.\nExample:- ");
    myFunction1(); // previously called function.

    // Function Parameters:
    printf(">>Information can be passed to functions as a parameter. Parameters act as variables inside the function. Example:-\n");
    myFunction2("Jenny", 18);
    myFunction2("Lisa", 16);

    // Return Values:
    printf(">>The void keyword, used in the previous examples, indicates that the function should not return a value. Example of a function which have return value:\n");
    printf("Result is: %d\n", myFunction3(5, 8)); // output (5 + 8)
    printf("The result in a variable can also be stored.\n");
    int res = myFunction3(12, 20);
    printf("Result = %d", res);

    return 0;
}

