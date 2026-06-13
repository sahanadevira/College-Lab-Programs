#include<stdio.h>
int main()
{
    float rupees, dollars;
    printf("enter amount in rupees:");
    scanf("%f", &rupees);
    dollars = rupees / 83;
    printf("%2f rupees = %2f dollars\n", rupees, dollars);
    return 0;
}
