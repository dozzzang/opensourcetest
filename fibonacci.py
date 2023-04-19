def fib(n):
    """Returns list's last port
       This is fibonacci's function.
       
       :param n: n은 3이상이어야한다. 3 이상의 n을 입력
       :type n: int, optional
       :return: list of returned : last fibonacci's number
       :rtyp: int
       """
    fib_list = [0,1,1];
    for i in range(3,n+1):
      new_fib = fib_list[-1] + fib_list[-2]
      fib_list.append(new_fib)
   return fib_list[-1]
  print(fib(10))
    
