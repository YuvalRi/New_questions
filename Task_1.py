# Task 1

def frequency_dict(st: str):
    '''
    Creating a frequency dictionary from a given string
    '''
    dict = {}
    values = [] 
    for char in set(st):
           values.append(st.count(char))
    keys = [*set(st)]
    dict = { key : value 
                for key, value in zip(keys, values) }    
    return(dict)
        
if __name__ == "__main__":
    print(frequency_dict("aadbc"))
