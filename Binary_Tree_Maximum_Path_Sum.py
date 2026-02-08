class TreeNode:

    # конструктор узла
    def __init__(self, val):
        # проверка значени€ узла
        if not isinstance(val, int):
            raise ValueError("«начение узла должно быть целым числом")
        self.val = val # значение узла (будет учавствовать в сумме пути)
        self.left = None # указатель на левое поддерево
        self.right = None # указатель на правое поддерево


    def build_tree(values):
        # проверка входных данных
        if not isinstance(values, list):
            raise TypeError("¬ходные данные должны быть списком")

        if not values:
            raise ValueError("—писок входных данных не должен быть пустым")

        nodes = []
        #
        for value in values:
            if value is None: # сохран€ем позицию None
                nodes.append(None)
            elif isinstance(value, int):
                nodes.append(TreeNode(value))
            else:
                raise ValueError(f"Ќекорректное значение во входных данных: {value}")

        child = nodes[::-1] # развернЄм список, чтобы вытащить узлы 
        root = child.pop()

        # строим дерево, св€зыва€ узлы
        for node in nodes:
            if node is not None:
                if child:
                    node.left = child.pop()
                if child:
                    node.right = child.pop()

        return root

    def max_path_sum(root):

        if root is None:
            raise ValueError(" орень дерева не может быть None")

        max_sum = -10**18  # аналог отрицательной бесконечности

        def dfs(node):

            # рекурсивный обход дерева сверху вниз
            nonlocal max_sum
            if node is None:
                return 0

            # рекурсивно вычисл€ем вклад левого поддерева
            left_gain = dfs(node.left)
            if left_gain < 0:
                left_gain = 0

            # рекурсивно вычисл€ем вклад правого поддерева
            right_gain = dfs(node.right)
            if right_gain < 0:
                right_gain = 0

            # полный путь через текущий узел
            current_path_sum = node.val + left_gain + right_gain

            # обновим глобальный максимум
            if current_path_sum > max_sum:
                max_sum = current_path_sum

           # возвращаем максимум дл€ одного пути (левый или правый)
            return node.val + (left_gain if left_gain > right_gain else right_gain)

        dfs(root)
        return max_sum