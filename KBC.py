questions=[
    "1.Which of the following elements has the highest melting point?",
    "2.The process of converting a solid directly into a gas without passing through the liquid phase is called:",
    "3.Which of the following diseases is caused by a deficiency of vitamin B12?",
    "4.The phenomenon of total internal reflection of light occurs when light travels from a medium of higher refractive index to a medium of:",
    "5.The process of converting glucose into ethanol and carbon dioxide is called:",
    "6.Which of the following is an example of an exothermic reaction?",
    "7.The pH value of a neutral solution is:",
    "8.Which of the following organs is responsible for filtering blood and producing urine in the human body?",
    "9.Which of the following particles has the smallest mass?",
    "10.The process by which green plants convert light energy into chemical energy is known as:",
    "11.Which African country is the most populous in terms of population?",
    "12.What is the chemical symbol for the element \"Lead\"?",
    "13.Who won the Nobel Prize in Literature in 2020?",
    "14.Which of the following countries is NOT a member of the G7?",
    "15.In which year did the United States land the first man on the Moon?"
]
options=[
    """
a) Carbon
b) Titanium
c) Tungsten
d) Silver
    """,
"""
a) Evaporation
b) Sublimation
c) Condensation
d) Fusion
    """,
    """
a) Rickets
b) Scurvy
c) Beriberi
d) Pernicious anemia
    """,
    """
a) Lower refractive index
b) Equal refractive index
c) Variable refractive index
d) Infinite refractive index
    """,
    """
a) Fermentation
b) Oxidation
c) Photosynthesis
d) Respiration
    """,
    """
a) Melting ice
b) Evaporating water
c) Burning wood
d) Rusting iron
    """,
    """
a) 0
b) 7
c) 14
d) -1
    """,
    """
a) Liver
b) Pancreas
c) Kidneys
d) Spleen
    """,
    """
a) Electron
b) Proton
c) Neutron
d) Alpha particle
    """,
    """
a) Photosynthesis
b) Respiration
c) Digestion
d) Combustion
    """,
    """
a) Nigeria
b) Ethiopia
c) Egypt
d) South Africa
    """,
    """
a) Ld
b) Pd
c) Le
d) Pb
    """,
    """
a) Bob Dylan
b) Alice Munro
c) Olga Tokarczuk
d) Kazuo Ishiguro
    """,
    """
a) Canada
b) Australia
c) Germany
d) Japan
    """,
    """
a) 1967
b) 1969
c) 1971
d) 1973
    """
]
correct_answers=["c) Tungsten",
"b) Sublimation",
"d) Pernicious anemia",
"a) Lower refractive index",
"a) Fermentation",
"c) Burning wood",
"b) 7",
"c) Kidneys",
"a) Electron",
"a) Photosynthesis",
"a) Nigeria",
"d) Pb",
"c) Olga Tokarczuk",
"b) Australia",
"b) 1969"
]

correct_options=["c","b","d","a","a","c","b","c","a","a","a","d","c","b","b"]

#c b d a a c b c a a a d c b b

print("Welcome to KBC!")
print("Rules for the game are-\n1.You have to choose from a,b,c,d.\n2.Press 1 to open lifelines and to see their discription.\n3.Press 2 to open quit menu.")
print("\n\n")
start=input("Press enter to start.")

points=[0,50,100,150,200,250,300,350,400,450,500,550,600,650,700,1000]

def print_ques(num):#added breaks at ques 5,10,14
        print(f"The points for the question are: {points[num+1]}\n")
        print(questions[num])
        print(options[num])
        print("Chose 1 for life lines and 2 to quit.")

def lifelines():
    print("Your lifelines are as belows-\n1.50:50-removes to wrong options.")

answers=[]
def take_answer():
    global ans
    ans=input("Enter a option: ")
    if ans == 'a' or ans == 'b' or ans == 'c' or ans == 'd' : answers.append(ans);return True
    if ans == '1': lifelines();return False
    if ans == '2': quit_game();return False

cal=[0]
def check_answers(num):
    if take_answer==True:
        if answers[num]==correct_options[num]:
            print("Correct Answer!")
            cal[0]=0
            return True
        elif answers[num]!=correct_options[num]:
            print("Wrong Answer!") 
            cal[0]=1
            print(f"Correct answer is: {correct_answers[num]}")
            return False

def calculate_points(num):
    x=0
    while num>=0:
        x += points[num]
        num-=1
    return x

#GAME FUNCTION
def quit_game(z=False) :
     if ans == "Quit" or ans == "quit" or ans == "q" or ans == "Q":
        y = None
        if temp < 5: y = 0
        if temp >= 5 and temp < 10: y = 300
        if temp >= 10 and temp < 14: y = 500
        if temp == 14: y = 700
        print("You have chosen to quit.")
        print(f"If you quit now you will get {y} points.")
        print("Are you sure you want to quit?")
        x=input("Q-Quit\nC-Continue\n")
        if x == "Quit" or x == "quit" or x == "q" or x == "Q":
            print("You have chosen to quit.")
            if y == 0 : print("Better luck next time.\nYou scored ZERO points.")
            else : print(f"Well played!!!\nYou scored {y} points.")
            cal[0]=1
            return True
        elif x == "Continue" or x == "continue" or x == "c" or x == "C":
            print("You have chosen to continue.")
            return False

def end_game():
    print(f"You scored {calculate_points} points.")

def game():
    for i in range(15):
        if cal[0]==0:
            print_ques(i)
            take_answer()
            # check_answers(i)
            if quit_game() == True : break
            # calculate_points(i)
            global temp
            temp=i
            if check_answers(i) == True : print(f"You have {points[temp+1]} points.\n") #{calculate_points(temp)}
            print('*'*30)
            if(i==14):
                print("Congratulations!!!You answers are all correct.")
                print(f"You scored {points[temp+1]} points.")                
        elif cal[0]==1:
            print("The game is over!!!")
            print(f"You scored {points[temp]} points.")
            break

game()

