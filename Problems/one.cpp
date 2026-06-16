#include <iostream>
#include <map>
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::map<int, int> repeat;
        vector<int> ans;
        for(int i = 0; i < nums.size(); i++) {
            int rem = target - nums[i];
            if (repeat.count(rem)) {
                ans.push_back(i);
                ans.push_back(repeat[rem]);
                return ans;
            }
            repeat[nums[i]] = i;
        }
        return ans;
    }
};
