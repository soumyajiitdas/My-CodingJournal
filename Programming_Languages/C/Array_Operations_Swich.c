#include <stdio.h>
#include <math.h>

//Function for reading values of array:
void create_array(int a[], int n) {
    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }
}


//Function for display array:
void display_array(int a[], int n) {
    for (int i = 0; i < n; i++) {
        printf("a[%d] = %d\n", i, a[i]);
    }
}


//Function for insert an element:
int insert_element(int a[], int n, int loc, int val) {
    for (int i = n; i >= loc; i--) {
        a[i] = a[i-1];
    }
    a[loc] = val;
}


//Function for delete an element:
void delete_element(int a[], int n, int loc) {
    for (int i = loc; i < n; i++) {
        a[i] = a[i+1];
    }
}


// Function for linear search:
int linear_search(int a[], int n, int key) {
    int found = 0;
    for (int i = 0; i < n; i++) {
        if (a[i] == key) {
            found = 1;
            return i;                                                                                  // Returns index of the key.
        }
    }
    if (found == 0) {
        return -1;
    }                                                                                                  // Returns -1 if the key was not found.
}


// Function for binary search (requires sorted array):
int binary_search(int a[], int key, int lb, int ub) {
    int found = 0;
    if (lb<ub) {
        int mid = floor((lb+ub)/2);
        if (key == a[mid]) {
            found = 1;
            return mid;                                                                                // Returns the index where the key was found.
        }
        if (key < a[mid]) {
            return binary_search(a, key, lb, mid-1);
        } else if (key > a[mid]) {
            return binary_search(a, key, mid+1, ub);
        }
    }
    if (lb > ub && found == 0) {
        return -1;                                                                                      // Returns -1 if the key was not found.
    }                                
}


//Bubble Sort of an Array:
void bubbleSort(int a[], int n) {
    for (int i = 0; i < n-1; i++) {
        int flag = 0;
        for (int j = 0; j < n-i-1; j++) {
            if (a[j] > a[j+1]) {
                int temp = a[j];
                a[j] = a[j+1];
                a[j+1] = temp;
                flag = 1;
            }
        }
        if (flag == 0) {
            break;
        }
    }
}


//Insertion Sort of an Array:
void insertionSort(int a[], int n) {
    int i, temp, j;
    for (i = 1; i < n; i++) {
        temp = a[i];
        j = i-1;
    while (temp < a[j] && j >= 0) {
        a[j+1] = a[j];
        j = j-1; 
    }
    a[j+1] = temp;
    }
}


//Main Function:
int main() {
    int n, choice;

    printf(">Enter the size of the array: ");
    scanf("%d", &n);
    
    int a[n];
    printf(">Enter %d elements:\n", n);
    create_array(a, n);                                                      //called create_array function.
    printf("\n>Your entered array is:\n");
    display_array(a, n);                                                    //called display_array function.


    do {
        //menu for operations:
            printf("\n>Select the operations:\n");
            printf("1. Insert Element.\n");
            printf("2. Delete Element.\n");
            printf("3. Bubble Sort.\n");
            printf("4. Insertion Sort.\n");
            printf("5. Linear Search.\n");
            printf("6. Binary Search (Shorting required).\n");
            printf("7. Exit.\n");
            printf(">Choose between 1 to 7: ");
            scanf("%d", &choice);


        int loc, val;
        int lb = 0, ub = n - 1, key;
        int index = -1, flag = 0;


        switch (choice) {

            //swich case for insert_element function-
            case 1:
                printf("\n>Enter the the value of the new element: ");
                scanf("%d", &val);
                printf(">Enter the the index of the new element: ");
                scanf("%d", &loc);
                if (loc > n || loc < 0) {
                    printf("\nInvalid input. Enter index between 0 to %d.\n", n);
                } else {
                     a[n+1] = insert_element(a, n, loc, val);                                           //called the insert_element function
                    printf("\n>After insertion, new updated array is:\n");
                    n = n + 1;
                    display_array(a, n);                                                              //called the display_array function.
                }
                break;

            //swich case for delete_element function-
            case 2:
                printf("\n>Enter the the index of the element: ");
                scanf("%d", &loc);
                if (loc >= n || loc < 0) {
                    printf("\nInvalid input. Enter index between 0 to %d.\n", n-1);
                } else {
                    delete_element(a, n, loc);                                                                 //called the delete_element function
                    printf("\n>After deletion, new updated array is:\n");
                    n = n - 1;
                    display_array(a, n);                                                                   //called the display_array function.
                }
                break;

            //swich case for bubbleSort function-
            case 3:
                printf("\n>After Bubble_Sort operation, the sorted array is:\n");
                bubbleSort(a, n);
                display_array(a, n);
                break;

            //swich case for intersectionSort function-
            case 4:
                printf("\n>After Insertion_Sort operation, the sorted array is:\n");
                insertionSort(a, n);
                display_array(a, n);
                break;

            //Swich case for linear_search function-
            case 5:
                printf("\n>Enter the key element to search for: ");
                scanf("%d", &key);
                index = linear_search(a, n, key);
                printf("Element %d found at index %d.\n", key, index);                                 //returns index -1 if element not found.
                break;

            //swich case for binary_search function-
            case 6:
                printf("\n>Enter the key element to search for: ");
                scanf("%d", &key);
                index = binary_search(a, key, lb, ub);
                printf("Element %d found at index %d.\n", key, index);                                     //returns index -1 if element not found.
                break;

            case 7:
                break;

            default:
                printf("\nINVALID INPUT. Try Again.\n");
        }

    }
    while (choice != 7);


    return 0;
}
