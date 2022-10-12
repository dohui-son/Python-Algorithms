def solution(arr1, arr2):
    ans = []
    for y in range(len(arr1)):
        tmp = [0]*len(arr2[0])
        for yy in range(len(arr2[0])):
            for x in range(len(arr1[0])):
                tmp[yy] += arr1[y][x]*arr2[x][yy]
        ans.append(tmp)
    return ans


def productMatrix(A, B):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]