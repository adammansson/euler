#include <stdio.h>
unsigned int number_factors(unsigned long n)
{
  unsigned long i;
  unsigned int c;
  i = 2;
  c = 2;
  while (i * i < n) {
    if (n % i == 0)
      c += 2;
    i++;
  }
  return c;
}
int main()
{
  unsigned long tn;
  unsigned int i;
  tn = 0;
  i = 1;
  while (1) {
    tn += i;
    if (number_factors(tn) > 500) {
      printf("%lu\n", tn);
      return 0;
    }
    i++;
  }
  return 1;
}

