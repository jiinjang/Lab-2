from problem4 import wears_jackets

def test_wears_jackets():
  assert wears_jackets(50,False)==True
  assert wears_jackets(70,False)==False
  assert wears_jackets(70,True)==True
  assert wears_jackets(60,False)==False
