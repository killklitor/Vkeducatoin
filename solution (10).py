input_string=input()
words=input_string.split()
word_count={}
for word in words:
    cleaned_word=word.strip('!.,?;:#$%^&*()').lower()
    if len(cleaned_word) >= 5 and len(set(cleaned_word)) >= 4:
        if cleaned_word in word_count:
            word_count[cleaned_word] += 1
        else:
            word_count[cleaned_word] = 1
filtered_words = {word: count for word, count in word_count.items() if count > 2}
sorted_words = sorted(filtered_words.keys())
for word in sorted_words:
    print(word)