#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <unordered_map>
using namespace std;

int main(int argc, const char** argv) 
{
    int p1_ans, p2_ans;

    // Get input in ifstream
    ifstream file("input.txt");
    if (!file) {
        cout << "Failed to open input.txt" << endl;
    }

    // Map of words to integers
    unordered_map<string, string> hashmap;
    hashmap["one"] = "o1e";
    hashmap["two"] = "t2o";
    hashmap["three"] = "t3e";
    hashmap["four"] = "4";
    hashmap["five"] = "5e";
    hashmap["six"] = "6";
    hashmap["seven"] = "7n";
    hashmap["eight"] = "e8t";
    hashmap["nine"] = "9";

    // Parse file line by line
    string str;
    while (getline(file, str)) {
        
        // Part 1: Just look for integer from start and end of string
        auto it = str.begin();
        while (it != str.end() && !isdigit(*it)) ++it;
        p1_ans += (*it-'0')*10;
        it = str.end()-1;
        while (it != str.begin()-1 && !isdigit(*it)) --it;
        p1_ans += *it-'0';

        // Part 2: Replace one with o1e and so on to get cases
        for (auto entry : hashmap) {
            int start_pos;
            while ((start_pos = str.find(entry.first)) != -1) {
                str.replace(start_pos, entry.first.length(), entry.second);
            }
        }
        it = str.begin();
        while (it != str.end() && !isdigit(*it)) ++it;
        p2_ans += (*it-'0')*10;
        it = str.end()-1;
        while (it != str.begin()-1 && !isdigit(*it)) --it;
        p2_ans += *it-'0';
    }

    cout << "Part 1: " << p1_ans << endl;
    cout << "Part 2: " << p2_ans << endl;
    return 0;
}
