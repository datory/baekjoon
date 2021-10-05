# # 1. 두 수 비교하기
# A, B = map(int, input().split())
# if A > B:
#     print(">")
# elif A < B:
#     print("<")
# elif A == B:
#     print("==")


# # 2. 시험 성적
# score = int(input())
# if score >= 90 and score <= 100:
#     print("A")
# elif score >= 80 and score <= 89:
#     print("B")
# elif score >= 70 and score <= 79:
#     print("C")
# elif score >= 60 and score <= 69:
#     print("D")
# else:
#     print("F")

# 3. 윤년
year = int(input())
if year >= 1 and year <= 4000:
    year_a = year%4
    year_b = year%100
    year_c = year%400
    if year_a == 0 and year_b != 0 or year_b == 0 and year_c == 0:
        print(1)
    else:
        print(0)




# 4. 사분면 고르기


# 5. 알람 시계
