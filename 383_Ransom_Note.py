# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
#         r_req = {}
#         for l in set(ransomNote):
#             r_req[l] = ransomNote.count(l)

#         m_mats = {}
#         for l in set(magazine):
#             m_mats[l] = magazine.count(l)

#         for key in r_req:
#             if m_mats.get(key):
#                 r_req[key] = r_req[key] - m_mats[key]
#             else:
#                 return False
#         return all(value <=0 for value in r_req.values())
                

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        for l in ransomNote:
            if l not in magazine:
                return False
            magazine = magazine.replace(l,'',1)
        return True
                

ransomNote = 'aa'
magazine = "ab"

sol = Solution()

sol.canConstruct(ransomNote, magazine)