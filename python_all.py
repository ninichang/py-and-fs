# python script 大全

# 雞兔同籠
n = input()
nlist = n.split()
nfst = int(nlist[0])
nsnd = int(nlist[1])
anslist = []   

for i in range(0 ,nfst+1):
    rhead = nfst - i
    if nsnd == rhead * 4 + i * 2:
        anslist.append(i)
        anslist.append(rhead)
if anslist == []:
    print('NO')
else:
    ans1 = int(anslist[0])
    ans2 = int(anslist[1])
    print('YES')
    print(ans1, ans2)
    
    
# 單位換算，打，dozen
n = eval(input())
if n % 12 == 0:
    print('%d dozen'%(n/12))
else:
    print('%d dozen and %d' %(n/12,n%12))
    
    
# 判斷成績是否及格 III
while True:
    roll=eval(input())
    if roll!=1 and roll!=2:
        print('roll error')
        break
    score=input()
    if roll==1:
        while True:
            if(int(score)<0)or(int(score)>100):
                print('score error')
                break
            elif(int(score)<60):
                print('fail')
                break
            else:
                print('pass')
                break
        break
    elif roll==2:
        while True:
            if(int(score)<0)or(int(score)>100):
                print('score error')
                break
            elif(int(score)<70):
                print('fail')
                break
            else:
                print('pass')
                break
        break


        
# 1 加到 n 

"""  
this is my code

n = eval(input())
total = 0
for i in range(1, n+1):
    total += i
    if (i <= (n - 1)):
        print(i,'+',end = '')
    else: 
        print(i, end = '')
print(' =' , total)

""" 

n = eval(input())
total = 0

for i in range (1, 1+n):
    total += i
    print(i, end = '')
    if(i < (n)):
        print('+', end = '')
print(' =', total)
        

    
# 直到輸入q後程式結束 -while

while True:
    x=input()
    print(x)
    if x=='q':
        break
        
        
        
# 豪華聖誕樹

k = eval(input())
for p in range(1,k):
    print(' ', end = '')
print('*')
for box in range(1,k-2+1):
    for item in (2*box-1,2*box+1,2*box+3):
        for spaceAmount in range(1, int(k-(item-1)/2)):
            print(' ', end = '')
        for pitem in range(1,item+1):
            print('^', end = '')
        print()
for b in range(1, k-1):
    for a in range(1, int((k+3)/2)):
        print(' ', end = '')
    for c in range(k-2):
        print('#', end = '')
    print()
    
    
    
# 數字轉文字輸出(中文大寫數字輸出)

