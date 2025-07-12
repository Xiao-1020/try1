def shell_sort(ori_list):
    gap=len(ori_list)//2
    while gap>=1:
        for i in range(gap,len(ori_list)):
            while i>0:
                if ori_list[i]<ori_list[i-gap]:
                    ori_list[i],ori_list[i-gap]=ori_list[i-gap],ori_list[i]
                    i-=gap
                else:
                    break
        gap//=2
    return(ori_list)

ori_list=list(map(int,input().split()))
print(shell_sort(ori_list))
#[2,4,  1,5,  3]  2,1,3 是同一组