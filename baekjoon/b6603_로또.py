global k,n
l = []
k, n = 0, 0
def BT(cur, arr, start):
    if cur == 6: print(*arr)
    elif cur<k and start<n :
        for i in range(start, n):
            tmp = arr[cur]
            arr[cur] = l[i]
            BT(cur+1, arr, i+1)
            arr[cur] = tmp

while True:
    st = input().rstrip()
    if st == "0": break
    l = list( map(int, st.split()) )
    k = l[0]


    del l[0]
    l.sort()
    n = len(l)
    arr = [0]*6

    BT(0, arr, 0)
    print()
