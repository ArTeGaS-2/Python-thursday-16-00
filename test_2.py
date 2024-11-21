num = int(input("Введіть кількість клумб: "))
data = []
for i in range(num):
    print(f"Введіть параметри для клумби{i + 1}:")
    a = float(input("Введіть довжину клумби в метрах: "))
    b = float(input("Введіть ширину клумби в метрах: "))
    perimeter = 2 * (a + b)
    seedlings = a * b * 4
    data.append([a,b,perimeter,seedlings])

print("+------------+------------+-----------+---------+")
for i in data:
    print(f"|Довжина: {i[0]}| Ширина: {i[1]}| Периметр: {i[2]}м| Сажанці: {i[3]}|")
    print("+------------+------------+-----------+---------+")