#include <stdio.h>
#include "IsPrime.c"

int allPassed = 1;

void testPrime(int value, int expected);

int main()
{
    int testData[][2] =
    {
        { -50, 0 },
        {  10, 0 },
        {  91, 0 },
        {  93, 0 },
        { 101, 1 },
        { 159, 0 },
        { 197, 1 }
    };

    int size, counter;
    size = sizeof(testData) / sizeof(testData[0]);

    for (counter = 0; counter < size; counter++)
    {
        testPrime(testData[counter][0], testData[counter][1]);
    }

    if (allPassed)
    {
        printf("All test cases are passed.\n");
    }

    return 0;
}

void testPrime(int value, int expected)
{
    int actual = IsPrime(value);

    if (actual != expected)
    {
        printf("%d failed.\n", value);
        allPassed = 0; 
    }  
}

