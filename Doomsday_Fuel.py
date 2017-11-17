"""
Doomsday Fuel
=============

Making fuel for the LAMBCHOP's reactor core is a tricky process because of the exotic matter involved. It starts as raw ore, then during processing, begins randomly changing between forms, eventually reaching a stable form. There may be multiple stable forms that a sample could ultimately reach, not all of which are useful as fuel. 

Commander Lambda has tasked you to help the scientists increase fuel creation efficiency by predicting the end state of a given ore sample. You have carefully studied the different structures that the ore can take and which transitions it undergoes. It appears that, while random, the probability of each structure transforming is fixed. That is, each time the ore is in 1 state, it has the same probabilities of entering the next state (which might be the same state).  You have recorded the observed transitions in a matrix. The others in the lab have hypothesized more exotic forms that the ore can become, but you haven't seen all of them.

Write a function answer(m) that takes an array of array of nonnegative ints representing how many times that state has gone to the next state and return an array of ints for each terminal state giving the exact probabilities of each terminal state, represented as the numerator for each state, then the denominator for all of them at the end and in simplest form. The matrix is at most 10 by 10. It is guaranteed that no matter which state the ore is in, there is a path from that state to a terminal state. That is, the processing will always eventually end in a stable state. The ore starts in state 0. The denominator will fit within a signed 32-bit integer during the calculation, as long as the fraction is simplified regularly. 

For example, consider the matrix m:
[
  [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
  [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
  [0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
  [0,0,0,0,0,0],  # s3 is terminal
  [0,0,0,0,0,0],  # s4 is terminal
  [0,0,0,0,0,0],  # s5 is terminal
]
So, we can consider different paths to terminal states, such as:
s0 -> s1 -> s3
s0 -> s1 -> s0 -> s1 -> s0 -> s1 -> s4
s0 -> s1 -> s0 -> s5
Tracing the probabilities of each, we find that
s2 has probability 0
s3 has probability 3/14
s4 has probability 1/7
s5 has probability 9/14
So, putting that together, and making a common denominator, gives an answer in the form of
[s2.numerator, s3.numerator, s4.numerator, s5.numerator, denominator] which is
[0, 3, 2, 9, 14].

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int) m = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
Output:
    (int list) [7, 6, 8, 21]

Inputs:
    (int) m = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
Output:
    (int list) [0, 3, 2, 9, 14]

Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.

"""

def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)

def lcmm(args):
    """Return lcm of args."""   
    return reduce(lcm, args)

class value(object):
    
    numerator = None
    denominator = None
    
    def __init__(self, numberator, denominator = 1):
        self.numerator = numberator
        self.denominator = denominator
        
    def __preCheck(self, v):
        if type(v).__name__ != 'value':
            raise 'This is an error line, but it should not reach here.'
        if not v.isInited:
            raise 'This is also an error line, but it should not reach here.'            

    def simplify(self):
        g = gcd(self.numerator, self.denominator)
        self.numerator = self.numerator / g
        self.denominator = self.denominator / g
        
    def add(self, v):
        self.__preCheck(v)
        newV = value(self.numerator * v.denominator + v.numerator * self.denominator, self.denominator * v.denominator)
        newV.simplify()
        return newV
    
    def minus(self,v):
        self.__preCheck(v)
        newV = value(self.numerator * v.denominator - v.numerator * self.denominator, self.denominator * v.denominator)
        newV.simplify()
        return newV
    
    def mult(self,v):
        self.__preCheck(v)
        newV = value(self.numerator * v.numerator, self.denominator * v.denominator)
        newV.simplify()
        return newV
    
    def divide(self,v):
        self.__preCheck(v)
        newV = value(self.numerator * v.denominator, self.denominator * v.numerator)
        newV.simplify()
        return newV
    
class node:
    nid = None          #node id
    weight = None       #list of probo to jump to next stage
    initInput = None    #value of initInput to this node
    feedback = value(0) #value of all init feedback sum
    isFinalStage = False
    
    systemOverallInput = 
    
    def __init__(self,nid, weight):
        self.nid = nid
        self.weight = weight
        #self.isFinalStage = ( self.weight.count(0) == len(self.weight) ) # this is wrong
        
    def feedbackto(self, nid):
        return feedback[nid] != 0
    
    def calculateSystemOverallInput(self):
        self.systemOverallInput = 


    while weight[0][anynonefinalpt] != 0:
        for i in range(10):
            if i is not final
                for k in range(10):
                    weight[0][k] = weight[0][k] + weight[0][i] * weight[i][k]
                weight[0][i] = 0
        
    

finalPoint = [] #True of False
    
def feedbackratio(v):
    v.denominator -= v.numerator



















