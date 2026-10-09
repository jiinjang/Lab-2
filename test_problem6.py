from problem6 import successor, add_without_add

def test_successor():
  assert successor(4)==5

def test_add_without_add():
  assert add_without_add(3,4)==7
  assert add_without_add(5,2)==7
  assert add_without_add(0,6)==6
