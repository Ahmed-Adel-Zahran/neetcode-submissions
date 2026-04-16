class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        most_common_list = count.most_common(k)
        print(most_common_list)
        i = 0
        output = []
        while i < k:
            pair = most_common_list[i]
            output.append(pair[0])
            i+=1
        return output
