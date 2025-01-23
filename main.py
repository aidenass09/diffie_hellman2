from dh import DiffieHellman

def main():
    print("Welcome to the Diffie-Hellman Key Exchange Simulator!")

    # Alice and Bob generate their keys
    alice = DiffieHellman()
    bob = DiffieHellman(p=alice.p, g=alice.g)

    print(f"\nPrime (p): {alice.p}")
    print(f"Primitive Root (g): {alice.g}")

    print("\nAlice's Public Key:", alice.public_key)
    print("Bob's Public Key:", bob.public_key)

    # Exchange public keys and compute shared secret
    alice_secret = alice.get_shared_secret(bob.public_key)
    bob_secret = bob.get_shared_secret(alice.public_key)

    print("\nShared Secret (Alice):", alice_secret)
    print("Shared Secret (Bob):", bob_secret)

    if alice_secret == bob_secret:
        print("\nSuccess! Shared secrets match.")
    else:
        print("\nError! Shared secrets do not match.")

if __name__ == "__main__":
    main()