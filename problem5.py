def trailing_zeros(n):
  """
  Returns the number of zeros at the end of n.

  >>> trailing_zeros(300)
  2
  >>> trailing_zeros(1200)
  2
  >>> trailing_zeros(123)
  0
  >>> trailing_zeros(1000)
  3
  """
  if n % 10 != 0:
    return 0
  return 1 + trailing_zeros(n // 10)


def trailing_zeros_in_factorial(n):
  """
  Returns the number of trailing zeros in n!.

  >>> trailing_zeros_in_factorial(5)
  1
  >>> trailing_zeros_in_factorial(10)
  2
  >>> trailing_zeros_in_factorial(25)
  6
  >>> trailing_zeros_in_factorial(100)
  24
  """
  if n < 5:
    return 0
  return n // 5 + trailing_zeros_in_factorial(n // 5)
