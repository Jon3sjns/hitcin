#!/bin/python
import random as cok
import os as ah
ah.system('clear')
ah.system("figlet 'Hitungan Cinta'|lolcat")
cowo=raw_input("Masukan Nama Cowo: ")
cewe=raw_input("Masukan Nama Cewe: ")
asu=[41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
itung = cok.choice(asu)
if itung < 50:
	print 'Maaf pacar anda kurang setia:) '
	print 'tingkat kesetiaannya adalah:'
	print itung
elif itung < 70:
	print 'Pacar anda lumayan setia'
        print 'tingkat kesetiaannya adalah:'
        print itung
elif itung < 90:
	print 'Pacar anda setia banged'
        print 'tingkat kesetiaannya adalah:'
        print itung
elif itung < 100:
	print 'Pacar anda sangat setia banget>,<'
        print 'tingkat kesetiaannya adalah:'
        print itung
	ah.system("echo boleh aku tykung gak??|lolcat")
