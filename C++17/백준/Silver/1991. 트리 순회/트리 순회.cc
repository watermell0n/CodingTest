#include <iostream>
using namespace std;
pair <char, char> arr[26];  // first: 왼쪽 자식, second: 오른쪽 자식

// 전위 순회
void preorder(char node) {
  if (node != '.') {
    cout << node;
    preorder(arr[node-'A'].first);
    preorder(arr[node-'A'].second);
  }
}

// 중위 순회
void inorder(char node) {
  if (node != '.') {
    inorder(arr[node-'A'].first);
    cout << node;
    inorder(arr[node-'A'].second);
  }
}

// 후위 순회
void postorder(char node) {
  if (node != '.') {
    postorder(arr[node-'A'].first);
    postorder(arr[node-'A'].second);
    cout << node;
  }
}

int main() {
  int N;
  cin >> N;
  for (int i=0; i<N; i++) {
    char node, left, right;
    cin >> node >> left >> right;
    arr[node-'A'].first = left;
    arr[node-'A'].second = right;
  }

  preorder('A');
  cout << '\n';
  inorder('A');
  cout << '\n';
  postorder('A');

  return 0;
}