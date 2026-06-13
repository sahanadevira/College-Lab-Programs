
#include<stdio.h>
int prime(int n);

// primei.c (function definition)
#include"prime.h"
int prime(int n)
{
    int i;
    if(n <= 1)
        return 0;
    for(i = 2; i <= n/2; i++)
    {
        if(n % i == 0)
            return 0;
    }
    return 1;
}

// primea.c (main program)
#include"prime.h"
int main()
{
    int num;
    printf("enter a number:");
    scanf("%d", &num);
    if(prime(num))
        printf("%d is a prime no.\n", num);
    else
        printf("%d isn't a prime no.\n", num);
    return 0;
}
