import unittest
from ShelterQueue import ShelterQueue

class ShelterQueue_test(unittest.TestCase):
  def test_empty_queue(self):
    queue = ShelterQueue()
    self.assertEqual(queue.empty(),True)

  def test_one_item(self):
    queue = ShelterQueue()
    queue.enqueue(1)
    self.assertEqual(queue.empty(),False)
    self.assertEqual(queue.dequeueAny(),1)
    self.assertEqual(queue.empty(),True)

  def test_two_item(self):
    queue = ShelterQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    self.assertEqual(queue.dequeueAny(),1)
    self.assertEqual(queue.empty(),False)
    self.assertEqual(queue.dequeueAny(),2)
    self.assertEqual(queue.empty(),True)

  def test_dequeue_dog(self):
    queue = ShelterQueue()
    queue.enqueue({"type":"cat","name":"larry"})
    queue.enqueue({"type":"dog","name":"fido"})
    self.assertEqual(queue.dequeueDog(),{"type":"dog","name":"fido"})
    self.assertEqual(queue.dequeueAny(),{"type":"cat","name":"larry"})


