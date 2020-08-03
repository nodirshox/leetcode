class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        converted_words = []

        for word in words:
            morse = ""
            for letter in word:
                if letter == "a":
                    morse += ".-"
                elif letter == "b":
                    morse += "-..."
                elif letter == "c":
                    morse += "-.-."
                elif letter == "d":
                    morse += "-.."
                elif letter == "e":
                    morse += "."
                elif letter == "f":
                    morse += "..-."
                elif letter == "g":
                    morse += "--."
                elif letter == "h":
                    morse += "...."
                elif letter == "i":
                    morse += ".."
                elif letter == "j":
                    morse += ".---"
                elif letter == "k":
                    morse += "-.-"
                elif letter == "l":
                    morse += ".-.."
                elif letter == "m":
                    morse += "--"
                elif letter == "n":
                    morse += "-."
                elif letter == "o":
                    morse += "---"
                elif letter == "p":
                    morse += ".--."
                elif letter == "q":
                    morse += "--.-"
                elif letter == "r":
                    morse += ".-."
                elif letter == "s":
                    morse += "..."
                elif letter == "t":
                    morse += "-"
                elif letter == "u":
                    morse += "..-"
                elif letter == "v":
                    morse += "...-"
                elif letter == "w":
                    morse += ".--"
                elif letter == "x":
                    morse += "-..-"
                elif letter == "y":
                    morse += "-.--"
                elif letter == "z":
                    morse += "--.."

            if morse not in converted_words:
                converted_words.append(morse)

        return len(converted_words)