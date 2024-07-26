
#range(start, stop[, step]) -> range object
   
  # Return an object that produces a sequence of integers from start (inclusive)
  # to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
  # start defaults to 0, and stop is omitted!


for i in range(10):
    print(i,end=" ")      #0 1 2 3 4 5 6 7 8 9 
print()

for i in range(10,1,-1):  #10 9 8 7 6 5 4 3 2 
    print(i,end=" ")
print()

