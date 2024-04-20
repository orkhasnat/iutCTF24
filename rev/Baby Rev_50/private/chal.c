#include <stdio.h>
#include <unistd.h>
// iutctf{7h3_3451357_r3v_3v3r}
// 0123456789012345678901234567
void _do(char *flag) {
  printf("hmm...");
  flag[7] = '7';
  flag[3] = 'c';
  flag[2] = 't';
  flag[11] = '3';
  flag[6] = '{';
  flag[10] = '_';
  flag[12] = '4';
}
void _something(char *flag) {
  printf("umm...");
  flag[0] = 'i';
  flag[4] = 't';
  flag[8] = 'h';
  flag[5] = 'f';
  flag[13] = '5';
  flag[9] = '3';
  flag[28] = '\0';
}
void _with(char *flag) {
  printf("huh...");
  flag[14] = '1';
  flag[26] = 'r';
  flag[24] = 'v';
  flag[22] = '_';
  flag[18] = '_';
  flag[27] = '}';
  flag[23] = '3';
}
void _the(char *flag) {
  printf("yah...");
  flag[20] = '3';
  flag[21] = 'v';
  flag[17] = '7';
  flag[25] = '3';
  flag[19] = 'r';
  flag[16] = '4';
  flag[15] = '3';
  flag[1] = 'u';
}
void _flag(char *flag) { printf("\nI get It."); }

void check(char *flag) {
  _do(flag);
  _something(flag);
  _with(flag);
  _the(flag);
  _flag(flag);
}
char PASSWORD[] = "password";
int main() {
  char password[32];
  char flag[32];
  printf("Password: ");
  fflush(stdout);
  read(0, password, 32);
  check(flag);
}
