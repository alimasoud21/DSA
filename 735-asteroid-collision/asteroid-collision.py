class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
    #[5,10,-5]
        for a in asteroids:

            while stack and stack[-1] > 0 and a < 0:
                if stack[-1] < -a:
                    stack.pop(-1)
                    continue
                elif stack[-1] == -a:
                    stack.pop(-1)

                break
            else:
                stack.append(a)
        
        return stack
            
                    

            
               
            
