def is_triangle(a,b,c):
  """
  Returns True if a,b,c can be side lengths of a triangle
  testCase
    >>> is_triangle(3,4,5)
    True
    >>> is_triangle(1,2,3)
    False
    >>> is_triangle(5,5,5)
    True
  """
  return a + b > c and a + c > b and b + c > a
