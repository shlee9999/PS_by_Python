n = int(input())
parent = [i for i in range(26)] 

for _ in range(n):
    p, c = map(ord, input().split(" is "))
    p -= 97
    c -= 97
    parent[c] = p 

def find(start_node, target):
    while True:
        if start_node == target:
            return True
        if start_node == parent[start_node]:
            break
        start_node = parent[start_node]
        
    return False

m = int(input())
for _ in range(m):
    p, c = map(ord, input().split(" is "))
    p -= 97
    c -= 97
    print("T" if find(c,p) else "F")

        
    
