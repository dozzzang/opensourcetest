def fib(n):
    fib_list = [0,1,1];
    for i in range(3,n+1):
      new_fib = fib_list[-1] + fib_list[-2]
      fib_list.append(new_fib)
   return fib_list[-1]
  print(fib(10))
    
