def demSoLanXuatHien(lst):
    count_dic ={}
    for item in lst:
        if item in count_dic:
            count_dic[item] += 1
        else:
            count_dic[item] = 1
    return count_dic

input_string = input("Nhập danh sách các từ, cách nhau bằng dấu cách: ")
word_list = input_string.split()
soLanXuatHien = demSoLanXuatHien(word_list)
print("Số lần xuất hiện của mỗi từ: ", soLanXuatHien)