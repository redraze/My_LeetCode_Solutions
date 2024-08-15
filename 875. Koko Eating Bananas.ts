function minEatingSpeed(piles: number[], h: number): number {
    let L = 1;
    let R = Math.max(...piles);
    let k;

    while (L <= R) {
        k = Math.floor((L + R) / 2);
        const hours = piles
            .map(pile => Math.ceil(pile / k))
            .reduce((a, b) => a + b);

        if (hours <= h) {
            R = k - 1;
        } else {
            L = k + 1;
        };
    };

    return L;
};
