class Solution:
    def freqAlphabets(self, s: str) -> str:
        converted_text = ""
        
        count = 0
        while count < len(s):
            if s[count] != '#':
                letter = s[count]
                if count <= (len(s) - 3) and s[count + 2] == '#':
                    digits = ""
                    digits += s[count]
                    digits += s[count + 1]
                    if digits == '10':
                        converted_text += 'j'
                    if digits == '11':
                        converted_text += 'k'
                    if digits == '12':
                        converted_text += 'l'
                    if digits == '13':
                        converted_text += 'm'
                    if digits == '14':
                        converted_text += 'n'
                    if digits == '15':
                        converted_text += 'o'
                    if digits == '16':
                        converted_text += 'p'
                    if digits == '17':
                        converted_text += 'q'
                    if digits == '18':
                        converted_text += 'r'
                    if digits == '19':
                        converted_text += 's'
                    if digits == '20':
                        converted_text += 't'
                    if digits == '21':
                        converted_text += 'u'
                    if digits == '22':
                        converted_text += 'v'
                    if digits == '23':
                        converted_text += 'w'
                    if digits == '24':
                        converted_text += 'x'
                    if digits == '25':
                        converted_text += 'y'
                    if digits == '26':
                        converted_text += 'z'

                    count += 2
                else:
                    if letter == '1':
                        converted_text += 'a'
                    if letter == '2':
                        converted_text += 'b'
                    if letter == '3':
                        converted_text += 'c'
                    if letter == '4':
                        converted_text += 'd'
                    if letter == '5':
                        converted_text += 'e'
                    if letter == '6':
                        converted_text += 'f'
                    if letter == '7':
                        converted_text += 'g'
                    if letter == '8':
                        converted_text += 'h'
                    if letter == '9':
                        converted_text += 'i'
    
                    count += 1

            else:
                count += 1
            
        return converted_text