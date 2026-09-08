#Problem 2. Pythagorean Numbers


def find_Pythagorean(n):
        triples = []
        for a in range(n):
            for b in range(n):
                  for c in range(n):
                        if a**2 + b**2 == c**2:
                            triples.append((a, b, c))
                            print(f"Pythagorean triple found: ({a}, {b}, {c})")
        return(triples)

n = int(input("Please input an integer n: "))
pythagoreans = find_Pythagorean(n)      