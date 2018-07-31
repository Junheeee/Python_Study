
print("게임을 시작하겠습니다.")

button = "R"
print("청기 올려")
input_button = input(">")
if button == input_button.upper():
    print("성공")
else:
    print("실패")

button = "F"
print("청기 내려")
input_button = input(">")
if button == input_button.upper():
    print("성공")
else:
    print("실패")

button = "U"
print("백기 올려")
input_button = input(">")
if button == input_button.upper():
    print("성공")
else:
    print("실패")

button = "J"
print("백기 내려 ")
input_button = input(">")
if button == input_button.upper():
    print("성공")
else:
    print("실패")

