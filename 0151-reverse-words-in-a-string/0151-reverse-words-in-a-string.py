class Solution:
    def reverseWords(self, s: str) -> str:
            left =  0
            right = 0

            myNewWord = "" 

            while left < len(s):
                # skip non alpha and  white spaces 
                
                while left < len(s) and not s[left].isalnum():
                    left += 1

                # No more words
                if left >= len(s):
                    break

                right = left 

                while right < len(s) and s[right].isalnum():
                    right += 1


                word = s[left:right]

                if myNewWord:
                    myNewWord = word + " " + myNewWord
                else:
                    myNewWord = word

                left = right 
            return myNewWord