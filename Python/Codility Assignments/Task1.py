#Ioannis Apomachos

def solution(S):
    # Implement your solution here
    twice_occuring_char=""
    for char in S:
        if S.count(char) ==2:
            twice_occuring_char=char
    print(twice_occuring_char)


test_string = "codility"
solution(test_string)