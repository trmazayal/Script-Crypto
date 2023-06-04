import GenerateModular as gm

# Diffie-Hellman Key Exchange
def main():
    modP = 83
    primitive_root = 5
    
    # private key
    Xa = 6
    Xb = 10
    
    # 1. User A memilih bilangan acak x < modP dan mengirimkan A = primitive_root^x mod modP kepada B.
    A = calculate_public_key('a',primitive_root, Xa, modP)
    
    # 2. User B memilih bilangan acak y < modP dan mengirimkan B = primitive_root^y mod modP kepada A.
    B = calculate_public_key('b',primitive_root, Xb, modP)
    
    # 3. User A menghitung kunci bersama K = B^x mod modP.
    K_A = calculate_shared_key(B, Xa, modP)
    print(f'User A menghitung kunci bersama K = B^x mod modP, yaitu {K_A}')
    
    # 4. User B menghitung kunci bersama K = A^y mod modP.
    K_B = calculate_shared_key(A, Xb, modP)
    print(f'User B menghitung kunci bersama K = A^y mod modP, yaitu {K_B}')
    
    # 5. Kedua user sekarang memiliki kunci bersama K = primitive_root^xy mod modP.
    print(f'Kedua user sekarang memiliki kunci bersama K = primitive_root^xy mod modP, yaitu {K_A} = {K_B}')
    
    # Tentukan nilai logaritma diskret dlog5,83(17).
    gen_modular = gm.generate_modular(5,83)
    # find 17 in gen_modular
    print(f'17 in gen_modular: {gen_modular.index(17)+1}')
   

def calculate_public_key(_from,primitive_root, a, modP):
    print(f'X{_from} = {a}')
    res = (primitive_root ** a) % modP
    print(f'Y{_from} = {primitive_root}^{a} mod {modP} = {res}', end='\n\n')
    return res

def calculate_shared_key(public_key, private_key, modP):
    return (public_key ** private_key) % modP

 
if __name__ == "__main__":
    main()