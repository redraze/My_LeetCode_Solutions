// O(n) time and O(1) space complexity

/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    let i = s.length - 1, ret = 0;

    while (i >= 0) {
        if (s[i] == ' ') {
            if (ret) { return ret };
            i--;
            continue;
        };

        i--;
        ret++;
    };

    return ret;
};
