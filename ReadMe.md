# Practice Exercises

## Basics
Tips:
- Remmember print functions arguments: ```end```, ```sep```.
- Use 'f-strings' They make printing easier.
### Task 1
1. Write a function That receives no arguments and prints the follwing:

    ```
    X
    X X
    X X X
    X X X X
    X X X X X
    ```
2. Write a function That receives no arguments and prints the follwing:

    ```
    X X X X X X X
      X X X X X
        X X X
          X
    ```
3. Write a function That receives no arguments and prints the follwing:

    ```
    X
    X X
    X X X
    X X X X
    X X X X X
    X X X X
    X X X
    X X
    X
    ```
4. Write a function That receives an integer n > 0 and prints the following patterns for all valid. for n <= 0, print "Value Error".

    for n = 3
    ```
    1
    1 2
    1 2 3
    ```
    for n = 5
    ```
    1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5
    ```
    and so on...

5. Write a function That receives an integer n > 0 and prints the following patterns for all valid. for n <= 0, print "Value Error".

    for n = 2
    ```
    1
    2 4
    ```
    for n = 4
    ```
    1
    2 4
    1 3 5
    2 4 6 8
    ```
    for n = 7
    ```
    1
    2 4
    1 3 5
    2 4 6 8
    1 3 5 7 9
    2 4 6 8 10 12
    1 3 5 7 9  11 13
    ```
    and so on...
    - Hint: Trying spliting this task into smaller functions
    - Hint: Create two more function; one will help you print odd rows, the other one will help you print even rows


## Dictionaries
### Task 1
Write a function that receives a string and returns a frequency dictionary (Histogram).
- Given a group of elements, a frequency dictionary is defined as a dictionary that each of it's keys defines an element in the group, (The elements can be anything as long as they are hasable - Google hash function for more information) and the respected values represent the number of accurences the element has in the given group.
- The string can include any type of characters
- Upper case letters are not treated the same as lower case letters
- Use the following function signiture:
    
    ```python
    def frequency_dict(st: str) -> dict:
    ```
* Example:
    ```
    >>> frequency_dict("aabaccd9")
    {"a": 3, "b": 1, "c": 2, "d": 1, 9: 1}
    ``` 
## Recursion

1. Write a function that receives a list of numbers (numbers can be either positive/negative) and returns ```True``` if the numbers can be devided into two foreign groups which their sum is equal to one another. The function will return ```False``` otherwise.
- Hint: Use a signiture as follows inorder to keep track of the sums:
```python
    def split_group(lst: list, s1: int=0, s2: int=0) -> bool:
        pass
```
- Function Should be called without the s1, s2 arguments on the first time (This means that on the first call the arguments will not appear, thus they will receive the value 0. But it is more than recommanded to use them in the recursive calls)
- Examples
    
```
>>> split_group([1, 4, 7, 4])
True
```

## Object Oriented 

Lets define a BinaryNode and a BinaryTree classes:

```python
    class BinaryNode:
        
        def __init__(self, val, lc: "Node"=None, rc:"Node"=None):
            self.val = val
            self.lc = lc
            self.rc = rc

    class BinaryTree:

        def __init__(self, root: Node):
            self.root = node

        def print_pre_order(self):
            """
            The function prints the tree nodes in a pre order fasion as follows:
            x1, x2, x3, x4....
            """
            pass

        def print_post_order(self):
            """
            The function prints the tree nodes in a post order fasion as follows:
            x1, x2, x3, x4....
            """
            pass

        def print_in_order(self):
            """
            The function prints the tree nodes in a in order fasion as follows:
            x1, x2, x3, x4....
            """
            pass
```

1. Define a new Node using the BinaryNode class and create a new Binary tree using the BinaryTree Class
2. The following function will help you create a sample Binary Tree:

```python
    def create_smaple_tree(root: BinaryNode) -> BinaryTree:
        """
        This function receives a BinaryNode and inserts a sample tree to it.
        """
        root.lc = BinaryNode(10, BinaryNode(6), BinaryNode(45))
        root.rc = BinaryNode(7, BinaryNode(3), BinaryNode(2))
        return root    
```

- Implement the print functions (3 in total) in the above 'BinaryTree' class. The implementation should be **recursive!**
- Use the given function to create a sample trre with the node you created in (1)
- print the tree 3 times, each time with a different function.

3. **(Hard)** We now want to improve the way we insert nodes into our tree, Therfore we will implement the following method in the Binary tree class:

```python
    def insert(self, val) -> None:
        """
        The function will insert the given value as a node to the tree.
        """
        pass
```
In order to figure out where to insert a new node to the tree, We will learn about AVL trees.
- Please read about AVL trees.
- Implement the insert function so that the tree will remain balanced after each insert. Use the internet!
- Write a function that returns True if the tree is balanced and false otherwise, Use the following signiture:
```python
    def is_balanced(self) -> bool:
        pass
```

4. Inset Method #2:

-   Write another insert function that inserts elements to the tree according to a SortedBinaryTree methodology. Use this signiture:
```python
    def insert_sorted(self, val) -> None:
        pass
```
- Write a function to check if a binary tree is sorted. The function will return True of the tree is sorted and false otherwise. Use the follwing:
```python
    def is_sorted(self) -> bool
        pass
```

5. Write a function in BinaryTree class that calculates the depth of the tree recursively:

```python
    def depth(self) -> int:
        """ The function will return the depth of the tree. """
        pass
```

6. Write a function in the Binary tree class named ```count_leaves``` that returns the number of leaves in the tree. If the tree is null, 0 will be returned. (define the function signiture yourself)

## Merge Sort
Let's implement merge sort with Linked List. I have provided you with an unimplemented template (API) of A LinkedList and Node classes. In this exercise we will implement the API of linked list to eventually be able to write the method for the merge sort algorithm.

1. Implement the Constructor of the Node class, remmember that the ```Node``` class has two fields: val and next.

2. Implement one by one, the function signitures provided in the ```LinkedList``` class.

3. Test yourself with the provided pytest module.

The template:

 ```python
    class Node:

        def __init__(self, val, next: "Node"=None):
            """ Initialize a new node """
            pass

    class LinkedList:
        
        def __init__(self, head: "Node"=None):
            self.head = head

        def insert(self, val) -> None:
            """ 
            The function will insert a new node, with the value val at the end of the list.
            """
            pass

        def push(self, val) -> None:
            """
            The function will add a new node, with the value val at the beggining of the list.
            """
            pass

        def peek(self, i: int):
            """
            The function will return the value of the node in index i. If a node of index i does not exist, a KeyError will be raised.
            """
            pass

        def pop(self, i: int):
            """
            The function will pop a node at index i from the list. When popping an element from the list, the node will be removed from the list and the value will be returned. The list will raise a KeyError if a node of index i does not exist.
            """
            pass

        def swap(self, i: int, j: int):
            """
            The function will swap the Nodes (Not just the values) of index i with j. if one of the indexes does not exist, raise a KeyError.
            """

        def is_empty(self):
            """
            The function will return True of the current list is empty and false otherwise. An empty list is a list with no nodes at all.
            """
            pass

        def merge_sort(self) -> None:
            """ Merge sort the list """
            pass

        def show(self) -> None:
            """ Print the list in a readable manner """
            pass
```