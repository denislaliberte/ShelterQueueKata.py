class ShelterQueue:
  count = 0
  def empty(self):
    return self.count == 0

  def enqueue(self,item):
    self.item = item
    self.count += 1

  def dequeueAny(self):
    self.count -= 1
    return self.item
