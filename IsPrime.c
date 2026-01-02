#include <math.h>

int IsPrime(int number)
{
	int counter, sqrt_number;
	int flag = 1;
	if (number < 2 || number > 2 && number % 2 == 0)
	{
		flag = 0;
	}
	else
	{
		sqrt_number = sqrt(number);
		for (counter = 3; counter <= sqrt_number; counter += 2)
		{
			if (number % counter == 0)
			{
				flag = 0;
			}
		}
	}
    return flag;
}