class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        lst=[]
        for i in asteroids: 
            while len(lst) and lst[-1]>0 and i<0:
                if i+lst[-1]==0:
                    lst.pop()
                    break
                elif(abs(i)<lst[-1]):
                    break
                else:
                    lst.pop()
                    continue
            else:
                 lst.append(i)
        return lst    