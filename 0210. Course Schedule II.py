# solution 1: iterative BFS with doubly-liked adjacency list
# O(n^2) time and space complexity
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return list(range(numCourses))

        # adjacency list has following format:
        # course_i: [prereqs, postreqs]
        adjList = {i: [set(), set()] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adjList[course][0].add(prereq)
            adjList[prereq][1].add(course)

        # queue courses that have no prereqs
        q = deque()
        for i in range(numCourses):
            if not adjList[i][0]:
                q.append(i)

        # iterative BFS
        ans, taken = [], set()
        while q:
            course = q.popleft()
            if not adjList[course][0]:
                if course not in taken:
                    ans.append(course)
                    taken.add(course)
                for postreq in adjList[course][1]:
                    try:
                        adjList[postreq][0].remove(course)
                    except KeyError:
                        pass
                    q.append(postreq)

        return ans if len(ans) == numCourses else []
