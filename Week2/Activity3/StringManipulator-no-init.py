class StringManipulator:
    pass


    def find_character(self, word,char):
        return word.find(char)
    
    def find_string_length(self,word):
        return len(word)
    
    def capitalize_string(self,word):
        return word.capitalize()
    
    def Uppercase_string(self,word):
        return word.upper()
    
   
    


if __name__ == "__main__": 
    name  =  StringManipulator()

    print(name.find_character("hello","e"))  # Output: 1
    print(name.find_string_length("hello"))
    print(name.capitalize_string("hello"))  # Output: Hello
    print(name.Uppercase_string("hello"))  # Output: HELLO
