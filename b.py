#!/usr/bin/python3
# -*- coding: utf-8 -*- 

val=0
with open("lien", "w") as f:
	val=f.read()
	print(val)
	f.seek(0)
	f.write(str(val+1))