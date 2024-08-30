import os
import heapq

class HuffmanCoding():
    def __init__(self, path: str) -> None:
        self.path: str = path
        self.heap: list = []

    def make_frequency_dict(self, text) -> dict:
        # calc freq and return
        ...

    def make_heap(self, frequency:dict):
        # make priority queue
        ...

    def merge_codes(self):
        # Build Huffman Tree, Save root node in heap
        ...

    def make_codes(self):
        # make codes for characters and save
        ...

    def get_encoded_text(self, text):
        # replace characters with code and return
        ...

    def pad_encoded_text(self, encoded_text):
        # pad Encoded Text and return
        ...

    def get_byte_array(self, padded_encoded_text):
        

    def compress(self):
        filename, file_extension = os.path.splitext(self.path)
        output_path: str = filename + '.bin'

        with open(self.path, "r") as file, open(output_path, "wb") as output:
            text: str = file.read()
            text = text.rsplit()
            
            frequency: dict = self.make_frequency_dict(text)

            self.make_heap(frequency)
            self.merge_codes()
            self.make_codes()

            encoded_text = self.get_encoded_text(text)
            padded_encoded_text = self.pad_encoded_text(encoded_text)









if __name__ == "__main__":
    ...