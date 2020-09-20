class Node(object):     #it is the must do thing in a graph or tree otr linked list problem
   def __init__(self,x):
      self.value=x;
      self.left=None
      self.right=None
class Solution:
   def isBst(self,node,lower=float('-inf'),upper=float('inf')):#recursive implementation of bst from binary tree checking it's validation.
       if not root:
           return True
       if root.val<=lower or root.val>=upper:
           return False
       return self.isBst(root.left,lower,root.val) or self.isBst(root.right,root.val,upper)
       
