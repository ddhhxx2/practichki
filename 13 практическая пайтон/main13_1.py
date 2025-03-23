def write_natural_numbers_to_file(filename, N):
    """Записывает N натуральных чисел в файл."""
    with open(filename, 'w') as f:
        for i in range(1, N + 1):
            f.write(f"{i}\n")

def filter_numbers_from_file(input_filename, output_filename, K):
    """Читает числа из входного файла и записывает в выходной файл только те, которые не кратны K."""
    with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
        for line in infile:
            number = int(line.strip())
            if number % K != 0:
                outfile.write(f"{number}\n")

def print_file_contents(filename):
    """Выводит содержимое файла на печать."""
    with open(filename, 'r') as f:
        for line in f:
            print(line.strip())

# Задаем параметры
N = 20  # Количество натуральных чисел
K = 5   # Число, кратность которому мы проверяем
input_filename = 'numbers.txt'
output_filename = 'filtered_numbers.txt'

# Записываем N натуральных чисел в файл
write_natural_numbers_to_file(input_filename, N)

# Фильтруем числа и записываем в другой файл
filter_numbers_from_file(input_filename, output_filename, K)

# Печатаем содержимое выходного файла
print("Содержимое выходного файла:")
print_file_contents(output_filename)

