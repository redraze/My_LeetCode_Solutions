class Solution {
public:
    // Solution 2: in-place grid manipulation, with a trick!
    // O(m * n) time and O(m + n) space complexity 
    vector<vector<int>> onesMinusZeros(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();

        vector<int> r(m);
        vector<int> c(n);

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                r[i] += grid[i][j];
                c[j] += grid[i][j];
            };
        };

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                grid[i][j] = 2 * (r[i] + c[j]) - (m + n);
            };
        };

        return grid;
    };

    // // solution 1
    // // O(m * n) time and space complexity 
    // vector<vector<int>> onesMinusZeros(vector<vector<int>>& grid) {
    //     map<int, vector<int>> r;
    //     r[0] = {};
    //     r[1] = {};
    //     for (int i = 0; i < grid.size(); i++) {
    //         r[0].push_back(0);
    //         r[1].push_back(0);
    //     };
        
    //     map<int, vector<int>> c;
    //     c[0] = {};
    //     c[1] = {};
    //     for (int i = 0; i < grid[0].size(); i++) {
    //         c[0].push_back(0);
    //         c[1].push_back(0);
    //     };

    //     for (int i = 0; i < grid.size(); i++) {
    //         for (int j = 0; j < grid[0].size(); j++) {
    //             int num = grid[i][j];
    //             r[num][i]++;
    //             c[num][j]++;
    //         };
    //     };

    //     vector<vector<int>> diff(grid.size());
    //     for (int i = 0; i < grid.size(); i++) {
    //         for (int j = 0; j < grid[0].size(); j++) {
    //             int zeroes = r[0][i] + c[0][j];
    //             int ones = r[1][i] + c[1][j];
    //             diff[i].push_back(ones - zeroes);
    //         };
    //     };
        
    //     return diff;
    // };
};
