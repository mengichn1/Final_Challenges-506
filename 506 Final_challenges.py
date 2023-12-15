Project 506 Solutions

Question 1: Palindrome Checker

# defining palindrome
def is_palindrome(input_str):
    # initializing a stack data structure using a list
    stack = []
    
    # pre-processing function on an inputstr
    def preprocess_string(input_str):
        # converting the string to lowercase
        input_str = input_str.lower()
        # remove spaces and punctuation
        input_str = ''.join(char for char in input_str if char.isalpha())
        return input_str
        
    # pre-processing inputstr
    input_str = preprocess_string(input_str)

    # push characters to stack
    for char in input_str:
        stack.append(char)

    # popping characters and comparing with the original string
    for char in input_str:
        if char != stack.pop():
            return False

    # string is a palindrome if the loop completes
    return True

# Test cases, True of False
print(is_palindrome("noah"))  # Checking my name
print(is_palindrome("racecar"))  
print(is_palindrome("hello"))  
print(is_palindrome("level"))  
print(is_palindrome("A man, a plan, a canal, Panama"))
print(is_palindrome("Was it a car or a cat I saw?"))


Question 2: Implementing a Queue using Stacks

# defining and implementing a queue 
class QueueWithStacks:
    def __init__(self):
        #initializing lists to represent the stacks for enqueue() and dequeue() operations
        self.stack_1 = []  # for enqueue operation
        self.stack_2 = []  # for dequeue operation
        
    # for enqueueing/appending elements onto stack_1
    def enqueue(self, element):
        self.stack_1.append(element)
    
    # for dequeueing/removing elements from stack_1 to to stack_2
    def dequeue(self):
        if not self.stack_2:  # if stack_2 is empty, transfer elements from stack_1 to stack_2
            while self.stack_1:
                self.stack_2.append(self.stack_1.pop())

        # if stack_2 is still empty, the queue is empty
        if not self.stack_2:
            return None

        # pop and return the front element from stack_2
        return self.stack_2.pop()

# implementing test cases
queue = QueueWithStacks()

# enqueue 3 elements: 5, 10, 15
queue.enqueue(5)
queue.enqueue(10)
queue.enqueue(15)

# run dequeue() operations, with expected output: 5
print(queue.dequeue())

# run dequeue(), with expected output: 10
print(queue.dequeue())

# enqueue elements: 20, 25, 30, 35
queue.enqueue(20)
queue.enqueue(25)
queue.enqueue(30)
queue.enqueue(35)

# perform dequeue() twice, expected output: 20, 25
print(queue.dequeue())
print(queue.dequeue())

# enqueue elements: 'a', 'b', 'c', 'd', 'e'
queue.enqueue('a')
queue.enqueue('b')
queue.enqueue('c')
queue.enqueue('d')
queue.enqueue('e')

# perform dequeue() thrice, expected output: 'a', 'b', 'c'
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())



Question 3: Word Frequency Counter

# using dictionary to count the frequency of words
def word_frequency_counter(text):
    # using curly bracketsto initialize empty dictionary for storing word frequencies
    word_frequency = {}

    # splitting the text into words
    words = text.split()

    # iterating through each word in the list, remove punctuations and convert to lower case
    for word in words:
        refined_word = word.strip(".,!?").lower()

        # update dictionary by incrementing the count for each word
        word_frequency[refined_word] = word_frequency.get(refined_word, 0) + 1

    return word_frequency

# test case
text = "Python is a powerful programming language. Python is used in various domains."
result = word_frequency_counter(text)
print(result)


Question 4: Balanced Parentheses Checker

# a function checking if a string of parentheses is balanced using a stack
def is_balanced_parentheses(input_str):
    #initialize an empty stack of strings
    stack = []

    for char in input_str:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:  # if the stack is empty, with no matching opening parenthesis
                return False
            stack.pop()

    # if the stack is empty, all opening parentheses have a matching closing parenthesis
    return not stack

# examples, output True or False
str_1 = "()((()))"
str_2 = "(()())("
print(is_balanced_parentheses(str_1))  
print(is_balanced_parentheses(str_2))

# test cases, output True or False
print(is_balanced_parentheses("((()))()"))  
print(is_balanced_parentheses("((())"))   
print(is_balanced_parentheses("()()()()"))


Question 5:Implement operations in a BST

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        # Initialize an empty BST
        self.root = None

    def insert(self, value):
        # to insert a value to the BST
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, root, value):
        # to recursively insert a value to the tree
        if root is None: ##can as well say "if not root:"
            return TreeNode(value)

        if value < root.value:
            root.left = self._insert_recursive(root.left, value)
        elif value > root.value:
            root.right = self._insert_recursive(root.right, value)

        return root

    def search(self, value):
        # searching a value in the BST
        return self._search_recursive(self.root, value)

    def _search_recursive(self, root, value):
        # to recursively search if a value is in the tree
        if root is None:  #can as well say "if not root:"
            return False

        if value == root.value:
            return True
        elif value < root.value:
            return self._search_recursive(root.left, value)
        else:
            return self._search_recursive(root.right, value)

    def delete(self, value):
        # deleting a node with a given value from the tree
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, root, value):
        # to recursively remove a node with a given value
        if root is None: 
            return None

        if value < root.value:
            root.left = self._delete_recursive(root.left, value)
        elif value > root.value:
            root.right = self._delete_recursive(root.right, value)
        else: #when a node has only one child or no child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            #node with two children
            root.value = self._find_min_value(root.right)
            root.right = self._delete_recursive(root.right, root.value)

        return root

    def _find_min_value(self, root):
        # to find the minimum value in a subtree
        while root.left:
            root = root.left
        return root.value


