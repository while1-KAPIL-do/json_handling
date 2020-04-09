import sys
import random

st = '''1. Liam
2. Noah
3. William
4. James
5. Oliver
6. Benjamin
7. Elijah
8. Lucas
9. Mason
10. Logan
11. Alexander
12. Ethan
13. Jacob
14. Michael
15. Daniel
16. Henry
17. Jackson
18. Sebastian
19. Aiden
20. Matthew
21. Samuel
22. David
23. Joseph
24. Carter
25. Owen
26. Wyatt
27. John
28. Jack
29. Luke
30. Jayden
31. Dylan
32. Grayson
33. Levi
34. Issac
35. Gabriel
36. Julian
37. Mateo
38. Anthony
39. Jaxon
40. Lincoln
41. Joshua
42. Christopher
43. Andrew
44. Theodore
45. Caleb
46. Ryan
47. Asher
48. Nathan
49. Thomas
50. Leo
51. Isaiah
52. Charles
53. Josiah
54. Hudson
55. Christian
56. Hunter
57. Connor
58. Eli
59. Ezra
60. Aaron
61. Landon
62. Adrian
63. Jonathan
64. Nolan
65. Jeremiah
66. Easton
67. Elias
68. Colton
69. Cameron
70. Carson
71. Robert
72. Angel
73. Maverick
74. Nicholas
75. Dominic
76. Jaxson
77. Greyson
78. Adam
79. Ian
80. Austin
81. Santiago
82. Jordan
83. Cooper
84. Brayden
85. Roman
86. Evan
87. Ezekiel
88. Xavier
89. Jose
90. Jace
91. Jameson
92. Leonardo
93. Bryson
94. Axel
95. Everett
96. Parker
97. Kayden
98. Miles
99. Sawyer
100. Jason
1. Amit
2. Anshul
3. Anurag
4. Arjun
5. Kapil
6. Karan
7. Komal
8. Manish
9. Mayank
10. Danish
11. Namita
12. Nishi
13. Prashant
14. Pratiksha
15. Prince
16. Rohit
17. Raunak
18. Shalini
19. Shivam
20. Shubham
21. Simran
22. Somya
23. Soumya
24. Swati
25. Annu
26. Kappu
27. Manjhi
28. Danny
29. Topper
30. Hum
31. Waiting
32. Guddu
33. Golu
34. Ramta
35. Matka
36. Taliwan
37. Billu'''

def k_generate_json_file(path,file_name):
	
	l1 = list(st.split("\n"))
	di = {}
	
	for i in l1:
		sp = i.find(" ")
		mydic = {}
		#name
		name = i[sp+1:]
		mydic["name"]=name
		
		#phone no
		no = str(random.randint(6,9))+str(random.randint(111111111,999999999))
		mydic["phoneno"]=no
		
		#password
		ps = str(random.randint(111,999))+name
		mydic["password"]=ps
		
		#email
		emailtype = ["gmail","yahoo","fb","bing"]
		em = name[0:3]+str(random.randint(11,99))+"@"+random.choice(emailtype)+random.choice([".in",".com",".us"])
		
		
		di[em]=mydic
	
	s = str(di)
	#print(s)
	
	
	try:
		new_path = path+file_name
		f = open(new_path,"x")
		f.write(s)
		print("File successfully created.")
		f.close()
	except:
		print("\n\n\n file not found....!\n\n\n")
		
