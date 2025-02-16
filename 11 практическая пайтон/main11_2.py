#Конушкина П.М.
# Вариант 16
'''Практическая 11 - Результаты вступительных экзаменов представлены в виде списка из N строк, в
каждой из которых записаны фамилия студента и его оценки по каждому из М
экзаменов. Определить количество абитуриентов, сдавших вступительные
экзамены только на «отлично».'''
def count_excellent_students(results):
    excellent_count = 0
    for student in results:
        # Пропускаем фамилию (первый элемент) и проверяем все оценки
        if all(grade == 5 for grade in student[1:]):
            excellent_count += 1
    return excellent_count


N = 5 
M = 3  


exam_results = [
    ["Иванов", 5, 5, 5],
    ["Петров", 4, 5, 5],
    ["Сидоров", 5, 5, 5],
    ["Козлов", 5, 4, 5],
    ["Смирнов", 5, 5, 5]
]

excellent_students = count_excellent_students(exam_results)
print(f"Количество абитуриентов, сдавших все экзамены на отлично: {excellent_students}")
