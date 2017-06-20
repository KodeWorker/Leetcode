class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        c1 = word.upper() == word
        c2 = word == word.lower()
        c3 = word[0] == word[0].upper() and word[1:] == word[1:].lower()
        return c1 or c2 or c3