import random
team = 'ABCDEFGHIJK'
result = {}
batting = ['.',1,2,3,4,6,'w']
umpire_decision = ['out','not out']
temp_strike1 = 0
score = 0
n = 0
q = 0
s = 0
for i in range(1,21):
    for j in range(1,7):
        if n == 11:
            break
        else:
            batsman = random.choice(batting)
            if batsman == '.':
                    pass
            elif batsman == 1:
                temp_strike1 += 1
            elif batsman == 2:
                temp_strike1 += 2
            elif batsman == 3:
                temp_strike1 += 3
            elif batsman == 4:
                temp_strike1 += 4
            elif batsman == 6:
                temp_strike1 += 6
            elif batsman == 'w':
                umpire = random.choice(umpire_decision)
                if umpire == 'not out':
                    pass
                else:
                    result[team[n]] = temp_strike1
                    score += temp_strike1
                    temp_strike1 = 0
                    n += 1
s = len(result)
if len(result) == 11:
    for k,v in result.items():
        q +=1
        if q <= 9:
            print(k,'-',v)
        else:
            print(k,'-',v,' NOT OUT')
    print('Total = ',score)
    
else:
    for k,v in result.items():
        q += 1
        if q <=len(result)-2:
            print(k,'-',v)
        elif q >=len(result)-2:
            print(k,'-',v,' NOT OUT')
    if len(result) <=10:
        for i in range(len(team)-len(result)):
            if s >10:
                pass
            else:
                print(team[s],'-')
                s += 1
    print('Total = ',score)