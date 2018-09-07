# Analysis of Algorithms
**Exercise I**: _Give an analysis of the running time of each snippet of pseudocode with respect to the input size n of each of the following:_
```
a)  a = 0
    while (a < n * n * n) 
      a = a + n * n
```

`O(n)` - linear

```
b)  sum = 0
    for (i = 0; i < n; i++)
      for (j = i + 1; j < n; j++)
        for (k = j + 1; k < n; k++)
          for (l = k + 1; l < 10 + k; l++)
            sum++
```

`O(¯\_(ツ)_/¯)`

```
c)  bunnyEars = function(bunnies) {
      if (bunnies == 0) return 0
      return 2 + bunnyEars(bunnies-1)
    }
```

`O(n)` - linear

**Exercise II**:
Suppose that you have an _n_-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor _f_ or higher, and doesn't get broken if dropped off a floor less than floor _f_. Devise a strategy to determine the value of _f_ such that the number of dropped eggs is minimized.

1. Create variables for floors and eggs
2. Create a max floor where it's safe to drop eggs and a min floor where eggs will break, or vice versa. the safe floor would be one less than the one where eggs break
3. Start looping thru the floors and testing the eggs
4. Do so until one breaks
5. Attach parachutes to the eggs to increase the max floor they can be dropped from
6. Scramble the broken eggs, kinda like my brain at the end of this week
