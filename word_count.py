def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) +
              " words.")
        
filenames = ['alice.txt', 'siddahartha.txt', 'moby_dick.txt', 'the_great_gatsby.txt']
for filename in filenames:
    count_words(filename)