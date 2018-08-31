// Demonstrate that a literal gets a null appended, and that a null will
// terminate a string.

#include <stdio.h>
#include <string.h>

void test_string_literal(char *str) {
	printf("String literal is: %s\n", str);
	printf("String literal length is: %d\n", strlen(str));
	printf("Value past end of string is: 0x%x\n", str[strlen(str)]);
}

int main () {
	test_string_literal("Hello, there");
	test_string_literal("With a \0 null");

	return(0);
}