class Solution:
    def flowerpot(self, flowerbed, n):
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                leftempty = (i==0) or (flowerbed[i-1] == 0)
                rightempty = (i == len(flowerbed)-1) or (flowerbed[i+1] == 0)

                if leftempty and rightempty:
                    flowerbed[i] = 1
                    count +=1
        return count >=n


#another 
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 0:
                if i == 0 or flowerbed[i - 1] == 0:
                    if i == len(flowerbed) - 1 or flowerbed[i + 1] == 0:
                        flowerbed[i] = 1
                        count += 1
                        if count >= n:
                            return True
                        i += 1  # Jump two positions ahead
            i += 1
        return count >= n

#another
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        i = 0

        while i < len(flowerbed):
            if flowerbed[i] == 0:
                if i == 0 or flowerbed[i - 1] == 0:
                    if i == len(flowerbed) - 1 or flowerbed[i + 1] == 0:
                        flowerbed[i] = 1
                        count += 1
            i += 1

        return count >= n







solution = Solution()
print(solution.flowerpot(flowerbed = [1,0,1,0,1,0,1], n = 1))