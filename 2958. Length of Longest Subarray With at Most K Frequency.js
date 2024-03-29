// O(n) time and space complexity
var maxSubarrayLength = function(nums, k) {
    let freq = {}, L = 0, ret = 0;

    nums.map((num, R) => {
        freq[num] = freq[num] ? freq[num] + 1 : 1;

        while (freq[num] > k) {
            freq[nums[L]] = freq[nums[L]] - 1;
            L++;
        };

        ret = ret > R - L + 1 ? ret : R - L + 1;
    });

    return ret;
};
