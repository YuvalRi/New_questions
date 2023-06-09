# Task 1- Version 2

def frequency_dict_2(st: str):
    '''
    Creating a frequency dictionary from a given string
    '''
    dict = {}
    for char in st:
        dict[char] = dict.get(char, 0) + 1
    return(dict)
        
if __name__ == "__main__":
    print(frequency_dict_2("aadbc"))
    print(frequency_dict_2("dbdb"))
    print(frequency_dict_2("dddd"))
    print(frequency_dict_2(""))
    print(frequency_dict_2("powflsdnslsl"))

