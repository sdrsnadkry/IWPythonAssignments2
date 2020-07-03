def anagram_check(paragraph):
    lowerParagraph = paragraph.lower()
    words = lowerParagraph.split(" ")

    anagrams = []

    for word1 in words:
        for word2 in words:
            if word1 != word2 and (sorted(word1) == sorted(word2)):
                anagrams.append(word1)

    return anagrams


paragraph = " My Cat brags because he grabs a mouse and act as nothing happened  "
print(anagram_check(paragraph))


# anagram_list = []
# for word_1 in word_list:
#     for word_2 in word_list:
#         if word_1 != word_2 and (sorted(word_1)==sorted(word_2)):
#             anagram_list.append(word_1)
# print(anagram_list)
