class Solution:
    def toLowerCase(self, str: str) -> str:
        text = str
        converted = ""
        
        for letter in text:
            lowered = letter.lower()
            converted += lowered

        return converted
