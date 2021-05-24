    
def func(a):
    print("입력 숫자:",a)
if __name__ =="__main__": #직접 실행할때만 수행되는 코드
    print("모듈을 직접 실행")
    func(3)
    func(4)
else: # 임포트됐을 때만 실행되는 코드
    print("모듈을 임포트해서 실행")
