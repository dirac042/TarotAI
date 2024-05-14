## Importing Libraries
import random
import time
import sys
import os
import datetime
import warnings
from tarot_reader import TarotReader

warnings.filterwarnings("ignore")

def input_exit(message):
    user_input = input(message)
    if message == "brains":
        sys.exit()
    return user_input

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


## Importing Classes
from opening import OpeningMessage
from PandasToList import PandasToList
from cards import cards
from pdf_converter import PDF
from emailsender import EmailSender
from secret import sender_email, password  # .gitIgnore에 추가됨.

email_sender = EmailSender(sender_email, password)

while True:

    ## Language Setting

    clear_screen()
    lang = print("Language:  \n\n1. English  \n2. 한국어  \n")


    def get_valid_input_lang(prompt):
        while True:
            try:
                value = int(input_exit(prompt))
                if value == 1 or value == 2:
                    return value
                else:
                    print(f"\nTry Again.")
            except ValueError:
                print("\nTry again.")


    lang = get_valid_input_lang("Choose your Language (1, 2):  ")

    if lang == 1:
        delay_num = 0.01
    else:
        delay_num = 0.01  # 텍스트 딜레이 (0에 가까울수록 빨라짐)

    # if lang = 1 -> English
    # if lang = 2 -> Korean


    def print_lang(eng, kor):
        if lang == 1:
            print(eng)
        else:
            print(kor)


    ## Before the Execution (String file)
    clear_screen()
    print_lang("Before we start...  \n", "시작하기 전에...  \n")
    m = OpeningMessage()
    if lang == 1:
        m.__init__(filename="BeforetheExecution_Eng.txt")
    else:
        m.__init__(filename="BeforetheExecution.txt")
    print(m.open_file())
    m.open_file()
    if lang == 1:
        open_after = input_exit("Press Enter to continue.  \n")
    else:
        open_after = input_exit("계속하려면 Enter 키를 누르세요.  \n")
    open_after
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
    if lang == 1:
        slow_type(
        """
Hey there! I'm TarotAI, an AI that can show you a glimpse of your future.

I know school life can be tough, so thanks for taking the time to come and get a reading.

Before we start, tell me your name. It can be a nickname, no need for your real name.
""",
        delay_num,
    )
    else:
        slow_type(
        """

안녕? 나는 오늘 너에게 잠깐이나마 미래를 보여줄 인공지능 TarotAI야.

학교생활 많이 힘들지? 이렇게 시간 내서 점 보러 와줘서 고마워. 

시작하기 전에, 네 이름을 알려줘. 진짜 이름 말고, 가명으로 적어도 돼.

""",
        delay_num,
    )
    if lang == 1:
        name = input_exit("Write your name (nickname):  ")
    else:
        name = input_exit("이름(가명)을 적어줘:  ")

