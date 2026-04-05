class Solution:
    def calPoints(self, operations: List[str]) -> int:
        total = []
        total_score = 0
        for i in range(len(operations)):
            operation = operations[i]
            if (operation == "+"):
                total.append(total[-1] + total[-2])
            elif (operation == "D"):
                total.append(int(total[-1]) * 2)
            elif (operation == "C"):
                total.pop()
            else:
                total.append(int(operations[i]))

            print(total)
        return sum(total)


             