#LAB12
# b) Write a function TreeSize that will count all the nodes of a linked binary tree.

def Treesize(T):
    if T.lc is None and T.rc is None:
        return 1
    lnc = 0
    rnc = 0
    if T.lc is not None:
        lnc = T.lc.Treesize()

    if T.rc is not None:
        rnc = T.rc.Treesize()

    return lnc + rnc + 1

# c) Write a function ClearTree that will traverse a binary tree (in whatever order you find worksbest) and assign zero at all the nodes.

def ClearTree(T):
    nodes = [self]
    i = 0
    n = 1
    self.data = 0
    while i<n:
        p = nodes[i]
        if p.lc is not None:
            p.lc.data = 0
            nodes.append(p.lc)
            n+=1
        if p.rc is not None:
            p.rc.data = 0
            nodes.append(p.rc)
            n+=1
        i+=1


# d) Implement an algorithm to perform a double-order traversal of a binary tree, meaning that each node of the tree, the algorithm first visits the node, then traverses the left subtree (in double order), then visits the node again, then traverses its right subtree (in double order).

def double_order_traversal(node):
    if node is not None:
        print(node.data)
        double_order_traversal(node.lc)
        print(node.data)
        double_order_traversal(node.rc)
