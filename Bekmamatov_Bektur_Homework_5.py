import re


file_path = "mock_data.txt"
result_file_path = "@mail.txt"
file_reader = open(file_path, mode='r', encoding='Latin-1')
mail = open(result_file_path, mode="w", encoding="Latin-1")
my_text_1 = file_reader.read()

searching_mail = r'[\w+_-]+@[\w+_-]+.[\w]+'
results_all_mail = re.findall(searching_mail, my_text_1) 

for i in results_all_mail:
    print(i)
    mail.write(i + "\n")




file_path = "mock_data.txt"
result_file_path = "fullname.txt"
file_reader = open(file_path, mode='r', encoding='Latin-1')
fullname = open(result_file_path, mode="w", encoding="Latin-1")
my_text_2 = file_reader.read()

searching_fullname = r"[A-Z]+[\w+-]+[a-z A-Z]+[\s]+[A-Z)\s+O'\s+[A-Z]+[A-Z}+[\w+-]\w+"
results_all_fullname = re.findall(searching_fullname, my_text_2) 

for i in results_all_fullname:
    print(i)
    fullname.write(i + "\n")




file_path = "mock_data.txt"
result_file_path = "other.txt"
file_reader = open(file_path, mode='r', encoding='Latin-1')
other = open(result_file_path, mode="w", encoding="Latin-1")
my_text_3 = file_reader.read()

searching_other = r'[A-Z]\w*\.\w+'
results_all_other = re.findall(searching_other, my_text_3) 

for i in results_all_other:
    print(i)
    other.write(i + "\n")




file_path = "mock_data.txt"
result_file_path = "hashtag.txt"
file_reader = open(file_path, mode='r', encoding='Latin-1')
hashtag = open(result_file_path, mode="w", encoding="Latin-1")
my_text_4 = file_reader.read()

searching_hashtag = r'#[\w 0-9]+'
results_all_hashtag = re.findall(searching_hashtag, my_text_4) 

for i in results_all_hashtag:
    print(i)
    hashtag.write(i + "\n")





