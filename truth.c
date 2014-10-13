#include <stdio.h>

int main () {
  if (~(-1))
    printf("Yay, it worked! My syntax appears valid!\n");
  else
    printf("This is why you don't represent TRUE this way.\n");

  return (0);
}
