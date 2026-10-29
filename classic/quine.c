/*
 * C Quine - classic self-reproducing program.
 * Build & verify: gcc -o quine quine.c && ./quine | diff - quine.c
 */
#include <stdio.h>

int main(void) {
    char *s = "/*%c * C Quine - classic self-reproducing program.%c * Build & verify: gcc -o quine quine.c && ./quine | diff - quine.c%c */%c#include <stdio.h>%c%cint main(void) {%c    char *s = %c%s%c;%c    printf(s, 10, 10, 10, 10, 10, 10, 10, 34, s, 34, 10, 10, 10, 10);%c    return 0;%c}%c";
    printf(s, 10, 10, 10, 10, 10, 10, 10, 34, s, 34, 10, 10, 10, 10);
    return 0;
}
