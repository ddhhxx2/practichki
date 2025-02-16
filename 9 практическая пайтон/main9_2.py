#Конушкина П.М.
#Вариант 17
'''Практическая 9 - Дана последовательность целых чисел a1, а2, ..., аn. Определить пары чисел аi аj,
сумма которых аi, + аj, = m.'''
def find_pairs(sequence, m):
    pairs = []
    seen = set()
    for num in sequence:
        complement = m - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)

    return pairs
sequence = [1, 5, 7, 2, 9, 3, 6, 4]
m = 10
result = find_pairs(sequence, m)
if result:
    print(f"Пары чисел, сумма которых равна {m}:")
    for pair in result:
        print(f"{pair[0]} + {pair[1]} = {m}")
else:
    print(f"Нет пар чисел, сумма которых равна {m}")
