class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # intinal max = -1
        # reverse traversal
        # max = max(max_right , arr(i)) 

        right_max = -1
        for i in range(len(arr)-1,-1,-1):
            new_max =  max(right_max,arr[i])
            arr[i] = right_max
            right_max = new_max
        return arr





            