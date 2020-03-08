from collections import Counter
from mymodule.decrypt import SeasarCipher


class Process:
    def file_content(path):
        with open(path) as secret_messages:
            file_content = secret_messages.readlines()
        file_content[:] = [line.rstrip('\n') for line in file_content]

        return file_content

    def process_secret_message(self):
        result_string = 'SPACE'
        king_symbols = {'SPACE': 'Gorilla',
                        'LAND': 'Panda',
                        'WATER': 'Octopus',
                        'ICE': 'Mammoth',
                        'AIR': 'Owl',
                        'FIRE': 'Dragon'}
        for message in self:
            king_message = message.split(None, 1)
            result = SeasarCipher.seasar_decrypt(king_message[1].replace(' ', ''), len(king_symbols.get(king_message[0])))
            count1 = dict(Counter(king_symbols.get(king_message[0]).upper()))
            count2 = dict(Counter(result.upper()))
            flag = False
            for ele in count1:
                if count2.get(ele) is None:
                    flag = True
                    break
                if count2.get(ele) >= count1[ele]:
                    pass
                else:
                    flag = True
                    break
            if not flag:
                result_string = result_string + ' ' + king_message[0]
        return result_string
