#include <stdio.h>
int main()
{
  FILE *fp;
  char b[5101];
  int i;
  int j;
  unsigned short s;
  unsigned short c;
  char a[11];
  fp = fopen("p13.txt", "r");
  fread(b, 1, 5100, fp);
  fclose(fp);
  b[5100] = '\0';
  c = 0;
  for (i = 49; i >= 0; --i) {
    s = c;
    for (j = 0; j < 100; ++j)
      s += b[i + 51*j] - '0';
    c = s / 10;
    if (i < 8)
      a[i + 2] = (s % 10) + '0';
  }
  a[0] = (c / 10) + '0';
  a[1] = (c % 10) + '0';
  a[10] = '\0';
  printf("%s\n", a);
}
