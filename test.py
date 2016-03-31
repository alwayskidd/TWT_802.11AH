import dutyTable
import dutyCycle
import copy

limit=200
scale=100
lower=100
upper=1500

table=dutyTable.DutyTable(limit,scale,lower,upper)


for each in table.table:
    print('cycle='+str(each.duty_cycle)+' amount='+str(each.amount))



#############        duty cycle division      ###################
counter=0
while True:
    print("table division")
    change=False
    tmp_table=copy.copy(table.table)

    for each in tmp_table: #start to divide the duty_cycles using the targets within the table, i.e., table division
        index=[x for x, y in enumerate(table.table) if each==y]
        if index: #if there still exist this duty cycle
            targets=[]
            for target in table.table: #find the targets, i.e. the other duty_cycles
                if target.duty_cycle!=each.duty_cycle:
                    targets.append(target.duty_cycle)
            # print(targets)
            divisions=table.table[index[0]].find_division(targets)
            change= change or list(filter(lambda x:x>1, divisions)) #record if combination has happened
            table.table_after_division(each.duty_cycle,divisions)
    counter+=1

    tmp_table=copy.copy(table.table)
    tmp_table.sort(key=lambda x:x.duty_cycle)
    print("self division")

    for each in tmp_table: #divide the duty_cycles using the divisors of certain duty-cycle, i.e. self division
        index=[x for x, y in enumerate(table.table) if each==y]
        if index:
            targets=copy.copy(table.table[index[0]].divisors)
            targets=targets.pop() #delete the item whose value is the duty cycle itself
        # print("targets"+str(targets))
            divisions=table.table[index[0]].find_division(targets)
        # print("division:"+str(divisions))
            change= change or list(filter(lambda x:x>1, divisions))
            if list(filter(lambda x:x>1,divisions)):
                table.table_after_division(each.duty_cycle,divisions)
                break

    print("round: "+str(counter))
    for each in table.table:
        print('cycle='+str(each.duty_cycle)+' amount='+str(each.amount))
    if not change:
        break

#############         offset assignment      ######################
import virtualStation
import virtualStationTable