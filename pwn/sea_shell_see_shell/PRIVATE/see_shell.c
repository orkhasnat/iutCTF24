// Compile with:
// gcc -fno-stack-protector -z execstack -o see_shell see_shell.c

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{
    char overflow_me[69];
    char buf[169];

    printf("Hello, dear! Dare you venture into the dark hay`stack`?\n");
    printf("Let me tell you where darner lives: %p\n", buf);
    printf("Can you go to her?\n");
    fflush(stdout);
    fgets(buf, sizeof(buf), stdin);

    printf("Cloning the darner onto the needle...\n");
    fflush(stdout);
    strcpy(overflow_me, buf);

    printf("Neither ever, nor never\nGoodbye...\n");
    fflush(stdout);
}

