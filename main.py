import matplotlib
matplotlib.rcParams['text.usetex'] = False
import matplotlib.pyplot as plt

def count_and_list_words():
    
    # Insert here the text file path and the negative_words path so it can read and generate the plot
    text_path = 'C:\\Users\\...\\Pets.txt'
    negative_words_path = 'C:\\Users\\...\\Negative_Words.txt'

    # Open the file
    with open(text_path, 'r', encoding='utf-8') as f:

        # Read in the contents of the file as a string
        text = f.read()

        # Convert the text to lower case
        text = text.lower()

        # Convert the string to a list of words
        words = text.split()

        # If a negative_words_path file is provided, read in the negative_words_path words
        if negative_words_path is not None:
            with open(negative_words_path, 'r', encoding='utf-8') as bf:
                negative_words_path = set(line.strip() for line in bf)
        else:
            negative_words_path = set()

        # Count the number of occurrences of each word, ignoring words in the negative_words_path
        word_counts = {}
        for word in words:
            if word not in negative_words_path:
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1

        # Sort the words by frequency in descending order
        sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

        # Print out the results
        for word, count in sorted_words[:20]:
            print(f"{word}: {count}")

        # Generate a horizontal bar chart of the top 20 words, if requested
        if plt:
            top_words, top_counts = zip(*sorted_words[:20])
            plt.barh(top_words, top_counts)
            plt.xlabel('Count')
            plt.ylabel('Word')
            plt.title('Top 20 Words')
            for i, v in enumerate(top_counts):
                plt.text(v + 1, i, str(v))
            plt.gca().invert_yaxis()
            plt.subplots_adjust(right=0.9)
            plt.show()

# Call the function
count_and_list_words()
