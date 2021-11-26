from Crypto.Util.number import long_to_bytes,bytes_to_long,getPrime,isPrime
import random

def isG (g, p, q):
    if g**2%p == 1:
        return False
    if pow(g, q, p) == 1:
        return False
    return True
def KeyGen():
    # hoge
    N = 100
    q = getPrime(100)
    p =  2*q + 1
    g = 3
    x = random.randint(2, q-2)
    while g < p:
        if isG(g, p, q):
            break
        g+=1
    # h = (g**x)%p
    h = pow(g, x, p)
    return (p,q,g,h),x

def Enc(m,pk):
    p = pk[0]
    q = pk[1]
    g = pk[2]
    h = pk[3]
    r = random.randint(0, g-1)
    c1 = g**r % p
    c2 = m*(h**r) % p
    return (c1,c2)

def Dec(c,pk,sk):
    c1 = c[0]
    c2 = c[1]
    p = pk[0]
    m = c2*(pow(c1, -sk, p))%p
    return m

def HomMul(C,D):
    c1,c2 = C
    d1,d2 = D
    print(c1, c2, d1, d2)
    return (c1*d1,c2*d2)

if __name__ == '__main__':
    pk,sk = KeyGen()
    # print(pk, sk)
    # pk = (3928183223695497849842826335509679739572553697729210728552188161759961024444090329512086579, 1964091611847748924921413167754839869786276848864605364276094080879980512222045164756043289, 6, 445897201511510255180792595822889700778240185834370601901412545366645765220403565765194680)
    # sk = 1894578738804487409653291304962474167944515654334990521866776740633856235762243237188071393
    # c = (1076002951604504406631102357918366662054908533242717091065851509391971540733638353445818500, 3262609107672234771995435583585096584207001684303777674579568332995354005258716639353469378)

    # mb = b'flag'
    # m = bytes_to_long(mb)

    # c = Enc(m,pk)

    # mm = Dec(c,pk,sk)

    # assert mm == m
    # print(long_to_bytes(mm))

    m1 = 10
    m2 = 11
    c1 = Enc(m1, pk)
    c2 = Enc(m2, pk)
    H = HomMul(c1, c2)

    mm = Dec(H,pk,sk)
    print(mm)
