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


//Heapsort function
void max_heaptify(int arr[], int n, int i) {
    int largest = i;                     // Initialize largest as root
    int left = 2 * i;                   // Left child
    int right = 2 * i + 1;             // Right child
    int heapsize = n;

    // If left child is larger than root
    if (left < heapsize && arr[left] > arr[largest])
        largest = left;

    // If right child is larger than largest so far
    if (right < heapsize && arr[right] > arr[largest])
        largest = right;

    // If largest is not root
    if (largest != i) {
        int temp = arr[i];
        arr[i] = arr[largest];
        arr[largest] = temp;

        // Recursively max_heaptify the affected sub-tree
        max_heaptify(arr, n, largest);
    }
}

void buildMaxHeap(int arr[], int n) {
    int heapsize = n;
    // Build a max heap
    for (int i = floor(heapsize / 2 - 1); i >= 0; i--)
        max_heaptify(arr, n, i);
}

// Main function to perform heap sort
void heapSort(int arr[], int n) {
    int heapsize = n;
    buildMaxHeap(arr, n);

    // Extract elements from the heap one by one
    for (int i = heapsize - 1; i >= 0; i--) {
        // Move the current root to the end
        int temp = arr[0];
        arr[0] = arr[i];
        arr[i] = temp;
        heapsize = heapsize - 1;

        // Call max_heaptify on the reduced heap
        max_heaptify(arr, i, 0);
    }
}


int heap_insert(int a[], int n, int val) {
    int heapSize = n;
    a[n] = val;
    while (heapSize > 0) {
        int pnode = floor(heapSize/2);
        if (a[pnode] < a[heapSize]) {
            int temp = a[pnode];
            a[pnode] = a[heapSize];
            a[heapSize] = temp;
            heapSize = pnode;
        } else {
            return 0;
        }
    }
}

void heap_delete(int a[], int n, int indx) {
    int heapsize = n;
    a[indx] = a[heapsize];
    heapsize = heapsize - 1;
    max_heaptify(a, heapsize, indx);
}

//Main Function:
int main() {
    int n, val, indx;

    printf(">Enter the size of the array: ");
    scanf("%d", &n);
    
    int a[n];
    printf(">Enter %d elements:\n", n);
    create_array(a, n);                           //called create_array function.
    printf("\n>Your entered array is:\n");
    display_array(a, n);                          //called display_array function.

    printf("\n>After heap_Sort operation, the sorted array is:\n");
    heapSort(a, n);
    display_array(a, n);
    
    printf("Enter the value you want to insert:");
    scanf("%d", &val);
    heap_insert(a, n, val);
    n = n+1;
    display_array(a, n);

    printf("Enter the value you want to delete:");
    scanf("%d", &indx);
    heap_delete(a, n, indx);
    n = n-1;
    display_array(a, n);

    return 0;
}