from problem1 import pythagorean_triples

def test_pythagorean_triples():
  assert pythagorean_triples(3,4,5)==True
  assert pythagorean_triples(5,6,7)==False
  assert pythagorean_triples(6,8,10)==True
