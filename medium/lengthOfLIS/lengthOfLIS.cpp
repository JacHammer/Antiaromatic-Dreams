# include <iostream>
# include <vector>
# include <cstring>

using namespace std;


class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {

        if (nums.size() == 0){
            return 0;
        }
        if (nums.size() == 1){
            return 1;
        }

        int length = 0;
        vector <int> dp(nums.size(), 0);

        // base case
        dp[0] = 1;


        for (int i = 1; i < nums.size(); ++i){
            int maxval = 0;
            for (int j = 0; j < i; ++j){
                if (nums[i] > nums[j] && maxval < dp[j]){
                    maxval = dp[j];
                }
            }

            // update length
            dp[i] = maxval + 1;
            if (dp[i] > length){
                length = dp[i];
            }
        }
        return length;

    }
};