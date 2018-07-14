import re

file_name = input("Please enter file name --> ")
with open(file_name + ".txt", 'r', encoding="utf8") as infile:
  para = infile.read()
  para_list = re.split("(?<=[!.?]) +",para)
  word_list = para.split(" ")
  num_sentences = len(para_list)
  word_count = len(word_list)
  replaced = re.sub("\s+", "", para)
  letr_count = len(replaced)

  print("Paragraph Analysis")
  print("--------------------")
  print("Approximate Word Count: {}".format(word_count))
  print("Approximate Sentence Count: {}".format(num_sentences))
  print("Average Letter Count: {}".format(letr_count/word_count))
  print("Average Sentence Length: {}".format(word_count/num_sentences))


