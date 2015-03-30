import random
graph={}
visited={}
n=int(input('dwse diastaseis grafou :'))
while (n<0)and (n>30):
    n=int(input('dwse diastaseis grafou :'))
start_x=int(input('dwse arxh ekinhshs x :'))
while (start_x<0)and(start_x>30):
    start_x=int(input('dwse arxh ekinhshs x :'))
start_y=int(input('dwse arxh ekinhshs y :'))
while (start_y<0) and (start_y>30):
    start_y=int(input('dwse arxh ekinhshs y :'))
outputfile = input('dwse onoma arxeiou se morfh .txt: ')
for i in range(0,n+1):
    for j in range(0,n+1):
        visited[(i,j)]=False
        neib=[]
        if i==0:
            if j==0:
                neib.append((i,j+1))
                neib.append((i+1,j))
                graph[(i,j)]=neib
            elif j==n:
                neib.append((i,j-1))
                neib.append((i+1,j))
                graph[(i,j)]=neib
            else:
                neib.append((i,j-1))
                neib.append((i,j+1))
                neib.append((i+1,j))
                graph[(i,j)]=neib
        elif j==n:
             if i==0:
                 neib.append((i-1,j))
                 neib.append((i,j+1))
                 graph[(i,j)]=neib
             elif i==n:
                 neib.append((i,j-1))
                 neib.append((i-1,j))
                 graph[(i,j)]=neib
             else:
                 neib.append((i,j-1))
                 neib.append((i,j+1))
                 neib.append((i-1,j))
                 graph[(i,j)]=neib
        elif j==0:
              neib.append((i-1,j))
              neib.append((i+1,j))
              neib.append((i,j+1))
              graph[(i,j)]=neib
        elif j==n:
              neib.append((i-1,j))
              neib.append((i+1,j))
              neib.append((i,j-1))
              graph[(i,j)]=neib
        else:
              neib.append((i,j-1))
              neib.append((i,j+1))
              neib.append((i-1,j))
              neib.append((i+1,j))
              graph[(i,j)]=neib
              

arxeio = open(outputfile, 'w')




def bfs(adj, start, suche):
    
    oura = [ start ]
    visited = []
    while len(oura) > 0:
        shmeioa = oura.pop(0)
        visited.append(shmeioaa)
        if adj[shmeio]:
            for shmeiob in adj[shmeioa]:
                if shmeiob in visited:
                    continue
                if shmeiob == suche:
                    return True
                queue.append(shmeiob)
    return False
	
print(graph)
print(visited)
arxeio.close();
