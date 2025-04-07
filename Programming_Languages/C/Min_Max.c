#include<stdio.h>
//Function for max_min:
void Max_Min(int a[], int i, int j, int *max, int *min) {
    int max1, min1;
    if (i==j) {
        *max = *min = a[i];
    } else if (i==j-1) {
        *min= (a[i]<a[j]) ? a[i]:a[j];
        *max= (a[i]>a[j]) ? a[i]:a[j];
    } else {
        int mid = ((i+j)/2);
        Max_Min(a, i, mid, max, min);
        Max_Min(a, mid+1, j, &max1, &min1);
        if (*max < max1){
            *max = max1;
        }
        if (*min > min1) {
            *min = min1;
        }
    }  
}
//Function for display array:
void display_array(int a[], int n) {
    for (int i = 0; i < n; i++) {
        printf("a[%d] = %d,", i, a[i]);
    }
}
int main() {
    int a[] = {30, 23, 46, 47, 85};
    int n = sizeof(a)/sizeof(a[0]);
    int max, min;
    display_array(a, n);
    Max_Min(a, 0, n-1, &max, &min);
    printf("\nMinimum Element %d.\n", min);
    printf("Maximum Element %d.", max);
    return 0;
}