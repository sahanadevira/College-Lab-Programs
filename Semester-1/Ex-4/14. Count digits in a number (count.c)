
#include<stdio.h>
int countdigits(int n);

// counti.c (function definition)
#include"count.h"
int countdigits(int n)
{
    int count = 0;
    while(n != 0){
        count++;
        n /= 10;
    }
    return count;
}

// counta.c (main program)
#include"count.h"
int main()
{
    int num;
    printf("enter a number:");
    scanf("%d", &num);
    printf("number of digits:%d\n", countdigits(num));
    return 0;
}
