#include <stdio.h>

int main(void){
  int a;
  a = 1;
  while(a<100){
    printf("%d\n", a);
    a = a * 3;
  }
  return 0;
}
