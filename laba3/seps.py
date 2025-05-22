def is_palindrome(lst):
    for i in range(len(lst) // 2):
          if lst[i] != lst[(i+1)*-1]:
               return False
    else:
         return True


print(is_palindrome([1, 2, 3,4,7, 2, 1]))
print(is_palindrome('spam'))

def is_palindrome_rec(lst):
     if len(lst)==0 or len(lst)==1:
          return True
     else:
          if lst[0]==lst[-1]:
               return is_palindrome_rec(lst[1:-1]) 
          else: 
               return False 
          
print(is_palindrome_rec([1, 2, 3, 4 ,7, 2, 1]))
print(is_palindrome_rec('spam'))
print(is_palindrome_rec('ololo'))


def qwe(n):
    if n <= 3:
          return 1
    x1 = x2 = x3 = 1 
    for i in range(n):
          tmp = x3+x1
          x1 = x2
          x2 = x3
          x3 = tmp 
    return x3

print(qwe(10))

def qwe_rec(x1, x2, x3, n):
     if n < 1:
          return x3
     tmp = x3 + x1
     x1 = x2
     x2 = x3
     x3 = tmp 
     return(qwe_rec(x1, x2, x3, n-1))

print(qwe_rec(1, 1, 1, 10)) 
