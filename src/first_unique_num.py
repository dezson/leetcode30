class FirstUnique:
    def __init__(self, nums: List[int]):
        self.q = []
        self.helper = {}
        for i in nums:
            self.add(i)

    def showFirstUnique(self) -> int:
        while len(self.q) > 0 and self.helper[self.q[0]] > 1:
            self.q.pop(0)
        if len(self.q) == 0:
            return -1
        else:
            return self.q[0]


    def add(self, value: int) -> None:
        if value in self.helper:
            self.helper[value] += 1
        else:
            self.helper[value] = 1
            self.q.append(value)
