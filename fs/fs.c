#include <stdio.h>

int main() {
  int num;

  printf("%d\n", 123);             // "123"
  printf("%s\n", "Hello, world");  // "Hello, world"
  printf("%x\n", 0xdeadbeef);      // "deadbeef"
  printf("%p\n", &num);            // "0x7ffe6d1cb2c4"
  
  return 0;
}
