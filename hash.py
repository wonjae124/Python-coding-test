def solution(participant, completion):
    #{key,value}: 딕셔너리, []: 리스트, (): 튜플
    answer = ''
    d ={} 
    for x in participant:
        d[x] = d.get(x, 0) + 1 #기본 메소드함수. x가 존재하면 x를 리턴, 아니면 0 리턴, 사전이 헤시 테이블이므로 복잡도 : 상수 시간(participant의 길이에 비례)
    for x in completion: # 상수시간(completion에 비례)
        d[x] -= 1

    dnf = [k for k, v in d.items() if v>0] 
    answer = dnf[0] 
    return answer

# 알고리즘의 복잡도 : O(N)
# 해시 테이블 검색 및 수정 : O(1)
# 리스트 순회 : O(N)
# 참고 : https://jocoma.tistory.com/entry/%EC%8B%9C%EA%B0%84-%EB%B3%B5%EC%9E%A1%EB%8F%84-%EA%B3%B5%EA%B0%84-%EB%B3%B5%EC%9E%A1%EB%8F%84