# Examples and inserting valuues into a BST
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)
bst.insert(12)
bst.insert(18)

#output
print(bst.search(7))  # True
print(bst.search(11))  # False

#output
bst.delete(15)
print(bst.search(15))  # False


Question 6: Graph Traversal - BFS and DFS

from collections import defaultdict

class Graph:
    def __init__(self):
        # Using a defaultdict to store the graph as an adjacency list
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        # Add an edge to the graph
        self.graph[u].append(v)

def dfs(graph, start, visited):
    # Mark the current node as visited and print it
    visited[start] = True
    print(start, end=' ')

    # Recur for all the adjacent vertices
    for neighbor in graph[start]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

def bfs(graph, startV):
    # Mark the source node as visited and enqueue it
    visited = [False] * (max(graph) + 1)
    queue = []

    queue.append(startV)
    visited[startV] = True

    while queue:
        # Dequeue a vertex from the queue and print it
        current = queue.pop(0)
        print(current, end=' ')

        # Get all adjacent vertices of the dequeued vertex
        # If an adjacent vertex has not been visited, mark it as visited and enqueue it
        for neighbor in graph[current]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True

# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

start_vertex = 1

print(f"Depth-First Search starting from vertex {start_vertex}:")
visited_dfs = [False] * (max(g.graph) + 1)
dfs(g.graph, start_vertex, visited_dfs)

print(f"\nBreadth-First Search starting from vertex {start_vertex}:")
bfs(g.graph, start_vertex)


Question 7:Finding Duplicates in a List or Array

def find_duplicates(input_list):
    # initialize an empty set to store elements 
    # initialize an empty set to store duplicate elements
    seen = set()
    duplicates = set()

    # iterate through the input list
    for element in input_list:
        # check if the element is already in the set of seen elements
        if element in seen:
            # if the element is in the set, add it to the duplicates set
            duplicates.add(element)
        else:
            # if the element is not in the set, add it to the set of seen elements
            seen.add(element)

    # return the set containing duplicate elements
    return duplicates

# Examples
arr_1 = [1, 2, 3, 4, 4, 2, 5, 6, 3]
arr_2 = ['a', 'b', 'c', 'b', 'd', 'e', 'a']

# finding duplicates for the example arrays
result_1 = find_duplicates(arr_1)
result_2 = find_duplicates(arr_2)

# print output
print(result_1)  # {2, 3, 4}
print(result_2)  # {'b', 'a'}

# Test cases
test_case_1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
test_case_2 = ['x', 'y', 'z', 'x', 'y', 'x', 'z']
test_case_3 = [1, 2, 3, 4, 5]

# expected output for the test cases
print(find_duplicates(test_case_1))  # output: {1, 2, 3, 4, 5}
print(find_duplicates(test_case_2))  # output: {'x', 'y', 'z'}
print(find_duplicates(test_case_3))  # outputt: set()


Question 8: Reverse a Linked List

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse_linked_list(head):
    # initialize reversed linked-list pointers
    prev = None       # pointing previous node 
    current = head    # pointing to the current node in the original list

    while current:
        next_node = current.next  # Save the next node before reversing the link
        current.next = prev        # reverse the link by pointing the current node to the previous node

        # moving the pointers one step forward in the list
        prev = current
        current = next_node

    return prev  # return the new head of the reversed list

# creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
head1 = Node(1)
head1.next = Node(2)
head1.next.next = Node(3)
head1.next.next.next = Node(4)
head1.next.next.next.next = Node(5)

# Reverse the linked list
reversed_head1 = reverse_linked_list(head1)

# Print the reversed linked list: 5 -> 4 -> 3 -> 2 -> 1
while reversed_head1:
    print(reversed_head1.value, end=" -> ")
    reversed_head1 = reversed_head1.next
print("None")

# Test cases with various scenarios: 2 -> 4 -> 6 -> 8 -> 10
head2 = Node(2)
head2.next = Node(4)
head2.next.next = Node(6)
head2.next.next.next = Node(8)
head2.next.next.next.next = Node(10)

# Reverse the linked list
reversed_head2 = reverse_linked_list(head2)

# Print the reversed linked list: 10 -> 8 -> 6 -> 4 -> 2
while reversed_head2:
    print(reversed_head2.value, end=" -> ")
    reversed_head2 = reversed_head2.next
print("None")

