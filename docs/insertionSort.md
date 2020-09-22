# Insertion Sort

An insertion sort is more or less what you do when you're sorting your hand of cards in a game like Hearts or Go Fish: you start with one card, then you add new cards one at a time into their correct spot in the order. In effect, you are "inserting" them into their spot in your hand. We're following a "functional style" of writing this algorithm, so we're going to start by considering what the "data structures" are that we are working with here.

To perform an insertion sort, we need to keep track of three things:
- the "sorted list" we are building
- the "unsorted list" we are drawing from
- the "item to sort"-- the "card" as it were that we're moving from the unsorted list to the sorted list

The sorted list (`slist`) and unsorted list (`ulist`) are both lists of arbirtrary length. The item to sort (`item`) is just a single piece of data (for simplicity, we're assuming a number, but it could be something else like a letter).

In essence, this algorithm starts by moving the first `item` from `ulist` over to `slist`. Then for each additional `item`, we compare it to each element of `slist` and insert it just after the last element it is larger/greater than.

Let's explore this in pseudocode. First, we're going to write our unit tests:

## Tests

    expect: insert-sort ( 6, 2, 3, 4, 5, 1 ) -> [1, 2, 3, 4, 5, 6]
    expect: insert-sort ( 1, 2, 3, 4, 5, 6 ) -> [1, 2, 3, 4, 5, 6] // case where the list is already sorted
    expect: insert-sort ( 1 ) -> [1] // case with only one element
    
## Pseudocode

From our tests, we can see that our function is going to accept one parameter: the `ulist`. So that's the parameter that is going to guide our structure, which is going to recursively operate on a list of arbitrary length:

    // list -> list
    define: insert-sort ( list ):
        if ( list.length <=1 ): return list
        else:
            insert( slist, list[1] )
            insert-sort ( rest.list )
            
Let's walk through this: we're given a list (which we presume is unsorted). If the list is of length 1 (or less), we're done and we just return the list. This is our base case. Otherwise, we need to start adding items to our "sorted list". This is triggering for us the need for a secondary function: `insert`, which will actually figure out where the item goes in the `slist`.

But wait: where does `slist` come from? We've just added it to the above, but it's not defined anywhere. Also, if our base case returns the `list`, won't this mean that `slist` doesn't get returned? We'll have done all this work for nothing!

It turns out, we need to treat `slist` as a "work-done-so-far" tracker. Here's what that looks like:

    // list -> list
    define: insert-sort ( list ):
        local define: insert-sort ( list, slist ):
            if ( list.length == 0 ): return slist
            else:
                insert ( slist,  list[1] )
                insert-sort ( rest.list, slist )
        insert-sort ( list, [] )
        
A couple of things here:

First, we've made `slist` explictly a work-tracking placeholder. This involves creating an inner function that will include `slist` as a parameter (which we initialize as an empty array when we call the inner-function).

Second, we've changed the base case. This is because even when we get down to the last item in the original `list`, we still have to make sure we `insert` it into `slist` in the proper place. So really, we aren't done until there are no items left in `list` to insert. When that happens, we're ready to call it quits and return `slist` in it's entirety.

Ok, so that's the overall function, but now what about `insert`?

    // list + item -> list
    define: insert ( list, item )
        if ( list.length == 0 ): return ( list + item ) // append the item to the end of the list
        else:
            
            
