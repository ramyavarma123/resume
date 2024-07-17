def occurrences(sentence, c):
    count = 0
    # Iterate through each character in the sentence
    for char in sentence:
        if char == c:
            count += 1
    return count

# Reading input
sentence = input().strip()  
c= input().strip()        
occurrences = occurrences(sentence, c)

# Print the result
print(occurrences)
