with open('input.txt', encoding='ascii') as file:
    nums = [int(line.strip()) for line in file]

fuel = 0
fuel_total = 0

for n in nums:
    mass = n // 3 - 2
    fuel += mass
    while mass > 0:
        fuel_total += mass
        mass = mass // 3 - 2

print(fuel)
print(fuel_total)
