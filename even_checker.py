import sys
#함수명은 동사가 가장 앞에
#함수 정의는 실행보다 위에

def extract_even_list(arrays): #짝수만 추출해서 새로운 배열을 만드는 함수
    even_list = []
    for index, number in enumerate(arrays):
        if number % 2 == 0 :
            even_list.append(number)
        print(even_list + [16, 18]) #이렇게해도 문제없이 잘됨 (파이썬만 그럼)

def extract_even_set(arrays): #set은 중괄호를 사용함, set은 순서가 없음, 인덱싱
    even_set = set()
    for index, number in enumerate(arrays):
        if number % 2 == 0:
            even_set.add(number)
        print(even_set)

def extract_even_dict(arrays): #dict는 키 밸류 맞춰서 넣어줘야 함
    even_dict = {"index" : [], "number" : []}
    for index, number in enumerate(arrays):
        if number % 2 == 0:
            even_dict["index"].append(index)
            even_dict["number"].append(number)
        print(even_dict)

def main(arrays):
    flag = True #Flag는 반드시 true or false 값
    for index, number in enumerate(arrays, start=1):
        #enumerate는 인덱스 값도 같이 반환시키는 함수
        #start = 숫자 -> 시작 인덱스 설정 가능
        if number % 2 == 0 :
            continue
        else:
            print(f"{index}번째 숫자{number}은 짝수가 아닙니다.") #f"~{num}~" num 변수 넣을 수 있음
            flag = False #홀수를 만나면 반복문 종료
            break

if __name__ == "__main__":
    if len(sys.argv) < 2: #사용법 설명
        print("Usage : python even_checker.py <1 2 3 5 6 7 8>") 
        sys.exit(1)
    else:
        arrays = list(map(int, sys.argv[1:])) 
        #argv = argument의 약자, 인자 값을 받는데 배열 형태로 받겠다.
        #받아서 int 형식으로 매핑해서 list에 넣겠다.
        extract_even_dict(arrays) 