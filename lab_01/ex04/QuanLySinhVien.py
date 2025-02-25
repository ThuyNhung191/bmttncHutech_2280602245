from SinhVien import SinhVien

class QuanLySinhVien:
    listSV = []
    
    def generateID(self):
        maxID = 1
        if(self.soLuongSinhVien() > 0):
            maxID = self.listSV[0]._ID()
            for sv in self.listSV:
                if(maxID < sv._ID()):
                    maxID = sv._ID()
            maxID += 1
        return maxID 
    
    def soLuongSinhVien(self):
        return self.listSV.__len__()
    
    def themSinhVien(self):
        svID = self.generateID()
        name = input("Nhập tên sinh viên: ")
        sex = input("Nhập giới tính sinh viên: ")
        major = input("Nhập chuyên ngành sinh viên: ")
        dtb = float(input("Nhập điểm trung bình sinh viên: "))
        sv = SinhVien(svID,name,sex,major,dtb)
        self.xepLoaiHocLuc(sv)
        self.listSV.append(sv)
        
    def updateSinhVien(self, ID):
        sv:SinhVien = self.findByID(ID)
        if(sv != None):
            name = input("Nhập tên sinh viên: ")
            sex = input("Nhập giới tính sinh viên: ")
            major = input("Nhập chuyên ngành sinh viên: ")
            dtb = float(input("Nhập điểm trung bình sinh viên: "))
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._dtb = dtb
            self.xepLoaiHocLuc(sv)
        else:
            pritn("Sinh vien co ID = {} khong ton tai".format(ID))
            
    def sortByID(self):
        self.listSV.sort(key=lambda x: x._ID(), reverse=False)
        
    def sortByName(self):
        self.listSV.sort(key=lambda x: x._name, reverse=False)
    
    def sortByDTB(self):
        self.listSV.sort(key=lambda x: x._dtb, reverse=True)
        
    def findByID(self, ID):
        ssearchResult = None
        if(self.soLuongSinhVien() > 0):
            for sv in self.listSV:
                if(sv._ID() == ID):
                    ssearchResult = sv
                    
        return ssearchResult
    
    def findByName(self, name):
        listsv = []
        if(self.soLuongSinhVien() > 0):
            for sv in self.listSV:
                if(keyWord.upper() in sv._name.upper()):
                    listsv.append(sv)
                    
        return listsv
    
    def deleteByID(self,ID):
        isDeleted = False
        sv = self.findByID(ID)
        if(sv != None):
            self.listSV.remove(sv)
            isDeleted = True
        return isDeleted
    
    def xepLoaiHocLuc(self, sv:SinhVien):
        if(sv._dtb >= 8):
            sv._hocluc = "Giỏi"
        elif(sv._dtb >= 6.5):
            sv._hocluc = "Khá"
        elif(sv._dtb >= 5):
            sv._hocluc = "Trung Bình"
        else:
            sv._hocluc = "Yếu"  
    
    def ShowSV(self,listsv):
        print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}".format("ID","name","sex","major","DTB","Học Lưc"))
        if(listsv.__len__() > 0):
            for sv in listsv:
                print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}".format(sv._ID(),sv._name,sv._sex,sv._major,sv._dtb,sv._hocluc))
        print("\n")
        
    def getListSV(self):
        return self.listSV
                                                                    
        
            
    
                    