n = eval(input())
while True:
    if n < 1 or n > 99999:
        print('out of range')
        break
    n1 = n//10000
    n2 = (n-n1*10000)//1000
    n3 = (n-n1*10000-n2*1000)//100
    n4 = (n-n1*10000-n2*1000-n3*100)//10
    n5 = (n-n1*10000-n2*1000-n3*100-n4*10)
    for i in (n1, n2, n3, n4, n5):
        if i==0:
            continue
        if i==1:
            print('壹', end = '')
            if n1>0:
                print('萬', end = '')
                n1 = 0
                continue     
            if n2>0:
                print('仟', end = '')
                n2 = 0
                continue
            if n3>0:
                print('佰', end = '')
                n3 = 0
                continue
            if n4>0:
                print('拾', end = '')
                n4 = 0
                continue
        if i==2:
            print('貳', end = '')
            if n1>0:
                print('萬', end = '')
                n1 = 0
                continue     
            if n2>0:
                print('仟', end = '')
                n2 = 0
                continue
            if n3>0:
                print('佰', end = '')
                n3 = 0
                continue
            if n4>0:
                print('拾', end = '')
                n4 = 0
                continue
        if i==3:
            print('參', end = '')
            if n1>0:
                print('萬', end = '')
                n1 = 0
                continue     
            if n2>0:
                print('仟', end = '')
                n2 = 0
                continue
            if n3>0:
                print('佰', end = '')
                n3 = 0
                continue
            if n4>0:
                print('拾', end = '')
                n4 = 0
                continue
        if i==4:
            print('肆', end = '')
            if n1>0:
                print('萬', end = '')
                n1 = 0
                continue     
            if n2>0:
                print('仟', end = '')
                n2 = 0
                continue
            if n3>0:
                print('佰', end = '')
                n3 = 0
                continue
            if n4>0:
                print('拾', end = '')
                n4 = 0
                continue
        if i==5:
            print('伍', end = '')
            if n1>0:
                print('萬', end = '')
                n1 = 0
                continue     
            if n2>0:
                print('仟', end = '')
                n2 = 0
                continue
            if n3>0:
                print('佰', end = '')
                n3 = 0
                continue
            if n4>0:
                print('拾', end = '')
                n4 = 0
                continue
        if i==6:
            print('陸', end = '')
            if n1>0:
                print('萬', end = '')
                n1 = 0
                continue     
            if n2>0:
                print('仟', end = '')
                n2 = 0
                continue
            if n3>0:
                print('佰', end = '')
                n3 = 0
                continue
            if n4>0:
                print('拾', end = '')
                n4 = 0
                continue
        if i==7:
            print('柒', end = '')
            if n1>0:
                print('萬', end = '')
                n1 = 0
                continue     
            if n2>0:
                print('仟', end = '')
                n2 = 0
                continue
            if n3>0:
                print('佰', end = '')
                n3 = 0
                continue
            if n4>0:
                print('拾', end = '')
                n4 = 0
                continue
        if i==8:
            print('捌', end = '')
            if n1>0:
                print('萬', end = '')
                n1 = 0
                continue     
            if n2>0:
                print('仟', end = '')
                n2 = 0
                continue
            if n3>0:
                print('佰', end = '')
                n3 = 0
                continue
            if n4>0:
                print('拾', end = '')
                n4 = 0
                continue
        if i==9:
            print('玖', end = '')
            if n1>0:
                print('萬', end = '')
                n1 = 0
                continue     
            if n2>0:
                print('仟', end = '')
                n2 = 0
                continue
            if n3>0:
                print('佰', end = '')
                n3 = 0
                continue
            if n4>0:
                print('拾', end = '')
                n4 = 0
                continue
    print('元整')
    break
    
    
    
# 身分證檢驗

n = input()
n = n.upper()
if len(list(n)) != 10:
    print('fake')
