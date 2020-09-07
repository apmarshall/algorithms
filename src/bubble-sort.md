# Bubble Sort

A bubble sort is a very simple sorting algorithm which iterates over a list, swapping adjacent elements as necessary, until it reaches the end. It then repeats this process until the list is sorted. After the first sort, the final element should be in the right place, so the second time through it only needs to go `n-1` iterations through the list. The next time through, the final two elements are correct, so then it repeats until the `n-2`nd element, and so on and so forth until we have sorted all the elements.

## Pseudocode:

**Tests:**
    expect: bubble-sort (4 2 1 6 3 5) -> [1,2,3,4,5,6]
    expect: bubble-sort (1 2 3 4 5 6) -> [1,2,3,4,5,6] // case: already sorted
    expect: bubble-sort (1) -> [1] // case: single element should return itself
    
**Function**
    define: bubble-sort ( list ):
        define: outer-loop:
            start k = list.length
            while k > 0:
                perform inner-loop
                k--
        define: inner-loop (list):
            for each i in list:
                if i < i-1, swap, then i++
                else, i++

The `outer-loop` is taking advantage of the fact that each time through the sorting process, we get one more element at the end of the list that is in the right order. So each time, we can iterate one less pair because we know that the final `n` element are sorted. The inner loop is then doing the pair comparison and sorting for us. One thing to note: because we're assuming the final element will be sorted after our first run, we're comparing each element with the item before it. This won't work for our first element in the list, so we should start iterating at item [1] in our array, not item [0].

**Optimizations:**
There are two special cases we've already identified:
- If the list only has one element (or, really, if it has no elements), just return the list.
- If the list is already sorted, we should also just return the list

The first optimization just requires inserting an "if" clause in the outer-loop:
    define: outer-loop:
        if list.lenght => 1: return list
        else:
            start k = list.lenght
            while k > 0:
                peform inner-loop
                k--

The second optimization is a bit trickier, it requires some sort of state variable. One way to do this would be to put that variable in the main function and increment it for each swap performed by the inner loop. If we make it all the way to the end and the variable is still zero, we can just return the list as already sorted:

    define: bubble-sort ( list ):
        start: swaps = 0
        define: outer-loop ( list ):
            if list.length >= 1: return list
            else if: k = list.length - 1 && swaps = 0: return list
            else:
                start k = list.length
                while k > 0:
                    perform inner-loop
                    k--
        define: inner-loop (list):
            for each i in list:
                if i < i-1, swap, then swaps++, then i++
                else, i++

So basically: if we make it through the inner-loop once without making a single swap, send us back the already sorted list. Done.

But wait: what if the list is only off by one and after the first iteration, it's sorted? Or what if it's sorted after the second iteration? We could ostensibly use our state variable to catch these cases, too, and return the list after the first pass through with no additional swaps. Here's what that might look like:

    define: bubble-sort (list ):
        start: t = 0 // times through the outer loop
        start: swaps = 1 // explained in a moment
        define: outer-loop ( list ):
            if list.length >= 1: return list
            else if: k = list.length - t && swaps = 0: return list
            else: 
                start k = list.length
                swaps = 0
                while k > 0:
                    perform inner-loop
                    k--
        define: inner-loop ( list ):
            for each i in list:
                if i < i-1, swap, then swaps++, then i++
                else, i++
                
Thing to note here: if we start our swaps at zero in this case, we'll always get the list back because we'll match the second conditional in the outer-loop on the first pass. So we start swaps at 1, then set it to zero when we start the fork that calls the inner-loop.

