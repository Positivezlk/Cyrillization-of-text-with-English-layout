import time
from search import binary_search
from ru_en_list import ru_en_keyboard_layaout


def fix_input(text):
    result = ''
    ru_words = []
    for word in text.split(' '):
        ru_word = ''
        for char in word:
            if char.lower() in ru_en_keyboard_layaout.keys():
                ru_word += f'{ru_en_keyboard_layaout.get(char)}'
            else:
                ru_word += char
        if not binary_search(ru_word.lower()):
            ru_word = word
        ru_words.append(ru_word)
    for word in ru_words:
        result += word + ' '
    return result.strip()


while True:
    request = input('Напишите сюда что-нибудь: ')
    start_time = time.time()
    fixed_text = fix_input(request)
    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f'Исправленный текст: {fixed_text}')
    print(f'Время отклика: {elapsed_time:.4f} секунд\n')
