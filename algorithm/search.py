def binary_search(target): # На данный момент бинарный поиск не реализован
    words = []

    with open("russian.txt", "r", encoding="windows-1251") as file: # Исли у вас текстовый файл со словами с кодировкой UTF-8, меняйте encoding. Так же сюда надо вставить текстовый файл с русскими словами.
        for line in file:
            word = line.strip()
            words.append(word) 
    return target in words # Бинарный поиск через раз работает (представлен ниже). Возможно знаю, в чем проблема, буду разибраться

    # low = 0
    # high = len(words) - 1
    # while low <= high:
    #     mid = (low + high) // 2
    #     if words[mid] == target:
    #         return True
    #     elif words[mid] < target:
    #         low = mid + 1
    #     else:
    #         high = mid - 1
    # return False
