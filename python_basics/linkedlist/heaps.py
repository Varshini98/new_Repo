from heapq import heappush,heappop,heapify,heapreplace

l = list(map(int,input().split()))
heapify(l)
print(l)
x=heappop(l)
print(l)
heapreplace(l,12)
heappush(-1,l)
print(l)

