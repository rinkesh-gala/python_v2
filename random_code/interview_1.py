"""input = [1,2,3,6,4,5,7,8]
output = [(3,5)] - Start_index and End_Index """


def find_el(input_list):
    start_index =0
    for index in range(0,len(input_list)-1):
        next_el = input_list[index]+1
        print (f"for start:, {index=}, {input_list[index]=} {next_el=}")
        if input_list[index+1] == next_el:
            print (f"if:, {index=}, {input_list[index]=}, {next_el=}")
            continue
        elif start_index==0 :
            start_index = index+1
            print (f"elif:, {index=}, {input_list[index]=}, {next_el=}, {start_index=}")
        else:
            end_index = index
            print (f"else:, {index=}, {input_list[index]=}, {next_el=}, {start_index=}, {end_index=}")
    print (f"final output: {start_index=}, {end_index=}")

input_list = [1,2,3,6,4,5,7,8]
find_el(input_list)

        


