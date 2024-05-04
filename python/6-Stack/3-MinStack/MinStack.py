class MinStack(object):

    def __init__(self):
        self.min_stack = []
        self.stack = [] 

    def push(self, val):
        min_val = val if not self.stack else min(self.min_stack[-1], val)
        self.stack.append(val) 
        self.min_stack.append(min_val)
        

    def pop(self):
        self.min_stack.pop()
        return self.stack.pop()
        

    def top(self):
        return self.stack[-1]
        

    def getMin(self):
        return self.min_stack[-1]



# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
obj.pop()
print(obj.top())
print(obj.getMin())






# class MinStack(object):

#     def __init__(self):
#         self.stack=[]
#         self.Min=[]
        

#     def push(self, val):
#         """
#         :type val: int
#         :rtype: None
#         """
#         self.stack.append(val)
#         if not self.Min or val<=self.Min[-1]:
#             self.Min.append(val)
        

#     def pop(self):
#         """
#         :rtype: None
#         """
#         if self.stack:
#             if self.stack[-1]==self.Min[-1]:
#                 self.Min.pop()
#             self.stack.pop()

#     def top(self):
#         """
#         :rtype: int
#         """
#         return self.stack[-1]
        
#     def getMin(self):
#         """
#         :rtype: int
#         """
#         return self.Min[-1]
        





        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()