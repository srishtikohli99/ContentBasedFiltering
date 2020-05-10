# import numpy as np
# import os
# dir_path = os.path.dirname(os.path.realpath(__file__))
# dirs = os.path.join(dir_path,"X.npy")
# X = np.load(dirs,allow_pickle=True)
# def recom(x):
# 	y = db.child(x)
# 	j=0
# 	fam_size= y.child("fam_size").get().val()
# 	age= y.child("age").get().val()
# 	loc= y.child("fam_size").get().val()
# 	gender = y.child("gender").get().val()
# 	Y=np.zeroes(15)
# 	Y[0]=age 
# 	Y[1]=gender
# 	Y[2]=fam_size
# 	if loc=='Delhi':
# 		j=11
# 	elif loc=='New York':
# 		j=12
# 	elif loc=='Mumbai':
# 		j=13
# 	elif loc =='LA':
# 		j=14
# 	Y[j]=1
# 	print(Y)
