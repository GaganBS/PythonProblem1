class SeasarCipher:
    def seasar_decrypt(self, s):
        result = ""
        for i in range(len(self)):
            char = self[i]
            if char.isupper():
                result += chr((ord(char) - s - 65) % 26 + 65)
            elif char.islower():
                result += chr((ord(char) - s - 97) % 26 + 97)
        return result
