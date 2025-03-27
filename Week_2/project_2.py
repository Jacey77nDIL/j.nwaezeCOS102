import math


def solve_quadratic():
    A = float(input("Enter coefficient A: "))
    B = float(input("Enter coefficient B: "))
    C = float(input("Enter coefficient C: "))

    discriminant = B ** 2 - 4 * A * C
    if discriminant > 0:
        root1 = (-B + math.sqrt(discriminant)) / (2 * A)
        root2 = (-B - math.sqrt(discriminant)) / (2 * A)
        print(f"The roots are: {root1} and {root2}")
    elif discriminant == 0:
        root = -B / (2 * A)
        print(f"The root is: {root}")
    else:
        real_part = -B / (2 * A)
        imaginary_part = math.sqrt(abs(discriminant)) / (2 * A)
        print(f"The roots are: {real_part} ± {imaginary_part}i")


def solve_cubic():
    A = float(input("Enter coefficient A: "))
    B = float(input("Enter coefficient B: "))
    C = float(input("Enter coefficient C: "))
    D = float(input("Enter coefficient D: "))

    # Convert to depressed cubic form: x^3 + px + q = 0
    p = (3 * A * C - B ** 2) / (3 * A ** 2)
    q = (2 * B ** 3 - 9 * A * B * C + 27 * A ** 2 * D) / (27 * A ** 3)

    delta = (q ** 2 / 4) + (p ** 3 / 27)
    if delta > 0:
        u = (-q / 2 + math.sqrt(delta)) ** (1 / 3)
        v = (-q / 2 - math.sqrt(delta)) ** (1 / 3)
        root = u + v - B / (3 * A)
        print(f"One real root: {root}")
    elif delta == 0:
        u = (-q / 2) ** (1 / 3)
        root1 = 2 * u - B / (3 * A)
        root2 = -u - B / (3 * A)
        print(f"Double root: {root1}, Single root: {root2}")
    else:
        r = math.sqrt(-p ** 3 / 27)
        theta = math.acos(-q / (2 * r))
        root1 = 2 * (-p / 3) ** 0.5 * math.cos(theta / 3) - B / (3 * A)
        root2 = 2 * (-p / 3) ** 0.5 * math.cos((theta + 2 * math.pi) / 3) - B / (3 * A)
        root3 = 2 * (-p / 3) ** 0.5 * math.cos((theta + 4 * math.pi) / 3) - B / (3 * A)
        print(f"Three real roots: {root1}, {root2}, {root3}")

def quadratic_roots(a, b, c):
    """Solves ax^2 + bx + c = 0 and returns real roots if they exist."""
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None  # No real roots
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    return root1, root2

def solve_quartic():
    print("\nSolving Quartic Equation: ax⁴ + bx³ + cx² + dx + e = 0")
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    d = float(input("Enter coefficient d: "))
    e = float(input("Enter coefficient e: "))

    if a == 0:
        print("This is not a quartic equation.")
        return

    # Try factorizing into two quadratics
    for p in range(-100, 101):
        for q in range(-100, 101):
            for r in range(-100, 101):
                for s in range(-100, 101):
                    # Check if (x² + px + q)(x² + rx + s) expands to the original equation
                    if (p + r) == b/a and (q + p*r + s) == c/a and (p*s + q*r) == d/a and (q * s) == e/a:
                        print(f"Factorized form: (x² + {p}x + {q})(x² + {r}x + {s})")
                        roots1 = quadratic_roots(1, p, q)
                        roots2 = quadratic_roots(1, r, s)
                        roots = []
                        if roots1:
                            roots.extend(roots1)
                        if roots2:
                            roots.extend(roots2)
                        print(f"Real roots: {roots}")
                        return

    print("Factorization failed. Using numerical solution.")

    # Numerical approach (Ferrari’s method, fixed)
    alpha = -3 * (b ** 2) / (8 * a ** 2) + c / a
    beta = (b ** 3) / (8 * a ** 3) - (b * c) / (2 * a ** 2) + d / a
    gamma = -3 * (b ** 4) / (256 * a ** 4) + (c * b ** 2) / (16 * a ** 3) - (b * d) / (4 * a ** 2) + e / a

    # Solve cubic resolvent
    P = -alpha**2 / 12 - gamma
    Q = -alpha**3 / 108 + (alpha * gamma) / 3 - beta**2 / 8
    R = -Q / 2 + math.sqrt(Q**2 / 4 + P**3 / 27)

    if R < 0:
        print("No real roots exist.")
        return

    U = R ** (1 / 3)
    y = -5 * alpha / 6 + U - P / (3 * U)
    W = math.sqrt(alpha + 2 * y)

    roots = []
    for sign1 in [-1, 1]:
        for sign2 in [-1, 1]:
            term = -b / (4 * a) + sign1 * W / 2 + sign2 * math.sqrt(-(3 * alpha + 2 * y + sign1 * (2 * beta / W))) / 2
            if not math.isnan(term):
                roots.append(term)

    print(f"Real roots: {roots}")

def main():
    while True:
        print("Choose an operation:")
        print("1. Solve Quadratic Equation")
        print("2. Solve Cubic Equation")
        print("3. Solve Quartic Equation")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            solve_quadratic()
        elif choice == '2':
            solve_cubic()
        elif choice == '3':
            solve_quartic()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if True:
    main()