else:
    first = n[0] 
    dic = {'A':10,'J':18,'S':26,
     'B':11,'K':19,'T':27,
     'C':12,'L':20,'U':28,
     'D':13,'M':21,'V':29,
     'E':14,'N':22,'W':32,
     'F':15,'O':35,'X':30,
     'G':16,'P':23,'Y':31,
     'H':17,'Q':24,'Z':33,
     'I':34,'R':25}
    firstnum = (dic[first])
    firstnum01 = (firstnum//10)
    firstnum02 = (firstnum%10)
    lettersum = firstnum01*1+firstnum02*9
    k = lettersum + int(n[1])*8 + int(n[2])*7 + int(n[3])*6 + int(n[4])*5 + int(n[5])*4 + int(n[6])*3 + int(n[7])*2 + int(n[8])*1 + int(n[9])*1
    if k%10 == 0:
        print('real')
    else:
        print('fake')
        
        
        
# n 階乘
n = eval(input())
total = 1
for i in range (1,n+1):
    total *= i
print(total)



# 三角形判斷
a = eval(input())
b = eval(input())
c = eval(input())
if a+b>c and b+c>a and a+c>b:
    print('True')
    if a>b and a>c:
        if a*a == b*b + c*c:
            print('Right Triangle')
    elif b>c and b>a:
        if b*b == a*a + c*c:
            print('Right Triangle')
    elif c>a and c>b:
        if c*c == a*a + b*b:
            print('Right Triangle')
    else:
        print('Non-Right Triangle')
else:
    while True:
        print('False')
        break
        
        
# 三角數字列印

'''
印出
1  
2  3  4  
5  6  7  8  9  10  
三角形的函式
(但還是需要修改, 這邊 kplus 數量不對)

n = eval(input())
k = 0
if n == 1:
    while True:
        print('1')
        break
else:
    for j in range (1,n+1):
        for i in range (1,j+1):
            for kplus in range(1,i+1):
                k += 1
                print (k, ' ',end = '')
        print()    
'''

n = eval(input())
k = 0
if n == 1:
    while True:
        print('1')
        break
else:
    for j in range (1,n+1):  # 幾行
        for i in range (1,j+1): # 印幾個數字
            for p in range(1,2): # p 永遠都是1
                k += 1
                print (k, ' ', end = '') 
        print()
        
# 但這個答案是錯的，正確答案在下面
        

n = eval(input())
k = 0
if n == 1:
    while True:
        print('1')
        break
else:
    for j in range (1,n+1):
        for i in range (1,j+1):
            for p in range(1,2):
                k += 1
                print (k, ' ', end = '',sep='')#因為你沒設定這邊的sep=''，不然這樣會多出一個空白
        print()
#空白太多了！



# 2到m之間的質數
n = eval(input())
for nums in range(1, n+1):
    fct = 0
    for i in range(1,n+1):
        if nums%i ==0:
            fct += 1
    if fct ==2:
        print(nums, 'is prime')
        
        
        
# 猜數字進階版-終極密碼
m = eval(input())
ansMax=100
ansMin=1
guessAnswer = m
guessNum=0
while guessNum != guessAnswer:
    print(ansMin, '< ? <',ansMax)
    guessNum=eval(input())
    if guessNum > ansMin and guessNum < ansMax:
        if guessNum > guessAnswer:
            print('wrong answer, guess smaller')
            ansMax = guessNum
        elif guessNum < guessAnswer:
            print('wrong answer, guess larger')
            ansMin = guessNum
        else:
            print('bingo answer is', m)
            
            
            
# 公司大危機

# 這是比較慢的作法
'''
n = eval(input())
nStart = input()
m = eval(input())
nLeave = input()
leaveIndexLst = []
leftLst = []
nStartLst = list(nStart.split())
leaveLst = list(nLeave.split())
for index in leaveLst:
    leaveIndex = int(index)-1
    leaveIndexLst.append(leaveIndex)
leaveIndexLst.sort()

for i in nStartLst:
    if len(leaveIndexLst) == 0:
        leftLst.append(i)
        continue
    for j in leaveIndexLst:
        if nStartLst.index(i) == j:
            leaveIndexLst.remove(j)
            break
        else:
            if leftLst.count(i) == 1 and nStartLst.count(i) == 1 :
                break
            else:
                leftLst.append(i)
sumLeftLst = 0                
for i in leftLst:
    sumLeftLst += int(i)
leftLst.sort(key=int)
bigNum = leftLst[len(leftLst)-1]
bigNumIndex = nStartLst.index(bigNum)+1
print(sumLeftLst, end = '\n')
print(bigNumIndex, end = ' ')
print(bigNum, end = '\n')
'''

# 比較快的作法:把撤資人數的金額換成零，這樣就不用一直sort
n = eval(input())
nStart = input()
m = eval(input())
nLeave = input()
leaveIndexLst = []
nStartLst = list(nStart.split())
leaveLst = list(nLeave.split())
for index in leaveLst:
    leaveIndex = int(index)-1
    leaveIndexLst.append(leaveIndex)
for i in nStartLst:
    for j in leaveIndexLst:
        if nStartLst.index(i) == j:
            nStartLst.remove(i)
            nStartLst.insert(j,0)
            break
nStartLstNew = []

# 把原本 list of string 轉換成 list of int
for i in nStartLst:
    nStartLstNew.append(int(i))
maxNum = max(nStartLstNew)
print(sum(nStartLstNew), end = '\n')
print(nStartLstNew.index(maxNum)+1,end = ' ')
print(maxNum, end = '\n')


# 但是雙層迴圈仍然不夠快，最快的是這個做法


# 公司大危機

n=int(input())
Money_List=[int(x) for x in input().strip().split()]

#這是小迴圈，把所有的list中元素轉成int，
#但是如果不會這樣寫的話，可以用一般for迴圈來處理

m=int(input())
Leave=[int(x) for x in input().strip().split()]
 
if 0 in Leave: #老師題目出錯，可能會有第0位的人，但事實上不存在，我們要把它去除
    Leave.remove(0)

for i in Leave:#把離開的人金額歸零
    Money_List[i-1] = 0

total = sum(Money_List)
Max = max(Money_List)
Max_Position = Money_List.index(Max) + 1
 

print("%d\n%d %d"%(total,Max_Position,Max))




# 成績計算與列印-二維陣列-輸入版

a = input()
b = input()
c = input()
d = input()
e = input()
a1 = a.strip().split()
b1 = b.strip().split()
c1 = c.strip().split()
d1 = d.strip().split()
e1 = e.strip().split()
sumValLst = []
avgLst =[]
for m in (a1,b1,c1,d1,e1):
    val = int(m[0])+int(m[1])+int(m[2])
    sumValLst.append(val)
    avg = val/3
    avgLst.append(avg)
sumSum = 0
for i in sumValLst:
    sumSum += int(i)
gradeLst = [a1,b1,c1,d1,e1]
for i in range(5):
    print('student',i+1,end = '\n')
    for j in gradeLst:
        print(' 1:', j[0])#前面少一個空格
        print(' 2:', j[1])#前面少一個空格
        print(' 3:', j[2])#前面少一個空格
        gradeLst.remove(j)
        break
    print(' sum:',sumValLst[i], end = '\n')#前面少一個空格
    print(' avg:','%.2f'%(avgLst[i]), end = '\n')#前面少一個空格
print('total:',sumSum, end = '')
print(', avg: %.2f'%(sumSum/15), end = '\n')
avgLst2 = avgLst.copy()
avgLst2.sort()
stu = avgLst.index(avgLst2[4])+1
print
print('highest avg: student', stu, end = '')
print(': %.2f'%(avgLst2[4]), end = '\n')



# Set 找出兩籃水果中沒有重複的水果
itemsA = {"蘋果","香蕉","鳳梨","芭樂"}
itemsB = {"鳳梨","蘋果","水梨","蓮霧"}

iA01 = input()
iA02 = input()
iB01 = input()
iB02 = input()

itemsA.add(iA01)
itemsA.add(iA02)
itemsA.remove('蘋果')
iAlist = list(itemsA)
iAlist.sort()
print('iA:',iAlist)

itemsB.add(iB01)
itemsB.add(iB02)
itemsB.remove('蓮霧')
iBlist = list(itemsB)
iBlist.sort()
print('iB:',iBlist)

u = itemsA.union(itemsB)
ulist = list(u)
ulist.sort()
print('union:', ulist)

intersec = itemsA.intersection(itemsB)
intersecLst = list(intersec)
intersecLst.sort()
print('intersection:',intersecLst)

dif01 = list(itemsA.difference(itemsB))
dif01.sort()
print('A diff B:', dif01)

dif02 = list(itemsB.difference(itemsA))
dif02.sort()
print('B diff A:', dif02)

ansXor = u - intersec
lst = list(ansXor)
lst.sort()
print('A xor B:', lst)



# dict字典練習II (C++ STL map)

dict01 = {'P':'Pikachu', 'M':'Mickey Mouse', 'H':'Hello kitty'}
while True:
    n = input()
    if n == '-1':
        break
    elif n in dict01:
        print(dict01[n])
        continue
    elif n not in dict01:
        print(n, 'does not exist. Enter a new one:')
        m = input()
        dict01[n] = m
        
        

# AB猜數字遊戲

ans = input()
ansInt = eval(ans)
ans1 = ansInt//1000
ans2 = (ansInt - ans1*1000)//100
ans3 = (ansInt - ans1*1000 - ans2*100)//10
ans4 = ansInt - ans1*1000 - ans2*100 - ans3*10
ansLst = [ans1, ans2, ans3, ans4]
while True:
    guess = input()
    guessInt = eval(guess)
    if guessInt == ansInt:
        print('4A0B', end = '\n')
        print('You Win!')
        break
    else:
        g1 = guessInt//1000
        g2 = (guessInt - g1*1000)//100
        g3 = (guessInt - g1*1000 - g2*100)//10
        g4 = guessInt - g1*1000 - g2*100 - g3*10
        gLst = [g1, g2, g3, g4]
        act = 0
        bct = 0    
        for g in range(4):
            for ans in ansLst:
                if gLst[g] == ans:
                    if g == ansLst.index(ans):
                        act += 1
                        continue
                    else: 
                        bct += 1
                        continue
        bMinus = 0
        for n in gLst:
            if ansLst.count(n) > 0 and gLst.count(n) > 1:
                bMinus = gLst.count(n)-1
        bct -= bMinus
        print(act,end='')
        print('A',end='')
        print(bct,end='')
        print('B',end='\n')
        continue
        
        
        
# 阿宅的書單
nlst = []
m1 = input()
m = m1.lower()
while True:
    n = input()
    if n == 'q':
        if nlst.count(m) != 0:
            print('Yes',end = ' ')  # 考試時要注意大小寫
            print(nlst.index(m)+1)
            break
        else:
            sumN = 0
            for i in nlst:
                sumN += 1
            print('No',end = ' ')
            print(sumN)
            break
    else:
        nlst.append(n)
        
        
        
# 小當家買食材
n1 = eval(input())
lst = []
dict01 = {}
for i in range(n1):
    n2 = input()
    n3 = n2.strip().split()
    lst.append(n3)
for i in lst:
    if i[0] not in dict01:
        dict01[i[0]] = i[1]
    else:
        y = int(dict01[i[0]]) + int(i[1])
        dict01[i[0]] = y
keyLst =[]
valueLst =[]
for i in dict01:
    keyLst.append(i)
    valueLst.append(int(dict01[i]))
valueLst2 = valueLst.copy()
valueLst2.sort()
ans = valueLst2[(len(valueLst2)-1)]
ansIndex = valueLst.index(ans)
print(keyLst[ansIndex],ans, end = '\n')



# 文字外殼包裝
lst = []
lenlst = []
while True:
    n = input()
    if n == '-1':
        break
    n.strip().split(sep = ' ')
    lst.append(n)
sym = input()
for i in lst:
    lenlst.append(len(i))
maxLen = max(lenlst)
for pFst in range(maxLen+2):
    if pFst == maxLen+1:
        print(sym, end = '\n')
    else:
        print(sym, end = '')
for p in lst:
    print(sym, end = '')
    print(p,end = '')
    for space in range(maxLen-len(p)):
        print(' ',end ='')
    print(sym)
for pLast in range(maxLen+2):
    if pLast == maxLen+1:
        print(sym, end = '\n')
    else:
        print(sym,end='')
        
        
        
# 高山與盆地
n = eval(input())
n1 = input()
nlst = n1.strip().split(sep = ' ')
nlst2 = nlst.copy()
nlst2.sort(key=int)
bigAns = nlst2[len(nlst) - 1]
bigNum = nlst.index(bigAns)+1
smaAns = nlst2[0]
smaNum = nlst.index(smaAns)+1
print(bigNum, bigAns, end = '\n')
print(smaNum, smaAns, end = '\n')


# 標準函式庫
import time
n = eval(input())
print(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(n)))
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(n)))