## Concern
    clear_screen()
    print("================================================================")
    if lang == 1:
        slow_type(f"\nNice to meet you, {name}!  I'm glad you're here!", delay_num)
        slow_type(
        """
Now, tell me your concern.

You can ask me about your fortune for a specific period, like 'How's my luck today?' or

you can write about a specific problem, like 'I'm not studying well these days' or 'Can I date someone?'.
""",
        delay_num,
    )
    else:
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

    if lang == 1:
        reader.korean = False
    else:
        reader.korean = True


    if lang == 1:
        concern = input_exit("What's your concern?  \n\nConcern:  ")
        while True:
            concern_true = input_exit(f"Is this your concern? (Y / n):\n\n{concern}\n\n")
            if concern_true in ["Y", "y"]:
                break
            elif concern_true == "n":
                print("\n")
                concern = input_exit("Is this your concern? \n\nConcern:  ")
    else:
        concern = input_exit("너의 고민은 뭐니? \n\n고민:  ")
        while True:
            concern_true = input_exit(f"이 고민이 맞니? (Y / n):\n\n{concern}\n\n")
            if concern_true == "Y":
                break
            elif concern_true == "n":
                print("\n")
                concern = input_exit("너의 고민은 뭐니? \n\n고민:  ")
        
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
    if lang == 1:
        slow_type(
        f"""
Great! Now, let's pick some cards, shall we?
I'm going to draw a total of {card_num} cards from now on.

{card_num_desc}

Got it? If you don't understand, I'll explain it to you again when interpreting the cards.
""",
        delay_num,
    )
    else:
        slow_type(
        f"""
좋아,  그럼 이제 카드를 뽑아볼까? 
지금부터 총 {card_num}개의 카드를 뽑을거야.

{card_num_desc}

이해했어?  잘 모르겠으면 카드를 해석할 때  다시 알려줄게.

""",
        delay_num,
    )

    if lang == 1:
        next = input_exit("Press Enter to continue.  \n")
    else:
        next = input_exit("계속하려면 Enter를 누르세요.\n")

    ## Card Selection

    list_tarot_deck = list_up_tarot + list_rev_tarot
    list_tarot_deck_mixed = list_tarot_deck[:]
    random.shuffle(list_tarot_deck_mixed)

    clear_screen()
    print("===================================================================")
    if lang == 1:
        slow_type(
        """
Alright,  let's draw the cards now.

Since I'm an AI, I can't show you how I shuffle the cards,
so tell me the number of the card you want to draw.

Calm your mind and write down the number of the card you want to draw from the top.
    
""",
        delay_num,
    )
    else:
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
    def get_valid_input_exit(prompt, max_value):
        while True:
            try:
                value = int(input_exit(prompt))
                if 0 <= value <= max_value:
                    return value
                else:
                    if lang == 1:
                        print(
                            f"\nPlease enter a number between 0 and {max_value}. Try again."
                        )
                    else:
                        print(
                            f"\n숫자는 0부터 {max_value} 사이로 입력해야 해요. 다시 시도해주세요."
                        )
            except ValueError:
                if lang == 1:
                    print("\nPlease enter a valid number.")
                else:
                    print("\n유효한 숫자를 입력해주세요.")


    if lang == 1:
        first_card = get_valid_input_exit(
        "Write down the number of the card you want to draw (from 0 to 43): ", 43
    )
    else:
        first_card = get_valid_input_exit("0부터 43까지의 수를 적으세요: ", 43)
    first_card

    if card_num == 3:
        if lang == 1:
            slow_type(
            "\nI've drawn the first card. Now, let's draw the next card.", delay_num
        )
            second_card = get_valid_input_exit(
            "Write down the number of the card you want to draw (from 0 to 42): ", 42
        )
        else:
            slow_type("\n첫번째 카드를 뽑았어,  그럼 다음 카드를 뽑아볼까?", delay_num)
            second_card = get_valid_input_exit("0부터 42까지의 수를 적으세요: ", 42)
        second_card

        if lang == 1:
            slow_type(
            "\nI've drawn the second card. Now, let's draw the last card.", delay_num
        )
            third_card = get_valid_input_exit(
            "Write down the number of the card you want to draw (from 0 to 41): ", 41
        )
        else:
            slow_type("\n이제 마지막으로 세번째 카드를 뽑아보자.", delay_num)
            third_card = get_valid_input_exit("0부터 41까지의 수를 적으세요: ", 41)

    ## Card Loading (string)
    clear_screen()
    print("================================================================")
    if lang == 1:
        slow_type(
        """
Great! Now, let's look at the cards one by one and get a glimpse of the future!
Are you ready?
""",
        delay_num,
    )
    else:
        slow_type(
        """
잘했어!
이제 카드를 하나씩 살펴보면서 미래를 살짝 엿보도록 하자!
준비됐어?
""",
        delay_num,
    )

    if lang == 1:
        next2 = input_exit("Press Enter to continue.  \n")
    else:
        next2 = input_exit("계속하려면 Enter를 누르세요  \n")

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

    if lang == 1:
        slow_type(
        f"""
The first card you drew is {first_tarot_card[0]}.

{interpretation_word_first}

{interpretation_concern_first}

""",
        delay_num,
    )
    else:
        slow_type(
        f"""
너가 처음으로 뽑은 카드는 {first_tarot_card[1]} (이)야. 

{interpretation_word_first}

{interpretation_concern_first}

""",
        delay_num,
    )

    if lang == 1:
        next3 = input_exit("Press Enter to continue.  \n")
    else:
        next3 = input_exit("계속하려면 Enter 키를 눌러주세요  \n")

    if card_num == 3:
        for n in range(len(list_tarot_deck_mixed)):
            if second_tarot_card[0] == cards[n]["name"]:
                second_tarot_card_ascii = cards[n]["card"]

        for n in range(len(list_tarot_deck_mixed)):
            if third_tarot_card[0] == cards[n]["name"]:
                third_tarot_card_ascii = cards[n]["card"]

        reader.set_meaning_by_idx(1)
        reader.set_interpretation_by_idx(1)
        interpretations = reader.cards
        interpretation_word_second = interpretations[1]["meaning"]
        interpretation_concern_second = interpretations[1]["interpretation"]

        clear_screen()
        print(second_tarot_card_ascii + "\n")
        if lang == 1:
            slow_type(
            f"""
The second card you drew is {second_tarot_card[0]}.

{interpretation_word_second}

{interpretation_concern_second}

""",
            delay_num,
        )
        else:
            slow_type(
            f"""
너가 두번째로 뽑은 카드는 {second_tarot_card[1]} (이)야.

{interpretation_word_second}

{interpretation_concern_second}

""",
            delay_num,
        )
        if lang == 1:
            next3 = input_exit("Press Enter to continue.  \n")
        else:
            next3 = input_exit("계속하려면 Enter 키를 눌러주세요  \n")

        reader.set_meaning_by_idx(2)
        reader.set_interpretation_by_idx(2)
        interpretations = reader.cards
        interpretation_word_third = interpretations[2]["meaning"]
        interpretation_concern_third = interpretations[2]["interpretation"]
        interpretations = reader.cards
        clear_screen()
        print(third_tarot_card_ascii + "\n")
        if lang == 1:
            slow_type(
            f"""
The third card you drew is {third_tarot_card[0]}.

{interpretation_word_third}

{interpretation_concern_third}

""",
            delay_num,
        )
        else:
            slow_type(
            f"""
너가 세번째로 뽑은 카드는 {third_tarot_card[1]} (이)야.

{interpretation_word_third}

{interpretation_concern_third}

""",
            delay_num,
        )
        if lang == 1:
            next3 = input_exit("Press Enter to continue.  \n")
        else:
            next3 = input_exit("계속하려면 Enter 키를 눌러주세요  \n")

