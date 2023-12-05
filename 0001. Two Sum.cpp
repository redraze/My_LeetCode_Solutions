class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) { 
        map<int, int> dict;

        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            
            if (dict.count(complement)) {
                return {dict[complement], i};
            }

            dict[nums[i]] = i;
        }

        return {};
    }
};
