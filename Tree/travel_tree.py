# 트리의 각 노드 클래스
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = self._setting_tree()

    # 노드로 트리 세팅
    @staticmethod
    def _setting_tree():
        root = Node('A')
        new_node = Node('B')
        root.left = new_node
        new_node.left = Node('C')
        new_node.right = Node('D')
        new_node = Node('E')
        root.right = new_node
        new_node.left = Node('F')
        new_node.right = Node('G')
        new_node = new_node.right
        new_node.right = Node('H')
        new_node = new_node.right
        new_node.left = Node('I')
        return root

    # 전위 순회 (preorder travel)
    @classmethod
    def preorder_traverse(cls, node):
        if node is None:
            return
        print('preorder_traverse : ', node.data)
        cls.preorder_traverse(node.left)
        cls.preorder_traverse(node.right)

    # 중위 순회 (inorder travel)
    @classmethod
    def inorder_traverse(cls, node):
        if node is None:
            return
        cls.inorder_traverse(node.left)
        print('inorder_traverse : ', node.data)
        cls.inorder_traverse(node.right)

    # 후위 순회 (postorder travel)
    @classmethod
    def postorder_traverse(cls, node):
        if node is None:
            return
        cls.postorder_traverse(node.left)
        cls.postorder_traverse(node.right)
        print('postorder_traverse : ', node.data)


if __name__ == '__main__':
    tree = Tree()
    root = tree.root
    methods = dir(Tree)
    # Tree 클래스 객체 메소드 순회
    for method in methods:
        if 'traverse' in method:
           call = getattr(Tree, method)         
           call(root)



    # root_node = setting_tree()
    # explains = [preorder_traverse, inorder_traverse, postorder_traverse]
    # for explain in explains:
    #     print('*' * 50, f'{explain.__name__}', '*' * 50)
    #     explain(root_node)
