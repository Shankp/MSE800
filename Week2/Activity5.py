class SentenceManipulator:
    def __init__(self, text):
        self.text = text

    def find_word_count(self):
        return len(self.text.split())


if __name__ == "__main__":
    sentence = SentenceManipulator("test hello world")
    
    print(f"Number of word count in the sentence: {sentence.find_word_count()}")  # Output: 1
   