#include <iostream>
using namespace std;

int main() {
    int n, capacity;
    int weight[100], value[100];
    float ratio[100], totalValue = 0;

    cout << "Enter number of items: ";
    cin >> n;

    for (int i = 0; i < n; i++) {
        cout << "Enter weight and value of item " << i + 1 << ": ";
        cin >> weight[i] >> value[i];

        ratio[i] = (float)value[i] / weight[i];
    }

    cout << "Enter knapsack capacity: ";
    cin >> capacity;

    // Sort items by value/weight ratio in descending order
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (ratio[i] < ratio[j]) {
                float temp = ratio[i];
                ratio[i] = ratio[j];
                ratio[j] = temp;

                int t = weight[i];
                weight[i] = weight[j];
                weight[j] = t;

                t = value[i];
                value[i] = value[j];
                value[j] = t;
            }
        }
    }

    // Greedy selection
    for (int i = 0; i < n; i++) {
        if (capacity >= weight[i]) {
            totalValue = totalValue + value[i];
            capacity = capacity - weight[i];
        }
        else {
            totalValue = totalValue +
                         ratio[i] * capacity;
            break;
        }
    }

    cout << "Maximum value = " << totalValue << endl;

    return 0;
}
