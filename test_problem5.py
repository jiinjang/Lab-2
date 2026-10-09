from problem5 import trailing_zeros, trailing_zeros_in_factorial

def test_trailing_zeros():
  assert trailing_zeros(300)==2
  assert trailing_zeros(123)==0
  assert trailing_zeros(1000)==3

def test_trailing_zeros_in_factorial():
  assert trailing_zeros_in_factorial(3)==0
  assert trailing_zeros_in_factorial(10)==2
  assert trailing_zeros_in_factorial(25)==6
