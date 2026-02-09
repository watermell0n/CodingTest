#include <iostream>
#include <stack>
#include <string>
using namespace std;

string check(string parenthesis) {
    stack<char> st;
    for (char ch : parenthesis) {
        if (ch == '(') {
            st.push(ch);
        }
        else {  // ch==')'
            if (st.empty()) return "NO";
            else st.pop();
        }
    }
    if (!st.empty()) return "NO";
    return "YES";
}

int main() {
    int T;
    cin >> T;
    string parenthesis;
    for (int i=1; i<=T; i++) {
        cin >> parenthesis;
        cout << check(parenthesis) << '\n';
    }
    return 0;
}