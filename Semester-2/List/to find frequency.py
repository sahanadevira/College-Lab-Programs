def count_matching_string(word):
   return sum (1 for s in word if len(s)>=2
         and s[0]==s[-1])
samplelist=['abc','xyz','aba','1221','a','bb']
result=count_matching_string(samplelist)
print(f"total making string : {result}")
