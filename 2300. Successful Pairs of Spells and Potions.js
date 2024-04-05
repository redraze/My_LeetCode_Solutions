/**
 * @param {number[]} spells
 * @param {number[]} potions
 * @param {number} success
 * @return {number[]}
 */
var successfulPairs = function(spells, potions, success) {
    let ret = [];
    potions = potions.sort((a, b) => a - b);
    const n = potions.length;

    for (let i = 0; i < spells.length; i++) {
        // normalize success strength with the potion's strength
        let limit = Math.ceil(success / spells[i]);

        let idx = bisect_left(potions, limit);
        ret.push(n - idx);
    };

    return ret;
};

/**
 * Returns index of left-most value in array 'arr' that is larger than 'val'
 * @param {number[]} arr
 * @param {number} val
 * @return {number}
 */
var bisect_left = function(arr, val) {
    let L = 0, R = arr.length;

    while(L < R) {
        const idx = Math.floor((L + R) / 2);
        const num = arr[idx];

        if (num < val) {
            L = idx + 1
        }
        
        else if (num >= val) {
            R = idx
        };
    };

    return L;
};
