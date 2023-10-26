import sys
import random
import mcl
mcl.mcl_init(mcl.CurveType.MCL_BLS12_381)

r_A, h_A = [], []
r = mcl.Fr()
h = mcl.Fr()

data = input()
sys.stderr.write(f'\t[U] Data: {data} #\n')
sys.stdout.flush()
n = int(input())
sys.stderr.write(f'\t[U] Cached hashes: {n} #\n')
sys.stdout.flush()

for i in range(n):
    r.set_by_CSPRNG()
    r_A.append(r.getStr())
    h = h.set_hash_of(f'{data}{r}')
    h_A.append(h.getStr())

for r, h in zip(r_A, h_A):
    sys.stderr.write(f'  {r}: {h}\n')
sys.stderr.flush()

try:
    while True:
        command = input()

        if command == 'q':
            break
        if command == 's':
            for r, h in zip(r_A, h_A):
                sys.stderr.write(f'  {r}: {h}\n')
            sys.stderr.flush()
            continue

        if not command or command in r_A:
            if not command:
                c = random.randint(0, n - 1)
                r = r_A[c]
                h = h_A[c]
            else:
                r = command
                h = h_A[r_A.index(r)]
    
            sys.stderr.write(f'-> {r}: {h}\n')
            sys.stdout.write(f'{r}\n')
            sys.stdout.flush()
            cloud_out = input()
            if cloud_out == h:
                sys.stderr.write('\t[U] Cloud hash correct\n')
            else:
                sys.stderr.write('\t[U] CLOUD IS WRONG\n')

        else:
            r = command
            sys.stderr.write(f'-> : ???\n')
            sys.stdout.write(f'{r}\n')
            sys.stdout.flush()
            cloud_out = input()
            sys.stderr.write('\t[U] New hash stored\n')
            r_A.append(r)
            h_A.append(cloud_out.strip())
            
except EOFError:
    pass