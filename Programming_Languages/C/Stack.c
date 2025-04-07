#include <stdio.h>
int MAXSIZE = 5;
int top = -1;

//display the stack
void display(int stack[]) {
    if (top == -1) {
        printf("Stack underflow\n");
    }
    for(int i = 0; i < MAXSIZE; i++) {
        printf("%d ", stack[i]);
    }
}
/* Function to insert into the stack */
int push(int stack[], int val) {
    if(top == MAXSIZE - 1) {
        printf("Could not insert data, Stack is full.\n");
    } else {
        top = top + 1;
        stack[top] = val;
    }
}

int pop(int stack[]) {
    if (top == -1) {
        printf("Could not pop data, Stack is empty.\n");
        return -1;
    } else {
        int val = stack[top];
        top = top - 1;
        return val;
    }

}

/* Main function */
int main() {
    // printf("Enter the stack size:");
    // scanf("%d", &MAXSIZE);
    int stack[MAXSIZE];
    // int val;
    // printf("Enter the value:");
    // scanf("%d", &val);
    push(stack, 66);
    push(stack, 10);
    push(stack, 62);
    push(stack, 123);
    push(stack, 15);

    printf("Stack Elements: \n");
    display(stack);
    
    pop(stack);
    printf("\nStack Elements: \n");
    display(stack);

    return 0;
}