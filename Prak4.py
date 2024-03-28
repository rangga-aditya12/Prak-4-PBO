# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 12:20:21 2024

@author: Rangga Aditya
"""

class Student:
    def __init__(self, nama, nim, nilai):
        self.nama = nama 
        self.nim = nim
        self.nilai = nilai
    def Data(self):
        return f"Nama: {self.nama}\nNIM: {self.nim}\nNilai: {self.nilai}"
 
praktikan1 = Student("Rangga Aditya Pradana", "064002300026", "99")
teman1 = Student("Tasana", "01234567898", "85")
teman2 = Student("Joy", "045378439928", "88")
teman3 = Student("kochi", "04382702807", "43")

print("---Data Pribadi---")
print(praktikan1.Data())
print("---Data Teman 1---")
print(teman1.Data())
print("---Data Teman 2---")
print(teman2.Data())
print("---Data Teman 3---")
print(teman3.Data())


