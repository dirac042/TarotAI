## Importing Libraries
import random
import time
import sys


## slow_type for string output
def slow_type(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


delay_num = 0.01

## Importing Classes
from opening import OpeningMessage
from PandasToList import PandasToList
from cards import cards
from pdf_converter import PDF


## Language Setting

# if lang = 0 -> English
# if lang = 1 -> Korean

## Before the Execution (String file)
m = OpeningMessage()
m.__init__(filename="BeforetheExecution.txt")
print(m.open_file())
m.open_file()

open_after = input("계속하려면 Enter 키를 누르세요.  \n")


## Tarot Card import
p = PandasToList()
list_up_tarot = p.up_deck("TarotCardsUpright.csv")
list_rev_tarot = p.rev_deck("TarotCardsReversed.csv")


## Starting Message
print(
    """
=====================================================================

 _______  _______  ______    _______  _______  _______  ___  
|       ||   _   ||    _ |  |       ||       ||   _   ||   | 
|_     _||  |_|  ||   | ||  |   _   ||_     _||  |_|  ||   | 
  |   |  |       ||   |_||_ |  | |  |  |   |  |       ||   | 
  |   |  |       ||    __  ||  |_|  |  |   |  |       ||   | 
  |   |  |   _   ||   |  | ||       |  |   |  |   _   ||   | 
  |___|  |__| |__||___|  |_||_______|  |___|  |__| |__||___| 


=====================================================================
"""
)
slow_type(
    """

안녕? 나는 오늘 너에게 잠깐이나마 미래를 보여줄 인공지능 TarotAI야.

학교생활 많이 힘들지? 이렇게 시간 내서 점 보러 와줘서 고마워. 

시작하기 전에, 네 이름을 알려줘. 진짜 이름 말고, 가명으로 적어도 돼.
""",
    delay_num,
)
name = input("이름(가명)을 적어줘:  ")

## Concern
print("\n================================================================")
slow_type(f"\n네 이름은 {name}이구나.  반가워!", delay_num)
slow_type(
    """
그럼 이제, 네 고민을 알려줘.
'오늘 내 운세는 어때' 같이 특정 기간의 운세를 봐줄 수도 있고,
'요즘 공부가 잘 안 돼' 라던가 '내가 연애를 할 수 있을까' 처럼
특정 고민을 적어줘도 좋아.
    """,
    delay_num,
)

concern = input("너의 고민은 뭐니?  ")


## Card Selection - Info

card_num = 1
# AI가 card_num을 정한다 ->  1  or 3
card_num_desc = ""
# AI가 n번째 카드가 뜻하는 것을 적는다 (과거-현재-미래)
#  concern을 중점으로...

print("\n===============================================================")
slow_type(
    f"""
좋아,  그럼 이제 카드를 뽑아볼까? 
지금부터 총 {card_num}개의 카드를 뽑을거야.
{card_num_desc}
이해했어?  잘 모르겠으면 카드를 해석할 때  다시 알려줄게.

""",
    delay_num,
)
next = input("계속하려면 Enter를 누르세요. \n")


## Card Selection

list_tarot_deck = list_up_tarot + list_rev_tarot
list_tarot_deck_mixed = list_tarot_deck[:]
random.shuffle(list_tarot_deck_mixed)

print("===================================================================")
slow_type(
    """

좋아,  그럼 이제 카드를 뽑아볼까?

나는 AI라 카드를 섞는걸 보여주기 힘드니까,
숫자로 너가 뽑고싶은 카드를 알려줘.

마음을 가다듬고,  맨 위에서 몇번째 카드를 뽑을지 적어줘.

""",
    delay_num,
)


first_card = int(input("0부터 43까지의 수를 적으세요:  "))
if card_num == 3:
    slow_type("첫번째 카드를 뽑았어,  그럼 다음 카드를 뽑아볼까?", delay_num)
    second_card = int(input("0부터 42까지의 수를 적으세요:  "))
    if second_card > 43:
        print("숫자를 잘못 적은 것 같은데?  다시 적어줘.")
    slow_type("이제 마지막으로 세번째 카드를 뽑아보자.", delay_num)
    third_card = int(input("0부터 41까지의 수를 적으세요:  "))


## Card Loading (string)
slow_type(
    """
잘했어!
이제 카드를 하나씩 살펴보면서 미래를 살짝 엿보도록 하자!
준비됐어?
""",
    delay_num,
)

next2 = input("계속하려면 Enter를 누르세요  \n")

first_tarot_card = list_tarot_deck_mixed[int(first_card)]
if card_num == 3:
    list_wo_first = (
        list_tarot_deck_mixed[:first_card] + list_tarot_deck_mixed[first_card + 1 :]
    )
    second_tarot_card = list_tarot_deck_mixed[int(second_card)]
    list_wo_second = list_wo_first[:second_card] + list_wo_first[second_card + 1 :]
    third_tarot_card = list_wo_second[int(third_card)]


## Interpretation

first_tarot_card_ascii = ""
for n in range(len(list_tarot_deck_mixed)):
    if first_tarot_card[0] == cards[n]["name"]:
        first_tarot_card_ascii = cards[n]["card"]

print(first_tarot_card_ascii + "\n")

slow_type(
    f"""
너가 처음으로 뽑은 카드는 {first_tarot_card[1]} (이)야. 
""",
    delay_num,
)

next3 = input("계속하려면 Enter 키를 눌러주세요  \n ")

if card_num == 3:
    for n in range(len(list_wo_first)):
        if second_tarot_card[0] == cards[n]["name"]:
            second_tarot_card_ascii = cards[n]["card"]

    for n in range(len(list_wo_second)):
        if third_tarot_card[0] == cards[n]["name"]:
            third_tarot_card_ascii = cards[n]["card"]

    print(second_tarot_card_ascii + "\n")
    slow_type(
        f"""
    너가 두번째로 뽑은 카드는 {second_tarot_card[1]} (이)야.
        """,
        delay_num,
    )

    print(third_tarot_card_ascii + "\n")
    slow_type(
        f"""
    너가 세번째로 뽑은 카드는 {third_tarot_card[1]} (이)야.
    """,
        delay_num,
    )

# interpretation_word = AI(카드가 뜻하는 의미 (단어로))
# interpretation_concern = AI(카드의 의미를 concern의 맥락에서 해석)

## Interpretation - Overall

# interpretation_overall = AI(interpretation_concern들을 요약:  조언,  주의해야할 점)
slow_type(
    f"""
결과를 요약해보면:  ...

    """,
    delay_num,
)

next4 = input("계속하려면 Enter  키를 눌러주세요  \n")

## Rating (strings)
print("================================================================")

slow_type(
    f"""

여기까지가 내가 본 미래의 전부야.  
어땠어?  결과가 마음에 들었으면 좋겠네.  
만족도를 0에서 5까지 매긴다면,  내게 몇 점을 줄 것 같아?

""",
    delay_num,
)

rating = int(input("0부터 5까지 점수를 매겨주세요:  "))


## Ending

qr_code = ""


# pdf_convert

pdf = PDF()
pdf.add_page()

# Including variables:
# first_tarot_card_ascii, #first_tarot_card[0] (Eng), [1] (Kor)
# interpretation_concern
# interpretation_word
# interpretation_overall

pdf.multi_cell(10, 10, first_tarot_card_ascii)
pdf.output("test.pdf")


print("\n===============================================================")
slow_type(
    f"""

평가해줘서 고마워.
이제 헤어질  시간이야.

아 참, 가기 전에 이메일 주소 알려줄 수 있을까? 

오늘 본 점의 결과를 pdf 파일로 정리해서 이메일로 보내줄게!

""",
    delay_num,
)

while True:
    try:
        email = input("이메일 주소를 적어주세요:  ")
        email_confirm = input(f"{email} 이게 너의 이메일 주소가 맞아?  (Y/N): ")

        if email_confirm == "Y":
            break
    except:
        pass


slow_type(
    f"""
{qr_code}
이 QR코드를 스마트폰으로 찍어봐!

아직 나도 타로에 대해 배우는 중이라 복채는 받지 않을게.
가기 전에 부스 도장 받는 거 잊지 말고!

와줘서 고마워.  다음 기회가 되면 또 보자.  안녕!

""",
    delay_num,
)

next5 = input("끝내려면 Enter 키를 눌러주세요.  감사합니다.")

# jpg automation program
# Google Cloud API 사용해서 jpg 파일 저장 ->  link 생성
# QRCode Generator -> link embed


## ...repeat
