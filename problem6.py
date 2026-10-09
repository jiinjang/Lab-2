def successor(n):
  """
  integer -> integer

  returns the integer that comes immediately after n

  >>> successor(4)
  5
  """
  return n+1

def add_without_add(a,b):
  """
  integer, integer -> integer

  adds two numbers without using the + operator

  >>> add_without_add(3,4)
  7
  >>> add_without_add(5,2)
  7
  >>> add_without_add(0,6)
  6
  """
  while b > 0:
    a = successor(a)
    b = b - 1
  return a
