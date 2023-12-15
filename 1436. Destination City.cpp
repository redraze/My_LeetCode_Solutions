class Solution {
public:
    string destCity(vector<vector<string>>& paths) {
        unordered_set<string> starting_cities;

        for (auto &path : paths) {
            starting_cities.insert(path[0]);
        };

        unordered_set<string>::const_iterator end = starting_cities.end();
        for (auto &path : paths) {
            if (starting_cities.find(path[1]) == end) {
                return path[1];
            };
        };

        return paths[0][0];
    };
};
