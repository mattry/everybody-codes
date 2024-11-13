def count_runic_words(filename: str):
    WORDS = {"LOR", "LL" , "SI", "OR", "PA", "AG", "IS"}
    total_count = 0
    with open(filename) as f:
        input = f.readline().split(" ")
        # Loop through each word in the input
        for word in input:
            word_count = 0  # Reset count for each word

            # Check for occurrences of each substring in WORDS with overlaps
            for runic_word in WORDS:
                start = 0
                while start < len(word):
                    pos = word.find(runic_word, start)
                    if pos != -1:
                        word_count += 1
                        start = pos + 1  # Move start to the next character for overlap
                    else:
                        break

            # Update total count and print word with count if any runic word was found
            total_count += word_count
    
    return total_count


if __name__ == "__main__":
    input_path = "part1.txt"
    print("Result: ")
    print(count_runic_words(input_path))
