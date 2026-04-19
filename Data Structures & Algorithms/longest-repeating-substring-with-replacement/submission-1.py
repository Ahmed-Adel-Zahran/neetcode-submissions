class Solution:
    # We are essentially checking fo the longeset substring such that there is no more than k elements that are not identical 
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        # Use all possible uppercase English characters present in the string
        charSet = set(s)


        for c in charSet:
            l = 0 
            count = 0 
            for r in range(len(s)):
                # count of identical chars in window in string
                if s[r] == c:
                    count +=1
                
                #while the size of the window - the count of identical chars exceeds the number of moves (k)
                # basically if we can't make any more changes 
                while ((r - l + 1) - count > k):
                    #we slide the window to teh right and update the count
                    if s[l] == c:
                        count -=1
                    l +=1
                #t= the result is the max of the existing res and the size of the current valid window 
                res = max(res, r - l + 1)
        return res