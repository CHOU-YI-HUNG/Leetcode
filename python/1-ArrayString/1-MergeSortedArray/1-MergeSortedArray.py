
nums1=[1,2,3,0,0,0]
m=len(nums1)
nums2=[2,5,6]
n=len(nums2)

nums1.extend(nums2) 
nums1.sort()
start=0
while nums1[start]<0:
    start=start+1
for i in range(start,start+n):
    nums1.remove(0)
print(nums1)   