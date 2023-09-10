# 양쪽 끝과 연결되어있음.
# 그래프가 없어도 되나?
# 모두 짝수 모두 홀수
n, m, k = map(int, input().split())

dy = [-1,-1,0,1,1,1,0,-1]
dx = [0,1,1,1,0,-1,-1,-1]

graph = [[[] for i in range(n)] for j in range(n)]

for i in range(m):
    r, c, m, s, d = map(int, input().split())
    graph[r-1][c-1].append([m, s, d])

# for e in graph:
#     print(e)
# print('')

def move():
    global n
    tmpGraph = [[[] for i in range(n)] for j in range(n)]
    # for i in range(n):
    #     for j in range(n):
    #         tmpGraph[i][j] = [e for e in graph[i][j]] # 점검 필요
    
    
    for y in range(n):
        for x in range(n):
            for i in range(len(graph[y][x])):
                # 없어졌을 경우, 다음 i는..?
                # 굳이 없애지 않아도 되나?
                ny = (y + graph[y][x][i][1]*dy[graph[y][x][i][2]])%n
                nx = (x + graph[y][x][i][1]*dx[graph[y][x][i][2]])%n

                tmpGraph[ny][nx].append(graph[y][x][i])
    
    for y in range(n):
        for x in range(n):
            if len(tmpGraph[y][x]) >= 2:
                lenBackUp = len(tmpGraph[y][x])
                sumOfM = 0
                sumOfS = 0
                directionFlag = 0
                for e in tmpGraph[y][x]:
                    sumOfM += e[0]
                    sumOfS += e[1]
                    directionFlag += (e[2])%2
                
                calcedM = sumOfM//5
                calcedS = sumOfS//lenBackUp

                tmpGraph[y][x] = []

                if calcedM == 0:
                    continue

                # 끝난뒤 directionFlag는 모두 홀수였다면 len
                # 모두 짝수였다면 0
                
                # len 구하기 전에 []으로 만들어놓은 실수
                if directionFlag == lenBackUp or directionFlag== 0:
                    for i in range(4):
                        tmpGraph[y][x].append([calcedM, calcedS, i*2])

                else:
                    for i in range(4):
                        tmpGraph[y][x].append([calcedM, calcedS, i*2+1])              
                
    for i in range(n):
        for j in range(n):
            graph[i][j] = [e for e in tmpGraph[i][j]]

def sumOfM():
    sum = 0
    for e in graph:
        for ee in e:
            for eee in ee:
                sum+=eee[0]
    return sum

for i in range(k):
    move()

#     for e in graph:
#         print(e)
#     print('')

print(sumOfM())