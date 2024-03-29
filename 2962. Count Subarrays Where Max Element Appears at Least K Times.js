// O(n) time and O(1) space complexity
var countSubarrays = function(nums, k) {
    const n = nums.length;
    const MAX = Math.max(...nums);
    let L = 0, count = 0, ret = 0;

    nums.map((num, R) => {
        if (num == MAX) { count++ };

        while (count >= k) {
            ret = ret + (n - R)
            if (nums[L] == MAX) { count-- };
            L++
        };
    });

    return ret;
};
