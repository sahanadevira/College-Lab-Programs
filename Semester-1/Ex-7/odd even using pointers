#include<stdio.h>
#include<stdlib.h>
int main()
{
   int n,i;
   int roll[100],even[100],odd[100];
   int e=0;
   int o=0;
   printf("Enter number of students:");
   scanf("%d",&n);
   printf("Enter the roll numbers;\n");

   for(i=0;i<n;i++)
   {
      scanf("%d",&roll[i]);
   }
   for(i=0;i<n;i++)
   {
      if (roll[i]%2==0)
      {
         even[e++]=roll[i];
      }
      else
      {
         odd[o++]=roll[i];
      }
   }
      printf("\n Roll numner for advisor (even list):");

for(i=0;i<e;i++)
{
   printf("%d",even[i]);
}
printf("\n Roll number for advisor(odd list):");
for (i=0;i<o;i++)
{
   printf("%d",odd[i]);
}
printf("\n");
return 0;
}
