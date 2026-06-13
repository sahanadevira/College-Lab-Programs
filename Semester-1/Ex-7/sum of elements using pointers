#include<stdio.h>
#include<stdlib.h>
int main()
{
   int n,i,sum=0;
   int *arr;
   printf("Enter the number of elements:");
   scanf("%d",&n);
   arr = (int*)malloc(n*sizeof(int));

   if(arr==NULL)
   {
      printf("Memory not allocated.\n");
      return 1;
   }

   printf("Enter %d elements:\n",n);
   for(i=0;i<n;i++)
   {
      scanf("%d",&arr[i]);
   }
   for (i=0;i<n;i++)
   {
      sum+=arr[i];
   }
   printf("Sum of the %d elements =%d\n",n,sum);
   free(arr);
   return 0;
}
