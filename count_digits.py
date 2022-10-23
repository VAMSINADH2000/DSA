# Given a number N. Count the number of digits in N which evenly divides N.

def count_digits(N):
    count = 0
    n = N
    while(N):
        digit = N%10
        if  (digit!=0) and (n%digit == 0):
            count += 1
        N = N//10
    return count
print("ans",count_digits(2446))