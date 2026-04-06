class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # circular = 0 
        # square = 1
        count = [0, 0]
        for s in students:
            count[s] += 1
        
        for s in sandwiches:
            if count[s] > 0:
                count[s] -= 1
            else:
                break

        return count[0] + count[1]