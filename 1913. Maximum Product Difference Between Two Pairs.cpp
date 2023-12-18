class Solution {
public:
    // O(n) time and O(1) space complexity
    int maxProductDifference(vector<int>& nums) {
        int minHeap[2];
        int maxHeap[2];

        if (nums[0] < nums[1]) {
            minHeap[0] = nums[0], minHeap[1] = nums[1];
            maxHeap[0] = nums[1], maxHeap[1] = nums[0];
        } else {
            minHeap[0] = nums[1], minHeap[1] = nums[0];
            maxHeap[0] = nums[0], maxHeap[1] = nums[1];
        };

        for (int i = 2; i < nums.size(); i++) {
            if (nums[i] < minHeap[0]) {
                minHeap[1] = minHeap[0];
                minHeap[0] = nums[i];
            } else if (nums[i] < minHeap[1]) {
                minHeap[1] = nums[i];
            };

            if (nums[i] > maxHeap[0]) {
                maxHeap[1] = maxHeap[0];
                maxHeap[0] = nums[i];
            } else if (nums[i] > maxHeap[1]) {
                maxHeap[1] = nums[i];
            };
        };

        cout << minHeap[0] << '\t' << minHeap[1] << '\n';
        cout << maxHeap[0] << '\t' << maxHeap[1] << '\n';

        return (maxHeap[0] * maxHeap[1]) - (minHeap[0] * minHeap[1]);

    // // O(n log n) time and O(n) space comlexity
    // int maxProductDifference(vector<int>& nums) {
    //     sort(nums.begin(), nums.end());
    //     int len = nums.size();
    //     return (nums[len - 1] * nums[len - 2]) - (nums[0] * nums[1]);
    };
};