# ---- debugging ----------------------


    reader.set_interpretation_overall()
    interpretation_overall = reader.interpretation_overall
    clear_screen()
    print("================================================================")
    if lang == 1:
        slow_type(
        f"""
To summarize the results,

{interpretation_overall}

""",
        delay_num,
    )
    else:
        slow_type(
        f"""
결과를 요약해보면,

{interpretation_overall}

""",
        delay_num,
    )
    if lang == 1:
        next3 = input_exit("Press Enter to continue.  \n")
    else:
        next3 = input_exit("계속하려면 Enter 키를 눌러주세요  \n")

    ## Rating (strings)
    clear_screen()
    print("================================================================")

    if lang == 1:
        slow_type(
        f"""

This is all I've seen of your future.
How was it? I hope you liked the results.
    
    """,
        delay_num,
    )
    else:
        slow_type(
        f"""

여기까지가 내가 본 미래의 전부야.  
어땠어?  결과가 마음에 들었으면 좋겠네.  

""",
        delay_num,
    )

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

    print()
    ## Ending
    if lang == 1:
        slow_type(
        f"""
It's time to say goodbye.

Oh, can I have your email address before you go?

I'll summarize the results of today's reading into a pdf file and send it to you by email!
    
    """,
        delay_num,
    )
    else:
        slow_type(
        f"""
이제 헤어질  시간이야.

아 참, 가기 전에 이메일 주소 알려줄 수 있을까? 

오늘 본 점의 결과를 pdf 파일로 정리해서 이메일로 보내줄게!

""",
        delay_num,
    )

    while True:
        try:
            if lang == 1:
                email = input_exit("Write down your email address:  ")
                email_confirm = input_exit(f"Is {email} your email address?  (Y/N): ")
            else:
                email = input_exit("이메일 주소를 적어주세요:  ")
                email_confirm = input_exit(f"{email}    이게 너의 이메일 주소가 맞아?  (Y/N): ")

            if email_confirm == "Y" or email_confirm == "y":
                break
        except:
            pass

    # ------------------------------- email 보내기
    receiver_email = email
    result_pdf = f"{name}_TarotAI_Result.pdf"
    if lang == 1:
        subject = f"TarotAI Result for {name}"
        body = f"""
    Hey,  {name}!

    Hello!  Thanks for coming to see the tarot today!
    I've made the tarot results into a pdf, so check the attached file.
    Well then,  goodbye!

    TarotAI
    """
    else:
        subject = "정바융 Merge TarotAI 결과"
        body = f"""
    {name}에게,

    안녕,  {name}! 
    오늘 타로 보러 와줘서 다시 한 번 고마워!
    타로 결과를 pdf로 만들어봤으니,  첨부파일을 확인해봐.
    그럼,  안녕!

    TarotAI 올림.
    """
    if lang == 1:
        print("Sending an email...  \n")
    else:
        print("이메일 보내는 중...  \n")
    email_sender.send_email(receiver_email, subject, body, result_pdf)

    #  -------------------------------------------

    clear_screen()
    print("===============================================================")
    if lang == 1:
        slow_type(
        f"""
{receiver_email}
I sent an email to this address!  Be sure to check it later!

I'm still learning about tarot, so I won't receive any money from you.
Don't forget to get a stamp at the booth before you go!

Thanks for coming.  Let's see each other again next time.  Goodbye!

""",
        delay_num,
    )
    else:
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

    if lang == 1:
        next5 = input_exit("Press Enter to end.  Thank you.")
    else:
        next5 = input_exit("끝내려면 Enter 키를 눌러주세요.  감사합니다.")
    clear_screen()
    time.sleep(5)