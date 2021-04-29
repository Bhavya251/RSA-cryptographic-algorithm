import random

def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

primesList = get_primes(1000)

#=============================================================

def getStats():

    p = primesList[random.randint(0,100)]
    q = primesList[random.randint(0,100)]
    n = p*q
    phi = (p-1)*(q-1)
    e = 17

    return (n, phi, e)
'''
This code was in an effort to keep e from being a fector of phi
was ;ater just replaced with a larger prime number for e. (17)

    if phi%3 != 0
        e = 3
    elif phi%5 != 0
        e = 5
    elif phi%7 != 0
        e = 7
'''

statsTuple = getStats()
def getPrivateKey():
    newphi = statsTuple[1]
    newE = statsTuple[2]
    def euclid(num1, num2, num3, num4):
        if num3 == 1:
            key = num4
            return key
        else:
            newNum3 = num1 - ((num1//num3)*num3)
            newNum4 = (num2 - (num4 * (num1//num3))) %newphi
            return euclid(num3,num4,newNum3,newNum4)
    return euclid(newphi,newphi,newE,1)

privateKey = getPrivateKey()

def encrypt(message): #returns list of each char, encryted
    cipherList = []
    for ltr in message:
        encryptedLtr = (ord(ltr)**statsTuple[2] % statsTuple[0])
        cipherList.append(encryptedLtr)
    print("Encrypted Text : ",cipherList)
    return cipherList

def decrypt(cipherTextList):
    d = int(input("what's the private key?"))
    if d == privateKey:
        message = []
        for item in cipherTextList:
            decryptedLtr = chr((item**d) % statsTuple[0])
            message.append(decryptedLtr)

        print ("Message:", ''.join(message))

    else:
        print ("Invalid key")

















