import random

def is_prime(n, k=5):
    if n <= 1:
        return False
    for _ in range(k):
        a = random.randint(2, n - 1)
        if pow(a, n - 1, n) != 1:
            return False
    return True

def generate_prime(bits=128):
    while True:
        p = random.getrandbits(bits)
        if is_prime(p):
            return p

def generate_primitive_root(p):
    if p == 2:
        return 1
    for g in range(2, p):
        if all(pow(g, (p - 1) // factor, p) != 1 for factor in [2]):
            return g
    return None

class DiffieHellman:
    def __init__(self, p=None, g=None):
        self.p = p or generate_prime()
        self.g = g or generate_primitive_root(self.p)
        self.private_key = random.randint(2, self.p - 2)
        self.public_key = pow(self.g, self.private_key, self.p)

    def get_shared_secret(self, other_public_key):
        return pow(other_public_key, self.private_key, self.p)