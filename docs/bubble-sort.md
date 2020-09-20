# Bubble Sort

A bubble sort is a very simple sorting algorithm which iterates over a list, swapping adjacent elements as necessary, until it reaches the end. It then repeats this process, working it's way through the list in cycles until the list is sorted. 

This algorithm essentially treats the list as two distict types of data. The first is the list itself, which is an array of some arbitrary length. The second is the given pair of items being considered, which is essentially a tuple. Each tuple is sorted individually and reinserted into the list, then another pair is considered, then another until the end of the list is reached.

Of course, very rarely will one pass through the list result in a full sort. The complexity of this algorithm is that we need to keep running over the list until it is fully sorted. The easiest way to do this is just to complete `n = list.length` passes over the entire list, but there are several ways this can be optimized.

The first optimization can be found by considering how the bubble sort works through the list: one pair at a time. In each pair, the larger element is moved to the righmost place. This means that the larger element will then be included in the next pair considered. As a result, after the first sort we can be assured that the final element should be in the right place.  This means that when we start the second cycle through the list, we only needs to consider the first `n-1` elements, not the entire list. After the second cycle, the final two elements are correctly sorted, so then we can shorten the list we need to consider by two elements. This will continue until we only need to consider the first tuple pair. So the first optimization is that in each cycle through the list, the list we need to sort can be shortened by leaving off the last element.

The second optimization comes from the observation that eventually many lists (if not most) given to a bubble sort algorithm will find themselves "accidentially" sorted. It's possible for the list to already be in this state from the beginning or to be only off by one element (and so only require one cycle over the list). However many times we have passed through the list already, it would be nice to know that when we reach that happy accidental state, we can stop doing our comparisons and simply present our sorted list. This is a fairly intuitive thing for humans: if we looked through the list and realized that it was in order we wouldn't keep going over it again. But our alogrithm will need to be told how to graps that intuition and "optimize" itself for less work.

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

Definitionally, because of the way a bubble sort works, for each iteration, `i`, over a list of length `l`, the `l-i`th element will be sorted. In other words, after the first iteration, the last element will be sorted. After the second iteration, the second to last element will be sorted, and so on. This is because in each tuple comparison, the larger element is returned second (closer to the end of the list). The next tuple pair will include this larger element again, so again if it is the larger of the pair it will be returned second. As this process repeats, the largest element in the list will always end up the second element returned by the `tuple-sort` function. By the time you get through the list, it will therefore be the final element returned by the final `tuple-sort` comparison. This is in fact where the name "buble sort" comes from: the largest elements "buble up" to the end of the list in each pass.

This gives us a hint about how to get the whole list sorted. In the `list-iteration` function we worked through the list from the beginning to the end. In the `list-sort` function, we can do the reverse, working from the end to the beginning:

    // list -> sorted list
    define: list-sort ( list ):
        if ( list.length <= 1 ): return list
        else: list = list-iteration ( list )
            list-sort ( list[:final] )
            
Essentially, what this is doing is it is recursively calling the `list-iteration` function on our list, but each time it is dropping the last element of the list. Then it passes in the shortened list to the next recursive call. This seems to get us started, except that: each run of `list-iteration` returns an entire list. If we combine all those lists together, we don't get a sorted list, we get a series of partially sorted lists strung together. What we actually want is the final element of each run (because we know that element is sorted). So what we need is some sort of "work-done-so-far" container:

    // list -> sorted list
    define: list-sort ( list ):
        local define: list-sort ( list, slist ):
            if ( list.length <= 1 ): return list + slist // append the last item to the front of slist
            else:
                list = list-iteration ( list )
                slist = list[final] + slist // append the last item on the list to the front of slist
                list-sort ( list[:final], slist )
        list-sort ( list, [] ) // start with an emply slist

What we're doing now is using the `slist` item to build up our sorted list, starting with the final item of the first run of `list-iteration` and adding a new item to the front of `slist` with each run of `list-iteration` until we have only one item left in our list (at which point, we add that to the front of `slist` and return the result. This completes the sort algorithm. It also, because of it's recursive nature, builds in the first optimization we discussed in the intro. Each cycle through will consider a shorter and shorter list because the last element will be "left off" and considered sorted.

**Further Optimizations:**
There are two special cases we've already identified in our tests:
- If the list only has one element (or, really, if it has no elements), just return the list.
- If the list is already sorted, we should also just return the list

The first case is taken care of naturally by the recursive structure of our program because it will trigger the base case and simply return itself. So simple enough.

The second case is a bit trickier and requires some sort of state variable. The easiest way to do this with a boolean that tracks whether any swaps have been made in the previous iteration through the list. This boolean will start as `false` (meaning no swaps have been made) and be flipped by the `tuple-sort` method whenever it makes a swap. In other words, it's going to stretch across our entire class here, not just within one of the individual functions:

    define: bubble-sort (list):
        local define: list-sort ( list, slist, needed-sort ):
            if ( list.length <=1 || needed-sort = false ): return list + slist
            else:
                list = list-iteration ( list, false ) // set needed-sort to false when starting the list-iteration run
                slist = list[final] + slist
                list-sort ( list[:final], slist, needed-sort )
         list-sort ( list, [], true ) // start with an empty slist and with needed-sort set to true so we go through at least one iteration
         
         define: list-iteration ( list, needed-sort ):
             if (list.length <=1): return list
             else: list[0,1] = tuple-sort( list[0], list[1], needed-sort )
                 list-iteration( list[1:]
                 
         define: tuple-sort( x, y, needed-sort ):
             if ( x < y ): return ( x, y )
             else: 
                 needed-sort = true
                 return ( y, x )

Essentially, we're starting off with `needed-sort` set to true, guaranteeing at least one iteration through the list (unless the list is only one element long). When we start the iteration, we set `needed-sort` to false and if we ever perform a sort, `tuple-sort` changes it to true. This means that after every iteration that we have performed a swap, we are guaranteed at least one more iteration over the list. After the first iteration in which no swaps are peformed (indicating that the list is fully sorted), we'll trigger the base case and exit, returning our sorted list.

That completes the pseudocode version of the Bubble Sort alogrithm using a functional style of coding. Let me know if you spot any problems or additional optimizations of the algorithm as presented here. Thanks for reading!
