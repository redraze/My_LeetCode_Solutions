class Solution {
// O(n) time and O(1) space complexity
public:
    int maxProduct(vector<int>& nums) {
        int first = nums[0];
        int second = nums[1];
        if (second < first) {
            swap(first, second);
        };

        for (int i = 2; i < nums.size(); i++) {
            if (nums[i] > first) {
                if (nums[i] > second) {
                    first = second;
                    second = nums[i];
                } else {
                    first = nums[i];
                };
            };
        };

        return (first - 1) * (second - 1);

    // // using std::make_heap
    // int maxProduct(vector<int>& nums) {
    //     vector<int> heap;
    //     for (int i = 0; i < 2; i++) {
    //         heap.push_back(nums[i]);
    //     };
    //     make_heap(heap.begin(), heap.end());

    //     for (int i = 2; i < nums.size(); i++) {
    //         if (nums[i] > heap[1]) {
    //             heap[1] = nums[i];
    //             make_heap(heap.begin(), heap.end());
    //         };
    //     };

    //     return (heap[0] - 1) * (heap[1] - 1);
    }
};
