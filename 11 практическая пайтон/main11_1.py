#Конушкина П.М.
# Вариант 16
'''Практическая 11 - Дана строка. Указать слова в этой строке, содержащие хотя бы одну букву к.'''
def find_words_with_k(text):

    words = text.split()
    

    words_with_k = []
    

    for word in words:
        if 'к' in word.lower():
            words_with_k.append(word)
    
    return words_with_k


input_string = "Каждый охотник желает знать, где сидит фазан"
result = find_words_with_k(input_string)

print("Слова, содержащие букву 'к':")
for word in result:
    print(word)