# 系統內建os模組練習
import shutil
import os
n = eval(input())
if os.path.exists('files'):
    shutil.rmtree('files')
os.mkdir('files')
os.chdir('files')
for i in range(1,(n+1)):
    os.mkdir('f'+ str(i))
folder = os.listdir()
folder.sort()
print(folder)
os.rename('f1','folder1')
folder2 = os.listdir()
folder2.sort()
print(folder2)
os.rmdir('folder1')
folder3 = os.listdir()
folder3.sort()
print(folder3)



# 矩陣相乘-函式練習
a1 = input().strip().split(sep = ' ')
a2 = input().strip().split(sep = ' ')
a3 = input().strip().split(sep = ' ')
b1 = input().strip().split(sep = ' ')
b2 = input().strip().split(sep = ' ')
b3 = input().strip().split(sep = ' ')
alst = [a1,a2,a3]
blst = [b1,b2,b3]
a = alst
b = blst
def matrixMultiPly(a, b) :
    anslst = []
    for m in range(3):
        for n in range(3):
            for k in range(3):
                anslst.append(int(alst[m][k]) * int(blst[k][n]))
    anslst1 = []
    for a in range(0,len(anslst),3): 
        anslst1.append(anslst[a]+anslst[a+1]+anslst[a+2])
    anslst2 = [anslst1[0],anslst1[1],anslst1[2]]
    anslst3 = [anslst1[3],anslst1[4],anslst1[5]]
    anslst4 = [anslst1[6],anslst1[7],anslst1[8]]
    return [anslst2,anslst3,anslst4]
