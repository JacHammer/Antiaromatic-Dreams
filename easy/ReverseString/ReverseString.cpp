
# include <iostream>
# include <vector>

using namespace std;


class Solution {
public:
    void reverseString(vector<char>& s) {
        int j;
        for (int i = 0; i < s.size() / 2; ++i){
            j = s.size() - i - 1;
            s[i] ^= s[j];
            s[j] ^= s[i];
            s[i] ^= s[j];
        }

    }
};

int main(void){
    Solution sol;
    vector<char> s;
    s = {'a', 'b', 'c', 'd', 'e'};
    sol.reverseString(s);
    for (int i = 0; i < s.size(); ++i)
        cout << s[i] << ' ';
    cout << '\n';
    return 0;
}