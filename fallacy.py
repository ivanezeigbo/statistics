##############################################
# Logical Validity checker for two variable arguments
# Starter Code
##############################################

# Auxiliary functions (not necessarily complete)
#defining function for 'or'
def foo_or(a,b):
    return a or b
    # returns a or b
    
#defining function for 'and'    
def foo_and(a,b):
    return a and b

     # returns a and b   

#defining function for conditionals
def implication(a,b):
    # returns a->b
    return not a or b

#function that return 'a'        
def id1(a,b):
    return a
    # returns a

#function that returns 'b'    
def id2(a,b):
    return b
    # returns b

#function that returns '-a'    
def id3(a,b):
    return not a
    #returns the negation of a

#function that returns '-b'
def id4(a,b):
    return not b
    #returns the negation of b
    
def id5(a,c):
    return c

#############################################
# Function to run
#function that tests validity, using three inputs: two premises and a conclusion
def valid(f,g,h):
    # inputs: two-variable functions f,g,and h
    #   where f and g represent premises, and
    #   h represents a conclusion
    
    for a in [True, False]:
        for b in [True, False]:
            for c in [True, False]:
                if f(a,b) == True and g(a,b) == True and h(a,b) == False:
                    return False
    return True

    
    # returns True if the argument is valid
    # returns False otherwise

#############################################
# Examples of use

        

# tests premises: A or B, B, conclusion: A
print (valid(foo_or,id2,id1))

# tests premises: A, A->B, conclusion: B
print (valid(id1,implication,id2))

# tests premises: A or (A and B), B, conclusion: A
print (valid(foo_or(id1,foo_and),id2,id1))

# testing validity of modus ponens: P -> Q; P then Q
print (valid(implication, id1, id2))

#testing validity of modus tollens: P -> Q; -Q -> -P
print (valid(implication, id4, id3))

#testing validity of first case of disjunctive syllogism: P or Q; -P therefore Q
print (valid(foo_or, id3, id2))

#testing validity of second case of disjunctive syllogism: P or Q; -Q therefore P
print (valid(foo_or, id4, id1))

# test of the premise in question 3: (A and B) -> (-A or B), B -> -A; conclusion: A or -B
print (valid(implication(foo_and, foo_or(id3, id2)), implication(id2, id3), foo_or(id1, id4)))

#testing validity of hypothetical syllogism for question 4 on comment: p -> q -> r; therefore p -> q
print (valid(implication, implication(id2,id5), implication(id1, id5)))

#Explanation of above
#In a case when one has to use valid() to test the validity of other arguements such as 
#as hypothetical syllogism which is: a -> b -> c, and the conclusion: a -> c, first we create another 
#function that returns 'c', say id5(a, c); then under the 'for' loop for b in [True, False], we create a 'for' loop for c in [True, False]; then 'f' becomes 'implication',
#'g' becomes 'implication(id2,id5), and 'h' becomes 'implication(id1, id5)'.When run, it prints "True".
