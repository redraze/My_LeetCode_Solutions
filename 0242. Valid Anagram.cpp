class Solution {
public:
    // O(n + m) time and O(max(m, n)) space complexity
    bool isAnagram(string s, string t) {
        unordered_map<char, int> charMap;

        for (char &ch : s) {
            charMap[ch]++;
        };

        for (char &ch : t) {
            if (charMap[ch] == 1) {
                charMap.erase(ch);
                continue;
            };
            charMap[ch]--;
        };

        return charMap.empty();
    };
};
