// O(n log n) time and O(n) space complexity
function merge(intervals: number[][]): number[][] {
    // sort by interval starts
    const sortedIntervals: number[][] = intervals.sort((a, b) => a[0] - b[0]);

    // check for mergable intervals
    const mergedIntervals: number[][] = [];
    let min: number = intervals[0][0];
    let max: number = intervals[0][1];
    sortedIntervals.forEach((interval: number[]) => {
        // interval overlaps
        if (interval[0] <= max) {
            if (interval[1] > max) {
                max = interval[1];
            };
            return;
        };

        mergedIntervals.push([min, max]);
        min = interval[0];
        max = interval[1];
    });
    mergedIntervals.push([min, max]);

    return mergedIntervals;
};
