class ShelterQueue:
  count = 0
  def empty(self):
    return self.count == 0

  def enqueue(self,item):
    self.count += 1