c = matrixMultiPly(a,b)
for i in c:
    print(i,end = '\n')
    
    
# 這題不知道為何批改系統顯示錯誤，以下為助教給的答案

def matrixMultiPly(a,b):
    n=len(a)
    c=[[0]*n for row in range(n)]
    for i in range(0, n):
        for j in range(0, n):
            for k in range(0, n):
                c[i][j]=int(c[i][j])+int(a[i][k])*int(b[k][j])
    return c
 
a1 = input().strip().split()
a2 = input().strip().split()
a3 = input().strip().split()
a = [a1,a2,a3]
 
b1 = input().strip().split()
b2 = input().strip().split()
b3 = input().strip().split()
b = [b1,b2,b3]
 
c=matrixMultiPly(a, b)
for i in c:
    print(i)
 


# 部落的結合
file1 = input()
file2 = input()
f1txt = '../app/' + file1
f2txt = '../app/' + file2

f1 = open(f1txt,'r')
txtLst1 = f1.readlines()
f1.close()
lst = [] 
for i in range(len(txtLst1)):
    txtLst1[i] = txtLst1[i].strip().split()
for i in (txtLst1[0]):
    lst.append(int(i))

f1 = open(f2txt,'r')
txtLst2 = f1.readlines()
f1.close()
for i in range(len(txtLst2)):
    txtLst2[i] = txtLst2[i].strip().split()
