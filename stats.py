def word_count(file_path):
        count = file_path.split()
        return len(count)
def count_characters(text):
    characters = {}
    for character in text:
        lowerc = character.lower()
        if lowerc in characters:
            characters[lowerc] += 1
        else: 
            characters[lowerc] = 1
    return characters

def list_of_dicts(text):
    characters = {}
    for character in text:
        lowerc = character.lower()
        if lowerc in characters:
            characters[lowerc] += 1
        else: 
            characters[lowerc] = 1
    char_list = []
    for char, count in characters.items():
        if char.isalpha():
            char_list.append({"char": char, "count": count})  
    def sort_on(dict): 
        return dict["count"]
    char_list.sort(reverse = True, key = sort_on)
    return char_list 

    
    

                    
