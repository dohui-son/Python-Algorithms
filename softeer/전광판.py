import sys
reader = sys.stdin.readline
#도, 개, 걸, 윷, 모 로 각각 1, 2, 3, 4, 5칸
mal = []
score = [0,5,10,15,20,50,30,35,40,45,100,55,60,65,70,75,80,85,90,95,500,1000,275,250,150,125,175,150,300,350,400]
n = int(reader().rstrip())
ans = [0]*n
inp = []

def nextIdx( now, kan ):
  if now == 5: 
    if kan<=2: return 22+(kan-1)
    else : return 28 - (kan-3)
  elif now == 10:
    if kan<3: return 24 + (kan-1)
    else : return 28+(kan-3)
      
  if now==24 or now == 25:
    if now == 25: now = 24; kan +=1
    if kan == 1:return 25
    elif kan >= 5: return 20+(kan-5)
    else: return 28+(kan-2)

  if now == 27 or now == 26:
    if now == 26: now-=1; kan+=1
    if kan == 0: return now
    if kan==1: return 26
    else: return 15+(kan-2)
    
  if 28<= now <= 30  : #
    if now == 29: now -=1; kan+=1
    elif now == 30: now -=2; kan+=2
    if kan<=2: return now+kan
    if kan >= 4: return 21
    elif kan == 3: return 20
    
  if now == 22 or now == 23: #
    if now == 23: now = 22; kan+=1
    if kan==1: return 23
    if kan >= 5: return 15+(kan-5)
    else: return 28 - (kan-2)
  
  if now == 28:
    if kan<=2: return now+kan
    else: 
      if kan == 5 or kan ==4: return 21
      elif kan == 3: return 20
  if now < 21 : return now+kan if now+kan <= 21 else 21
  


def yoot(cur, ans_idx):
  global ans
  if cur == 10 or mal.count(21)==4 :
    summ = 0
    for i in range(4): summ += score[mal[i]]
    ans[ans_idx] = max(ans[ans_idx], summ )
  elif cur < 10:
    kan = inp[ans_idx][cur]
    for i in range(4):
      if mal[i] == 21:continue
      tmp = mal[i]
      res = nextIdx(tmp, kan)
      print(score[tmp], kan, score[res])
      if res in mal:continue
      mal[i] = res
      yoot(cur+1, ans_idx)
      mal[i] = tmp
      
for i in range(n):
  l = list(map(int,reader().split()))
  inp.append(l)
  mal = [0]*4
  yoot(0, i)
  
for i,val in enumerate(ans):
  st = "#"+str(i)
  print(st, ans[i])