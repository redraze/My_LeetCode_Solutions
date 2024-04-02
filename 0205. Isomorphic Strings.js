// O(n) time and space complexity
var isIsomorphic = function(s, t) {
    let sMap = {}, tSet = new Set();

    for (let i = 0; i < s.length; i++) {
        const sCh = s[i], tCh = t[i]

        if (!sMap[sCh]) {
            if (tSet.has(tCh)) { return false };
            sMap[sCh] = tCh;
            tSet.add(tCh);
        };

        if (sMap[sCh] !== tCh) {
            return false;
        };
    };

    return true
};
