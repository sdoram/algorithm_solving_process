# https://www.acmicpc.net/problem/25206

credit_input = [
    ["ObjectOrientedProgramming1", "3.0", "A+"],
    ["IntroductiontoComputerEngineering", "3.0", "A+"],
    ["ObjectOrientedProgramming2", "3.0", "A0"],
    ["CreativeComputerEngineeringDesign", "3.0", "A+"],
    ["AssemblyLanguage", "3.0", "A+"],
    ["InternetProgramming", "3.0", "B0"],
    ["ApplicationProgramminginJava", "3.0", "A0"],
    ["SystemProgramming", "3.0", "B0"],
    ["OperatingSystem", "3.0", "B0"],
    ["WirelessCommunicationsandNetworking", "3.0", "C+"],
    ["LogicCircuits", "3.0", "B0"],
    ["DataStructure", "4.0", "A+"],
    ["MicroprocessorApplication", "3.0", "B+"],
    ["EmbeddedSoftware", "3.0", "C0"],
    ["ComputerSecurity", "3.0", "D+"],
    ["Database", "3.0", "C+"],
    ["Algorithm", "3.0", "B0"],
    ["CapstoneDesigninCSE", "3.0", "B+"],
    ["CompilerDesign", "3.0", "D0"],
    ["ProblemSolving", "4.0", "P"],
]

course_credit_dict = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0,
}
# 학점 입력받기
credit_input = [input().split() for _ in range(20)]
# 필요한 학점, 성적 추출
split_credit_list = [[credit[1], credit[2]] for credit in credit_input]

MY_TOTAL_CREDIT = 0
TOTAL_CREDIT = 0
for num in split_credit_list:
    # P 거르기
    if num[1] in course_credit_dict:
        MY_TOTAL_CREDIT += course_credit_dict[num[1]] * float(num[0])
        TOTAL_CREDIT += float(num[0])
    # format으로 비어있는 소수점 확보하기
print(format(MY_TOTAL_CREDIT / TOTAL_CREDIT, ".6f"))
