class Solution {
public:
    vector<vector<int>> findMatrix(vector<int>& nums) {
        unordered_map<int, int> seen;
        vector<vector<int>> ret;

        for (int &num : nums) {
            int row = seen[num];
            seen[num] += 1;

            if (row >= ret.size()) {
                ret.push_back({});
            };

            ret[row].push_back(num);
        };

        return ret;
    }
};
