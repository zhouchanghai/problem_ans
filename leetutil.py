#python2 or python3
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def buildList(vals):
    ret = [ListNode(v) for v in vals]
    for i in range(len(ret)-1):
        ret[i].next = ret[i+1]
    return ret

def printList(head):
    s = []
    while head:
        s.append(str(head.val))
        head = head.next
    print(" ".join(s))
    
def buildTree(vals):
    if isinstance(vals, list):
        root = TreeNode(vals[0])
        root.left = buildTree(vals[1])
        root.right = buildTree(vals[2])
        return root
    elif vals != None: #single value
        return TreeNode(vals)

def printTree(root, indent=0):
    tab = "    "
    if root:
        print("{}{}".format(tab*indent, root.val))
        printTree(root.left, indent+1)
        printTree(root.right, indent+1)

if __name__ == "__main__":
    tree = r'''
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
[5,[4, [11, 7, 2], None], [8, 13, [4, 5, 1]]]
'''
    print(tree)
    root = buildTree([5,[4, [11, 7, 2], None], [8, 13, [4, 5, 1]]])
    printTree(root)
    print("*" * 16)

    head = buildList([1,2,3,4,5])[0]
    printList(head)