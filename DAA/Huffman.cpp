#include <iostream>
#include <queue>
using namespace std;

struct Node {
    char ch;
    int freq;
    Node *left, *right;

    Node(char c, int f) {
        ch = c;
        freq = f;
        left = right = NULL;
    }
};

// Compare nodes based on frequency
struct Compare {
    bool operator()(Node* a, Node* b) {
        return a->freq > b->freq;
    }
};

// Print Huffman codes
void printCodes(Node* root, string code) {
    if (root == NULL)
        return;

    // Leaf node
    if (root->left == NULL && root->right == NULL) {
        cout << root->ch << " : " << code << endl;
        return;
    }

    printCodes(root->left, code + "0");
    printCodes(root->right, code + "1");
}

int main() {
    int n;
    cout << "Enter number of characters: ";
    cin >> n;

    priority_queue<Node*, vector<Node*>, Compare> pq;

    // Input characters and frequencies
    for (int i = 0; i < n; i++) {
        char ch;
        int freq;

        cout << "Enter character and frequency: ";
        cin >> ch >> freq;

        Node* newNode = new Node(ch, freq);
        pq.push(newNode);
    }

    // Build Huffman Tree
    while (pq.size() > 1) {
        Node* left = pq.top();
        pq.pop();

        Node* right = pq.top();
        pq.pop();

        Node* parent = new Node('#', left->freq + right->freq);

        parent->left = left;
        parent->right = right;

        pq.push(parent);
    }

    // Generate Huffman Codes
    Node* root = pq.top();

    cout << "\nHuffman Codes:\n";
    printCodes(root, "");

    return 0;
}
