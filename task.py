# Импорт модуля os из стандартной библиотеки 
# для взаимодействия с операционной системой.
import os
# Считывание переменной окружения REMOTE_JUDGE, чтобы определить, 
# локально выполняется код или на удалённом сервере.
LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

# Если код выполняется на локальном компьютере, то...
if LOCAL:
    # Класс, описывающий элементы связного списка:
    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item


def solution(node, idx):
    # Напишите код функции здесь.
    # ヽ(´▽`)/
    pass


# Тестирующая функция для проверки решения.
# Не изменяйте её, она не требует вашего внимания.
def test():
    node3 = Node("Задача 4: Обследовать грунт в радиусе 3 м", None)
    node2 = Node("Задача 3: Измерить температуру атмосферы", node3)
    node1 = Node("Задача 2: Пробурить скважину глубиной 0.5 м", node2)
    node0 = Node("Задача 1: Фотосъёмка 360°", node1)

    new_head = solution(node0, 1)
    # Выражение, начинающееся с ключевого слова assert,
    # проверяет, что утверждение в выражении истинно.
    # Если утверждение ложно - в этом месте возникнет ошибка.
    assert new_head is node0
    assert new_head.next_item is node2
    assert new_head.next_item.next_item is node3
    assert new_head.next_item.next_item.next_item is None
    # result is node0 -> node2 -> node3


if __name__ == '__main__':
    # test()

    node5 = Node("Задача 6:", None)
    node4 = Node("Задача 5:", node5)
    node3 = Node("Задача 4:", node4)
    node2 = Node("Задача 3:", node3)
    node1 = Node("Задача 2:", node2)
    node0 = Node("Задача 1:", node1)

    
    # print(((node0.next_item).next_item).value)

    # print(node0.value)
    # print((node0.next_item).value)
    # print(((node0.next_item).next_item).value)
    # print((((node0.next_item).next_item).next_item).value)
    # print(((((node0.next_item).next_item).next_item).next_item).value)
    # print((((((node0.next_item).next_item).next_item).next_item).next_item).value)
    # print()

    previous_x = node0
    current_x = previous_x.next_item
    next_x = current_x.next_item

    print(previous_x.value)
    print(current_x.value)
    print(next_x.value)
    print()

    i = 0

    while i != 1:
        previous_x = current_x
        current_x = next_x
        next_x = current_x.next_item
        
        print(i)
        print(previous_x.value)
        print(current_x.value)
        print(next_x.value)
        print()

        i += 1

    previous_x.next_item = next_x

    print(previous_x.value)
    print((previous_x.next_item).value)

    # # step 1
    # previous_x = current_x
    # current_x = next_x
    # next_x = current_x.next_item

    # print(previous_x.value)
    # print(current_x.value)
    # print(next_x.value)
    # print()
    
    # # step 2
    # previous_x = current_x
    # current_x = next_x
    # next_x = current_x.next_item

    # print(previous_x.value)
    # print(current_x.value)
    # print(next_x.value)
    # print()



