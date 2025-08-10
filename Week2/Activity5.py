class SentenceManipulator:
    def __init__(self, text):
        self.text = text

    def find_word_count(self):
        return len(self.text.split())


def main():
    input_text = input("Enter a sentence: ")
    sentence = SentenceManipulator(input_text)    
    print(f"Number of word count in the sentence: {sentence.find_word_count()}")  

if __name__ == "__main__":
    main()
   
   