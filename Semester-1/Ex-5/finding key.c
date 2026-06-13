#include<stdio.h>
int main()
{
   int n,arr[100],key,i,count=0;

   printf("Enter number of elements:");
   scanf("%d",&n);

   printf("Enter array elements:");
   for(i=0;i<n;i++)
   {
   scanf("%d",&arr[i]);
   }

   printf("Enter key to search:");
   scanf("%d",&key);

   for(i=0;i<n;i++)
   {
      if(arr[i]==key)
      {
         printf("Key found at position %d\n",i+1);
         count++;
      }
   }
   if(count==0)
      printf("KEy not found.\n");
   else
      printf("Key occurred %d time(s).\n",count);
   return 0;
}
