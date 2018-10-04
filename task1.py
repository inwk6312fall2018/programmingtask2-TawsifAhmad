def crime_list():				# main function 
 fin = open("Crime.csv","r") 			# reading data from csv file
 my_dic = dict()
 my_list = []
 my_list2 = []
 for line in fin:
    line=line.strip()
    line2 = line.split(',')
    my_list.append(line2[-1]) 
    my_list2.append(line2[-2])			#appending data (only crime name data to list)
 for i in my_list:				#loop list
    if i not in my_dic:  			#checking the required data in dictinary
      my_dic[i]=1         			# if no exists it will append
    else:
      my_dic[i]+=1 	          		# if  exists it will add a count value
 print ("{:<8} {:<73}".format('Crime_type',' Crime_count')) 
 for key, value in my_dic.items(): 		  	# printing tabular format
    v= value
    print("{:<8} {:<15}".format(key, v))
       
 
crime_list() 					# function called
