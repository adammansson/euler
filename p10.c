#include <stdio.h>
unsigned int is_prime(unsigned int n)
{
  unsigned int i;
  i = 2;
  while (i * i < n + 1) {
    if (n % i == 0)
      return 0;
    i++;
  }
  return 1;
}
int main()
{
  unsigned int n;
  unsigned long s;
  n = 3;
  s = 2;
  while (n < 2000000) {
    if (is_prime(n))
      s += n;
    n += 2;
  }
  printf("%lu\n", s);
}

