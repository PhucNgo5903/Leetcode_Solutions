138. Copy List with Random Pointer
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.

Example 1:
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Example 2:
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        
        node_map = {}              #create a dictionary, implemented as a hash table
        """
        my_dict = {'a': 1, 'b': 2, 'c': 3}

        # Accessing values using keys
        print(my_dict['a'])  # Output: 1
        print(my_dict['b'])  # Output: 2
        print(my_dict['c'])  # Output: 3
        """
        current = head
        #First pass: Create a copy of each node and store it in the map
        while current:              
            node_map[current] = Node(current.val)#Đoạn mã gán giá trị cho khóa này bằng cách tạo ra một đối tượng mới kiểu Node 
                                                #với giá trị là current.val. Tức là khóa current(ĐỊA CHỈ của current) nhận giá trị current.val
            current = current.next
        current = head                            #Quay lại về head

        #Second pass: Connect the copied nodes' next and random pointers
        """
        Trong Python, bạn không cần khai báo kiểu dữ liệu của biến trước khi sử dụng nó. 
        Python là một ngôn ngữ lập trình có kiểu dữ liệu động, điều này có nghĩa là kiểu 
        dữ liệu của biến được xác định tự động dựa trên giá trị mà nó đang giữ.
        => giải thích dc cái newNode
        """
        while current:
            copy_node = node_map[current]          #lấy giá trị của phần tử mang khóa "địa chỉ node current" trong map để gán cho copy_node
            copy_node.next = node_map.get(current.next)
            copy_node.random = node_map.get(current.random)
            current = current.next

        return node_map[head]