for i in (txtLst2[0]):
    lst.append(int(i))
lst.sort()
for i in lst:
    if lst.index(i) == len(lst)-1:
        print(i, end = '')
        print(' ', end = '\n')
    else:
        print(i, end = '')
        print(' ', end = '')
        
        

# 讀寫*.csv檔 (檢查一組標準輸出與檔案輸出)

# ./stores_old.csv
f1 = open ('stores_old.csv', 'r', encoding = 'big5')
txtLst = f1.readlines()
f1.close()
for i in range(len(txtLst)):
    txtLst[i] = txtLst[i].strip()
for i in range(len(txtLst)):
    txtLst[i] = txtLst[i].split(',')
a=txtLst[0].index('sid')
b=txtLst[0].index('name')
c=txtLst[0].index('tel')
d=txtLst[0].index('wifi')
    
# .／stores_new.csv
f2 = open ('stores_new.csv', 'w', encoding = 'utf-8')
for i in txtLst:
    f2.write(i[a])
    f2.write(',')
    f2.write(i[b])
    f2.write(',')
    f2.write(i[c])
    f2.write(',')
    f2.write(i[d])
    f2.write('\n')
f2.close()

f3 = open('stores_new.csv', 'r', encoding = 'utf-8')
txtLst2 = f3.readlines()
f3.close()
for i in range(len(txtLst2)):
    txtLst2[i] = txtLst2[i].strip()
for i in range(len(txtLst2)):
    txtLst2[i] = txtLst2[i].split(',')
for i in txtLst2:
    print(i[0],end = '')
    print(',',end = '')
    print(i[1],end = '')
    print(',',end ='')
    print(i[2],end = '')
    print(',',end ='')
    print(i[3],end = '')
    print(',',end ='\n')
    
    

# 讀取txt-尋找班上黑馬(Dark Horse)

file1 = input()
file2 = input()
f1txt = './3035/' + file1   #../app/MathScoreMid01.txt    
f2txt = './3035/' + file2    # ../app/MathScoreFinal01.txt    

f1 = open(f1txt,'r')
txtLst1 = f1.readlines()
f1.close
stu = []
lst1 = [] 
lst2 = []
lst3 = []
for i in range(len(txtLst1)):
    txtLst1[i] = txtLst1[i].strip().split(sep = ',')

txtLst1.pop(0)

for i in txtLst1:
    lst1.append(int(i[1]))
    stu.append(i[0])

f1 = open(f2txt,'r')
txtLst2 = f1.readlines()
f1.close()

for i in range(len(txtLst2)):
    txtLst2[i] = txtLst2[i].strip().split(sep = ',')
txtLst2.pop(0)

for i in txtLst2:
    lst2.append(int(i[1]))
for i in range(len(lst2)):
    lst3.append(lst2[i]-lst1[i])
maxScore = max(lst3)
stuLst = []
print('Dark Horse: ', end = '')
if lst3.count(maxScore) > 1:
    for i in range(lst3.count(maxScore)):
        stuLst.append(stu[lst3.index(maxScore)])
        maxInd = lst3.index(maxScore)
        lst3.pop(maxInd)
        lst3.insert(maxInd,0)
        stuLst.sort()
    for i in stuLst:
        if stuLst.index(i) == len(stuLst)-1:
            print(i, end = '\n')
        else:
            print(i, end = '')
            print(' & ', end = '')
else:
    print(stu[lst3.index(maxScore)], end = '\n')
print('%.1f ' %(maxScore), end = '')
print('Points Progress', end = '\n')




# 讀寫*.csv檔

