def solution(s):
    arr = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for i in range(10):
        s = s.replace(arr[i],str(i)) # s 에서 arr[i] 문자 나올시 str(i)로 변환 
    return int(s)
solution("one4seveneight")