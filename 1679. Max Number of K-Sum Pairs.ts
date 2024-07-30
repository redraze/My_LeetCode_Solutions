// O(n) time and space complexity
function maxOperations(nums: number[], k: number): number {
    let out = 0;
    const d = {};

    nums.forEach((num, i) => {
        if (d[num]) {
            d[num]++;
        } else {
            d[num] = 1;
        };

        let comp = k - num;

        if (comp == num) {
            if (d[num] > 1) {
                out++, d[num] -= 2;
            };
            return
        };
        
        if (d[comp] && d[comp] > 0) {
            out++, d[comp]--, d[num]--;
        };
    });

    return out;
};


// // O(n log n) time and O(n) space complexity
// function maxOperations(nums: number[], k: number): number {
//     const sorted = nums.sort((a, b) => a - b);
//     let L = 0, R = sorted.length - 1;
//     let out = 0;

//     while (L < R) {
//         let sum = sorted[L] + sorted[R];
//         if (sum == k) {
//             out++, L++, R--;
//         } else if (sum > k) {
//             R--;
//         } else {
//             L++;
//         };
//     };

//     return out;
// };
