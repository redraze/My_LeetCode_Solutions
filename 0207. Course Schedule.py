class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # solution 1
        courses = defaultdict(set)
        for course, prereq in prerequisites:
            courses[course].add(prereq)

        for course, prereq in prerequisites:
            seen = {course}
            cursor = prereq
            while cursor in courses:
                if cursor in seen:
                    return False
                seen.add(cursor)
                if not courses[cursor]:
                    break
                cursor = courses[cursor].pop()
            if not courses[course]:
                del courses[course]
        return True
