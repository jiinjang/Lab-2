def is_triangle(a,b,c):
  """
  number, number, number -> boolean

  returns True if a, b and c can be side lengths of a triangle

  >>> is_triangle(3,4,5)
  True
  >>> is_triangle(1,2,3)
  False
  >>> is_triangle(5,5,5)
  True
  """
  return a + b > c and a + c > b and b + c > a
