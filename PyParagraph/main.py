import re

para = "Adam Wayne, the conqueror, with his face flung back and his mane like a lion's, stood with his great sword point upwards, the red raiment of his office flapping around him like the red wings of an archangel. And the King saw, he knew not how, something new and overwhelming. The great green trees and the great red robes swung together in the wind. The preposterous masquerade, born of his own mockery, towered over him and embraced the world. This was the normal, this was sanity, this was nature, and he himself, with his rationality, and his detachment and his black frock-coat, he was the exception and the accident - a blot of black upon a world of crimson and gold."

para_list = re.split("(?<=[!.?]) +",para)
word_list = re.split("\W", para.strip()) # para.split("\W")
# print(para)
num_sentences = len(para_list)
word_count = len(word_list)
replaced = re.sub("\W", "", para)
letr_count = len(para) - len(replaced)

#print(f"{letr_count} {word_list[0]} {word_list[120]}")
print (word_list)

# print("len 1 {} len 2 {}".format(len(replaced), len(para)))
# print(replaced)

print("Paragraph Analysis")
print("--------------------")
print("Approximate Word Count: {}".format(word_count))
print("Approximate Sentence Count: {}".format(num_sentences))
print("Average Letter Count: {}".format(letr_count/word_count))
print("Average Sentence Length: {}".format(word_count/num_sentences))
# for i in para_list:
#    print(i)
