class Node():
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None


class Tree():
    def __init__(self):
        self.root=None
    def add(self,node_value):
        node=Node(node_value)
        if self.root==None:
            self.root=node
            return
        lst=[self.root]
        while True:
            current_node=lst.pop(0)#lst里面是node形式，所以current_node是node形式
            if current_node.left==None:
                current_node.left=node
                return
            else:
                lst.append(current_node.left)
            if current_node.right==None:
                current_node.right=node
                return
            else:
                lst.append(current_node.right)
    def bfs(self):#广度优先
        lst=[self.root]
        while True:
            current_node=lst.pop(0)
            print(current_node.value,end = " ")
            if current_node.left!=None:
                lst.append(current_node.left)
            if current_node.right!=None:
                lst.append(current_node.right)
            if len(lst)==0:
                return
    
    def dfs(self,my_root):#深度优先
        if my_root is None:
            return
        print(my_root.value,end=" ")
        self.dfs(my_root.left)#root.left是node形式
        self.dfs(my_root.right)
tree=Tree()
tree.add(1)
tree.add(2)
tree.add(3)
tree.add(4)
tree.add(5)
tree.add(6)
tree.dfs(tree.root)