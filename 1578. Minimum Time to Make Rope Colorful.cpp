// O(n) time and O(1) space complexity
class Solution {
public:
    int minCost(string colors, vector<int>& neededTime) {
        int timeSpent = 0;
        int prevIdx = 0;
        char prevColor = colors[0];
        int sumTimeNeeded = 0;
        int maxTimeNeeded = neededTime[0];

        for (int i = 1; i < colors.size(); i++) {

            if (colors[i] != prevColor) {
                if (i - prevIdx > 1) {
                    timeSpent += sumTimeNeeded;
                };
                prevIdx = i;
                prevColor = colors[i];
                sumTimeNeeded = 0;
                maxTimeNeeded = neededTime[i];

            } else {
                sumTimeNeeded += min(maxTimeNeeded, neededTime[i]);
                maxTimeNeeded = max(maxTimeNeeded, neededTime[i]);
            };
        };

        if (colors.size() - prevIdx > 1) {
            return timeSpent + sumTimeNeeded;
        };
        return timeSpent;
    };
};
