# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
   def longestPalindrome(self, s: str) -> str:
        ret = s[0]
        max_len = 1
        for middle in range(1, len(s)):
            # aba
            min_new_len = max_len + 2 if (max_len % 2) else max_len + 1
            start = middle - int(min_new_len / 2)
            finish = middle + int(min_new_len / 2) + 1
            while start >= 0 and finish <= len(s) \
                and s[start:finish] == s[start:finish][::-1]:
                    ret = s[start:finish]
                    max_len = finish - start
                    start -= 1
                    finish += 1
            # aa
            min_new_len = max_len if not (max_len % 2) else max_len + 1
            start = middle - int(min_new_len / 2)
            finish = middle + int(min_new_len / 2)
            while start >= 0 and finish <= len(s) \
                and s[start:finish] == s[start:finish][::-1]:
                    ret = s[start:finish]
                    max_len = finish - start
                    start -= 1
                    finish += 1           
        return ret            
                      
import time        
s = Solution()
print(s.longestPalindrome("bb"))
print(s.longestPalindrome("babbad"))
print(s.longestPalindrome("babad"))
print(s.longestPalindrome("ccc"))
ts = time.time()
substr = "qbmhukucteihghldwdobtvgwwnhflpceiwhbkmvxavmqxedfndegztlpjptpdowwavemasyrjxxnhldnloyizyxgqlhejsdylvkpdzllrzoywfkcamhljminikvwwvqlerdilrdgzifojjlgeayprejhaequyhcohoeonagsmfrqhfzllobwjhxdxzadwxiglvzwiqyzlnamqqsastxlojpcsleohgtcuzzrvwzqugyimaqtorkafyebrgmrfmczwiexdzcokbqymnzigifbqzvfzjcjuugdmvegnvkgbmdowpacyspszvgdapklrhlhcmwkwwqatfswmxyfnxkepdotnvwndjrcclvewomyniaefhhcqkefkyovqxyswqpnysafnydbiuanqphfhfbfovxuezlovokrsocdqrqfzbqhntjafzfjisexcdlnjbhwrvnyabjbshqsxnaxhvtmqlfgdumtpeqzyuvmbkvmmdtywquydontkugdayjqewcgtyajofmbpdmykqobcxgqivmpzmhhcqiyleqitojrrsknhwepoxawpsxcbtsvagybnghqnlpcxlnshihcjdjxxjjwyplnemojhodksckmqdvnzewhzzuswzctnlyvyttuhlreynuternbqonlsfuchxtsyhqlvifcxerzqepthwqrsftaquzuxwcmjjulvjrkatlfqshpyjsbaqwawgpabkkjrtchqmriykbdsxwnkpaktrvmxjtfhwpzmieuqevlodtroiulzgbocrtiuvpywtcxvajkpfmaqckgrcmofkxynjxgvxqvkmhdbvumdaprijkjxxvpqnxakiavuwnifvyfolwlekptxbnctjijppickuqhguvtoqfgepcufbiysfljgmfepwyaxusvnsratn"
print(s.longestPalindrome(substr))
print(time.time() - ts)
substr = "qgecuralerljmghebsvkdxatotpbiqmxdyetorjhtmcxbgddcqwktfbpnrthsnctdmchbqqhmgtalwslepvrzsylxvlidzryqrvyoisfeqveqxivnslrtvegctcfdgfojjbohgqxxhltgaxqsfcuitjkyopbafjukbgyvkwddgbvznnvejxjlhgktoowpqlluabvhmoqnibhqlpmqgvhjdxthbhmrfrxlmxnhvhxsezehmvtxpdohjbgmnbvvemqhgaxpvytqyjrifubommzoeuqdidnmambohgegyfftsahhpoivetithnfuzppprkpovpymhqardzlohjwrfiyxcnqgdwslavpepmhopcqdabhmqsoqxjswitkwzkoefhfydeartdhreiyzgummxpbtmrxcogmtwjrhdejprotvhzebdvrbedsieznynuaxqcvuegtefvxltovozpqjqocqvnxkesbewmfeacmrmgehyvrfksbbctcmxnbqnlvogjjgzotghxdrpdzyyrdbpvgusyreehfkqxzcgdekjtahubwvcuiktwdczjxacwuqxrtbhjsoqmbqorihykbzcxlyteoourrhheveamoidfxqudkzrpfftcpropwjeymetuibsdatmbvlmjghexejvplaysxbguijitfvrlkgayprkljshhvlonydoxbcuvbwacyeuvzfqqzmanfioyrybcdhkvlizdagpskdcaloglhluokblzgsppcbj"
print(s.longestPalindrome(substr))
print(time.time() - ts)