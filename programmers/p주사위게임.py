def solution(monster, S1, S2, S3):
    die, suc, maxi = 0, 0, max(monster)
      
    for i in range(1, S1 + 1):
        for  j in range(1, S2 + 1):
            for k in range(1, S3 +1):
                if i + j + k > maxi: suc += 1
                elif (i + j + k + 1) in monster: die += 1
                else: suc += 1
    return int(suc / (die + suc) * 1000)