"""
A dictionary is an unordered collection of elements.
A dictionary is a mapping between the keys and a set of values, which are mutable.
Each key maps to a value. The association of a key and a value is called a key-value pair (item)
"""
import string

declaration_of_independence = "We hold these truths to be self-evident, that all men are created equal, that they are endowed by their Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness.--That to secure these rights, Governments are instituted among Men, deriving their just powers from the consent of the governed, --That whenever any Form of Government becomes destructive of these ends, it is the Right of the People to alter or to abolish it, and to institute new Government, laying its foundation on such principles and organizing its powers in such form, as to them shall seem most likely to effect their Safety and Happiness. Prudence, indeed, will dictate that Governments long established should not be changed for light and transient causes; and accordingly all experience hath shewn, that mankind are more disposed to suffer, while evils are sufferable, than to right themselves by abolishing the forms to which they are accustomed. But when a long train of abuses and usurpations, pursuing invariably the same Object evinces a design to reduce them under absolute Despotism, it is their right, it is their duty, to throw off such Government, and to provide new Guards for their future security.--Such has been the patient sufferance of these Colonies; and such is now the necessity which constrains them to alter their former Systems of Government. The history of the present King of Great Britain is a history of repeated injuries and usurpations, all having in direct object the establishment of an absolute Tyranny over these States. To prove this, let Facts be submitted to a candid world."

# Remove all the punctuations from the paragraph
print (f"Before punctuactions removal: {declaration_of_independence}")

for punctuation in string.punctuation:
    declaration_of_independence = declaration_of_independence.replace(punctuation, "")

print (f"\nAfter punctuactions removal: {declaration_of_independence}")

# Create a dictionay that holds all words
# book = {} # this is NOT a set
book = dict()
declaration_of_independence = declaration_of_independence.split()
print(f"After the paragraph split: {declaration_of_independence}")

for word in declaration_of_independence:
    print(word)
    # Update the count if the word is already the dictionary

    if word not in book: # ONLY FOR NEW WORD !
        # Add a word to the dictionary book (Option 1)
        # Create an item {word:word_count} to add to the dictionary book
        # An item is {key:value} pair
        entry = {word:1} # Map the count 1 to the key 'word'
        book.update(entry) # Add an item to the dictionary

        # Add a word to the dictionary book (Option 2)
        book[word] = 1 # Map the count 1 tot eh key 'word', Add the item to the dictionay
        # UP: This means book at key (word) has the value 1

    elif word in book:
        book[word] += 1 # Increment the value mapped to the key 'word' 
        
print(f"\n The dictionay of words is: {book}")
print(f"\n The keys in the book dictionary of words: {book.keys()}")
print(f"\n The values in the book dictionary of words: {book.values()}")
print(f"\n The items in the book dictionary of words: {book.items()}")

# Get the word with the maximum count
max_value = max(book, key=book.get)
print(f"The word with the highest frequency is: {max_value}")

# Iterating of the dictionary of books
# When iterating over a dictionay, the iterator is the key

print(f"{'Word'.upper():<16}{'count'.upper():^4}")
for n in book:
    # Row printing option 1
    print(f"{n:<16}{book[n]:^4}")

    # Row printing option 2
    # print(f"{n:<16}{book.get(n):^4}")

# Summary
# There are two ways to WRITE a value in a dictionay
print(f"Way 1: Set the word count of Government to 6")
book['Government'] = 6

print(f"Way 2: Set the word count of Government to 6")
entry = {'Government':6}
book.update(entry)

# There are two ways to READ a value from a dictionary
print(f"Way 1: the count of the word Government is: {book['Government']}")
print(f"Way 2: the count of the word Government is: {book.get('Government')}")

print(f"{'Word'.upper():<16}{'count'.upper():^4}")
for n in book:
    # Row printing option 1
    print(f"{n:<16}{book[n]:^4}")

    # Row printing option 2
    # print(f"{n:<16}{book.get(n):^4}")



# Comprehension of dictionary
odd_numbers = {n:2*n + 1 for n in range(10)}
print(f"{odd_numbers}")

odd_numbers = {n:n for n in range(20) if n%2 == 1}
print(f"{odd_numbers}")