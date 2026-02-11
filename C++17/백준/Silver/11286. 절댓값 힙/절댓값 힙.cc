#include <iostream>
#include <queue>
using namespace std;

// 우선순위 큐 정렬 기준 설정
struct cmp {
  bool operator()(int a, int b) {
    if (abs(a) == abs(b)) {
      return a > b;
    }
    else {
      return abs(a) > abs(b);
    }
  }
};

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  priority_queue<int, vector<int>, cmp> pq;  // 절댓값 기준 최소 힙
  int N;
  cin >> N;

  string ans;
  for (int i=0; i<N; i++) {
    int x;
    cin >> x;

    if (x == 0) {
      if (pq.empty()) ans += "0\n";
      else {
        ans += to_string(pq.top()) + '\n';
        pq.pop();
      }
    }
    else {
      pq.push(x);
    }
  }

  cout << ans;
}