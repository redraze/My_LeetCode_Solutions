class Solution {
public:
    vector<vector<int>> imageSmoother(vector<vector<int>>& img) {
        init(img);

        vector<vector<int>> ret(h, vector<int>(w, 0));

        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                ret[i][j] = findAverage(img, i, j);
            };
        };

        return ret;        
    };

private:
    int h;
    int w;
    void init(vector<vector<int>>& img) {
        h = img.size();
        w = img[0].size();
        return;
    };

    int range[3] = {-1, 0, 1};
    int findAverage(vector<vector<int>>& img, int& r, int& c) {
        int sum = 0;
        int count = 0;

        for (int &dr : range) {
            for (int &dc : range) {
                if (
                    (0 <= r + dr)
                    && (r + dr < h)
                    && (0 <= c + dc)
                    && (c + dc < w)
                ) {
                    sum += img[r + dr][c + dc];
                    count++;
                };
            };
        };

        return sum / count;
    };
};
