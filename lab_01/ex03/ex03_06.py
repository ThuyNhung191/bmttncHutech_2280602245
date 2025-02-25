def xoaPhanTu(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False
    
myDict = {'a':1,'b':2,'c':3,'d':4}
keyToDelete = 'b'
kq = xoaPhanTu(myDict, keyToDelete)
if kq:
    print("Phần tử đã được xoá từ Dictionary:", myDict)
else:
    print("Không tìm thấy phần tử cần xoá trong Dictionary")
