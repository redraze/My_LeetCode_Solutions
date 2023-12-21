class Solution {
public:
    // O(n log n) time and O(1) space complexity
    int maxWidthOfVerticalArea(vector<vector<int>>& points) {
        sort(points.begin(), points.end());

        int ret = 0;
        for (int i = 1; i < points.size(); i++) {
            int diff = points[i][0] - points[i - 1][0];
            ret = max(ret, diff);
        };

        return ret;
    };
};
