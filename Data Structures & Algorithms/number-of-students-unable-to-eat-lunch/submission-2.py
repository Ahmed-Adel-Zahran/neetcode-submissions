class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # circular = 0 
        # square = 1
        preferences = Counter(students)
        counts_circ = preferences.get(0)
        counts_square = preferences.get(1)

        for s in sandwiches:
            if preferences[s] > 0:
                preferences[s] -= 1
            else:
                break

        return preferences[0] + preferences[1]