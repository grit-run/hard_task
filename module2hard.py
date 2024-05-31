initial_number = int(input("Пожалуйста, введите число от 3 до 20: "))
result = []
for i in range(1, initial_number + 1):
    for k in range(2, initial_number):
        if i < k and i + k == initial_number or i < k and initial_number % (i + k) == 0:
            result.append(str(i))
            result.append(str(k))
print("".join(result))
