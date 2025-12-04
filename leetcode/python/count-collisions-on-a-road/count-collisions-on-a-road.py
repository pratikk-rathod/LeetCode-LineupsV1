class Solution: 
    def countCollisions(self, directions: str) -> int:
        # BRUTE FORCE

        stack=[]
        colision=0
        for i in directions:
            # print(stack)
            if len(stack)==0:
                stack.append(i)
                continue
            
            if i == "L":
                if stack[-1] == "L":
                    stack.append("L")
                    continue
                elif stack[-1] == "S":
                    stack.append("S")
                    colision+=1
                    continue
                elif stack[-1] == "R":
                    # colision+=1
                    count=0


                    idx = len(stack) - 1
                    while idx >= 0 and stack[idx] == "R":
                        count += 1
                        idx -= 1
                    for j in range(count):
                        stack.pop()
                    colision+=(count)+1


                    stack.append("S")


                    # colision+=2
                    continue


            if i == "R":
                if stack[-1] == "R":
                    stack.append("R")
                    continue
                elif stack[-1] == "S":
                    stack.append("R")
                    # colision+=1
                    continue
                elif stack[-1] == "L":
                    # colision+=1
                    stack.append("R")
                    continue


            if i == "S":
                
                if stack[-1] == "R": 

                    count=0


                    idx = len(stack) - 1
                    while idx >= 0 and stack[idx] == "R":
                        count += 1
                        idx -= 1
                    for j in range(count):
                        stack.pop()
                    colision+=(count)


                    # stack.append("S")


                    stack.append("S")
                    # colision+=1
                    continue
                
                else:
                    stack.append("S")
                    continue


        return colision