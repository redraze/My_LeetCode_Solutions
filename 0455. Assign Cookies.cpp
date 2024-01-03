// O(n log n) time and O(1) space complexity
class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        sort(begin(g), end(g));
        sort(begin(s), end(s));

        int i = 0;
        int j = 0;

        while (i < g.size() && j < s.size()) {

            while (s[j] < g[i]) {
                j++;

                if (j == s.size()) {
                    return i;
                };
            };

            i++;
            j++;
        };

        return i;
    }
};
