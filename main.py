## Importing Libraries


## Importing Classes


## Importing Card List (csv file)
# pd.read_csv(tarot_list.csv)


## Language Setting

# if lang = 0 -> English
# if lang = 1 -> Korean

## Before the Execution (String file)


## Starting Message

name = input("이름(가명)을 적어줘:  ")

## Concern

print(f"네 이름은 {name}이구나.  반가워!")

concern = input("너의 고민은 뭐니?  ")


## Card Selection - Info

# concern으로 카드 개수 (1 or 3) 정하기.
#  오늘의 운세를 물어보면?  1
#  그 이외의 '과거  현재  미래'가 필요한 고민이면?  3
# card_num = 1 or 3


## Card Selection

first_card = int(input("0부터 43까지의 수를 적으세요:  "))

# if card_num == 3:
# second_card = ()
# third_card = ()


## Card Loading (string)


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
