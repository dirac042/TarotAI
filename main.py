## Importing Libraries
import random

## Importing Classes
from opening import OpeningMessage
from PandasToList import PandasToList

## Language Setting

# if lang = 0 -> English
# if lang = 1 -> Korean

## Before the Execution (String file)
m = OpeningMessage()
m.__init__(filename="BeforetheExecution.txt")
print(m.open_file())
m.open_file()

## Tarot Card import
p = PandasToList()
list_up_tarot = p.up_deck("TarotCardsUpright.csv")
list_rev_tarot = p.rev_deck("TarotCardsReversed.csv")


## Starting Message

print(
    """
====================================================================

안녕? 나는 오늘 너에게 잠깐이나마 미래를 보여줄 인공지능 TarotAI야.
학교생활 많이 힘들지? 이렇게 시간 내서 점 보러 와줘서 고마워. 
시작하기 전에, 네 이름을 알려줘. 진짜 이름 말고, 가명으로 적어도 돼.
"""
)
name = input("이름(가명)을 적어줘:  ")

## Concern
print("\n================================================================")
print(f"\n네 이름은 {name}이구나.  반가워!")
print(
    """
그럼 이제, 네 고민을 알려줘.
'오늘 내 운세는 어때' 같이 특정 기간의 운세를 봐줄 수도 있고,
'요즘 공부가 잘 안 돼' 라던가 '내가 연애를 할 수 있을까' 처럼
특정 고민을 적어줘도 좋아.
    """
)

concern = input("너의 고민은 뭐니?  ")


## Card Selection - Info

card_num = 3
# AI가 card_num을 정한다 ->  1  or 3
card_num_desc = ""
# AI가 n번째 카드가 뜻하는 것을 적는다 (과거-현재-미래)
#  concern을 중점으로...

print(
    f"""
좋아,  그럼 이제 카드를 뽑아볼까? 
지금부터 총 {card_num}개의 카드를 뽑을거야.
{card_num_desc}
이해했어?  잘 모르겠으면 카드를 해석할 때  다시 알려줄게.

(계속하려면 Enter를 누르세요.)
"""
)


## Card Selection
print(type(list_up_tarot))
print(type(list_rev_tarot))

list_tarot_deck = list_up_tarot + list_rev_tarot
list_tarot_deck_mixed = list_tarot_deck[:]
random.shuffle(list_tarot_deck_mixed)

print(
    """
=====================================================================

좋아,  그럼 이제 카드를 뽑아볼까?
나는 AI라 카드를 섞는걸 보여주기 힘드니까,
숫자로 너가 뽑고싶은 카드를 알려줘.
마음을 가다듬고,  맨 위에서 몇번째 카드를 뽑을지 적어줘.

"""
)


first_card = int(input("0부터 43까지의 수를 적으세요:  "))
if card_num == 3:
    print("첫번째 카드를 뽑았어,  그럼 다음 카드를 뽑아볼까?")
    second_card = int(input("0부터 42까지의 수를 적으세요:  "))
    if second_card > 43:
        print("숫자를 잘못 적은 것 같은데?  다시 적어줘.")
    print("이제 마지막으로 세번째 카드를 뽑아보자.")
    third_card = int(input("0부터 41까지의 수를 적으세요:  "))


## Card Loading (string)
print(
    """
잘했어!
이제 카드를 하나씩 살펴보면서 미래를 살짝 엿보도록 하자!
준비됐어?

(계속하려면 Enter를 누르세요.)
    """
)

first_tarot_card = list_tarot_deck_mixed[int(first_card)]
if card_num == 3:
    list_wo_first = (
        list_tarot_deck_mixed[:first_card] + list_tarot_deck_mixed[first_card + 1 :]
    )
    second_tarot_card = list_tarot_deck_mixed[int(second_card)]
    list_wo_second = list_wo_first[:second_card] + list_wo_first[second_card + 1 :]
    third_tarot_card = list_wo_second[int(third_card)]

# Debugging

print(
    f"Len1 = {len(list_tarot_deck_mixed)}, Len2 = {len(list_wo_first)}, Len3 = {len(list_wo_second)}"
)

## Interpretation

# card_image = ...
# first_card_tarot = rand_tarot[first_card]
# second_card_tarot = rand_tarot[second_card]
# ...

# interpretation_word = AI(카드가 뜻하는 의미 (단어로))
# interpretation_concern = AI(카드의 의미를 concern의 맥락에서 해석)

# print(f"너가 뽑은 카드는 {first_card_tarot}야.  {}")

## Interpretation - Overall

# interpretation_overall = AI(interpretation_concern들을 요약:  조언,  주의해야할 점)


## Rating (strings)

rating = int(input("0부터 5까지 점수를 매겨주세요:  "))


## Ending

# jpg automation program
# Google Cloud API 사용해서 jpg 파일 저장 ->  link 생성
# QRCode Generator -> link embed


## ...repeat
