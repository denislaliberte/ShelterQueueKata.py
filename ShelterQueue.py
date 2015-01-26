class ShelterQueue:
  count = 0
  item = []
  def empty(self):
    return self.count == 0

  def enqueue(self,item):
    self.item.insert(self.count,item)
    self.count += 1

  def dequeueAny(self):
    return self.dequeueByType(['dog','cat'])

  def dequeueDog(self):
    return self.dequeueByType(['dog'])

  def dequeueCat(self):
    return self.dequeueByType(['cat'])

  def dequeueByType(self,animal_type):
    i =0 
    while( i< self.count):
      if (self.item[i]['type'] in animal_type):
        temp = self.item[i]
        self.item.pop(i)
        self.count -= 1
        return temp
      i += 1
    return None
