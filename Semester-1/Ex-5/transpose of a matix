#include<stdio.h>
int main()
{   int i,j;
   float det, a[2][2],transpose[2][2];

  printf("Enter elements of 2x2 matrix:\n");
  for(i=0;i<2;i++)
  {
     for(j=0;j<2;j++)
     {
        scanf("%f",&a[i][j]);
     }
  }
  printf("\nOriginal matrix:\n");
  for(i=0;i<2;i++)
  {
     for(j=0;j<2;j++)
     {
        printf("%.2f\t",a[i][j]);
     }
     printf("\n");
  }
  for (i=0;i<2;i++)
  {
     for(j=0;j<2;j++)
     {
        transpose[j][i]=a[i][j];
     }
  }
  det=(a[0][0]*a[1][1]-(a[0][1]*a[1][0]));
        printf("\n Transpose of matrix:\n");
        for (i=0;i<2;i++)
        {
        for(j=0;j<2;j++)
        {
        printf("%2f\t",transpose[i][j]);
        }
        printf("\n");
        }
        printf("\nDeterminant of matrix=%.2f\n",det);
        return 0;
        }
