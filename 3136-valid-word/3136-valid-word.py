class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3: return False
        v, c = False, False

        for x in word:
            if not x.isdigit() and not x.isalpha(): return False
            if x.lower() in 'aeiou': v = True
            elif not x.isdigit(): c = True

        return v and c