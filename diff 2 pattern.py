"""
*       *
 *     *
  *   *
   * *
    *
   * *
  *   *
 *     *
*       *
"""

def function(n):
    for i in range(n):
        for j in range(n):
            if(i+j==n-1 or i==j ):
                print("*",end="")
            else:
                print(" ",end="")
        print()
function(5)