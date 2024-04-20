// Compile with
// gcc -fno-stack-protector -o baby baby.c

#include <stdio.h>

void print_flag()
{
    FILE* fp;
    if ((fp = fopen("flag.txt", "r")) == NULL)
    {
        printf("Error! opening file");
        exit(1);
    }

    char flag[69];
    fgets(flag, sizeof(flag), fp);
    printf("%s", flag);
    fflush(stdout);
    return 0;
}

int main()
{
    int cg = 0;
    char buf[69];

    printf("Do you want to have high CG?\n");
    fflush(stdout);
    scanf("%s", buf);

    if (cg == 6969)
    {
        printf("Come on! No one can't have that much cg!\n");
        fflush(stdout);
        print_flag();
    }
    else
    {
        printf("Nah! You can't have what you want! Try hard.\n");
        fflush(stdout);
    }
}