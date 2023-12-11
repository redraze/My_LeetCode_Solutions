class Solution {
public:
    int findSpecialInteger(vector<int>& arr) {
        int count = 1;
        for (int i = 1; i < arr.size(); i++) {
            if (arr[i] == arr[i - 1]) {
                count++;
            } else {
                count = 1;
            };
            if (count > arr.size() / 4) {
                return arr[i];
            };
        };
        return arr.back();
    };
};
