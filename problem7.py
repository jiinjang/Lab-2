def sum_id(n):
  """
  Returns the sum of the integers from 1 to n.

  >>> sum_id(5)
  15
  >>> sum_id(1)
  1
  """
  total = 0
  i = 1
  while i <= n:
    total = total + i
    i = i + 1
  return total


def sum_squares(n):
  """
  Returns the sum of the squares from 1 to n.

  >>> sum_squares(3)
  14
  >>> sum_squares(5)
  55
  """
  total = 0
  i = 1
  while i <= n:
    total = total + i**2
    i = i + 1
  return total


def sum(n,f):
  """
  Returns the sum of f(i) from 1 to n.

  >>> sum(5, lambda x: x)
  15
  >>> sum(3, lambda x: x**2)
  14
  """
  total = 0
  i = 1
  while i <= n:
    total = total + f(i)
    i = i + 1
  return total


def product(n,f):
  """
  Multiplies f(i) for all i from 1 to n.

  >>> product(4, lambda x: x)
  24
  >>> product(3, lambda x: x**2)
  36
  """
  total = 1
  i = 1
  while i <= n:
    total = total * f(i)
    i = i + 1
  return total


def combine_sequence(n, combine=lambda x, y: x + y, f=lambda x: x):
  """
  Combines f(i) from 1 to n using combine.

  >>> combine_sequence(5, lambda x, y: x + y, lambda x: x)
  15
  >>> combine_sequence(4, lambda x, y: x * y, lambda x: x)
  24
  """
  total = f(1)
  i = 2
  while i <= n:
    total = combine(total, f(i))
    i = i + 1
  return total
