#include<stdio.h>
int main()
{
    int r, c, i, j, matrix[10][10], transpose[10][10];
    printf("enter the order of matrix:");
    scanf("%d%d", &r, &c);
    printf("enter elements of matrix:\n");
    for(i = 0; i < r; i++)
    {
        for(j = 0; j < c; j++)
        {
            scanf("%d", &matrix[i][j]);
        }
    }
    for(i = 0; i < r; i++){
        for(j = 0; j < c; j++)
        {
            transpose[j][i] = matrix[i][j];
        }
    }
    printf("\n original matrix:\n");
    for(i = 0; i < r; i++)
    {
        for(j = 0; j < c; j++){
            printf("%d\t", matrix[i][j]);
        }
        printf("\n");
    }
    printf("\n transpose of the matrix:\n");
    for(i = 0; i < r; i++)
    {
        for(j = 0; j < c; j++)
        {
            printf("%d\t", transpose[i][j]);
        }
        printf("\n");
    }
    return 0;
}
