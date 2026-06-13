#include<stdio.h>
#include<stdlib.h>
int main ()
{
   int n,i;
   int fib[50];
   int *ptr=fib;
   printf("Enter the number of terms:");
   scanf("%d",&n);
   if (n<=0)
   {
      printf("Invalid input! Enter a positive number:\n");
      return 0;
   }
   *ptr = 0;
   if (n>1)
      *(ptr+1)=1;
   for (i=2;i<n;i++)
   {
      *(ptr+i)=*(ptr+i-1)+*(ptr+1-2);
   }
   printf("\n Fibonaccci series:");
   for (i=0;i<n;i++)
   {
      printf("%d",*(ptr+i));
   }
   printf("\n");
   return 0;
}
