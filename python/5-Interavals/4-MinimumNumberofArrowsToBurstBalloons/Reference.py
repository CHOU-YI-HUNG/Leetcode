def findMinArrowShots(points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ans, last = 0,-10**15
        for a, b in sorted(points, key=lambda x: x[1]):
            if a > last:
                ans += 1
                last = b
        return ans
points=[[10,16],[2,8],[1,6],[7,12]]
print(findMinArrowShots(points))    

points=[[1,2],[3,4],[5,6],[7,8]]
print(findMinArrowShots(points))    