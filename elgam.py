def gcd(a, b):
    global x, y
    if (b == 0):
        x=1
        y=0
        return a 
    greatest_common_divisor = gcd(b, a % b)
    x1 = x 
    y1 = y 
    
    x = y1
    y = x1 - (a // b) * y1 # // divides and returns floor
    return greatest_common_divisor
    
def encrypt(message, p, g):
    alice = Alice()
    k = 5 # choose k randomly (0 < K <= phi_p). Note phi_p = p-1
    if(gcd(p-1, k) != 1):
        print("Cannot encrypt! Something went wrong!")
    S1 = g**k % p
    inv = modInverse(k, p-1)
    print("Multiplicative Inverse: of "+str(k)+" and "+str(p-1)+" is "+str(inv))
    S2 = inv * (message-alice.x*S1) % (p-1)
    return S1, S2

def modInverse (a, m):
    greatest_common_divisor = gcd(a, m)
    if(greatest_common_divisor != 1):
        print("Mod Inverse does not exist")
    else: 
        inv = (x % m + m) % m 
        return inv

def decrypt(message, p, g, s, r):
    V1 = g**message % p
    V2 = (alice_public_key(p, g)**s * s**r) % p
    print()
    return V1 == V2 

p=19
g=10
M=14

s, r = encrypt(M, p, g)
verified = decrypt(M, p, g, s, r)

print("Given p="+str(p)+" and g="+str(g)+" and M="+str(M))
print("Hashed message: "+str((s, r)))
print("Can the signature be verified?: "+str(verified))
