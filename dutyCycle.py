class DutyCycle:
    def __init__(self,cycle,amount):
        self.duty_cycle=cycle
        self.amount=amount
        self.divisors=find_divisor()

    def find_division(self,targets):
    #this function is target on combining the STAs (with the this duty-cycle) to form
    #as a group with certain target duty-cycles
    #
    #Args:
    #    targets: target duty-cycles
    #Returns:
    #    [list of division schemes,number of combinations]
        import copy
        groupings=[] #record how many STAs are needed to form a new duty-cycle
        #calculate groupins with given target duty-cycles
        for each in targets:
            if (self.duty_cycle% each)==0:
                groupings.append(self.duty_cycle//each)
        groupings.sort(reverse=1)
        # print(groupings)

        temp=[] #record states in BFS
        temp.append([self.amount,[]])
        division=[self.amount,[]] #record current best divisions, i.e., the fewest STAs are left

        while temp: #until all states have been searched
            current_state=temp.pop(0)
            # print("current_state" + str(current_state))
            if current_state[0]<division[0]:#renew the division
                division=current_state
            for each in groupings: #test all the grouping strategies
                amount=current_state[0]
                #print(each)
                for i in range(self.amount//each,0,-1): # grouping STAs using the strategy for several times
                    tmp_division=copy.copy(current_state[1])
                    if amount-each*i>0: #still has some STAs left
                        for j in range(0,i):
                            tmp_division.append(each)
                        if not [x for x, y in enumerate(temp) if y[0]==amount-each*i]: # if the left amount haven't occured, record a new state
                            temp.append([amount-each*i,tmp_division])
                    if amount-each*i==0: #no one is left
                        for j in range (0,i):
                            tmp_division.append(each)
                        return(tmp_division)
                    if amount-each*i<0:
                        break
    # some STAs are left after combination
        for i in range (0,self.amount-sum(division[1])):
            division[1].append(1)
        return division[1]


    def find_divisor(self):
    # find the divisors for this duty cycle
    # Returns
    #     divisors: list of divisors
        divisors=[]
        for i in range(1,self.duty_cycle+1):
            if self.duty_cycle%i==0:
                divisors.append(i)
        return divisors

    def gcd(self,table):
    #find the greatest common divisors of other duty cycles
    #Args: 
    #     list: list of duty cycles
    # Returns
    #     list of tuples consists of common divisors and the duty cycles 
        self.common_divisors=[1,[self]]

        for each in table.table:

            if each!=self:
                temp=list(set(self.divisors).intersect(set(each.divisors)))
                a=max(temp)
            index=[x for x, y in enumerate(self.common_divisors) if y[0]==a]
            if index:
                self.common_divisors[index[0]][1].append(each)
            else:
                self.common_divisors.append([a,[each]])