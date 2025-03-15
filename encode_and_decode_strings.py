from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''
        for string in strs:
            str_len= str(len(string))
            final_str = '#'+str_len+string 
            encoded_str += final_str
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_str = []
        i=0
        while i < len(s):
            if s[i]=='#':
                limit= int(s[i+1])
                decoded_str.append(s[i+2:(i+2)+limit])
                i+=(limit+2)
        return decoded_str

encoded_string = Solution().encode(["","","",""])
print(encoded_string)
print(Solution().decode(encoded_string))
