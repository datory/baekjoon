print("Hello World!")
print("강한친구 대한육군\n강한친구 대한육군")

A, B = map(int, input().split())
print(A+B)

A, B = map(int, input().split())
print(A-B)

A, B = map(int, input().split())
print(A*B)

A, B = map(int, input().split())
print(A/B)

A, B = map(int, input().split())
if A >= 1 and A <= 10000 and B >=1 and B <= 10000:
    print(A+B)
    print(A-B)
    print(A*B)
    print(A//B)
    print(A%B)