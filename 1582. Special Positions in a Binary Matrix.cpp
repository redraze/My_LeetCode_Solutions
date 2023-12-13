class Solution {
public:
    int numSpecial(vector<vector<int>>& mat) {
        int r[mat.size()];
        for (int i = 0; i < mat.size(); i++) {
            r[i] = 0;
        };
        int c[mat[0].size()];
        for (int i = 0; i < mat[0].size(); i++) {
            c[i] = 0;
        };

        for (int i = 0; i < mat.size(); i++) {
            for (int j = 0; j < mat[0].size(); j++) {
                if (mat[i][j] == 1) {
                    r[i]++;
                    c[j]++;
                };
            };
        };

        int ans = 0;
        for (int i = 0; i < mat.size(); i++) {
            for (int j = 0; j < mat[0].size(); j++) {
                if (mat[i][j] == 1 && r[i] == 1 && c[j] == 1) {
                    ans++;
                };
            };
        };

        return ans;
    };
};
