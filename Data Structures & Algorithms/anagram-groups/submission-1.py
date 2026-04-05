class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = list()
        dictionary = dict()
        if(len(strs) == 0):
            return [[""]]
        elif (len(strs)==1):
            return [strs]
        else:
            for str1 in range (len(strs)):
                key = tuple(sorted(strs[str1]))
                if key not in dictionary:
                    dictionary[key] = []
                dictionary[key].append(strs[str1])
                print (dictionary)
    
            result = list(dictionary.values())

        return result