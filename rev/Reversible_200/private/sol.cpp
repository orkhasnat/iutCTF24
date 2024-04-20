#include <iostream>

using namespace std;

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

int main() {
  int len = 36;
  int arr[36];
  for (int i = 0; i < 36; i++)
    arr[i] = i;
  for (int i = 0; i < 36; i++) {
    int l = lucky(i) % len;
    swap(arr[i], arr[l]);
  }
  char enc_flag[] = "u_cf140_cdb_t_l9t4y0}yu5'u5tk1{cryi0";
  char flag[37];
  for (int i = 0; i < 36; i++) {
    flag[arr[i]] = enc_flag[i];
  }
  cout << flag;
}
