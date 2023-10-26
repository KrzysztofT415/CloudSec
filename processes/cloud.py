import sys
import mcl
mcl.mcl_init(mcl.CurveType.MCL_BLS12_381)

h = mcl.Fr()

data = input()
sys.stderr.write(f'\t[C] Data received: {data} #\n')

try:
    while True:
        c = input()
        if not c:
            break
        h = h.set_hash_of(f'{data}{c}')
        sys.stderr.write(f'\t[C] Challenge: {c}\tHash: {h} #\n')
        sys.stdout.write(f'{h}\n')
        sys.stdout.flush()
except EOFError:
    pass