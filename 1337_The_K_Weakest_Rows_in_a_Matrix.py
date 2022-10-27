from typing import List


mat = [[1,1,0,0,0],
        [1,1,1,1,0],
        [1,0,0,0,0],
        [1,1,0,0,0],
        [1,1,1,1,1]]

# class Solution:
#     def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
#         obj = {}
#         for i, l in enumerate(mat):
#             obj[i] = sum(l)
#         return sorted(obj, key=lambda x: obj[x])[:k]

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        obj = {}
        for i in range(len(mat)):
            obj[i] = sum(mat[i])
        return sorted(obj, key=lambda x: obj[x])[:k]
        
        