# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        n,m  = binaryMatrix.dimensions()
        if n == 0:
            return -1

        def scan(n,m):
            x = 0
            y = m-1
            mini = float('inf')

            while x <= n-1 and 0 <= y:
                # Searching the first rightmost one
                if mini == float('inf'):
                    if binaryMatrix.get(x,y) == 1:
                        while y >= 0 and binaryMatrix.get(x,y) == 1:
                            y-=1
                        mini = y+1
                    x+=1
                    continue


                if binaryMatrix.get(x,y) == 0:
                    x+=1
                else:
                    if y < mini:
                        mini = y
                    y-=1

            return -1 if mini == float('inf') else mini

        return scan(n,m)
