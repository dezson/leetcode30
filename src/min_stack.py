class MinStack:

    def __init__(self):
        self.data = []
        
    def _is_empty(self):
        return len(self.data) == 0

    def push(self, x: int) -> None:
        if self._is_empty():
            minx = x
        else:
            minx = min(self.data[-1][1], x)
        self.data.append([x,minx])


    def pop(self) -> None:
        if not self._is_empty():
            self.data.pop()
        

    def top(self) -> int:
        if not self._is_empty():
            return self.data[-1][0]

    def getMin(self) -> int:
        if not self._is_empty():
            return self.data[-1][1]
