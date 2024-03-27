// O(n) time and O(1) space complexity
var numSubarrayProductLessThanK = function(nums, k) {
    if (k == 0) { return 0 };

    let prod = 1, out = 0, L = 0;
    nums.map((num, R) => {

        if (num < k) { out += 1 };
        prod *= num

        if (prod >= k && R >= L) {
            while (prod >= k && L <= R) {
                prod /= nums[L];
                L++
            };
        };

        if (L <= R) {
            out += (R - L);
        };
    });

    return out;
};
