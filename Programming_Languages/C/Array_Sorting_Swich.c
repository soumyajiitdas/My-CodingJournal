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


//Selection Sort of an Array:
void selectionSort (int a[], int n) {
    int i, j, min, temp;
    for (i = 0; i < n-1; i++) {
        min = i;
        for (j = i+1; j < n; j++) {
            if (a[j] < a[min]) {
                min = j;
            }
        }
        if (min != i) {
            temp = a[min];
            a[min] = a[i];
            a[i] = temp;
            }
        }
}


//QuickSort of an Array:
int partition(int a[], int lb, int ub) {
    int flag = 0;
    int l, p;
    l = p = lb;
    int r = ub;
    while (flag != 1) {
        while (a[p] <= a[r] && p!= r) {
            r = r - 1;
        }
        if (p == r) {
            flag = 1;
        }
        if (a[p] >= a[r]) {
            int x = a[p];
            a[p] = a[r];
            a[r] = x;
            p = r;
        }
        if (flag != 1) {
            while (a[p] >= a[l] && p != l) {
            l = l + 1;
        }
        if (p == l) {
            flag = 1;
        }
        if (a[p] < a[l]) {
            int y = a[p];
            a[p] = a[l];
            a[l] = y;
            p = l;
            }
        }
    }
    return p;
}

void quickSort(int a[], int lb, int ub) {
    if (lb < ub) {
    int p = partition(a, lb, ub);        //called partition function.
    quickSort(a, lb, p-1);              //for left sub array.
    quickSort(a, p+1, ub);             //for right sub array.
    }
}


//Merge Sort of an Array:
int  merge(int a[], int lb, int mid, int ub) {
    int i = lb;
    int j = mid + 1; 
    int k = lb;
    int b[k];
    while (i <= mid && j <= ub) {
        if (a[i] < a[j]) {
            b[k] = a[i];
            k = k + 1;
            i = i + 1;  
        } else {
            b[k] = a[j];
            k = k + 1;
            j = j + 1;
        }
    }
    while (i <= mid) {
        b[k] = a[i];
        k = k + 1;
        i = i + 1;
        }
    while (j <= ub) {
        b[k] = a[j];
        k = k + 1;
        j = j + 1;
        }
    for (k = lb; k <= ub; k++) {
        a[k] = b[k];
    }
}

void mergeSort(int a[], int lb, int ub) {
    if (lb < ub) {
        int mid = floor((lb+ub)/2);
        mergeSort(a, lb, mid);           //for left sub array.
        mergeSort(a, mid+1, ub);        //for right sub array.
        merge(a, lb, mid, ub);         //called merge function.
        }
}


//Main Function:
int main() {
    int n, choice;

    printf(">Enter the size of the array: ");
    scanf("%d", &n);
    
    int a[n];
    printf(">Enter %d elements in ascending order:\n", n);
    create_array(a, n);                           //called create_array function.
    printf("\n>Your entered array is:\n");
    display_array(a, n);                          //called display_array function.


    //menu for operations:
    printf("\n>Select the sorting method:\n");
    printf("1. Bubble Sort.\n");
    printf("2. Insertion Sort.\n");
    printf("3. Selection Sort.\n");
    printf("4. Quick Sort.\n");
    printf("5. Merge Sort.\n");
    printf(">Choose between 1 to 5: ");
    scanf("%d", &choice);
    
    int lb = 0, ub = n-1;

    switch (choice) {

        //swich case for bubbleSort function-
        case 1:
            printf("\n>After Bubble_Sort operation, the sorted array is:\n");
            bubbleSort(a, n);
            display_array(a, n);
            break;

        //swich case for intersectionSort function-
        case 2:
            printf("\n>After Insertion_Sort operation, the sorted array is:\n");
            insertionSort(a, n);
            display_array(a, n);
            break;

        //Swich case for selectionSort function-
        case 3:
            printf("\n>After Selection_Sort operation, the sorted array is:\n");
            selectionSort(a, n);
            display_array(a, n);
            break;

        //swich case for quickSort function-
        case 4:
            printf("\n>After Quick_Sort operation, the sorted array is:\n");
            quickSort(a, lb, ub);
            display_array(a, n);
            break;
        
        //swich case for mergeSort function-
        case 5:
            printf("\n>After Merge_Sort operation, the sorted array is:\n");
            mergeSort(a, lb, ub);
            display_array(a, n);
            break;

        default:
            printf("\nINVALID INPUT.\nNo results found, try again.\n");
    }

    return 0;
}