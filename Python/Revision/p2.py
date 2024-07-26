cnt=1
def doThis():
    global cnt
    for i in (1,2,3):
        cnt+=1
doThis()
print(cnt)
