import unittest

class math:
  def pow(num, power):
    ans = num
    while power - 1 > 0:
        power -= 1
        ans *= num
    return ans
  def fact(num):
    if num < 1:
      return 0
    ans = 1
    while num > 0:
      ans *= num
      num -= 1
    return ans
  def matr2x2det(x11, x12,
                 x21, x22):
    return x11 * x22 - x21 * x12
  def matr3x3det(x11, x12, x13,
                 x21, x22, x23,
                 x31, x32, x33):
    return x11 * (math.matr2x2det(x22, x23, x32, x33)) - x21 * (math.matr2x2det(x12, x13, x32, x33)) + x31 * (math.matr2x2det(x12, x13, x22, x23))


class math_test_case(unittest.TestCase):
  def test_pow2(self):
    self.assertEqual(math.pow(2, 1), 2)
    self.assertEqual(math.pow(2, 2), 4)
    self.assertEqual(math.pow(2, 3), 8)
    self.assertEqual(math.pow(2, 4), 16)
    self.assertEqual(math.pow(2, 5), 32)
    self.assertEqual(math.pow(2, 6), 64)
    self.assertEqual(math.pow(2, 7), 128)
    self.assertEqual(math.pow(2, 8), 256)
  def test_pow39(self):
    self.assertEqual(math.pow(39, 1), 39)
    self.assertEqual(math.pow(39, 2), 1521)
    self.assertEqual(math.pow(39, 3), 59319)
    self.assertEqual(math.pow(39, 4), 2313441)
    self.assertEqual(math.pow(39, 5), 90224199)
    self.assertEqual(math.pow(39, 6), 3518743761)
    self.assertEqual(math.pow(39, 7), 137231006679)
    self.assertEqual(math.pow(39, 8), 5352009260481)
  def test_fact(self):
    self.assertEqual(math.fact(0), 0)
    self.assertEqual(math.fact(1), 1)
    self.assertEqual(math.fact(2), 2)
    self.assertEqual(math.fact(3), 6)
    self.assertEqual(math.fact(4), 24)
    self.assertEqual(math.fact(5), 120)
    self.assertEqual(math.fact(6), 720)
  def test_matr2x2det(self):
    self.assertEqual(math.matr2x2det(1, 1, 1, 1), 0)
    self.assertEqual(math.matr2x2det(1, 1, 2, 2), 0)
    self.assertEqual(math.matr2x2det(1, 2, 30, 60), 0)
    self.assertEqual(math.matr2x2det(30, 2, -10, 5), 170)
  def test_matr2x2det(self):
      self.assertEqual(math.matr3x3det(6, 12, 1000,
                                       0, 8, 84928,
                                       0, 0, 100), 4800)
      self.assertEqual(math.matr3x3det(1, 2, 3,
                                       4, 5, 6,
                                       7, 8, 9), 0)
      self.assertEqual(math.matr3x3det(1, 2, 3,
                                       10, 10, 10,
                                       3, 2, 9), -80)
      self.assertEqual(math.matr3x3det(-9584, -134, 333,
                                       30, 30, 30,
                                       239, 777, 680), 35036880)