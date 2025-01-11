from collections import Counter

def count_word_frequencies(file_path):
    # Read the content of the file
    with open(file_path, 'r') as file:
        text = file.read()

    # Clean and split the text into words
    words = text.lower().split()
    words = [word.strip(".,!?;:\"'()[]{}") for word in words]

    # Count the frequency of each word
    word_counts = Counter(words)

    # Convert to a dictionary
    word_frequencies = dict(word_counts)

    return word_frequencies

def get_top_words(word_frequencies, top_n=10):
    # Sort the dictionary by frequency in descending order and get the top N words
    sorted_words = sorted(word_frequencies.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:top_n]

# Example Usage
if __name__ == "__main__":
    # Specify the text file to analyze
    file_path = "text.txt"

    # Count word frequencies
    word_frequencies = count_word_frequencies(file_path)

    # Find the top 10 most frequent words
    top_words = get_top_words(word_frequencies)

    # Print the results
    print("Word Frequencies:")
    for word, count in word_frequencies.items():
        print(f"{word}: {count}")

    print("\nTop 10 Most Frequent Words:")
    for word, count in top_words:
        print(f"{word}: {count}")
