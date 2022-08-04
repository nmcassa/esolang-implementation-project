#include <iostream>
#include <fstream> //read file
#include <vector>
#include <sstream>

using namespace std;

int mem[100];
int pointer = 0;
int instruPointer = 0;

void rotateInstructions(int &instruPointer) {
    if (instruPointer == 7) {
        instruPointer = 0;
    } else {
        instruPointer++;
    }
}

int main() {
    string myText;
    string total;

    char instructions[8] = {'+', '-', '>', '<', ',', '.', '[', ']'};

    ifstream MyReadFile("hello.rotf");

    while (getline (MyReadFile, myText)) {
        total = total + myText;
    }

    vector<char> characters;

    for (char c : total) {
        characters.push_back(c);
    }

    int i = 0;

    while (i < characters.size()) {
        char item = characters.at(i);

        bool nonComment = false;

        cout << instruPointer << endl;

        //>
        if (item == instructions[(instruPointer + 2) % 8]) {
            pointer++;
            nonComment = true;
        }
        //<
        else if (item == instructions[(instruPointer + 3) % 8]) {
            pointer--;
            nonComment = true;
        }
        //+
        else if (item == instructions[(instruPointer + 0) % 8]) {
            mem[pointer]++;
            nonComment = true;
        }
        //-
        else if (item == instructions[(instruPointer + 1) % 8]) {
            mem[pointer]--;
            nonComment = true;
        }
        //,
        else if (item == instructions[(instruPointer + 4) % 8]) {
            cin >> mem[pointer];
            nonComment = true;
        }
        //.
        else if (item == instructions[(instruPointer + 5) % 8]) {
            cout << 'A' -1 + mem[pointer] << endl;
            nonComment = true;
        }
        //[
        else if (item == instructions[(instruPointer + 6) % 8]) {
            if (mem[pointer] == 0) {
                while (characters.at(i) != ']') {
                    i++;
                }
                i++;
            }
            nonComment = true;
        }
        //]
        else if (item == instructions[(instruPointer + 7) % 8]) {
            if (mem[pointer] != 0) {
                while (characters.at(i) != '[') {
                    i--;
                }
                i--;
            }
            nonComment = true;
        }

        if (nonComment) {
            rotateInstructions(instruPointer);
        }

        i++;
    }
}