class Solution {
public:
    // O(n) time and O(1) space complexity
    int maxScore(string s) {
        int ones = 0;
        for (char &digit : s) {
            if (digit == '1') {
                ones++;
            };
        };

        int score = 0, zeroes = 0;

        for (int i = 0; i < s.size() - 1; i++) {
            if (s[i] == '1') {
                ones--;
            } else {
                zeroes++;
            };

            score = max(score, ones + zeroes);
        };

        return score;
    };
};
