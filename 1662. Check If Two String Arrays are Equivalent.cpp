class Solution {
public:
    bool arrayStringsAreEqual(vector<string>& word1, vector<string>& word2) {
        return concatString(word1) == concatString(word2);
    }
private:
  string concatString(vector<string>& wordArr) {
    string retStr = "";

    for (string const &s : wordArr) {
      retStr += s;
    }

    return retStr;
  }
};
