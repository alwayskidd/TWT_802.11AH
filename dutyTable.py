import dutyCycle
class DutyTable():
    def __init__(self,limit,scale,lower,upper):
        import random
        self.table=[]
        for i in range (lower,upper+1,scale):
            self.table.append(dutyCycle.DutyCycle(i,random.randint(0,limit)))
        self.table.sort(key=lambda x:x.duty_cycle, reverse=1)

    def table_after_division(self,cycle,division):
#    generate the table after combinining STAs together using a certain strategies
#
#    Args:
#        cycle:STAs' duty cycle
#        division: combininig strategies
#    Return:
#        a new table
        index=[x for x, y in enumerate(self.table) if y.duty_cycle==cycle]
        print("division list:"+str(division))
        self.table.pop(index[0]) #pop the STAs' duty cycle out of the table
        division.sort()
        while division: #until all the strategies have been applied
            tmp=division.pop()
            n=division.count(tmp)+1
            tmp=cycle//tmp
            index=[x for x, y in enumerate(self.table) if y.duty_cycle==tmp]
            if index: #if the target duty cycle exist in the table
                self.table[index[0]].amount+=(n)
                print("add " +str(n)+" to "+str(self.table[index[0]].duty_cycle))
            else: # if the target duty cycle does not exist
                self.table.append(dutyCycle.DutyCycle(tmp,n))
                print(str(n)+" STAs added to new duty cycle "+str(tmp))
            for i in range(1,n): #pop all the applied strategies
                division.pop()
        self.table.sort(key=lambda x:x.duty_cycle,reverse=1)
        return(self.table)

    def cal_common_divisor_table(self):
        # generate the common divisor table
        # Return:
        #     common divisor list, each element is consists of the common divisor, amount of duty cycles, the duty cycle object
        self.cd_table=[] #common divisor table
        max_duty_cycle=self.table[0]
        for i in range (1,max_duty_cycle+1):
            temp=[]
            amount=0
            for each in self.table:
                if each.duty_cycle%i==0:
                    temp.append(each)
                    amount+=each.amount
            if temp.__len__()>2:
                self.cd_table.append([i,amount,temp])