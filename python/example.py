def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    i = min(a, b)
    while i:         #while/for循环完成迭代过程，函数自身调用完成递归过程
        if a % i != 0 or b % i != 0:
            i -= 1
        else :
            return i
            
#A  mathematical trick (due to Euclid)
def gcdRecur(a, b):            
if b ==0:
        return a
    else:
        return gcdRecur(b,a%b)
