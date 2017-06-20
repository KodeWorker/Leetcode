class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str (Input String)
        :type p: str (Regular Expression)
        :rtype: bool
        """
        # '.' Matches any single character.
        # '*' Matches zero or more of the preceding element.
        # The matching should cover the entire input string (not partial).
        
        ### Why "aaa", "ab*ac*a" Expected true?
        ### https://discuss.leetcode.com/topic/13556/why-aaa-ab-ac-a-expected-true
        ### ab*ac*a  means a (b*) a (c*) a
        
        # matching RegEx
        RegEx = self.genRegEx(p)
        
        RE_ind = 0
        S_ind = 0
        while RE_ind < len(RegEx):
            
#            if S_ind == len(s):
#                S_ind = max(S_ind - 1, 0) # incase of s=''
#            print(RE_ind, S_ind, RegEx[RE_ind], s[S_ind])
#            print(RE_ind,S_ind)
            if '*' in RegEx[RE_ind]:
                
                if '.*' == RegEx[RE_ind]: # pass 1~multiple char
                    if S_ind < len(s):                        
                        init_char = s[S_ind]
                        while S_ind < len(s) and s[S_ind] == init_char:
                            S_ind += 1
                    else:
                        RE_ind += 1
                    
                else:
                    if S_ind < len(s) and RegEx[RE_ind][0] == s[S_ind]: # (A*) = A ; A=A case ; pass 0~multiple char if matched
                        S_ind += 1
                    else:
                        RE_ind += 1
                        
            elif S_ind < len(s) and '.' == RegEx[RE_ind]: # C = any case ; pass 1 char
                RE_ind += 1
                S_ind += 1
            
            elif len(s) > 0 and S_ind < len(s) and RegEx[RE_ind] == s[S_ind]: # C = C case ; pass 1 char if matched
                RE_ind += 1
#                S_ind += 1
                s = s[S_ind+1:]
#                print(s)
                S_ind = 0
            
            elif S_ind == len(s) and '*' in RegEx[RE_ind-1]: # .....(C*)C <- case
                S_ind -= 1
#                RE_ind += 1
            else:
                break
            
#        print(RE_ind,S_ind)
        if RE_ind == len(RegEx) and S_ind == len(s):
            return True
        else:
            return False
        
    
    def genRegEx(self, p):
        RegEx = []
        ind = 0
        while ind < len(p):
            if p[ind] != '*':
                RegEx.append(p[ind])
            else:
                RegEx[-1] = p[ind-1] + p[ind]
            ind += 1
        
        return RegEx
            
    

if __name__ == '__main__':
#    s = ''
#    p = '.*'
    
#    s='aab'
#    p='c*a*b'

#    s = 'aa'
#    p = 'a**'

#    s = 'ab'
#    p = '.*c'

#    
#    s = "aaa"
#    p = "ab*a"

#    s = "aaa"
#    p = "ab*ac*a"
    
#    s = 'aaa'
#    p = "ab*a*c*a"

#    s = 'aaa'
#    p = "ab*c*aa*"

#    s = 'a'
#    p= 'ab*a'

    s = "ab"
    p = ".*.."

#    s= 'ab'
#    p ='.*'

#    s= 'abasd'
#    p ='a.*'
    
#    s = "aa"
#    p = ".*"

#    s = 'aa'
#    p = 'a*'

#    s = ''
#    p = 'c*'

#    s = ''
#    p = '.'

#    s = 'aaaa'
#    p = 'aaaaaa'

    sol = Solution()
    o = sol.isMatch(s, p)
    print(o)    