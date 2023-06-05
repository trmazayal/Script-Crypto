def main():
    p = 5
    q = 11
    e = 27
    
    
    ku,kr = key_setup(p,q,e)
    
    M = [88] # Note: 88<187
    
    # Encrytion
    C = encrypt(M,ku)
    print(C)
    
    # Decryption
    M = decrypt(C,kr)
    print(M)
    # -------------------------------------
    
    # p = 53
    # q = 61
    # e = 71
    
    
    # ku,kr = key_setup(p,q,e)
    
    # M = 'sance'
    
    # Encrypt String
    # C = encrypt_string(M,ku)
    # print(C)
    
    # print('-'*50)
    
    # Decrypt String
    # C = [ '3106', '0100']
    # M = decrypt_string(C,kr)
    # print(M)
    
    # -------------------------------------
    
    # Brad mendapat pesan dari Angelina, yaitu 20. Dekripsikan pesan itu.
    cipher = [20]
    ret = decrypt(cipher, kr)
    print(f'pesan dari Angelina Untuk Brad = {ret}')
    
    # Brad mau membuat tandatangan digital untuk pesan 15 sehingga orang lain (termasuk Angelina) 
    # dapat yakin bahwa pesan itu berasal dari Brad. Buat tandatangan digital itu (tanpa fungsi hash).
    M = [15]
    cipher = encrypt(M, kr)
    print(f'tandatangan digital punya Brad = {cipher}')
    
    # Apa yang harus dilakukan oleh orang lain (misalnya Angelina) untuk memverifikasi tandatangan 
    # digital Brad tersebut?
    ret = decrypt(cipher, kr)
    print(f'Verif pesan dari Brad = {ret}')
    
    # Keamanan RSA berdasarkan kesulitan dalam pemecahan problem apa?
    # Keamanan RSA berdasarkan kesulitan dalam pemecahan problem faktorisasi bilangan bulat yang besar.
    
    
mapping_string = {
    'a': '00','b':'01','c':'02','d':'03','e':'04',
    'f': '05','g':'06','h':'07','i':'08','j':'09',
    'k': '10','l':'11','m':'12','n':'13','o':'14',
    'p': '15','q':'16','r':'17','s':'18','t':'19',
    'u': '20','v':'21','w':'22','x':'23','y':'24',
    'z': '25','A':'26','B':'27','C':'28','D':'29',
    'E': '30','F':'31','G':'32','H':'33','I':'34',
    'J': '35','K':'36','L':'37','M':'38','N':'39',
    'O': '40','P':'41','Q':'42','R':'43','S':'44',
    'T': '45','U':'46','V':'47','W':'48','X':'49',
    'Y': '50','Z':'51','0':'52','1':'53','2':'54',
    '3': '55','4':'56','5':'57','6':'58','7':'59',
    '8': '60','9':'61',' ':'62','.':'63',',':'64',
    ';': '65','?':'66'
}

#  create key generation
def key_setup(p,q,e):
    print(f'1. Select primes: p = {p}, q = {q}')
    n = p*q
    print(f'2. Compute n = p*q = {p}*{q} = {n}')
    phi = (p-1)*(q-1)
    print(f'3. Compute phi({n}) = (p-1)*(q-1) = {phi}')
    print(f'4. Select e: gcd(e,{phi}) = 1, choose e = {e}')
    d = modinv(e,phi)
    print(f'5. Determine d: de = 1 mod {phi} and d < {phi}. The value is d = {d}, since {e}*{d} = {e*d} = 1 mod {phi}')
    print(f'6. Publish public key KU (e,n) = ({e},{n})')
    print(f'7. publish secret private key KR (d,n) = ({d},{n})')
    print('-'*50)
    return (e,n),(d,n)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse tidak ada')
    else:
        return x % m
    
def egcd(a, b):
    # if a == 0:
    #     return (b, 0, 1)
    # else:
    #     g, y, x = egcd(b % a, a)
    # return (g, x - (b // a) * y, y)
    print("q\tr\tx\ty\ta\tb\tx2\tx1\ty2\ty1")
    x2, x1, y2, y1 = 1, 0, 0, 1
    if b == 0:
        d, x, y = a, 1, 0
        return d, x, y
    else:
        q, r, x, y = '-', '-', '-', '-'
        print(q, r, x, y, a, b, x2, x1, y2, y1, sep = "\t")
        while b > 0:
            q = a // b
            r = a -q*b
            x = x2 - q*x1
            y = y2 - q*y1
            a = b
            b = r
            x2 = x1
            x1 = x
            y2 = y1
            y1 = y
            print(q, r, x, y, a, b, x2, x1, y2, y1, sep = "\t")
        d = a
        x = x2
        y = y2
        return d, x, y

#  create encryption and decryption
def encrypt(M,ku):
    e,n = ku
    res = []
    for Mi in M:
        C = Mi ** e % n
        print(f'Encrypt C = {Mi}^{e} mod {n}', end=' = ')
        res.append(C)
    return res

    # C = M ** e % n
    # return C

def decrypt(C,kr):
    d,n = kr
    ret = []
    for Ci in C:
        M = Ci ** d % n
        print(f'Decrypt M = {Ci}^{d} mod {n}', end=' = ')
        ret.append(M)
    return ret

    # M = C ** d % n
    # return M


def encrypt_string(string,ku):
    e,n = ku
    blocks = []
    string = string + ' '
    for char in string:
        blocks += mapping_string[char]
    # Break the message into blocks of 4 digits each
    four_blocks = [''.join(blocks[i:i+4]) for i in range(0,len(blocks),4)]
    for i in range(len(four_blocks)):
        if len(four_blocks[i]) < 4:
            four_blocks[i] = '0'*(4-len(four_blocks[i])) + four_blocks[i]
            
    # Convert each block into an integer
    print(f'Encrypt String [{string}], M = {four_blocks}')
    M = [int(block) for block in four_blocks]
    res = []
    # Encrypt each block
    for Mi in M:
        C = Mi ** e % n
        if C < 1000:
            C = '0'*(4-len(str(C))) + str(C)
            print(f'Encrypt C = {Mi}^{e} mod {n} = {C}')
            res.append(C)
            continue
        print(f'Encrypt C = {Mi}^{e} mod {n} = {C}')
        res.append(str(C))
    return res

def decrypt_string(C,kr):
    print(f'The plaintext for C = {C}')
    d,n = kr
    ret = []
    for Ci in C:
        M = int(Ci) ** d % n
        if M < 1000:
            M = '0'*(4-len(str(M))) + str(M)
            print(f'Decrypt M = {Ci}^{d} mod {n} = {M}')
            ret.append(M)
            continue
        print(f'Decrypt M = {Ci}^{d} mod {n} = {M}')
        ret.append(M)
    # Convert each block back into 4 digits
    M = [str(block) for block in ret]
    for i in range(len(M)):
        if len(M[i]) < 4:
            M[i] = '0'*(4-len(M[i])) + M[i]
            
    # Convert each block back into a character
    string = ''
    for block in M:
        string += chr(int(block[:2])+97) + chr(int(block[2:])+97)
    return string


if __name__ == '__main__':
    main()
    