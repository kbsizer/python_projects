"""
Five Prisoners Puzzle

Five comrades, Andy, Ben, Carl, Dan and Ed, have been 
taken prisoner by the Bad Guy(TM).
Bad Guy is evil but loves logic puzzles, so he says:
You will be put in separate cells with no way to communicate.
(1) Each of you has been given a number greater than 1 And 
less than 100.
(2) Andy's number < Ben's number < Carl's number < Dan's number < Ed's number.
(3) Only one of the numbers is divisible by 2.
(4) Another number is the only one divisible by 3.
(5) A third number is the only one divisible by 5.
(6) A fourth number is the only one divisible by 7.
(7) The remaining number is the only one divisible by 11.
(8) Two numbers sum to 100.
(9) I will free anyone who can determine who has what number AND
I will inform the others who has been freed.

QUESTION: Who was the first to solve the puzzle and escape? 
What number did each prisoner have?
"""

from sortedcontainers import SortedSet

div2 = []
div3 = []
div5 = []
div7 = []
div11 = []

for i in range(2,100):
    # print('i=', i)
    if(i % 2 ==0):
        div2.append(i)
    if(i % 3 == 0):
        div3.append(i)
    if(i % 5 == 0):
        div5.append(i)
    if(i % 7 == 0):
        div7.append(i)
    if(i % 11 == 0):
        div11.append(i)


div11Only = SortedSet(div11).difference(div2).difference(div3).difference(div5).difference(div7)
print('div11Only = ', div11Only)
div7Only = SortedSet(div7).difference(div2).difference(div3).difference(div5).difference(div11)
print('div7Only = ', div7Only)
div5Only = SortedSet(div5).difference(div2).difference(div3).difference(div7).difference(div11)
print('div5Only = ', div5Only)
div3Only = SortedSet(div3).difference(div2).difference(div5).difference(div7).difference(div11)
print('div3Only = ', div3Only)
div2Only = SortedSet(div2).difference(div3).difference(div5).difference(div7).difference(div11)
print('div2Only = ', div2Only)

# Find pairs which add to 100
allCandidateNumbers = div11Only | div7Only | div5Only | div3Only | div2Only
for a in allCandidateNumbers:
    for b in allCandidateNumbers:
        if(a + b == 100 and                 # condition we're looking for
           a <= b and                       # suppress duplicates
           ( a % 2 != 0 or b % 2 != 0 )):   # at least one of the numbers is odd
            print(a,'+',b,'=',a+b)

"""
Results of above:
     5 + 95 = 100   X    <-- both divisible by 5
     7 + 93 = 100
     9 + 91 = 100
    49 + 51 = 100


 Only 3 choices, but how to decide which of the three?

"""
