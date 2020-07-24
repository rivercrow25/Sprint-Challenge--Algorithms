#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
the time complexity is O(n) due to a incrementing by n*n while the while loop comparison is n*n*n, it can be reduced to while a is less the n a += 1

b)
the time compexity is O(n^2) due to nested for loops even if j doubling

c)
the time complexity is O(n) due to a single decrementing recursive call
## Exercise II


i would create a list of floors using a comprehension then initialize 3 pointers start, middle and end.
start would point at the beginning of the list and end would point at the length of the list while middle will be start plus end divided by 2
as well as create a while loop that checks if middle is not f
then i would create an if, else block to tell if middle is comparable to f otherise find out if its higher or lower then reasign start to mid plus 1 or end to mid minus 1 

once middle is comparable to f the while loop will exit and the function will return middle leading to a run time complexity of O(log n) due to reducing the array by half each time the while loop repeats until the value of f is found