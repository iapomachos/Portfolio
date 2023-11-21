#Ioannis Apomachos

def solution(A):
    # Implement your solution here
    array_A=[]
    array_B=[]

    if len(A)% 2 == 1:
        return False

    sorted_list=sorted(A)
    for number in range(0,len(A),2):
        if sorted_list[number]==sorted_list[number+1]:
            array_A.append(sorted_list[number])
            array_B.append(sorted_list[number+1])
        else:
            return False

    if array_A==array_B:
        return True


test_array=[1,2,2,1,3,3,7]
answer=solution(test_array)
print(answer)