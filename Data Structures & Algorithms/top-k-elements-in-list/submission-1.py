class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        print(count)
        output = []
        '''
        i = 0
        while i < k:
            for key in count.keys():
                if count.get(key) >= k :
                    output.append(key)
            i++
            '''
        most_common_list = count.most_common(k)
        print(most_common_list)
        i = 0
        output = []
        while i < k:
            pair = most_common_list[i]
            print (pair)
            output.append(pair[0])
            i+=1

        return output
