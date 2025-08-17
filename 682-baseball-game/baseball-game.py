class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for val in operations:
            if val not in ["C", "D", "+"]:
                stack.append(int(val))
            elif val == "C":
                stack.pop()
            elif val == "D":
                stack.append(2 * stack[-1])
            elif val == "+":
                stack.append( int(stack[-1])+  int(stack[-2]) )

        sum = 0

        for number in stack:
            sum += number
        
        return sum