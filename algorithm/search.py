
words = []


def create_list():
    global words
    with open("russian.txt", "r", encoding="windows-1251") as file: # Исли у вас текстовый файл со словами с кодировкой UTF-8, меняйте encoding 
            for line in file:
                word = line.strip()
                words.append(word)
            words = sorted(words) 


def binary_search(target):
    low = 0
    high = len(words) - 1
    while low <= high:
        mid = (low + high) // 2
        if words[mid] == target:
            return True
        elif words[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False
