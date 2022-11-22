# Example function return
def is_prime(num):
    for i in range(2,num):
        if (num%i==0):
            return False
    return True

for i in range(2,21):
    if is_prime(i):
        print(i)