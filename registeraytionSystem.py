
def func():
    n=int(input())
    count={}
    for i in range(n):
        s=input()
        if s in count:
            print(s+str(count[s]))
            count[s]+=1
            
        else:
            print("OK")
            count[s]=1

func()
    

