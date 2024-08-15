function successfulPairs(spells: number[], potions: number[], success: number): number[] {
    potions.sort((a, b) => a - b);

    return spells.map(spell => {
        let L: number = 0;
        let R: number = potions.length;
        let mid: number = Math.floor((L + R) / 2);

        while (L < R) {
            const strength: number = spell * potions[mid];
            if (strength < success) {
                L = mid + 1;
            } else {
                R = mid;
            };
            mid = Math.floor((L + R) / 2);
        };

        return potions.length - L;
    });
};
