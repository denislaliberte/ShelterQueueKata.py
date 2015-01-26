import unittest
from ShelterQueue import ShelterQueue

class ShelterQueue_test(unittest.TestCase):
  def setup_method(self, method):
    self.queue = ShelterQueue()
  def test_empty_queue(self):
    self.assertEqual(self.queue.empty(),True)
    self.assertEqual(self.queue.dequeueAny(),None)

  def test_one_item(self):
    self.queue.enqueue(1)
    self.assertEqual(self.queue.empty(),False)
    self.assertEqual(self.queue.dequeueAny(),1)
    self.assertEqual(self.queue.empty(),True)

  def test_two_item(self):
    self.queue.enqueue(1)
    self.queue.enqueue(2)
    self.assertEqual(self.queue.dequeueAny(),1)
    self.assertEqual(self.queue.empty(),False)
    self.assertEqual(self.queue.dequeueAny(),2)
    self.assertEqual(self.queue.empty(),True)

  def test_dequeue_dog(self):
    self.queue.enqueue({"type":"cat","name":"larry"})
    self.queue.enqueue({"type":"dog","name":"fido"})
    self.assertEqual(self.queue.dequeueDog(),{"type":"dog","name":"fido"})
    self.assertEqual(self.queue.dequeueAny(),{"type":"cat","name":"larry"})
    
  def test_dequeue_cat(self):
    self.queue.enqueue({"type":"dog","name":"fido"})
    self.queue.enqueue({"type":"cat","name":"larry"})
    self.assertEqual(self.queue.dequeueCat(),{"type":"cat","name":"larry"})
    self.assertEqual(self.queue.dequeueCat(),None)
    self.assertEqual(self.queue.dequeueAny(),{"type":"dog","name":"fido"})



