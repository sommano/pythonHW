def compute_power(x, y):
    running_total = 1          # initialize the accumulator!
    for counter in range(y):
        running_total = running_total * x

    return running_total

base = int(input("Enter a base number:"))
power = int(input("Enter a power:"))

result = compute_power(base, power)
print("The result of", base, "to the power of",power, "is", result)

print(base**power)