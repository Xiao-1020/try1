def merge_sort(ori_list):
    middle=len(ori_list)//2
    if len(ori_list)<=1:
        return ori_list
    first_list=merge_sort(ori_list[:middle])
    second_list=merge_sort(ori_list[middle:])
    result=[]
    i=0
    j=0
    while i<len(first_list) and j<len(second_list):
        if first_list[i]<=second_list[j]:
            result.append(first_list[i])
            i+=1
        else:
            result.append(second_list[j])
            j+=1
    result+=(first_list[i:])
    result+=(second_list[j:])
    return result
ori_list=list(map(int,input().split()))
print(merge_sort(ori_list))