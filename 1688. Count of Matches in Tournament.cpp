class Solution {
// O(1) time and space complexity
public:
    int numberOfMatches(int n) {
        return n - 1;
    }

// public:
//     int numberOfMatches(int n) {
//         int matches = 0;

//         while (n > 1) {
//             matches += floor(n / 2);
//             n -= floor(n / 2);
//         };

//         return matches;
//     }
};
