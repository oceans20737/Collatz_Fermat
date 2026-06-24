# -*- coding: utf-8 -*-
"""code_01_collatz_fermat_branches.ipynb
"""

# Collatz Dynamics: Mersenne-Fermat Factorization in the Collatz Inverse Tree
# Hiroshi Harada
# June 24, 2026
# Released under the MIT License
# © 2026 Hiroshi Harada

import csv

def calculate_branches(a, k_max=8, csv_filename=None):
    """
    Collatz Dynamics: Mersenne-Fermat factorization and 3J/cJ selection gate.

    This function computes the M-type and F-type factors generated from an odd nucleus 'a'
    through the transformation a*2^k ± 1, and determines which factor belongs to the 3J
    (multiples of 3) or cJ (conjugate J) class. Only the M-type factor divisible by 3
    produces the next odd nucleus in the Collatz inverse tree.

    Parameters
    ----------
    a : int
        Odd nucleus from which the inverse Collatz branches are generated.
    k_max : int
        Maximum depth (k) of the Mersenne-Fermat expansion.
    csv_filename : str or None
        If provided, results will be saved to a CSV file.

    Notes
    -----
    - M-type factor:  a*2^k - 1
    - F-type factor:  a*2^k + 1
    - Only the M-type factor divisible by 3 yields the next odd nucleus (J).
    - F-type factors are NOT used for Collatz transitions; they are used only for
      classification into the conjugate J-series (cJ).
    """

    header = [
        "k",
        "M_factor (a*2^k - 1)",
        "F_factor (a*2^k + 1)",
        "3J_source",
        "Next_odd_nucleus (J)",
        "Branch_type"
    ]

    rows = []

    print(f"=== Collatz Dynamics: Branching from odd nucleus a = {a} ===")
    print(f"{'k':<3} | {'M-factor':<22} | {'F-factor':<22} | {'3J source':<15} | {'Next J':<15} | {'Branch'}")
    print("-" * 105)

    for k in range(1, k_max + 1):
        M = a * (2 ** k) - 1
        F = a * (2 ** k) + 1

        # 3J / cJ selection gate
        if M % 3 == 0:
            J = M // 3
            branch = "Collatz (3J)"
            source = f"M ({M})"
        elif F % 3 == 0:
            J = F // 3
            branch = "Not Collatz (Conjugate J)"
            source = f"F ({F})"
        else:
            J = None
            branch = "None"
            source = "None"

        print(f"{k:<3} | {M:<22} | {F:<22} | {source:<15} | {str(J):<15} | {branch}")

        rows.append([k, M, F, source, J, branch])

    print("\n")

    # Save to CSV if requested
    if csv_filename:
        with open(csv_filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(rows)
        print(f"[Saved] CSV file written to: {csv_filename}")


if __name__ == "__main__":
    # Example test
    a = 5
    calculate_branches(a, k_max=8, csv_filename=f"collatz_branches_a={a}.csv")

