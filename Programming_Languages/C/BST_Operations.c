#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *left;
    struct node *right;
};

//INSERTION OPERATION IN BST:
struct node *new_node(int val) {
    struct node *ptr = (struct node *)malloc(sizeof(struct node));
    ptr->data = val;
    ptr->left = NULL;
    ptr->right = NULL;
    return ptr;
}

struct node *bst_insert(struct node * tree, int val) {
    if (tree == NULL) {
        tree = new_node(val);
        return tree;
    } else if (val < tree->data) {
        tree->left = bst_insert(tree->left, val);
    } else {
        tree->right = bst_insert(tree->right, val);
    }
    return tree;
}

//DISPLAY OPERATION IN BST:
void inOrder(struct node *tree) {
    if (tree != NULL) {
        inOrder(tree->left);
        printf("%d\t", tree->data);
        inOrder(tree->right);
    }
}


//DELETION OPERATION IN BST:
struct node *FindMin(struct node *tree) {
    if (tree == NULL || tree->left == NULL) {
        return tree;
    } else {
        return FindMin(tree->left);
    }
}

struct node *bst_delete(struct node *tree, int val) {
    if (tree == NULL) {
        printf("Tree is Empty.\n");
    } else if (val < tree->data) {
        tree->left = bst_delete(tree->left, val);
    } else if (val > tree->data) {
        tree->right = bst_delete(tree->right, val);
    } else if (tree->left != NULL && tree->right != NULL) {
        struct node *temp = FindMin(tree->right);
        tree->data = temp->data;
        tree->right = bst_delete(tree->right, temp->data);
        temp = NULL;
        free(temp);
    } else {
        if (tree->left == NULL && tree->right == NULL) {
            tree = NULL;
        } else if (tree->left != NULL) {
            tree = tree->left;
        } else {
            tree = tree->right;
        }
    }
    return tree;
}


//SEARCHING OPERATION IN BST:
void bst_search(struct node *tree, int key) {
    if (tree == NULL) {
        printf("%d is not present in the tree.", key);
    } else if (key == tree->data) {
        printf("%d is present in the tree.", key);
    } else if (key < tree->data) {
        bst_search(tree->left, key);
    } else {
        bst_search(tree->right, key);
    }
}


//MAIN FUNCTION TO PERFORM:
int main() {
    struct node *tree = NULL;
    int value1, value2, value3;
    do {
        //Insertion of Value into the BST
        printf("Enter the new value: ");
        scanf("%d", &value1);
        tree = bst_insert(tree, value1);

        printf("In-order traversal of the BST:\n");
        inOrder(tree);
        printf("\n\n");
    }
    while(value1 != 0);

    //Searching value in BST
    printf("Enter the value of the key: ");
        scanf("%d", &value2);
        bst_search(tree, value2);

    //Deletion of Value from the BST
    printf("\nEnter the value: ");
    scanf("%d", &value3);
    tree = bst_delete(tree, value3);
    printf("In-order traversal of the BST:\n");
    inOrder(tree);

    return 0;

}