def print_range(start, stop, step):
  """
  number, number, number -> None

  prints numbers starting at start and stopping before stop using a while loop

  >>> print_range(0,5,1)
  0
  1
  2
  3
  4
  """
  while start < stop:
    print(start)
    start = start + step
