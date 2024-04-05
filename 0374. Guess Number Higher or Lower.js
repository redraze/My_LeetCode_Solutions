// O(log n) time and O(1) space complexity
var guessNumber = function(n) {
    let num = Number(n / 2);
    let min = 0, max = n;

    while(true) {
        let g = guess(num);

        // guess is correct
        if (g == 0) { return num }

        // guess is too low
        else if (g == 1) {
            min = num;
            num = Number((min + max) / 2) + 1;
        }

        // guess is too high
        else if (g == -1) {
            max = num;
            num = Number((min + max) / 2);
        };
    };
};
