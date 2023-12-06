class Solution {
public:
    int totalMoney(int n) {
        int completeWeeks = n / 7;

        int bank = completeWeeks * 28;

        for (int i = 0; i < completeWeeks; i++) {
            bank += i * 7;
        }

        int remainingDays = n - (completeWeeks * 7);

        for (int i = 1; i < remainingDays + 1; i++) {
            bank += (i + completeWeeks);
        }

        return bank;
    }
};
