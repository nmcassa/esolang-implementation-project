#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

char instructions[8] = {'+', '-', '>', '<', ',', '.', '[', ']'};

int findIndex(char target) {
    int i = 0;
    while (i < 8) {
        if (instructions[i] == target) {
            return i;
        }
        i++;
    }
    return -1;
}

int main() {
    string myText;
    string total;
    int curr = 0;

    ifstream MyReadFile("hello.bf");

    while (getline (MyReadFile, myText)) {
        total = total + myText;
    }

    for (char item : total) {
        int index = findIndex(item);

        //comment char
        if (index == -1) {
            continue;
        }

        cout << instructions[(index + curr) % 8];

        curr++;
    }

    return 0;
}