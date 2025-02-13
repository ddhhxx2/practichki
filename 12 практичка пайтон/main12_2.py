#Конушкина П.М.
#Вариант 17
#Практическая 12 - Слова в тексте разделены пробелами. Напечатать буквы, которых нет в первом слове, но которые присутствуют во всех других словах этого текста.
def find_unique_letters(text):
  
    words = text.split()
    
    if not words:
        return
    
  
    first_word_letters = set(words[0])
    
  
    common_letters = set(words[1]) if len(words) > 1 else set()
    
   
    for word in words[1:]:
        common_letters.intersection_update(set(word))

    unique_letters = common_letters - first_word_letters
    

    print("Буквы, которых нет в первом слове, но которые присутствуют во всех других словах:")
    print(' '.join(unique_letters))


text = "привет мир программирования"
find_unique_letters(text)