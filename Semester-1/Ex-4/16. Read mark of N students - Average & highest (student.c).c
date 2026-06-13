#include<stdio.h>
int main(){
    int n, avg = 0, i, marks[100], max = 0, s = 0;
    printf("enter number of students:");
    scanf("%d", &n);
    printf("enter marks\n");
    for(i = 0; i < n; i++)
    {
        scanf("%d", &marks[i]);
        s += marks[i];
    }
    avg = s / n;
    max = marks[0];
    for(i = 1; i < n; i++)
    {
        if(marks[i] > max)
        {
            max = marks[i];
        }
    }
    printf("average=%d\n", avg);
    printf("highest=%d\n", max);
    return 0;
}

