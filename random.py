import random
countera = 0
my_hand = input('自分の手')
computer = random.choice(["グー", "チョキ", "パー"])

if my_hand == "グー":
    countera = 1
elif my_hand == "パー":
    countera = 2
elif my_hand == "チョキ":
    countera = 3

counterb = 0
if computer == "グー":
    counterb = 1
elif computer == "パー":
    counterb = 2
elif computer == "チョキ":
    counterb = 3

result = (countera + 3 - counterb) % 3

if result == 0:
    print("あなたは", my_hand)
    print("コンピューターは", computer)
    print("よって", "あいこ")
elif result == 1:
    print("あなたは", my_hand)
    print("コンピューターは", computer)
    print("よってあなたの", "勝ち")
else:
    print("あなたは", my_hand)
    print("コンピューターは", computer)
    print("よってあなたの", "負け")
