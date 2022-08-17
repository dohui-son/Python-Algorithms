load = [[1],[2],[3],[4],[5], [6,21],[7],[8],[9],[10], [11,25],[12],[13],[14],[15], [16,27], [17],[18],[19],[20], [32], [22],[23],[24],[30], [26],[24], [28],[29],[24], [31], [20], [32]]

points = [0,2,4,6,8, 10,12,14,16,18, 20,22,24,26,28, 30,32,34,36,38 ,40  ,13,16,19,25, 22,24, 28,27,26, 30,35, 0]

dices = list(map(int, input().split()))

result = 0
def check(horse, cnt, point):
  global result
  if cnt >= 10:
    result = max(result, point)
    return  
  for j in range(4):
    pos = horse[j]
    
    if len(load[pos]) > 1:
      pos = load[pos][1]
    else:
      pos = load[pos][0]

    for i in range(1, dices[cnt]):
      pos = load[pos][0]

    if pos == 32 or (pos <= 32 and (pos not in horse)):      
      before = horse[j]
      horse[j] = pos
      check(horse, cnt+1, point + points[pos])
      horse[j] = before              
      
check([0,0,0,0], 0, 0)

print(result)