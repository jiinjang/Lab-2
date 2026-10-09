from problem2 import is_triangle

def test_is_triangle():
  assert is_triangle(3,4,5)==True
  assert is_triangle(1,2,3)==False
  assert is_triangle(5,5,5)==True
