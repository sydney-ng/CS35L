#!/bin/bash
IFS="
"
my_dir=$1
let file_counter=0
declare -a file_array
hidden_files=`ls -a $my_dir | sort | grep "^\."`
reg_files=`ls $my_dir | sort`
for reg_file in ${reg_files}
do
	if [ ! -r "$my_dir/$reg_file" ] 
	then
		echo "I'm sorry, $reg_file is not a readable file" 
	elif [ -r "$my_dir/$reg_file" ] &&
	 [ ! -L "$my_dir/$reg_file" ] &&
	 [ ! -d "$my_dir/$reg_file" ]  
	then 
		file_array[$file_counter]="$my_dir/$reg_file"
		let file_counter=file_counter+1
	fi 
done 
for hidden_file in ${hidden_files}
do
        if [ ! -r "$my_dir/$hidden_file" ]
        then
                echo "I'm sorry, $hidden_file is not a readable file"
        elif [ -r "$my_dir/$hidden_file" ] &&
 	[ ! -L "$my_dir/$hidden_file" ] && 
	[ ! -d "$my_dir/$hidden_file" ]
	then    
                file_array[$file_counter]="$my_dir/$hidden_file"
        	let file_counter=file_counter+1
	fi
done
let array_iter1=0
let max_len=file_counter-1
while [ $array_iter1 -lt $max_len ] 
do 
	let array_iter2=array_iter1+1
	while [ $array_iter2 -lt $file_counter ]
	do 
		cmp "${file_array[$array_iter1]}" "${file_array[$array_iter2]}"
		if [ $? -eq "0" ] 
		then 
			rm "${file_array[$array_iter2]}"
			ln "${file_array[$array_iter1]}" "$file_array[$value2]"  
		fi 
		let array_iter2=array_iter2+1
	done
	let array_iter1=array_iter1+1
done
