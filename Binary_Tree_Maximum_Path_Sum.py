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