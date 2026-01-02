#include <stdio.h>
#include "IsPrime.c"

int AllPassed = 1;

void TestPrime(int value, int expected);

int main()
{
    int TestData[][2] =
    {
        { -50, 0 },
        { 10, 0 },
        { 91, 0 },
        { 93, 0 },
        { 101, 1 },
        { 159, 0 },
        { 197, 1 }
    };

    int size, counter;
    size = sizeof(TestData) / sizeof(TestData[0]);

    for (counter = 0; counter < size; counter++)
    {
        TestPrime(TestData[counter][0], TestData[counter][1]);
    }

    if (AllPassed)
    {
        printf("All test cases have passed.\n");
    }

    return 0;
}

void TestPrime(int value, int expected)
{
    int actual = IsPrime(value);

    if (actual != expected)
    {
        printf("%d failed.\n", value);
        AllPassed = 0; 
    }  
}

