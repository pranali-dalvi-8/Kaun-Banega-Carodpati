questions=[
    [
        "which language is used to  developed fb?","python","java","javascript","php",4
    ],
    [
        "Which one is the first search engine in internet?", "Google","Archie", "Altavista","WAIS", 2
    ],
    [
        "Which one is the first web browser invented in 1990?", "Internet Explorer", "Mosaic", "Mozilla","Nexus", 4
    ],
    [
        "Which of the following programming language is used to create programs like applets?", "cobol", "c", "java","basic", 3
    ],
    [
         "First computer virus is known as ","rabbit","creeper virus" ,"ALP cloner","sca",2
    ],
    [
        "Which one programming language is exclusively used for artificial intelligence?","c","java","j2ee","prolog",4
    ],
    [
        "Firewall in computer is used for ","security","data transmission","authentication","monitoring",1
    ],
    [
        "Which of the following is not an operating system?","dos","mac","c","linux",3
    ],
    [
        "Which of the following is not a database management software?","mysql","oracle","sybase","cobol",4
    ],
    [
      "Number of layers in the OSI Model","9","7","4","5",2
    ],
    [
        "Mac Operating System is developed by which company","IBM","microsoft","apple","samsung",3
    ],
    [
        "Where is the headquter of Microsoft office located","texas","new york","california","washington",4
    ],
    [
        ".gif is an extension of","image","vedio","audio","word",1
    ],
    [
        "Computer Hard Disk was first introduced in 1956 by","dell","apple","microsoft","IBM",4
    ],
]
levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,850000,900000,10000000]
money=0
for i in range(0,len(questions)):
    question=questions[i]
    print(f"\n\nquestion for RS.{(levels[i])}")
    print(f"{(question[0])}")
    print(f"A.{(question[1])}           B.{(question[2])}")
    print(f"C.{(question[3])}           D.{(question[4])}")
    reply=int(input("Enter Your Answer Beetween (1-4) and if you want quit enter (0) : "))
    if (reply == 0):
        break
    if(reply==question[-1]):
        print(f" Congrats!! You Answer Is Correct..")

        if(i==4):
            money=10000
        elif(i==9):
            money=320000
        elif(i==14) :
            money=10000000
    else:
        print("Best Luck For Next Time !! You Answer Is Wrong")

print(f"Your Take Home Money Is {(money)}")