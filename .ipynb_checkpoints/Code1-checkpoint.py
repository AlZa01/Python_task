words = []
word_count = int(input("How many books do you want to read? "))
for i in range(word_count):
    word = (input(f"Enter number {i+1}: "))
    words.append(word)
    print("The books you want to read:")
    for book in words:
        print(f"- {book}")