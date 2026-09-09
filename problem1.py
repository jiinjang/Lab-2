def pythagorean_triples(a,b,c):
      """
      Returns True if a^2 + b^2 = c^2
      
      testCase
        >>> pythagorean_triples(3,4,5)
        True
        >>> pythagorean_triples(5,6,7)
        False
        >>> pythagorean_triples(6,8,10)
        True
      """

      return a**2 + b**2 == c**2
