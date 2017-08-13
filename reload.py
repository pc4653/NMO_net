def complete_strip(x):
	x = x.strip()
	x = x.strip("()")
	#x = x.replace(" ","")
	x = x.replace("'","")
	return x;

tags = open('test3.txt').readlines()
tags = map(complete_strip, tags)
T1FC_dic = {}
T1F_dic = {}
T1C_dic = {}
T1_dic = {}
T1E_dic = {}
T1FSE_dic = {}
T1FSPGR_dic = {}
T1SE_dic = {}
T1FS_dic = {}
for tag in tags:
	
	[desc,number] = tag.split(',')
	desc1 = desc.replace(" ","")
	number = int(number)
	if 't2' in desc1.lower():
		if 'flair+c' in desc1.lower():
			if T1FC_dic.has_key(desc):
				T1FC_dic[desc] = T1FC_dic[desc] + number
			else:
				T1FC_dic.update({desc:number})
		elif 'flair' in desc1.lower():
			if T1F_dic.has_key(desc):
				T1F_dic[desc] = T1F_dic[desc] + number
			else:
				T1F_dic.update({desc:number})
		elif 't2+c' in desc1.lower():
			if T1C_dic.has_key(desc):
				T1C_dic[desc] = T1C_dic[desc] + number
			else:
				T1C_dic.update({desc:number})
		elif 'fse' in desc1.lower():
			if T1FSE_dic.has_key(desc):
				T1FSE_dic[desc] = T1FSE_dic[desc] + number
			else:
				T1FSE_dic.update({desc:number})
		elif 'fspgr' in desc1.lower():
			if T1FSPGR_dic.has_key(desc):
				T1FSPGR_dic[desc] = T1FSPGR_dic[desc] + number
			else:
				T1FSPGR_dic.update({desc:number})
		elif 'se' in desc1.lower():
			if T1SE_dic.has_key(desc):
				T1SE_dic[desc] = T1SE_dic[desc] + number
			else:
				T1SE_dic.update({desc:number})
		elif 'fs' in desc1.lower():
			if T1FS_dic.has_key(desc):
				T1FS_dic[desc] = T1FS_dic[desc] + number
			else:
				T1FS_dic.update({desc:number})			

		elif len(desc1) < 8:
			if T1_dic.has_key(desc):
				T1_dic[desc] = T1_dic[desc] + number
			else:
				T1_dic.update({desc:number})
		else:
			if T1E_dic.has_key(desc):
				T1E_dic[desc] = T1E_dic[desc] + number
			else:
				T1E_dic.update({desc:number})
			
				
