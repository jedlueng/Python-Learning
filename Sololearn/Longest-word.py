#Jedlueng 
#17 September 2021 
#Can do it because I solved leetcode before 


txt = input()

#your code goes here

txt_ls = txt.split(' ')
txt_ls_dict = {}
txt_ls_len = [] 
for word in txt_ls: 
	txt_ls_dict[word] = len(word)
	txt_ls_len.append(len(word))




for key, value in txt_ls_dict.items():
    if value == max(txt_ls_len):
        print(key)