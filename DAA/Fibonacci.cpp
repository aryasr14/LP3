#include <iostream>
using namespace std;

// Non-recursive Fibonacci
void iterative(int n) {
    int a = 0, b = 1, c;
    
    for (int i = 0; i < n; i++) {
        cout << a << " ";
        c = a + b;
        a = b;
        b = c;
    }
}

// Recursive Fibonacci
int recursive(int n) {
    if (n <= 1)
        return n;

    return recursive(n - 1) + recursive(n - 2);
}

int main() {
    int n;

    cout << "Enter the number of terms: ";
    cin >> n;

    cout << "Non-recursive Fibonacci: " << endl;
    iterative(n);

    cout << "\nRecursive Fibonacci: " << endl;

    for (int i = 0; i < n; i++) {
        cout << recursive(i) << " ";
    }

    cout << endl;

    return 0;
}
