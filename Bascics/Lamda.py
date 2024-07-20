x=lambda i:i+10
print(x(3))

def shinchan(n):
    return lambda i:i*n
myShinchan=shinchan(2)
print(myShinchan(3))

square = {2: 4, -3: 9, -1: 1, -2: 4}

ans=max(square)
print(ans)

ans1=max(square,key=lambda i:square[i])
print(ans1)