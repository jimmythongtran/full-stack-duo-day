#include <stdio.h>
#include <stdlib.h>

int collatz(int num)
{
    int counter;
    counter = 0;
    while (num != 1)
    {
        if (num % 2 == 0)
        {
            num = num / 2;
            counter ++;
        }
        else
        {
            num = (3 * num) + 1;
            counter ++;
        }
    }
    return counter;
}
int main(void)
{
    int n;
    printf("Enter an integer: ");
    scanf("%d", &n);
    n = collatz(n);
    printf("%d\n", n);
}
