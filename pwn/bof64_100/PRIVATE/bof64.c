// Compile with
// gcc -fno-stack-protector -fno-pie -no-pie -o bof64 bof64.c

#include <stdio.h>

FILE* fp;

void win2()
{
    char flag_2[16];
    fgets(flag_2, 16, fp);
    printf("flag part 2: %s\n", flag_2);
    printf("Now I'm flowinnnnnngggg.....\n");
    fflush(stdout);
}

void win1()
{
    char flag_1[17];
    if ((fp = fopen("flag.txt", "r")) == NULL)
    {
        printf("Error! opening file");
        exit(1);
    }
    fgets(flag_1, 17, fp);
    printf("flag part 1: %s\n", flag_1);

    printf("I need more to flow...\n");
    fflush(stdout);
    fgets(flag_1, 69, stdin);
}



int main()
{

    char buf[0x69];

    printf("The previous one was too easy. Lets ramp up a little bit.\n");
    printf("Give me something to flow...\n");
    fflush(stdout);

    gets(buf);
}