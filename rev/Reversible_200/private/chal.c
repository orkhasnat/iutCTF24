#include <stdio.h>
#include <string.h>
#include <unistd.h>

int lucky(int n) {
  int lucky = 1;
  int count = 0;
  int i;

  while (count < n) {
    int found = 0;
    lucky++;
    for (i = 2; i <= lucky; i++) {
      if (lucky % i == 0) {
        found++;
      }
      if (found > 1) {
        break;
      }
    }
    if (found == 1) {
      count++;
    }
  }

  return lucky;
}

void swap(char *a, char *b) {
  char t = *a;
  *a = *b;
  *b = t;
}

void enc(char *flag, int len) {
  for (int i = 0; i < len; i++) {
    int l = lucky(i) % len;
    swap(&flag[i], &flag[l]);
  }
}

int main() {
  char inp[64];
  char enc_flag[] = "u_cf140_cdb_t_l9t4y0}yu5'u5tk1{cryi0";
  printf("Flag: ");
  fflush(stdout);
  int len = read(0, inp, 64) - 1;
  inp[len] = 0;
  enc(inp, len);
  if (strncmp(inp, enc_flag, 36)) {
    printf("Wrong");
    return 0;
  }
  printf("Right");
}
