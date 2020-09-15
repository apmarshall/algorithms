def bubbleSort ( list ):
    def listSort ( list, slist, needSort ):
        if ( list.length <= 1 || needSort == false ):
            return list + slist
        else:
            list = listIteration ( list, false )
            slist = list[list.length] + slist
            listSort( list[:list.length], slist, needSort )
    listSort( list, [], true )

    def listIteration ( list, needSort )
        if ( list.length <= 1 ): return list
        else:
            list[0,1] = tupleSort( list[0], list[1], needSort )
            listIteration( list[1:] )

    def tupleSort ( x, y, needSort ):
        if ( x < y ): return ( x, y )
        else:
            needSort = true
            return ( y, x )
