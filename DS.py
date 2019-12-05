

class Stack:
    def __init__(self):
        self.node = []
        self.count = 0
    def sempty(self):
        return self.count == 0
    def push(self,val):
        self.node.append(val)
        self.count += 1
    def pop(self):
        self.count -= 1
        return self.node.pop()

class Queue:
    def __init__(self):
        self.node = []
        self.count = 0
    def qempty(self):
        return self.count == 0    
    def nq(self,val):
        self.node.append(val)
        self.count += 1
    def dq(self):
        self.count -= 1    
        return self.node.pop(0)

class Tree:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

    def inorder(self):
        if(type(self) == None):
            return
        else:
            if(self.left != None):
                self.left.inorder()
            print(self.data)
            if(self.right != None):
                self.right.inorder()
                
   def preorder(self):
        if(type(self) == None):
            return
        else:
            print(self.data)
            
            if(self.left != None):
                self.left.preorder()
            
            if(self.right != None):
                self.right.preorder()
                
    def postorder(self):
        if(type(self) == None):
            return
        else:
            
            
            if(self.left != None):
                self.left.postorder()
            
            if(self.right != None):
                self.right.postorder() 
                
            print(self.data)    
                
            

    def height(self):
        if(self == None):
            return -1
        else:
            l = 0
            r = 0
            if(self.left != None):
                l = self.left.height()
            if(self.right != None):
                r = self.right.height()
            return 1 + max(l,r)    

    def length(self):
            if(self == None):
                return 0
            else:
                l = 0
                r = 0
                if(self.left != None):
                    l = self.left.length()    
                    
                if(self.right != None):
                    r = self.right.length()
                return 1 + l + r             

    def insert(self,val):
        if(self.data == None):
            self.left = None
            self.data = val
            self.right = None
            return            
        else:
            p = Tree()
            q = Tree()
            p = self
            while(p != None):
                k = self.data
                q = p
                if(k > val):
                    p = p.left
                else:
                    p = p.right        

            if(q.data > val):
                q.left = Tree()
                q.left.data = val
                q.left.left = None
                q.left.right = None
            else:
                q.right = Tree()
                q.right.data = val
                q.right.left = None
                q.right.left = None  
        

              



"""
t = Tree()
t.insert(5)
t.insert(15)
t.insert(10)
t.insert(45)
t.insert(65)
t.insert(2)
t.insert(16)
t.insert(655)
t.inorder()
print("Height is ",t.height())      
print("Count is ",t.length())      
"""
