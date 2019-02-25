#include <iostream>
#include <string>
using namespace std;

extern "C" const char* strconcat(const char* str1, const char* str2) {


    cout << str1 << endl;
    cout << str2 << endl;

    auto strsum = new string(str1);

    strsum->append(str2);

    return strsum->c_str();
}
