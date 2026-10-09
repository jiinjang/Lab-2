from problem7 import sum_id, sum_squares, sum, product, combine_sequence

def test_sum_id():
  assert sum_id(5)==15
  assert sum_id(1)==1

def test_sum_squares():
  assert sum_squares(3)==14
  assert sum_squares(5)==55

def test_sum():
  assert sum(5,lambda x: x)==15
  assert sum(3,lambda x: x**2)==14

def test_product():
  assert product(4,lambda x: x)==24
  assert product(3,lambda x: x**2)==36

def test_combine_sequence():
  assert combine_sequence(5,lambda x,y: x+y,lambda x: x)==15
  assert combine_sequence(4,lambda x,y: x*y,lambda x: x)==24
