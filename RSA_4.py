import random

def isPrime(num):
    flag = 0
    temp = num / 2
    for j in range(2, int(temp)+1):
        if (num % j) == 0:
            flag = 1
            break

    if flag == 0:
        return 1
    else:
        return 0


# def isPrime(n):
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return 0
#     return 1


def gcd(e, phi):

    if e < phi:
        temp = e
        e = phi
        phi = temp

    if e%phi==0:
        return phi
    else:
        return gcd(phi,e%phi)


size = int(input('Range of Prime Number: '))

p = random.randrange(2, size)
while isPrime(p) == 0 and p != 0:
    p = random.randrange(1, size)

q = random.randrange(2, size)
while isPrime(q) == 0 or p == q or q == 0:
    q = random.randrange(1, size)

print('\nP: ', p)
print('\nQ: ', q)

n = p * q
print('\nN: ', n)

fi = (p - 1) * (q - 1)
print('\nFI(n): ', fi)

pubkey = random.randrange(1, size)
while fi<pubkey or gcd(pubkey, fi) != 1:
    pubkey = random.randrange(1, size)
print('\nPublic Key: ', pubkey)

for i in range(1,size*1000):
    ans = (pubkey*i) % fi;
    # print(ans)
    if ans==1:
        privatekey = i;
        break;

print('\nPrivate Key: ', privatekey)

plaintext = int(input('\n\nEnter a message: '))

ciphertext = int(pow(plaintext, pubkey) % n)
print('\n\nEncrypted Text: ', ciphertext)

decrypted = int(pow(ciphertext, privatekey) % n)
print('\n\nDecrypted Text: ', decrypted)
