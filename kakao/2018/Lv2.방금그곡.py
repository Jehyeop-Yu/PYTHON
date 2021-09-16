# - m은 음 1개 이상 1439개 이하로 구성되어 있다.
# - musicinfos는 100개 이하의 곡 정보를 담고 있는 배열로, 각각의 곡 정보는 음악이 시작한 시각, 끝난 시각, 음악 제목, 악보 정보가 ','로 구분된 문자열이다.
# - 음악의 시작 시각과 끝난 시각은 24시간 HH:MM 형식이다.
# - 음악 제목은 ',' 이외의 출력 가능한 문자로 표현된 길이 1 이상 64 이하의 문자열이다.
# - 악보 정보는 음 1개 이상 1439개 이하로 구성되어 있다.
# 시작한 시각, 끝난 시각, 음악 제목, 악보 정보
# "ABCDEFG"	["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]	"HELLO"
# 'C, C#, D, D#, E, F, F#, G, G#, A, A#, B' #12개이다

# < 내가 푼거 실패 >------------------------------------------------------
import re

def solution(m, musicinfos):
    answer = ''
    musics = [re.split(",", music) for music in musicinfos]
    musics[0][3] = musics[0][3].replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
    musics[1][3] = musics[1][3].replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
    m = m.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')

    # music1 기본 멜로디 길이
    p = re.compile('([a-zA-Z])')
    music1_slice = p.findall(musics[0][3])
    music2_slice = p.findall(musics[1][3])

    # music1 재생 시간
    music1_times = [re.split(":", music1) for music1 in musics[0]]
    music1_time = (int(music1_times[1][0])*60+int(music1_times[1][1])) - (int(music1_times[0][0])*60+int(music1_times[0][1]))
    music2_times = [re.split(":", music2) for music2 in musics[1]]
    music2_time = (int(music2_times[1][0])*60+int(music2_times[1][1])) - (int(music2_times[0][0])*60+int(music2_times[0][1]))

    # 재생 길이 
    music1_length = music1_slice
    music2_length = music2_slice

    # 재생 길이 조절 
    if len(music1_length) > music1_time:
        music1_length = music1_length[0:music1_time]
    elif len(music1_length) < music1_time:
        music1_length = music1_length + music1_slice*(int(music1_time/len(music1_slice))+1)
    music1_length = music1_length[0:music1_time]

    if len(music2_length) > music2_time:
        music2_length = music2_length[0:music2_time]
    elif len(music2_length) < music2_time:
        music2_length = music2_length + music2_slice*(int(music2_time/len(music2_slice))+1)
    music2_length = music2_length[0:music2_time]

    # 합치기 
    music1_length = ''.join(music1_length)
    music2_length = ''.join(music2_length)

    # 걸러내기
    if m in music1_length and m in music2_length:
        if len(music1_length) >= len(music2_length):
            answer = musics[0][2]
        elif len(music1_length) < len(music2_length):
            answer = musics[1][2]
    elif m in music1_length and m not in music2_length:
        answer = musics[0][2]
    elif m in music2_length and m not in music1_length:
        answer = musics[1][2]
    else:
        answer = '(None)'

    return answer

# solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"])
# -----------------------------------------------------------------

# < 모범답안 >------------------------------------------------------

def change(melody):
    if 'A#' in melody: melody = melody.replace('A#', 'a')
    if 'C#' in melody: melody = melody.replace('C#', 'c')
    if 'D#' in melody: melody = melody.replace('D#', 'd')
    if 'F#' in melody: melody = melody.replace('F#', 'f')
    if 'G#' in melody: melody = melody.replace('G#', 'g')
    return melody

def solution(m, musicinfos):
    m = change(m)
    answer = ('(None)', None)
    for info in musicinfos:
        start, end, title, melody = info.split(',')
        start_h, start_m, end_h, end_m = map(int, start.split(':') + end.split(':'))
        time = 60*(end_h-start_h) + (end_m-start_m)
        melody = change(melody)
        melody_played = (melody*time)[:time]
        if m in melody_played:
            if (answer[1] == None) or (time > answer[1]):
                answer = (title, time)
    return answer[0]
# -----------------------------------------------------------------
