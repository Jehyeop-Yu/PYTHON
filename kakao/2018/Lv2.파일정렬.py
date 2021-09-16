# 파일명에 포함된 숫자를 반영한 정렬 기능을 저장소 관리 프로그램에 구현하기로 했다.
# 내가 풀지 못함--------------------------------------------------------
# ---------------------------------------------------------------------
# 해법--------------- 
import re 
def solution(files): 
    answer = [] 
    head_num_tail = [re.split(r"([0-9]+)", file) for file in files] 
    sorted_head_num_tail = sorted(head_num_tail, key=lambda x: (x[0].lower(), int(x[1])))   # key =str.lower -> 대문자 소문자 구분없이 정렬
    answer = ["".join(h_n_t) for h_n_t in sorted_head_num_tail] 
    return answer
    print(answer)
solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])