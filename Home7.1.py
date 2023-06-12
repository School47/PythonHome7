# 7.1[34]: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, 
# если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, 
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
# Написать функцию, которая принимает строку текста и проверяет ее ритм (по Винни-Пуху)
# Если ритм есть, функция возвращает True, иначе возвращает False
    

text1 = "пара-ра-рам рам-пам-папам па-ра-па-дам"
text2 = "пара-ра-рам рам-пум-пупам па-ре-по-дам"
text3 = "пара-ра-рам рам-пуум-пупам па-ре-по-да"
text4 = "Трам-пара-папам-парам-па-пам-пам-па Пум-пурум-пу-пурум-трам-пам-па"
text5 = "Пам-парам-пурум Пум-пурум-карам"


def is_my_text_rythmic(text):
    phrases = text.split()
    Slog_counts = []
    for phrase in phrases:
        words = phrase.split("-")
        glass_letters_counts = 0 
        for word in words:
            for letter in word:
                if letter.lower() in "аеёиоуыэюя": #все возможные гласные
                    glass_letters_counts += 1
        Slog_counts.append(glass_letters_counts)

    if all(count == Slog_counts[0] for count in Slog_counts):
        return True
    else:
        return False
    
print(is_my_text_rythmic(text1))
print(is_my_text_rythmic(text2))
print(is_my_text_rythmic(text3))
print(is_my_text_rythmic(text4))
print(is_my_text_rythmic(text5))