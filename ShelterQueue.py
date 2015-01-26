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

  def dequeueDog(self):
    i =0 
    while(self.item[i]['type'] !="dog"  and i<= self.count ):
      i += 1
    if self.item[i]['type'] =="dog":
      temp = self.item[i]
      self.item.pop(i)
      self.count -= 1
      return temp

  def dequeueCat(self):
    return self.dequeueByType('cat')

  def dequeueByType(self,animal_type):
    i =0 
    while(self.item[i]['type'] != animal_type  and i<= self.count ):
      i += 1
    if self.item[i]['type'] == animal_type:
      temp = self.item[i]
      self.item.pop(i)
      self.count -= 1
      return temp
