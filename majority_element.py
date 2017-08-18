# Uses python3
import sys

def get_majority_element(a,n):
    maximum = a[0]
    amount = 1
    for i in (a[1:]):
        if not  maximum == i:
            if amount >= 1:
                amount = amount - 1
            else:
                maximum = i
                amount = 1
        else:
            amount = amount + 1
    output = a.count(maximum)
    if output > n//2:
        return 1
    return 0



if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print (get_majority_element(a,n))
 