f1 = open ('stores_old.csv', 'r', encoding = 'big5')
txtLst = f1.readlines()
f1.close()
for i in range(len(txtLst)):
    txtLst[i] = txtLst[i].strip()
for i in range(len(txtLst)):
    txtLst[i] = txtLst[i].split(',')
a=txtLst[0].index('sid')
b=txtLst[0].index('name')
c=txtLst[0].index('tel')
d=txtLst[0].index('wifi')
for elemLst in txtLst:
    print(elemLst[a],end = '')
    print(',',end = '')
    print(elemLst[b],end = '')
    print(',',end = '')
    print(elemLst[c],end = '')
    print(',',end = '')
    print(elemLst[d],end = '')
    print(',')
    
    
    
# 讀寫*.csv檔 並回傳 set

f1 = open('../app/math_list.csv','r',encoding = 'big5')
lst1 = f1.readlines()
f1.close()
setNum1 = set()
for i in range(len(lst1)):
    lst1[i] = lst1[i].strip().split(sep = ',')
    setNum1.add(lst1[i][0])
setNum1.remove('學號')

f2 = open('../app/english_list.csv','r',encoding = 'big5')
lst2 = f2.readlines()
f2.close()
setNum2 = set()
      
for i2 in range(len(lst2)):
    lst2[i2] = lst2[i2].strip().split(sep = ',')
    setNum2.add(lst2[i2][0])
setNum2.remove('學號')

ans1 = list(setNum1.intersection(setNum2))
ans1.sort()
ans2 = list(setNum1.union(setNum2)-setNum1.intersection(setNum2))
ans2.sort()
ans3 = list(setNum1.difference(setNum2))
ans3.sort()
ans4 = list(setNum2.difference(setNum1))
ans4.sort()
ans5 = list(setNum1.union(setNum2))
ans5.sort()

print(ans1)
print(ans2)
print(ans3)
print(ans4)
print(ans5)


# 例外處理-兩數相除

while True:
    try:
        a = eval(input())
        b = int(input())
        c = a/b
        print('%d/%d = %.2f' %(a, b, c))
        break
    except ZeroDivisionError:
        print('ZeroDivisionError')
    except SyntaxError:
        print('SyntaxError')
    except NameError:
        print('NameError')
    except ValueError:
        print('ValueError')
        
        
        
# 類別練習II 找出平均最高分

# 原本的答案系統說錯誤，因為空格問題
class student:
    def __init__ (self, name, gender,):
        self.Name = name
        self.Gender = gender
        self.Grades = []
        
    def avg(self):
        return sum(self.Grades) / len(self.Grades)
    def add(self, score):
        self.Grades.append(score)
    def fcount(self):            # 不及格的數量
        fct = 0
        for i in range(len(self.Grades)):
            if self.Grades[i] < 60:
                fct += 1
        return fct
    def info(self):
        infoAll = (self.Name,self.Gender,self.Grades,self.avg(),self.fcount())
        return infoAll

s1 = student("Tom","M")
s2 = student("Jane","F")
s3 = student("John","M")
s4 = student("Ann","F")
s5 = student("Peter","M")
s1.add(80)
s1.add(90)
s1.add(55)
s1.add(77)
s1.add(40)
s2.add(58)
s2.add(87)
s3.add(100)
s3.add(80)
s4.add(40)
s4.add(55)
s5.add(60)
s5.add(60)

def top(a):
    maxAvg = 0
    maxStu = ()
    for i in a:
        if int(i[3]) > maxAvg:
            maxAvg = int(i[3])
            maxStu = i
    return maxStu

for i in (s1,s2,s3,s4,s5):
    print('Name: ', end='')
    print(i.Name)
    print('Gender: ',end='')
    print(i.Gender)
    print('Grades: ', end='')
    print(i.Grades)
    print('Avg: ',end='')
    print(i.avg())
    print('Fail Number: ',end = '')#少了空格，您寫成'Fail Number:'
    print(i.fcount(), end = '')
    print('\n')

k = (s1.info(),s2.info(),s3.info(),s4.info(),s5.info())
print('Top Student:',end='\n')#多了空格，您寫成'Top Student: '
print('Name: ',end='')
print(top(k)[0])
print('Gender: ',end='')
print(top(k)[1])
print('Grades: ',end='')
print(top(k)[2])
print('Avg: ',end ='')
print(top(k)[3])
print('Fail Number: ',end='')
print(top(k)[4],end='')
print('\n')

    
    

