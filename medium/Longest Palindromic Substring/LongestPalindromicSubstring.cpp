# include <iostream>
# include <vector>
# include <cstring>
#
using namespace std;


class Solution {
public:
    string longestPalindrome(string s) {
        if (s.size() == 0)
            return "";
        
        int x = 0;
        int y = 0;
        int k;
        vector<vector<int> > dp(s.size(), vector<int>(s.size(), 0));
        //int dp[s.size()][s.size()];
        
        //memset(&dp, 0, s.size() * s.size());
        
        for (int i = 0; i < s.size(); ++i)
            dp[i][i] = 1;
        
        
        for (int i = 0; i < s.size() - 1; ++i){
            if (s[i] == s[i+1]){
                dp[i][i+1] = 1;
                if (x == 0 and y == 0){
                    x = i;
                    y = i + 1;
                }
            }
        }
        
        for (int i = 2; i < s.size(); ++i){
            for (int j = 0; j < s.size() - 2; ++j){
                k = i + j;
                if (k == s.size())
                    break;
                if (dp[j+1][k-1] == 1 and s[j] == s[k]){
                    dp[j][k] = 1;
                    if (k - j > y - x){
                        x = j;
                        y = k;
                        
                    }
                    
                }
            }
        }
        cout << x << ' ' << y << '\n'; 
        
        // re-zero dp table
        //memset(&dp, 0, s.size() * s.size());
        return s.substr(x, y - x + 1);
    }
};

int main (void){
    Solution sol;
    string q = sol.longestPalindrome("babadada");
    cout << q << '\n';
    return 0;
}