#include <iostream>
#include <vector>
using namespace std;

vector<int> adj_list[101];
int visited[101]; // 전역 변수 -> 0으로 자동 초기화
int cnt = 0;

void worm_virus(int node) {
  for (int n: adj_list[node]) {
    if (!visited[n]) {
      visited[n] = 1;
      cnt++;
      worm_virus(n);
    }
  }
}

int main() {
  int comp, pairs;
  cin >> comp >> pairs;
  for (int i=0; i<pairs; i++) {
    int u, v;
    cin >> u >> v;
    adj_list[u].push_back(v);
    adj_list[v].push_back(u);
  }

  visited[1] = 1;
  worm_virus(1);
  cout << cnt;

  return 0;
}