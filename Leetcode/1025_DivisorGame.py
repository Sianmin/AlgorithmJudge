class Solution:
    def divisorGame(self, N: int) -> bool:
        arr = {1:False, 2:True, 3:False}
        
        for i in range(4, N+1):
            max_n = floor(sqrt(i))
            arr[i] = False
            for j in range(1, max_n):
                if i%j == 0:
                    if not arr[i-j]:
                        arr[i] = True
                        break
        return arr[N]