# 확장자 py 인 것은 모두 모듈임


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


# 모듈을 만들때 아래와 같은 테스트 코드를 만듦
if __name__ == "__main__":  # 테스트 코드가 출력 안되게 걸어두는 코드
    print(add(6, 5))
    print(sub(16, 5))
