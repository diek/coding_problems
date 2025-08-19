def foo (x):
   def bar (z):
      return z + x
   return bar(3)

print foo(2)
