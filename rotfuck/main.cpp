#include <iostream>
#include <fstream> //read file
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

int mem[100];
int pointer = 0;
int instruPointer = 0;

//https://stackoverflow.com/questions/12015571/how-to-print-unicode-character-in-c
string unicode_to_utf8(int unicode){
    string s;

    if (unicode>=0 and unicode <= 0x7f) { // 7F(16) = 127(10)
        s = static_cast<char>(unicode);

        return s;
    }
    else if (unicode <= 0x7ff) { // 7FF(16) = 2047(10)
        unsigned char c1 = 192, c2 = 128;

        for (int k=0; k<11; ++k) {
            if (k < 6)  c2 |= (unicode % 64) & (1 << k);
            else c1 |= (unicode >> 6) & (1 << (k - 6));
        }

        s = c1;    s += c2;

        return s;
    }
    else if (unicode <= 0xffff) { // FFFF(16) = 65535(10)
        unsigned char c1 = 224, c2 = 128, c3 = 128;

        for (int k=0; k<16; ++k) {
            if (k < 6)  c3 |= (unicode % 64) & (1 << k);
            else if (k < 12) c2 |= (unicode >> 6) & (1 << (k - 6));
            else c1 |= (unicode >> 12) & (1 << (k - 12));
        }

        s = c1;    s += c2;    s += c3;

        return s;
    }
    else if (unicode <= 0x1fffff) { // 1FFFFF(16) = 2097151(10)
        unsigned char c1 = 240, c2 = 128, c3 = 128, c4 = 128;

        for (int k=0; k<21; ++k) {
            if (k < 6)  c4 |= (unicode % 64) & (1 << k);
            else if (k < 12) c3 |= (unicode >> 6) & (1 << (k - 6));
            else if (k < 18) c2 |= (unicode >> 12) & (1 << (k - 12));
            else c1 |= (unicode >> 18) & (1 << (k - 18));
        }

        s = c1;    s += c2;    s += c3;    s += c4;

        return s;
    }
    else if (unicode <= 0x3ffffff) { // 3FFFFFF(16) = 67108863(10)
        ;  // actually, there are no 5-bytes unicodes
    }
    else if (unicode <= 0x7fffffff) { // 7FFFFFFF(16) = 2147483647(10)
        ;  // actually, there are no 6-bytes unicodes
    }
    else  ;  // incorrect unicode (< 0 or > 2147483647)

    return "";
}

int utf8_to_unicode(string utf8_code) {
    unsigned utf8_size = utf8_code.length();
    int unicode = 0;

    for (unsigned p=0; p<utf8_size; ++p) {
        int bit_count = (p? 6: 8 - utf8_size - (utf8_size == 1? 0: 1)),
            shift = (p < utf8_size - 1? (6*(utf8_size - p - 1)): 0);

        for (int k=0; k<bit_count; ++k)
            unicode += ((utf8_code[p] & (1 << k)) << shift);
    }
    return unicode;
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

        //>
        if (item == instructions[2]) {
            pointer++;
            nonComment = true;
        }
        //<
        else if (item == instructions[3]) {
            pointer--;
            nonComment = true;
        }
        //+
        else if (item == instructions[0]) {
            mem[pointer]++;
            nonComment = true;
        }
        //-
        else if (item == instructions[1]) {
            mem[pointer]--;
            nonComment = true;
        }
        //,
        else if (item == instructions[4]) {
            string input;
            cin >> input;
            int uni = utf8_to_unicode(input);
            mem[pointer] = uni;
            nonComment = true;
        }
        //.
        else if (item == instructions[5]) {
            cout << unicode_to_utf8(mem[pointer]) << endl;
            nonComment = true;
        }
        //[
        else if (item == instructions[6]) {
            int matching = 0;
            if (mem[pointer] == 0) {
                while (i < characters.size()) {
                    //[
                    if (characters.at(i) == instructions[6]) {
                        matching++;
                    //]
                    } else if (characters.at(i) == instructions[7]) {
                        if (matching != 0) {
                            matching--;
                        } else {
                            break;
                        }
                    }
                    rotate(instructions, instructions + 1, instructions + 8);
                    i++;
                }
                i++;
            }
            nonComment = true;
        }
        //]
        else if (item == instructions[7]) {
            int matching = 0;
            if (mem[pointer] != 0) {
                while (i >= 0) {
                    cout << i << " " << matching << " ";
                    //]
                    if (characters.at(i) == instructions[7]) {
                        matching++;
                    //[
                    } else if (characters.at(i) == instructions[6]) {
                        if (matching != 0) {
                            matching--;
                        } else {
                            break;
                        }
                    }
                    rotate(instructions, instructions + 7, instructions + 8);
                    i--;
                }
                i--;
            }
            nonComment = true;
        }

        if (nonComment) {
            rotate(instructions, instructions + 1, instructions + 8);
        }

        i++;
    }
}