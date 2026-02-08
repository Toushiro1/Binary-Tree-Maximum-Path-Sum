class TreeNode:

    # конструктор узла
    def __init__(self, val):
        # проверка значени€ узла
        if not isinstance(val, int):
            raise ValueError("«начение узла должно быть целым числом")
        self.val = val # значение узла (будет учавствовать в сумме пути)
        self.left = None # указатель на левое поддерево
        self.right = None # указатель на правое поддерево
