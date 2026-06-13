#include<stdio.h>
#include<stdlib.h>
#include<time.h>
int main()
{
   int dice1,dice2,sum;
   int frequency[13]={0};
   int i;
   srand(time(NULL));
     for (i=0;i<50;i++)
   {
     dice1=rand()%6+1;
     dice2=rand()%6+1;
     sum=dice1+dice2;
     frequency[sum]++;
   }
   printf("sum\tFrequency\n");
   printf("--------------------------\n");
   for(sum=2;sum<=12;sum++)
   {
      printf("%d\t%d\n",sum,frequency[sum]);
   }
   return 0;
}

