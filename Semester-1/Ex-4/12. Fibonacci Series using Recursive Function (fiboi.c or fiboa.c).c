
#include<stdio.h>
int fibo(int n);

#include"fibo.h"
int fibo(int n)
{
    int y;
    if(n == 0)
    {
        return 0;
    }
    else if(n == 1)
    {
        return 1;
    }
    else{
        y = fibo(n-1) + fibo(n-2);
    }
    return y;
}

// fiboa.c (main program)
#include"fibo.h"
void main(){
    int n, i;
    printf("enter n");
    scanf("%d", &n);
    for(i = 0; i < n; i++)
    {
        printf("%d\t", fibo(i));
    }
}
