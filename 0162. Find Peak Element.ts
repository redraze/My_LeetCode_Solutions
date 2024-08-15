function findPeakElement(nums: number[]): number {
    let L: number = 0;
    let R: number = nums.length;
    let mid: number = Math.floor((L + R) / 2);

    let left: number | undefined = nums[mid - 1];
    let right: number | undefined = nums[mid + 1];

    // while mid is not peak
    while (
        (left && left > nums[mid])
        || (right && right > nums[mid])
    ) {
        // slopes up to the left
        if (left && left > nums[mid]) {
            R = mid - 1;
        } 
        
        // slopes up to the right
        else if (right && right > nums[mid]) {
            L = mid + 1;
        };

        mid = Math.floor((L + R) / 2);
        left = nums[mid - 1];
        right = nums[mid + 1];
    };

    return mid;
};
