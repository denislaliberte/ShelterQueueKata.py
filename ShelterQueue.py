class ShelterQueue:
  count = 0
  item = []
  def empty(self):
    return self.count == 0

  def enqueue(self,item):
    self.item.insert(self.count,item)
    self.count += 1

  def dequeueAny(self):
    self.count -= 1
    temp = self.item[0]
    self.item.pop(0)
    return temp
