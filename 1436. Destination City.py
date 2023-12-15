class Solution:
    # O(n) time and space complexity
    def destCity(self, paths: List[List[str]]) -> str:
        cities = set()
        trips = {}

        for trip in paths:
            cities.add(trip[0])
            cities.add(trip[1])
            trips[trip[0]] = trip[1]

        for city in cities:
            if city not in trips:
                return city
        
        return paths[0][0]
