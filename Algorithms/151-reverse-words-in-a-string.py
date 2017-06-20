# incomplete description
# one or multiple spaces at the end of string will be ignored!!!

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        wl = s.split(" ")
        ind = 0
        while ind < len(wl):
            if wl[ind] == "":
                wl = wl[:ind] + wl[ind+1:]
            else:
                ind+= 1
        string = " ".join(wl[::-1])
        return string

if __name__ == '__main__':
    s = "the sky is blue  "
#    s = " "
    string = Solution().reverseWords(s)
#    print(string)
    print(len(string))