# Bubble Sort

A bubble sort is a very simple sorting algorithm which iterates over a list, swapping adjacent elements as necessary, until it reaches the end. It then repeats this process until the list is sorted. 

This process essentially treats the list as two distict types of data. The first is the list itself, which is an array of some arbitrary length. The second is the given pair of items being considered, which is essentially a tuple. Each tuple is sorted individually and reinserted into the list, then another pair is considered, then another until the end of the list is reached.

Of course, very rarely will one pass through the list result in a full sort. The complexity of this algorithm is that we need to keep running over the list until it is fully sorted. The easiest way to do this is just to complete `n = list.length` passes over the entire list, but there are several ways this can be optimized.

The first optimization is that after the first sort, the final element should be in the right place, so the second time through it only needs to go `n-1` iterations through the list. The next time through, the final two elements are correct, so then it repeats until the `n-2`nd element, and so on and so forth until we have sorted all the elements. So we want some sort of state-tracker that tells us how many fewer elements we need to consider in the next pass through the list.

Additionally, we want to make some sort of allowance for a case in which the list is already sorted. This may happen because the list was sorted to begin with (so we didn't need todo anything) or because the list was close to sorted and after a short number of iterations the sorting is complete and we don't need to continue working. We'll consider this in a bit.

## Pseudocode:

### Tests:
    expect: bubble-sort (4 2 1 6 3 5) -> [1,2,3,4,5,6]
    expect: bubble-sort (1 2 3 4 5 6) -> [1,2,3,4,5,6] // case: already sorted
    expect: bubble-sort (1) -> [1] // case: single element should return itself
    
### Tuple Data Type:

Let's start with the "tuple" data type: the individual pairs that are being passed in for comparison.

    // tuple -> tuple
    define: tuple-sort ( x, y ):
        if ( x < y ): return ( x, y )
        else: return ( y, x )
        
That's it for the sorting of the pairs.

### Iterating Through the List:

Now, let's consider how we pass over the whole list itself:

    // list -> list
    define: list-iteration ( list ):
        if ( list.length <= 1 ): return list
        else: list[0,1] =  tuple-sort ( list[0], list[1] )
            list-iteration ( list[1:] )

This is a simple recursive function for iterating over a list. The base case is when the list contains only one element (so there is no tuple to compare). This will also catch an "empty" list, which contains nothing to compare or sort. In those cases, the "list" will simply be returned, which will pass back out through the existing function calls and give us our list as returned from all the tuple-sorts in this iteration.

### Making Multiple Passes Over the List:

The `list-iteration` function gets us through one pass over the list. But one pass will rarely get the list sorted. Instead, we will need to keep going through the list until all the elements are sorted.

Definitionally, because of the way a bubble sort works, for each iteration, `i`, over a list of length `l`, the `l-i`th element will be sorted. In other words, after the first iteration, the last element will be sorted. After the second iteration, the second to last element will be sorted, and so on. This is because in each tuple comparison, the larger element is returned second (closer to the end of the list). The next tuple pair will include this larger element again, so again if it is the larger of the pair it will be returned second. As this process repeats, the largest element in the list will always end up the second element returned by the `tuple-sort` function. By the time you get through the list, it will therefore be the final element returned by the final `tuple-sort` comparison.

This gives us a hint about how to get the whole list sorted. In the `list-iteration` function we worked through the list from the beginning to the end. In the `list-sort` function, we can do the reverse, working from the end to the beginning:

    // list -> sorted list
    define: list-sort ( list ):
        if ( list.length <= 1 ): return list
        else: list = list-iteration ( list )
            list-sort ( list[:list.length] )
            
Essentially, what this is doing is it is recursively calling the `list-iteration` function on our list, but each time it is dropping the last element of the list. Then it passes in the shortened list to the next recursive call. This seems to get us started, except that: each run of `list-iteration` returns an entire list. If we combine all those lists together, we don't get a sorted list, we get a series of partially sorted lists strung together. What we actually want is the final element of each run (because we know that element is sorted). So what we need is some sort of "work-done-so-far" container:

    // list -> sorted list
    define: list-sort ( list ):
        local define: list-sort ( list, slist ):
            if ( list.length <= 1 ): return list + slist // append the last item to the front of slist
            else:
                list = list-iteration ( list )
                slist = list[final] + slist // append the last item on the list to the front of slist
                list-sort ( list[:list.length], slist )
        list-sort ( list, [] ) // start with an emply slist

What we're doing now is using the `slist` item to build up our sorted list, starting with the final item of the first run of `list-iteration` and adding a new item to the front of `slist` with each run of `list-iteration` until we have only one item left in our list (at which point, we add that to the front of `slist` and return the result. This completes the sort algorithm.

**Optimizations:**
There are two special cases we've already identified:
- If the list only has one element (or, really, if it has no elements), just return the list.
- If the list is already sorted, we should also just return the list

The first case is taken care of naturally by the recursive structure of our program because it will trigger the base case and simply return itself. So simple enough.

The second case is a bit trickier and requires some sort of state variable.

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

