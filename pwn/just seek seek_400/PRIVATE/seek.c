// Compile with:
// gcc -fno-stack-protector -static-pie -fPIE -o seek seek.c
// create an empty file "file.txt" in the current directory before building the docker image

#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/stat.h>


void read_flag(int whence, int fd, off_t offset)
{
    lseek(fd, offset, whence); // the core line
    char* buf = malloc(22);
    if (read(fd, buf, 22) == -1)
    {
        perror("Error reading: ");
    }
    close(fd);
    if (buf[0] == 'i' && buf[21] == '}')
    {
        printf("Here's your flag:\n");
        for (int i = 0; i < 22; i++)
        {
            printf("%02x ", buf[i]);
        }
        printf("\n");
    }
    else
    {
        printf("No flag for you. Seek harder.\n");
    }
}

int main(int argc, char* argv[]) {
    char seek[69];

    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);

    int fd_1 = open("/tmp/file.txt", O_CREAT | O_RDWR | O_TRUNC, S_IRUSR | S_IWUSR);
    if (fd_1 == -1)
    {
        perror("Error opening file.txt: ");
        exit(1);
    }
    printf("File descriptor: %d\n", fd_1);
    char* flag = malloc(40);


    int fd_2 = open("flag.txt", O_RDONLY);
    read(fd_2, flag, 40);
    close(fd_2);

    char msg[] = "The mark of a seeker is to bounce back after a failure and not give up\n";
    write(fd_1, msg, strlen(msg));
    lseek(fd_1, 5, SEEK_END);
    write(fd_1, flag, strlen(flag));

    printf("Hello, wanderer! I live at %p\n", main);
    printf("Where do ye live?\n");
    gets(seek);
}

