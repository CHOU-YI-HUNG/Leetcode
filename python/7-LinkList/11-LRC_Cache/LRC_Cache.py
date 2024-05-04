class ListNode(object):
    def __init__(self,key=0,val=0,pre=None,next=None):        
        self.key=key
        self.val=val
        self.pre=pre
        self.next=next
        
class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity=capacity
        self.oldest=None
        self.newest=None
        self.cacheSize=0                
        self.cache={}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            self.updateNode(key)
            return self.cache[key].val
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """ 
        if self.cacheSize==0:              # empty
          self.empty(key,value)
        elif self.cacheSize<self.capacity: #non-full        
            #還需要考慮，key有沒有在裡面
            if key not in self.cache:                       
                self.increseNode(key,value)
            else:
                #還需要考慮pre是空的或next是空的
                #存在的key是不是最老的
                self.cache[key].val=value
                self.updateNode(key)
        else:                              # full
            if key not in self.cache:
                # Delete
                self.cache.pop(self.oldest.key)                                                
                if self.oldest.next!=None:                     
                    self.oldest=self.oldest.next                                        
                    
                del self.oldest.pre
                self.oldest.pre=None
                
                
                self.cacheSize-=1
                if self.cacheSize==0:
                    self.empty(key,value)
                else:    
                    self.increseNode(key,value)                            
            else:
                #key存在
                self.cache[key].val=value
                self.updateNode(key)
                    

    def empty(self,key,value):
        self.oldest=self.newest=ListNode(key,value)
        self.cache[key]=self.newest
        self.cacheSize+=1
    def increseNode(self,key,value):
        self.newest.next=ListNode(key,value,self.newest)
        self.newest=self.newest.next
        self.cache[key]=self.newest
        self.cacheSize+=1
    def updateNode(self,key): ##有問題 等等檢查                    
        if self.cache[key]==self.oldest: # at the front
            if self.cache[key].next==None: return None
                        
            self.oldest=self.oldest.next
            self.oldest.pre=None
            #self.oldest.next=(self.cache[key].next.next)
            
            
            self.cache[key].next=None
            self.cache[key].pre=self.newest
            self.newest.next=self.cache[key]
            self.newest=self.cache[key]            
            
        elif self.cache[key]==self.newest: #at the last  
            pass
        else: #at the middle 
            (self.cache[key]).pre.next=(self.cache[key]).next #2            
            if (self.cache[key]).next!=None: (self.cache[key]).next.pre=(self.cache[key]).pre            
            self.cache[key].next=None
            self.cache[key].pre=self.newest
            self.newest.next=self.cache[key]
            self.newest=self.cache[key]
            
            
# Your LRUCache object will be instantiated and called as such:
# InputList=[[10],
# [10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],
# [8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],
# [4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],
# [2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],
# [12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],
# [8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
# print(len(InputList)-1)
InputList=[[1],[6],[8],[12,1],[2],[15,11],[5,2],[1,15],[4,2],[5],[15,15]]

obj = LRUCache(InputList[0][0])
for i in range(1,len(InputList)):
    if i==5:
        pass
    if len(InputList[i])==1:
        print(obj.get(InputList[i][0]))
    else:        
        obj.put(InputList[i][0],InputList[i][1])



# obj = LRUCache(2)
# obj.put(2,1)
# obj.put(3,2)
# print(obj.get(3))
# print(obj.get(2))
# obj.put(4,3)
# print(obj.get(2))
# print(obj.get(3))
# print(obj.get(4))


# obj = LRUCache(2)
# obj.put(2,1)
# obj.put(2,2)
# print(obj.get(2))
# obj.put(1,1)
# obj.put(4,1)
# print(obj.get(2))

# obj = LRUCache(1)
# obj.put(2,1)
# print(obj.get(2))


# obj = LRUCache(2)
# obj.put(1,1)
# obj.put(2,2)
# print(obj.get(1))
# obj.put(3,3)
# print(obj.get(2))
# obj.put(4,4)
# print(obj.get(1))
# print(obj.get(3))
# print(obj.get(4))



