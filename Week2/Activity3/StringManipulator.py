class StringManipulator:
    def  __init__(self, text):  
        self.text = text

    def find_character(self,char):
        return self.text.find(char)
    
    def find_string_length(self):
        return len(self.text)
    
    def capitalize_string(self):
        return self.text.capitalize()
    
    def Uppercase_string(self):
        return self.text.upper()
    


if __name__ == "__main__": 
    name  =  StringManipulator("hello")

    print(name.find_character("e"))  # Output: 1
    print(name.find_string_length())
    print(name.capitalize_string())  # Output: Hello
    print(name.Uppercase_string())  # Output: HELLO
