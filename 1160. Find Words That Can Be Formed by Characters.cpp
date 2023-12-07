class Solution {
public:
    int countCharacters(vector<string>& words, string chars) {
        int cMap[26] = {};
        for (char const &ch : chars) {
            cMap[ch - 'a']++;
        }

        int res = 0;
        for (string const &word : words) {
            if (check(word, cMap)) {
                res += word.size();
            }
        }

        return res;
    }
private:
    bool check(string const &word, int cMap[26]) {
        int wMap[26] = {};
        for (char const &ch : word) {
            wMap[ch - 'a']++;
            if (wMap[ch - 'a'] > cMap[ch - 'a']) {
                return false;
            }
        }
        return true;
    }
};
