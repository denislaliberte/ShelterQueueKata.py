import unittest
from ShelterQueue import ShelterQueue

class ShelterQueue_test(unittest.TestCase):
  def test_empty_queue(self):
    queue = ShelterQueue()
    self.assertEqual(queue.empty(),True)
