def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = int(n**0.5)
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True


numbers = list(range(1, 101))

output: list[str] = []
for n in reversed(numbers):
    if is_prime(n):
        continue
    if n % 15 == 0:
        output.append("FooBar")
    elif n % 3 == 0:
        output.append("Foo")
    elif n % 5 == 0:
        output.append("Bar")
    else:
        output.append(str(n))

print(", ".join(output))
