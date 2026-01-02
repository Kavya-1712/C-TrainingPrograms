#include <math.h>

int IsPrime(int number)
{
	int counter, sqrt_number;
	sqrt_number = sqrt(number);
	if (number<2 || number>2 && number%2==0)
		return 0;
	else
	{
		for (counter = 3; counter <= sqrt_number; counter += 2)
		{
			if (number % counter == 0)
			{
				return 0;
				break;
			}
		}
	}
    return 1;
}