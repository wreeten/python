# Data Structures and Algorithms
[https://youtu.be/8hly31xKli0]
## 01 / 02 / 2022

---
In this section, I will be learning Algorithms and Data Structures using the following link.

Algorithm - Step(s) or instructions for compelting a task

Similar to a maze, there are many ways to complete the maze, and some are faster than other routes.

There is an established body of problem and how to solve the problem well, and you may be able to solve problems but with understanding the problem the better we can tackle the problem and break it down into destinct steps. 

6:50
Pick number 1 - 10, guess, either say higher or lower.
Q: is 1 and 10 included? > clarify value are inputs
 > > 1 , 2, 3 - correct
Q2: 5, 2, 3?
    Start with middle :O WHAAAT okay, crazy.

So in this problem example, it shows the difference in strategies. Q had 10 tries wheras Q2 took 2 tries when the namber was 10.

10:21
Second example, this time to 100
Q = 1 > 5
Q2 > 50, 25, 13, 6, 3

This time the chosen number is 
Q = 1 > 100
Q2 = 50, 75, 90, 95, 97, 99, 100

We can pretend that the number of tries = 1s.

13:04
The example above are examples of searching for a value. The speed of the result obtained differed. 

Similarly, Facebook has 2.1billion users. We want to add a friend at another country. Imagine, searching for a friend could take hours, so algorithms help search friends faster.
Ooof, didn't really think of that.

Q => sequential search, or linear search
Linear search is a search algorithm. Begining of the list or range of value, then compare the value to the target, if the current value = target then we're done. If we reach the end of the value, then the target value is not in the list.

16:00
Like the bookstore,]
We're looking for the book, and we go to a bookcase. We look at the spine book by book by row. If not there, then book is not available. 

In defining the problem, how the input is defined and how the output looks like.
Algorithm definition must contain specific instructions in which order the instructions are initiated. Specific order is important.
You shouldn't be able to break down the steps into further subtasks. 
Algorithms should produce result, if not then how do we know if it works? The result can be nothing, aka value not found and that's okay. As long as it produces result.
Algorithm should compute and not take an infinite amount of time. (19:08)


### Important 19:50
1. Clearly defined problem statement, input, and output.
2. The steps in the algorithm need to be in a very specific order.
3. The steps also need to be distinct.
4. The algorithm should produce result.
5. Should complete in a finite amount of time

Consistent results is how we check if the algorithms are correct.

The same set of guidelines encourages algorithmic thinking.
---

### What is Good Algorithm?  (21:33)
1. correctness
    a. define the problem > defined input and outpput
    b. algorithm is correct if any possible input, output is always correct
    c. if the input and output are not true then algorithm isn't correct
    d. proof through induction > this is for math, but we don't really need that, but can read later.
2. efficiency 23:00
    a. time and space
     i. time complexity a measure on how long it takes for the algorithm to run
     ii. space complexity, how much it takes memory to complete the algorithm
---
In round 1:
Q : r1 = 3, r2 = 10, r3 = 5, r4 = 100
Plotting the value, target and value, on the x axis, whichever you choose can leave out some other information.
27:30
Example, facebook linear, a - j = 50%, letters after j may take longer than the average.
Runtime might be a good strategy, it won't give the accurate picutre
We should analyze the worst case scenario, because it wouldn never perform worse than we expect - no room for surprises
28:40
n = x axis 
tries = y axis
by evaluating the worst case scenario, we know whwat the result will be.
Lienar search , as value gets large, so does the runtime 
Linear search seems familiar to use because we use it often

In round 2: for comparison 30:30
Q2 strategy is always starting in the middle, and if the value is greater than she can eliminate the values less than the one she's evaluating. She repeats this process until she arrives at the answer.
With every value she evaluates, she can discard the other half that's not in range.
Binary search, the values need to be SORTED
linear search, the values doesn't have to be sorted, and if the target value is in the list then it can be found.
Binary search is providing something to search for, so the result is returned of the position where the target occupies.

#### Binary Search 35:54
1. input a sorted list of values
2. the output > the position in the list of the target values we're searching for, or target dne

36:15 / Time Complexity