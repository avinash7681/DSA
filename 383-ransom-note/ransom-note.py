class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        m_count = Counter(magazine)
        for char in ransomNote:
            if m_count[char] <= 0:
                return False
            m_count[char] -= 1
        return True
