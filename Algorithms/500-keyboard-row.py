class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
        row1 = 'qwertyuiop'
        row2 = 'asdfghjkl'
        row3 = 'zxcvbnm'
        
        out = []
        ind_word = 0
        
        while ind_word < len(words):
            w = words[ind_word].lower()
            
            if w[0] in row1:
                ind_char = 1
                while ind_char < len(w):
                    if w[ind_char] not in row1:
                        break # early exit
                    ind_char += 1
                if ind_char == len(w):
                    out.append(words[ind_word])
            elif w[0] in row2:
                ind_char = 1
                while ind_char < len(w):
                    if w[ind_char] not in row2:
                        break # early exit
                    ind_char += 1
                if ind_char == len(w):
                    out.append(words[ind_word])
            else:
                ind_char = 1
                while ind_char < len(w):
                    if w[ind_char] not in row3:
                        break # early exit
                    ind_char += 1
                if ind_char == len(w):
                    out.append(words[ind_word])
            
            ind_word += 1
        
        return out

if __name__ == '__main__':
    words = ["Hello", "Alaska", "Dad", "Peace"]
    sol = Solution()
    o = sol.findWords(words)
    print(o)