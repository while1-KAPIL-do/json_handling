import json_generator as jg
import read_data as rd
import sys
def title(title,extra=" "):
	print("\n"*2,"-"*75,"\n","\t"*6,end="")
	print(title,extra,end="")
	print("\n\n","-"*75,end="\n\n")
	
file_name = input("Please enter a file name : ")

path = "~/CCR/UserFiles/my_data_analysis/"

n = True
while n:
	print("\n\n\t\t\t M E N U",file_name,"\n")
	print("1. Genrate New Json file ")
	print("2. Print all data in CSV formate")
	print("3. Print all data by name (A-Z)")
	print("4. Print all data by name (Z-A)")
	print("5. Print data ordered by phone no")
	print("6. sort data by thier domain (gmail,fb,being)")
	print("7. Sort data by thier top level domain (com,in,us)")
	print("0. Exit...!")
	ch=""
	try:
		ch = int(input("\nEnter your choice :"))
	except:
		print("\n\t\tSomething went wrong....!")
		
	if ch == 1:
		# for generate json file
		new_file_name = input("Enter the file name :")
		jg.k_generate_json_file(path,new_file_name)
	
	elif ch==2:
		# printing like excel
		title(" E X C E L   S H E E T")
		rd.k_print_json(path,file_name)
		
	elif ch==3:
		# sort by name A-Z
		sorttype = "A - Z"
		title(" Sort by Name ",sorttype)
		rd.k_sortbyname(path,file_name,sorttype)
		
	elif ch==4:
		# sort by name Z-A
		sorttype = "Z - A"
		title(" Sort by Name ",sorttype)
		rd.k_sortbyname(path,file_name,sorttype)
		
	elif ch==5:
		# phone no sorting
		no=input("Enter the digit :")
		title("Phone no sorted by ",no)
		rd.k_phonno_startwith(path,file_name,no)
		
	elif ch==6:
		# email sort by domail
		emailtype = input("Enter the domain (gmail,fb,bing) :")
		title("Email sortby domain :",emailtype)
		rd.k_sortby_email(path,file_name,emailtype)
	
	elif ch==7:
		# email sort by top level domain
		suffix = input("Enter the top level domain (in,com,us) :")
		title("Email sort by Top level domain :",suffix)
		rd.k_sortby_toplevel_domain(path,file_name,suffix)
	elif ch==0:
		n= False
		sys.exit()
		
	else :
		print("please select a valid option...!!")
