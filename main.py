## Importing Libraries
import random
import time
import sys
import os
from tarot_reader import TarotReader

# clear screen function
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


## slow_type for string output
def slow_type(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush() 
        time.sleep(delay)
    print()


delay_num = 0.01  # 텍스트 딜레이 (0에 가까울수록 빨라짐)

## Importing Classes
from opening import OpeningMessage
from PandasToList import PandasToList
from cards import cards
from pdf_converter import PDF
from emailsender import EmailSender
from secret import sender_email, password  # .gitIgnore에 추가됨.

email_sender = EmailSender(sender_email, password)


## Language Setting

# if lang = 0 -> English
# if lang = 1 -> Korean

## Before the Execution (String file)
clear_screen()
print("시작하기 전에...  \n")
m = OpeningMessage()
m.__init__(filename="BeforetheExecution.txt")
print(m.open_file())
m.open_file()
open_after = input("계속하려면 Enter 키를 누르세요.  \n")
clear_screen()


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
clear_screen()
print("================================================================")
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

reader = TarotReader()

concern = input("너의 고민은 뭐니? \n\n고민:  ")
reader.set_concern(concern)

## Card Selection - Info
reader.set_cards_num()
card_num = reader.cards_num
# AI가 card_num을 정한다 ->  1  or 3
card_num_desc = "\n\n".join(reader.cards_num_meaning)
# AI가 n번째 카드가 뜻하는 것을 적는다 (과거-현재-미래)
#  concern을 중점으로...

clear_screen()
print("===============================================================")
slow_type(
    f"""
좋아,  그럼 이제 카드를 뽑아볼까? 
지금부터 총 {card_num}개의 카드를 뽑을거야.

{card_num_desc}

이해했어?  잘 모르겠으면 카드를 해석할 때  다시 알려줄게.

""",
    delay_num,
)
next = input("계속하려면 Enter를 누르세요.\n")


## Card Selection

list_tarot_deck = list_up_tarot + list_rev_tarot
list_tarot_deck_mixed = list_tarot_deck[:]
random.shuffle(list_tarot_deck_mixed)

clear_screen()
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

# valid input을 위한 함수

def get_valid_input(prompt, max_value):
    while True:
        try:
            value = int(input(prompt))
            if 0 <= value <= max_value:
                return value
            else:
                print(f"\n숫자는 0부터 {max_value} 사이로 입력해야 해요. 다시 시도해주세요.")
        except ValueError:
            print("\n유효한 숫자를 입력해주세요.")

first_card = get_valid_input("0부터 43까지의 수를 적으세요: ", 43)

if card_num == 3:
    slow_type("\n첫번째 카드를 뽑았어,  그럼 다음 카드를 뽑아볼까?", delay_num)
    second_card = get_valid_input("0부터 42까지의 수를 적으세요: ", 42)

    slow_type("\n이제 마지막으로 세번째 카드를 뽑아보자.", delay_num)
    third_card = get_valid_input("0부터 41까지의 수를 적으세요: ", 41)


## Card Loading (string)
clear_screen()
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
    second_tarot_card = list_wo_first[int(second_card)]
    list_wo_second = list_wo_first[:second_card] + list_wo_first[second_card + 1 :]
    third_tarot_card = list_wo_second[int(third_card)]
    reader.set_cards([first_tarot_card, second_tarot_card, third_tarot_card])
else:
    reader.set_cards([first_tarot_card])

## Interpretation

# AI의 Tarot Interpretation -----------------------------------
reader.set_meaning_by_idx(0)
reader.set_interpretation_by_idx(0)
interpretations = reader.cards

interpretation_word_first = interpretations[0]["meaning"]
interpretation_concern_first = interpretations[0]["interpretation"]
# -------------------------------------------------------------

clear_screen()
first_tarot_card_ascii = ""
for n in range(len(list_tarot_deck_mixed)):
    if first_tarot_card[0] == cards[n]["name"]:
        first_tarot_card_ascii = cards[n]["card"]

print(first_tarot_card_ascii + "\n")

slow_type(
    f"""
너가 처음으로 뽑은 카드는 {first_tarot_card[1]} (이)야. 

{interpretation_word_first}

{interpretation_concern_first}

""",
    delay_num,
)

next3 = input("계속하려면 Enter 키를 눌러주세요  \n")

if card_num == 3:
    for n in range(len(list_wo_first)):
        if second_tarot_card[0] == cards[n]["name"]:
            second_tarot_card_ascii = cards[n]["card"]

    # Problematic
    for n in range(len(list_wo_second)):
        if third_tarot_card[0] == cards[n]["name"]:
            third_tarot_card_ascii = cards[n]["card"]

    reader.set_meaning_by_idx(1)
    reader.set_interpretation_by_idx(1)
    interpretations = reader.cards
    interpretation_word_second = interpretations[1]["meaning"]
    interpretation_concern_second = interpretations[1]["interpretation"]
    
    clear_screen()
    print(second_tarot_card_ascii + "\n")
    slow_type(
    f"""
너가 두번째로 뽑은 카드는 {second_tarot_card[1]} (이)야.

{interpretation_word_second}

{interpretation_concern_second}

""",
    delay_num,
    )

    next3 = input("계속하려면 Enter 키를 눌러주세요  \n ")

    reader.set_meaning_by_idx(2)
    reader.set_interpretation_by_idx(2)
    interpretations = reader.cards
    interpretation_word_third = interpretations[2]["meaning"]
    interpretation_concern_third = interpretations[2]["interpretation"]
    interpretations = reader.cards
    clear_screen()
    print(third_tarot_card_ascii + "\n")
    slow_type(
        f"""
너가 세번째로 뽑은 카드는 {third_tarot_card[1]} (이)야.

{interpretation_word_third}

{interpretation_concern_third}

""",
        delay_num,
    )
    next3 = input("계속하려면 Enter 키를 눌러주세요  \n ")

# ---- debugging ----------------------


reader.set_interpretation_overall()
interpretation_overall = reader.interpretation_overall
clear_screen()
slow_type(
    f"""
결과를 요약해보면,

{interpretation_overall}

""",
    delay_num,
)

next4 = input("계속하려면 Enter  키를 눌러주세요  \n")

## Rating (strings)
clear_screen()
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

# pdf generation
pdf = PDF(f"{name}")
pdf.add_page()
pdf.add_concern(concern)
pdf.add_block(
    first_tarot_card_ascii,
    first_tarot_card[0],
    interpretation_concern_first,
)
if card_num == 3:
    pdf.add_block(
        second_tarot_card_ascii,
        second_tarot_card[0],
        interpretation_concern_second,
    )
    pdf.add_block(
        third_tarot_card_ascii,
        third_tarot_card[0],
        interpretation_concern_third,
    )
pdf.add_result(interpretation_overall)
pdf.output(f"{name}_TarotAI_Result.pdf")



## Ending
clear_screen()
print("===============================================================")
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
        email_confirm = input(f"{email}    이게 너의 이메일 주소가 맞아?  (Y/N): ")

        if email_confirm == "Y" or email_confirm == "y":
            break
    except:
        pass

# ------------------------------- email 보내기
receiver_email = email
result_pdf = f"{name}_TarotAI_Result.pdf"
subject = "정바융 Merge TarotAI 결과"
body = f"""
{name}에게,

안녕,  {name}! 
오늘 타로 보러 와줘서 다시 한 번 고마워!
타로 결과를 pdf로 만들어봤으니,  첨부파일을 확인해봐.
그럼,  안녕!

TarotAI 올림.
"""
print("이메일 보내는 중...  \n")
email_sender.send_email(receiver_email, subject, body, result_pdf)

#  -------------------------------------------

clear_screen()
slow_type(
    f"""

{receiver_email}
이 주소로 이메일을 보냈어!  나중에 꼭 확인해봐!

아직 나도 타로에 대해 배우는 중이라 복채는 받지 않을게.
가기 전에 부스 도장 받는 거 잊지 말고!

와줘서 고마워.  다음 기회가 되면 또 보자.  안녕!

""",
    delay_num,
)

next5 = input("끝내려면 Enter 키를 눌러주세요.  감사합니다.")
clear_screen()
