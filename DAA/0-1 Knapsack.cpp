#include <iostream>
using namespace std;

int main() {
    int n, capacity;
    int weight[100], value[100];
    int dp[101][101];

    cout << "Enter number of items: ";
    cin >> n;

    for (int i = 0; i < n; i++) {
        cout << "Enter weight and value of item " << i + 1 << ": ";
        cin >> weight[i] >> value[i];
    }

    cout << "Enter knapsack capacity: ";
    cin >> capacity;

    // Initialize first row and column
    for (int i = 0; i <= n; i++) {
        for (int w = 0; w <= capacity; w++) {
            dp[i][w] = 0;
        }
    }

    // Dynamic Programming
    for (int i = 1; i <= n; i++) {
        for (int w = 1; w <= capacity; w++) {
            if (weight[i - 1] <= w) {
                int take = value[i - 1] + dp[i - 1][w - weight[i - 1]];
                int skip = dp[i - 1][w];

                if (take > skip)
                    dp[i][w] = take;
                else
                    dp[i][w] = skip;
            }
            else {
                dp[i][w] = dp[i - 1][w];
            }
        }
    }

    cout << "Maximum value = " << dp[n][capacity] << endl;

    return 0;
}
