scores = [3,4,21,36,10,28,35,5,24,42]
#scores =[10,5,20,20,4,5,2,25,1]
min_score= scores[0]
max_score = scores[0]
min_count =0
max_count =0 
for values in scores:
    if (values > max_score):
        max_score= values
        max_count +=1
    if ( values < min_score):
        min_score = values
        min_count +=1
print(f"{max_count=}, {min_count=}")