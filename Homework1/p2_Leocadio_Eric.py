#Problem 2. Pythagorean Numbers


def find_Pythagorean(n):
        triples = []
        #double nested loop to iterate over each possible combination of three numbers up to n
        for a in range(1, n+1):
            for b in range(1, n+1):
                  for c in range(1, n+1):
                        if a**2 + b**2 == c**2:
                            triples.append((a, b, c))
        return(triples)

n = int(input("Please input an integer n: "))
print(f"list of pythagorean triples: {find_Pythagorean(n)}")      