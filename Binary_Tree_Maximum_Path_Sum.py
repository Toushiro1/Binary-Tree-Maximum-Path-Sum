class TreeNode:

    # конструктор узла
    def __init__(self, val):
        # проверка значения узла
        if not isinstance(val, int):
            raise ValueError("Значение узла должно быть целым числом")
        self.val = val # значение узла (будет учавствовать в сумме пути)
        self.left = None # указатель на левое поддерево
        self.right = None # указатель на правое поддерево


def build_tree(values):
    # проверка входных данных
    if not isinstance(values, list):
        raise TypeError("Входные данные должны быть списком")

    if not values:
        raise ValueError("Список входных данных не должен быть пустым")

    nodes = []
    #
    for value in values:
        if value is None: # сохраняем позицию None
            nodes.append(None)
        elif isinstance(value, int):
            nodes.append(TreeNode(value))
        else:
            raise ValueError(f"Некорректное значение во входных данных: {value}")

    child = nodes[::-1] # развернём список, чтобы вытащить узлы 
    root = child.pop()

    # строим дерево, связывая узлы
    for node in nodes:
        if node is not None:
            if child:
                node.left = child.pop()
            if child:
                node.right = child.pop()

    return root

def max_path_sum(root):

    if root is None:
        raise ValueError("Корень дерева не может быть None")

    max_sum = -10**18  # аналог отрицательной бесконечности

    def dfs(node):

        # рекурсивный обход дерева сверху вниз
        nonlocal max_sum
        if node is None:
            return 0

        # рекурсивно вычисляем вклад левого поддерева
        left_gain = dfs(node.left)
        if left_gain < 0:
            left_gain = 0

        # рекурсивно вычисляем вклад правого поддерева
        right_gain = dfs(node.right)
        if right_gain < 0:
            right_gain = 0

        # полный путь через текущий узел
        current_path_sum = node.val + left_gain + right_gain

        # обновим глобальный максимум
        if current_path_sum > max_sum:
            max_sum = current_path_sum

        # возвращаем максимум для одного пути (левый или правый)
        return node.val + (left_gain if left_gain > right_gain else right_gain)

    dfs(root)
    return max_sum


# функция для вычисления максимальной суммы пути в бинарном дереве
    def binary_tree_max_path_sum(data):

        root = build_tree(data)
        return max_path_sum(root)


class Solution:
    def maxPathSum(self, root):
        return max_path_sum(root)