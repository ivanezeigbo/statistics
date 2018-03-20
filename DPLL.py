'''
class Literal:
    def __init__(self, name):
        self.name = name #names the literal
        self.sign = None
        self.neg = None
 

    def __neg__(self, other = True): #indicates whether a negation exist for the literal
        self.other = other      

    def l_child(self): #all left children are True
        self.sign = False
        self.neg = True #negated sign. Negated literals are defined alongside the positives.

    def r_child(self): #all right children are false
        self.sign = True
        self.neg = False

A = Literal(‘A’)
A.__neg__()
B = Literal(‘B’)
C = Literal(‘C’)
C.__neg__()
D = Literal(‘D’)

'''

#KB = [{'-C'}, {'C'}]

def DPLL(KB):
    global count
    pos_literals = {} #important for answering Extension problem 2. This is a dictionary that would have valies of the form [positive_literal/or positive of negated literal, 0/1/2]. 0 (positive) and 2 (negative) are for pure symbols; 1 (positive and negative) is impure.  
    pos_list = [] #important for answering Extension Problem 1
    model= {} #gives the actual model
    count ={} #important for addressing Extension Problem 1 for checking which one occurs most in clause. This is a dict of each literal and the amount of times they occur. Then we rank them.
    for disjuncts in KB:
        if disjuncts == {}:
            print ('Please put KB in correct CNF syntax!')
            return
        for literals in disjuncts:
            if literals[0] == '-':
                pos = literals[1:]
                if pos in pos_list:
                    pos_literals[pos] = [pos, 1] #for impure symbols
                    count[pos] += 1
                    model[literals] = None
                else:
                    pos_list.append(pos)
                    pos_literals[pos] = [pos, 2] #for pure symbols that are negations unless we find their positive literal
                    count[pos] = 1
                    model[pos] = None
                    model[literals] = None
            else:
                if literals not in pos_list:
                    pos_literals[literals] = [literals, 0] #this are pure symbols unless we find a negative literal
                    count[literals] = 1
                    pos_list.append(literals)
                    model[literals] = None
                else:
                    count[literals] += 1
    #For Extensions: Problem 1
    most_freq = [k for k in sorted(count, key=count.get, reverse=True)] #ranked from highest to lease from most frequent to least frequent literals
    #pos_list = most_freq[:] #if we are to pick the one that appears most in the clauses than any arbitary number

    def SAT_checker(model): #checks for satisfiability
        a = pos_list[:] #copies the list of positive literals
        b = len(a) -1
        c = len(a[b]) - 1
        last_literal = a[b][c] #checks for the last positive literal to see if it can be free
        for clauses in KB: #loops through the clauses in KB to check satisfiability
            Value = False #gives a clause an initial value of False and then checks for a True value
            for literals in clauses:
                if (last_literal == literals or (('-' + last_literal) == literals)) and (model[literals] == None):
                    model1, model2 = dict(model), dict(model)
                    model1[literals] = False
                    model2[literals] = True
                    model1 = SAT_checker(model1) #recursive function to check for free literals
                    model2 = SAT_checker(model2) #recursive function to check for free literals
                    if model1[0] and model2[0]:
                        model = dict(model1[1])
                        model[literals] = 'free'
                        return [True, model] 
                if model[literals] == None:
                    return [False, model]
                Value = Value or model[literals] #a truth value shows  that this is sadfiable, but since we need a model, we have to see other clauses as well
            if Value == False:
                return [False, model] #once the boolean of one clause is False, we know that it cannot be satisfiable
        return [True, model] 
        

    def recurse(pos_list, model): #interested in using only positive literals since I already define the positives of all negatives at the same time. 
        global found_model #indicates whether a model has been found after recursive algorithm is done        
        found_model = False
        Model = dict(model)
        Pos_list = pos_list[1:] #copies the rest of the positive literal except for the first one that we are working on - so we do not go back to it
        for truth_val in [True, False]: #loops on True or False values   
            for lit in pos_list:
                if not found_model:
                    Model[lit] = truth_val #assigns this momentarily to the first positive literal and checks to find a model
                    '''
                    #Implements Unit Clause Heuristics. Extension Problem 2
                    UnitClause_list = []
                    for clauses in KB:
                        List = []
                        for literals in clauses:
                            List.append(Model[literals])
                        UnitClause_list.append(List)
                    for unit_clause in UnitClause_list:
                        big_index = 0
                        count = 0
                        ind = None
                        for each in range(len(unit_clause)):
                            if unit_clause[each] == None:
                                count += 1
                                ind = each
                        if count == 1:
                            unit_clause[ind] = True
                            Model[KB[big_index][ind]] = True
                            Pos_list.remove(KB[big_index][ind])
                            pos_list.remove(KB[big_index][ind])
                        big_index += 1
                    '''
                    
                    if pos_literals[lit][1] != 0: #for impure symbols
                        Model['-'+lit] = not truth_val #gives their negations the opposite of the positive literal values
                    checker = SAT_checker(Model) #checks for satisfiability. checker = (satisfiability, model)
                    if checker[0] == False: #if not satisfiable
                        if lit != pos_list[len(pos_list) - 1]: #if it is not the last literal to check
                            recurse(Pos_list, Model) #recurses until a model is found
                    else:
                        found_model = True #when a model is found
                        model = checker[1] #gives the valie of model
                        print ('Satisfiable!! Model given below:', '\n')
                        print ('Model: ', model)
                        return
                else:
                    return
        if found_model == False:
            return 
    '''
    #For Extension Problem 2. Sets all pure symbols to True using the list of the most frequently occuring in clauses
    for m in pos_literals:
        if pos_literals[m][1] == 0:
            pos_list.remove(m) #we can ignore them in the algorithm since we have set all pure clauses to True following the pure symbol heuristic
            model[m] = True
    '''
    recurse(pos_list, model)
    if found_model == False: #prints Not satisfiable when model not found
        print ('Not satisfiable!')

KB_list = [[{'A','B'},{'A','-C'},{'-A','B','D'}], [{'-A', 'B', 'E'}, {'-B', 'A'}, {'-E', 'A'}], [{'-E', 'D'}], [{'-C', '-F', '-B'}], [{'-E', 'B'}], [{'-B', 'F'}], [{'-B', 'C'}]] 
       
for KB in KB_list:
    print ('Result for the KB:', KB)
    DPLL(KB)
    print("")
                
            
