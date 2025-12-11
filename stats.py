def get_num_words(book_path): #returns a list of words
    with open(book_path, "r") as f:
        words = f.read()
        return len(words.split())



def characters(book_path): # returns all characters from a file
    with open(book_path, "r") as f:
        chars = f.read()
    return chars


def count_string(alphs): #counts chars in lowercase and returns a dict
    low = alphs.lower()
    frequency = {}
    for char in low:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency


#get value of key named "num", used in .sort(key = "num")
def sort_on(items):
    return items["num"]

#sorts a list of dictionaries in descending order based on number
# of times character used and excluding special chars and spaces
def make_dict_list(book_path):
    counted = count_string(characters(book_path)) #dependant on the above functions
    temp_list = []
    for ch in counted: #used to create a list of dictionaries
        temp_dic = {}
        value = counted[ch]
        temp_dic["char"] = ch #get char value
        temp_dic["num"] = value #get num value
        temp_list.append(temp_dic)
    return temp_list
      

      

#used for debugging pay no mind
if __name__ == "__main__":
    
    #print(f"Found {get_num_words(file_path[1])} total words")

    #print(count_string(characters(file_path)))
    
    #sort_dict_list().sort(reverse=True, key=sort_on) #sorts in descending order
    sorted_dict = sorted(make_dict_list(), reverse=True, key=sort_on, )
    for item in sorted_dict: # removes special char and spaces
        if item["char"].isalpha():
            print(item["char"]+":", item["num"])
    