class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        smallest='ÿ'
        current=letters[0]

        for c in letters:
            if ord(c)> ord(target):
                current=c
                print("here ")
                if ord(current)<ord(smallest):
                    smallest=current
                    
        
        if smallest=='ÿ':
            return letters[0]
        return smallest
        