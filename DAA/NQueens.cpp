#include <iostream>
using namespace std;

int board[20][20];

// Check whether a queen can be placed safely
bool isSafe(int row, int col, int n) {

    // Check same column
    for (int i = 0; i < row; i++) {
        if (board[i][col] == 1) {
            return false;
        }
    }

    // Check upper-left diagonal
    int i = row - 1;
    int j = col - 1;

    while (i >= 0 && j >= 0) {
        if (board[i][j] == 1) {
            return false;
        }
        i--;
        j--;
    }

    // Check upper-right diagonal
    i = row - 1;
    j = col + 1;

    while (i >= 0 && j < n) {
        if (board[i][j] == 1) {
            return false;
        }
        i--;
        j++;
    }

    return true;
}

// Backtracking function
bool solveNQueens(int row, int n) {

    // All queens are placed
    if (row == n) {
        return true;
    }

    // Try each column in the current row
    for (int col = 0; col < n; col++) {

        if (isSafe(row, col, n)) {

            board[row][col] = 1;

            if (solveNQueens(row + 1, n)) {
                return true;
            }

            // Backtrack
            board[row][col] = 0;
        }
    }

    return false;
}

// Display the chessboard
void display(int n) {

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << board[i][j] << " ";
        }
        cout << endl;
    }
}

int main() {

    int n;

    cout << "Enter value of N: ";
    cin >> n;

    // Place first queen at (0, 0)
    board[0][0] = 1;

    if (solveNQueens(1, n)) {

        cout << "\nFinal N-Queens Matrix:\n";
        display(n);

    } else {

        cout << "Solution does not exist.";
    }

    return 0;
}
