#!/usr/bin/env python3

"""
Simple Secure MPC Demo (No Modulus, Beginner Friendly)

- Demonstrates how additive secret sharing works.
- No modulus, no cryptography terminology, no complexity.
- Only shows the basic intuition behind MPC.
"""

import random

def share_secret(secret, n_parties):
    """
    Split a secret into n random pieces that sum to the original secret.
    Example: 42 -> [10, -5, 37] (random values)
    """
    shares = []
    for _ in range(n_parties - 1):
        shares.append(random.randint(-1000, 1000))  # random-looking numbers
    
    final_share = secret - sum(shares)
    shares.append(final_share)
    random.shuffle(shares)
    return shares

def secure_sum_demo(secrets, n_parties):
    print("\n=== Secure MPC Demo: Secret Sharing for Sum ===")
    print(f"Number of parties: {n_parties}")
    print(f"Input values: {secrets}")
    print("\nStep 1: Split each input into random shares.\n")

    # Step 1: Secret share each number
    all_shares = []
    for i, s in enumerate(secrets, start=1):
        shares = share_secret(s, n_parties)
        all_shares.append(shares)
        print(f"  Secret {i}: {s} -> Shares: {shares}")

    print("\nStep 2: Each party adds the shares they received.\n")

    # Step 2: each party adds their column
    party_totals = []
    for p in range(n_parties):
        party_total = sum(row[p] for row in all_shares)
        party_totals.append(party_total)
        print(f"  Party {p+1} sees partial sum: {party_total}")

    print("\nStep 3: Combine the party partial sums.\n")

    final_sum = sum(party_totals)
    print(f"Final secure sum revealed: {final_sum}")
    print(f"Average: {final_sum / len(secrets)}")

def prompt_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Please enter an integer.")

def main():
    print("Simple Secure MPC Demo (No Modulus)")
    print("----------------------------------")

    n_parties = prompt_int("Number of parties (>=2): ")
    if n_parties < 2:
        print("Need at least 2 parties.")
        return

    count = prompt_int("How many input numbers? ")
    secrets = []
    for i in range(count):
        secrets.append(prompt_int(f"  Input {i+1}: "))

    secure_sum_demo(secrets, n_parties)

if __name__ == "__main__":
    main()