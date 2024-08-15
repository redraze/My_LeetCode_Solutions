/** 
 * Forward declaration of guess API.
 * @param {number} num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * var guess = function(num) {}
 */


function guessNumber(n: number): number {
    let L: number = 0;
    let R: number = n;
    let mid: number = Math.floor(n / 2);
    let g: -1 | 0 | 1 = guess(mid);

    while (g != 0) {
        if (g == 1) {
            L = mid + 1;
        } else {
            R = mid - 1;
        };
        mid = Math.floor((L + R)/ 2);
        g = guess(mid);
    };

    return mid;
};
