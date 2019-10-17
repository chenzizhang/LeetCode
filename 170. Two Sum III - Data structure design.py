class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.values = {}
        

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        if number not in self.values:
            self.values[number] = 1
        else:
            self.values[number] += 1
        

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        values = self.values
        for num in values:
            """
            add[0] add[0] find[0] -> True, add[5] find[10] -> False
            """
            if value - num in values and (values[num] > 1 or (value - num) != num):
                return True
        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)