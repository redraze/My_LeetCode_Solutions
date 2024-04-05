// O(n) time and O(1) space complexity
var largestAltitude = function(gain) {
    let alt = 0, ret = 0;
    for (let i = 0; i < gain.length; i++) {
        alt += gain[i];
        if (alt > ret) { ret = alt };
    };
    return ret;
};
