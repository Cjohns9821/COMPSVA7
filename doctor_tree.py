class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class DoctorTree:
    def __init__(self):
        self.root = None

    def insert(self, parent_name, child_name, side):
        """
        Insert a doctor under a parent on the given side ("left" or "right").
        """
        parent_node = self._find(self.root, parent_name)
        if parent_node is None:
            print(f"Error: Parent '{parent_name}' not found.")
            return

        if side not in ("left", "right"):
            print("Error: Side must be 'left' or 'right'.")
            return

        new_node = DoctorNode(child_name)

        if side == "left":
            if parent_node.left is None:
                parent_node.left = new_node
            else:
                print(f"Error: Parent '{parent_name}' already has a left report.")
        else:
            if parent_node.right is None:
                parent_node.right = new_node
            else:
                print(f"Error: Parent '{parent_name}' already has a right report.")

    def _find(self, node, name):
        """Recursive search for a doctor node."""
        if node is None:
            return None
        if node.name == name:
            return node

        left_search = self._find(node.left, name)
        if left_search:
            return left_search

        return self._find(node.right, name)

    def preorder(self, node):
        if node is None:
            return []
        return [node.name] + self.preorder(node.left) + self.preorder(node.right)

    def inorder(self, node):
        if node is None:
            return []
        return self.inorder(node.left) + [node.name] + self.inorder(node.right)

    def postorder(self, node):
        if node is None:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.name]


# Example test
if __name__ == "__main__":
    tree = DoctorTree()
    tree.root = DoctorNode("Dr. Croft")

    tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
    tree.insert("Dr. Croft", "Dr. Phan", "left")
    tree.insert("Dr. Phan", "Dr. Boston", "right")
    tree.insert("Dr. Phan", "Dr. Oswald", "left")

    print("Preorder:", tree.preorder(tree.root))
    print("Inorder:", tree.inorder(tree.root))
    print("Postorder:", tree.postorder(tree.root))


"""
==========================
      DESIGN MEMO
==========================

A tree is ideal for modeling the doctor reporting structure because hospitals often organize staff in hierarchical relationships. 
Each doctor may supervise zero, one, or two direct reports, making a binary tree a natural fit. 
Trees allow recursive traversal, which mirrors real-world reporting flows where information moves from supervisors to subordinates or vice versa.

Preorder traversal is useful when a supervisor needs to communicate instructions down the chain of command, visiting the leader first and then their reports.
Inorder traversal is helpful for structured workflows or alphabetical processing when the left and right branches represent ordered categories. 
Postorder traversal is ideal for collecting reports upward—subordinates are processed first, then the supervisor last.

Heaps are essential for real-time systems like emergency intake because they maintain priority dynamically.
As patients arrive, the heap ensures the most urgent case is always accessible in O(1) time. 
Insertions and removals remain efficient, allowing the system to scale even during high-volume emergencies.
This mirrors real ER behavior, where critical patients must always be treated first regardless of arrival order.
"""
