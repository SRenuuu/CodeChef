# cook your dish here
t = int(input())
while t:
    N, K = map(int, input().split())
    stairs = list(map(int, input().split()))
    count=0
    no=len(stairs)
    i=0
    while True:
        if stairs[0]>K:
            count+=1
            stairs.insert(0,stairs[0]-K)
        else:
            break

    while i<no-1:
        if(stairs[i+1]-stairs[i]>K):
            count+=1
            stairs.insert(i+1,stairs[i]+K)
        i+=1
        no=len(stairs)

    print(count)
    t-=1
