needSort = true

def bubbleSort ( list ):
    def listSort ( list, slist ):
        if ( list.length <= 1 || needSort == false ):
            return list + slist
        else:
            needSort = false
            list = listIteration ( list )
            slist = list[list.length] + slist
            listSort( list[:list.length], slist )
    listSort( list, [] )

def listIteration ( list )
   if ( list.length <= 1 ): return list
   else:
         list[0,1] = tupleSort( list[0], list[1] )
         listIteration( list[1:] )

def tupleSort ( x, y ):
   if ( x < y ): return ( x, y )
   else:
      needSort = true
      return ( y, x )
