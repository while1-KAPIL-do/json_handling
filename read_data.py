import json
import sys

def comman_task(path,file_name):
	# Read from txt file
	try:
		new_path = path+file_name
		f = open(new_path,"r")
		d2=f.read()
		d2=d2.replace("\'","\"")
		f.close()
	except:
		print("\n\n\file not found....!\n\n\n")
		
	# convert json string to nested dictonery
	ddd=d2.encode().decode('utf-8-sig') 
	d = json.loads(ddd)
	#print(d)
	
	print("{:3}   {:15}\t\t{:10}\t\t{:10}\t\t{:10}".format("SN","Email","Name","Phone No","Password"),end="\n\n")
	return d
	
	
# my 2nd try
def excel_type(i,email,name,phon,pasw):
	print("{:3}   {:15}".format(i+1,email),sep="\t",end="\t\t")
	print("{:10}".format(name),end="\t\t")
	print("{:10}".format(phon),end="\t\t")
	print("{:10}".format(pasw),end="")
	print()

def k_print_json(path,file_name):	
	
	# keys for access data
	d = comman_task(path,file_name)
	l1=list(d.keys())
	for i in range(0,len(d)):
		email = l1[i]
		name = d[email]["name"]
		phon = d[email]["phoneno"]
		pasw = d[email]["password"]
		excel_type(i,email,name,phon,pasw)
		
def k_sortbyname(path,file_name,sorttype):
	
	# keys for access data
	d = comman_task(path,file_name)
	l1=list(d.keys())
		
	nd={}
	for i in range(0,len(d)):
		email = l1[i]
		name = d[email]["name"]
		phon = d[email]["phoneno"]
		pasw = d[email]["password"]
		
		nd[name]=[email,phon,pasw]
	l1=list(nd.keys())
	l1.sort()
	
	if sorttype == "A - Z":
	
		for i in range(0,len(d)):
			name = l1[i]
			email = nd[name][0]
			phon = nd[name][1]
			pasw = nd[name][2]
			excel_type(i,email,name,phon,pasw)
			
	elif sorttype =="Z - A":
		l1.reverse()
		for i in range(0,len(d)):
			name = l1[i]
			email = nd[name][0]
			phon = nd[name][1]
			pasw = nd[name][2]
			excel_type(i,email,name,phon,pasw)

def k_phonno_startwith(path,file_name,no):
	
	# keys for access data
	d = comman_task(path,file_name)
	l1=list(d.keys())
	
	for i in range(0,len(d)):
		email = l1[i]
		name = d[email]["name"]
		phon = d[email]["phoneno"]
		pasw = d[email]["password"]
		
		if phon.startswith(no):
			excel_type(i,email,name,phon,pasw)


def k_sortby_email(path,file_name,emailtype):
	
	# keys for access data
	d = comman_task(path,file_name)
	l1=list(d.keys())
	
	for i in range(0,len(d)):
		email = l1[i]
		name = d[email]["name"]
		phon = d[email]["phoneno"]
		pasw = d[email]["password"]
		
		if email.find(emailtype) != -1 :
			excel_type(i,email,name,phon,pasw)


def k_sortby_toplevel_domain(path,file_name,suffix):
	
	# keys for access data
	d = comman_task(path,file_name)
	l1=list(d.keys())
	
	for i in range(0,len(d)):
		email = l1[i]
		name = d[email]["name"]
		phon = d[email]["phoneno"]
		pasw = d[email]["password"]
		
		if email.find(suffix) != -1 :
			excel_type(i,email,name,phon,pasw)
