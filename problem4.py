def wears_jackets(temp, raining):
  """
  number, boolean -> boolean

  returns True if Belle wears a jacket when it is raining or the temperature is below 60

  >>> wears_jackets(50,False)
  True
  >>> wears_jackets(70,False)
  False
  >>> wears_jackets(70,True)
  True
  >>> wears_jackets(60,False)
  False
  """
  return temp < 60 or raining
