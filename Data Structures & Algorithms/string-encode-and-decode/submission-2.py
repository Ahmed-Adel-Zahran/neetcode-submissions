class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_output = ""
        for string in strs:
            encoded_output = encoded_output + str(len(string)) + "#" + string
        print(encoded_output)
        return encoded_output
        


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        if(len(s) == 0):
            return res
        
        while i < len(s):
            j = i #points at position in the string
            while (s[j] != "#"): # while instead of if to keep incremeinting regardless of the top loop 
                j +=1 #While there are no delimiters , keep traversing through the string 
            size = int(s[i:j]) #When you find a # the the size = substring between i and j (right before the #, s[j] is the #)
            i = j + 1 # move i to beggining of the string 
            j = i + size # move j to the end of the string 
            word = s[i : j] # get the substring between i and j , this is the string 
            print(word)
                
            res.append(word) # appends it to the list 
            i = j # move i to j (from beggining of word to end of word) to move to the next word 
                
                       
        return res
