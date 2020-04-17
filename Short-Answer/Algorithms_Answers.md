#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) 
``` a = 0
    while (a < n * n * n):
      a = a + n * n
 ```
  The while loop is run to n^3, whereas the function is iterated only until n^2.
  The value of "a" is incremeneted by n^2, so the loop is run until a < n^3.
  n^3 / n^2 = n
  Run time: O(n) 


b) 
```
 sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
 ```
  The for loop runs n times in the context of range (indices), and the while loop is iterating in log n
  bc j is doubling it's value white every addition of sum increases by 1.
  n * log(n)
  Run time: O(n(log(n)))

   

c)  
``` 
 def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```
  Simple answer: The number of bunnies (argument of function) decreases linearly as n-1.
  Run time: O(n)

## Exercise II
``` 
Suppose that you have an n-story building and plenty of eggs. 
Suppose also that an egg gets broken if it is thrown off floor f or higher, 
and doesn't get broken if dropped off a floor less than floor f. 
Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.
```

If you have n floors, that is what your function should begin with as a variable.
   
 You should drop the egg at the n/2 floor, so half way in between the total floors, using floor rounding if odd. 
 [Implement Binary Search]
   
  If the egg gets broken: 

   - You should also drop it at the floor below to see if it breaks n/(2-1).
   - If the egg doesn't break, the n/2th floor is floor f, the threshold before the egg is no longer safe to be dropped.
   
   - If the egg does break, you would then be looking only at the bottom half of the floors.
   
  If the egg doesn't get broken, you would be looking only at the top half of the floors.
  
  This process would be repeat recursively as a binary search until the right floor is found to drop the egg safely from.
   
Run time of binary search is O(log(n))
