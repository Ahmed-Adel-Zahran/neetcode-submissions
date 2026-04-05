class Solution:
    def isValid(self, s: str) -> bool:
        if(len(s) %2 != 0):
            return False

         # stack solution
        stack = []
        close_to_open = { ")" : "(" , "}" : "{" , "]" : "[" }

        for p in s: # for each parenthesis in the list 
            if p in close_to_open:  # if it's a closing bracket
                if stack and stack[-1] == close_to_open[p]: #then if it is in the stack and the end of the stack = to the opening bracket
                    stack.pop() # we pop the top of the stack , aka the opening bracket 
                else:
                    return False # it starts with a closed bracket
            else: #it is a new opeening bracket
                stack.append(p)
        return True if not stack else False

        # first solution to mind -- wrong coz this doesn't guarantee the correct order
        '''
        else:
            s_counter = Counter(s)
            if (s_counter.get('(') == s_counter.get(')') 
                and s_counter.get('{') == s_counter.get('}')
                and s_counter.get('[') == s_counter.get(']')):
                return True
            else:
                return False
        '''
       