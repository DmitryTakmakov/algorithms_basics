# Закодируйте любую строку по алгоритму Хаффмана.

import collections
import operator


class Leaf:
    """
    Вспомогательный класс для создания дерева Хаффмана
    char - символ из кодируемой строки
    value - частота символа в строке
    """

    def __init__(self, char: str, *value: int):
        if isinstance(char, tuple):
            self.char, self.value = char
        else:
            self.char = char
            self.value = value

    def __repr__(self):
        return f'Leaf: char "{self.char}" value {self.value}'


class Node:
    """
    Вспомогательный класс для узлов дерева Хаффмана
    """

    def __init__(self, value: int, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f'Node: value {self.value} \nleft->{self.left} \nright->{self.right}'


class Huffman:
    """Основной класс для реализации алгоритма Хаффмана"""
    def __init__(self):
        self._code_table = {}

    def _get_table(self, tree, code=''):
        """рекурсивный обход дерева и построение таблицы"""
        if isinstance(tree, Node):
            self._get_table(tree.left, code=f'{code}0')
            self._get_table(tree.right, code=f'{code}1')
        elif isinstance(tree, Leaf):
            self._code_table[tree.char] = code

    def encode(self, string, detail=False):
        """Основной метод для кодирования строки"""
        self._code_table = {}
        count = collections.Counter(string)
        array = collections.deque(map(Leaf, count.most_common()))
        if detail:
            print(array)  # массив из листьев

        while len(array) > 1:  # формируем дерево
            array = collections.deque(sorted(array, key=operator.attrgetter('value')))
            leaf_small = array.popleft()
            leaf_bigger = array.popleft()
            array.append(Node(leaf_small.value + leaf_bigger.value, leaf_small, leaf_bigger))

        tree = array.pop()
        if detail:
            print(tree)  # а вот и само дерево!

        self._get_table(tree)
        if detail:
            print(self._code_table)

        return ' '.join([self._code_table[char] for char in string])


if __name__ == '__main__':
    huf = Huffman()
    print(huf.encode('beep boop beer'))

    print('*' * 50)
    my_string = input('Введите строку для кодировки: ')
    print(huf.encode(my_string, detail=True))
