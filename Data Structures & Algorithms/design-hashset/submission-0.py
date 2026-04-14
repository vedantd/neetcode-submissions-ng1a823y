class MyHashSet:
    
    def __init__(self):
        self.arr = []
        return 


        
        

    def add(self, key: int) -> None:
        for x in self.arr:
            if x == key:
                return
        self.arr.append(key)
        return
        

    def remove(self, key: int) -> None:
        for x in  self.arr:
            if x == key:
                self.arr.remove(key)
        return
        

    def contains(self, key: int) -> bool:
        for x in  self.arr:
            if x == key:
                return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)