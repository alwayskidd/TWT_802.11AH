import duty_cycle

def find_division(number,group,amount):
    print('start diviision with'+str([number,group,amount]))
#number: the duty-cycle needs to be divided into small one
#group: all the possible small duty-cycle can reach
#amount: how many STAs are in current duty-cycle
    import copy
    possible=[]
    for each in group:
        if (number%each)==0:
            possible.append(number//each)
    possible.sort()

    temp=[]
    temp.append([amount,[]])
    smallest=[amount,[]]

    while temp: #if temp is not an empty list
        current_state=temp.pop(0)
     #   print("amount left:"+str(current_state[0]))
    #    print("temp length:"+str(temp.__len__()))
        if current_state[0]<smallest[0]:
            smallest[1]=current_state[1]

        for each in possible:
            tmp_amount=current_state[0]
            for i in range(1,amount//each+1):
                division_list=copy.copy(current_state[1])
                tmp=each*i
                if tmp_amount-tmp>0:
                    for j in range (0,i):
                        division_list.append(each)
                    if not [x for x, y in enumerate(temp) if y[0]==tmp_amount-tmp]: #if the left amount has never appeared
                        temp.append([tmp_amount-tmp,division_list])
                if tmp_amount-tmp==0:
                    for j in range(0,i):
                        division_list.append(each)
                    return(division_list)
                if tmp_amount-each<0:
                    break

    for i in range (0,amount-sum(smallest[1])):
        smallest[1].append(1)
    #print(smallest[1])
    return smallest[1]

def new_table(cycle,table,division_list):
    index=[x for x, y in enumerate(table) if y.duty_cycle==cycle]
    #print(index[0])
    print("division list"+str(division_list))
    table.pop(index[0])
    division_list.sort()
    while division_list:
        tmp=division_list.pop()
        n=division_list.count(tmp)
        tmp=cycle//tmp
        index=[x for x, y in enumerate(table) if y.duty_cycle==tmp]
        if index:
            table[index[0]].amount+=(n+1)
            print("add "+str(n+1)+" onto "+str(table[index[0]].duty_cycle))
        else:
            table.append(duty_cycle.duty_cycle(tmp,n+1))
        #print(n)
        for i in range(0,n):
            division_list.pop()
        #print(division_list)
    table.sort(key=lambda x:x.duty_cycle)
    return(table)

def table_generate(n,scale,lower,upper):
    import random
    table=[]
    for i in range (lower,upper+1,scale):
        table.append(duty_cycle.duty_cycle(i,random.randint(1,n)))
    return(table)

table=table_generate(30,1,1,15)
for each in table:
    print('cycle='+str(each.duty_cycle)+'  amount='+str(each.amount))


temp=[]
for each in table:
    temp.append(each.duty_cycle)


for i in range(temp.__len__()-1,0,-1):
    group=[]
    for each in table:
        group.append(each.duty_cycle)
    number=temp[i]
    index=[x for x, y in enumerate(table) if y.duty_cycle==number]
    group.pop(index[0])
    division_list=find_division(number,group,table[index[0]].amount)
    table=new_table(number,table,division_list)
    for each in table:
        print('cycle='+str(each.duty_cycle)+'  amount='+str(each.amount))
