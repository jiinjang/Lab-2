def wears_jackets(temp, raining):
  """
  Returns True if Belle wears a jacket when it is raining or tempearture<60

  testCase
  >>>wears_jackets(50,False)
  True
  >>>wears_jackets(70,False)
  False
  >>>wears_jackets(70,True)
  True
  >>>wears_jackets(60,False)
  False
  """
  return temp < 60 or raining

