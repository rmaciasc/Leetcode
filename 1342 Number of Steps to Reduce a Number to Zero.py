# class Solution:
#     def numberOfSteps(self, num: int) -> int:

#         def steps(num: int) -> int:
#             if num % 2 == 0:
#                 num = int(num / 2)
#             elif num % 2 != 0:
#                 num = num - 1
#             return num

#         counter = 0
#         while num > 0:
#             num = steps(num)
#             counter += 1
#         return counter

class Solution:
    def numberOfSteps(self, num: int) -> int:
        c = 0
        while num > 0:
            c += 1 + (num & 1)
            num = num >> 1
        return c - 1
 
