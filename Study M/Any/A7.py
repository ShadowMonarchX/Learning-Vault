class CollegeQueue:
    def __init__(self, a):
        self.size = a
        self.front = 0
        self.rear = -1
        self.array = [None] * self.size

    def add(self, data):
        if self.rear < self.size - 1:
            self.rear += 1
            self.array[self.rear] = data
        else:
            print("Queue is full. Cannot enqueue", data)

    def display(self):
        print("* * * * * *    COLLEGES    * * * * * *")
        for i in range(self.front, self.rear + 1):
            print(f"{i + 1}).{self.array[i]}")


class ChoiceCollege:
    def __init__(self, a):
        self.size = a
        self.front = 0
        self.rear = -1
        self.array = [None] * self.size

    def add(self, data):
        if self.rear < self.size - 1:
            self.rear += 1
            self.array[self.rear] = data
        else:
            print("~~~~~~~~~ YOU ENTER ALL COLLEGES NOW YOU CAN'T ENTER MORE  ~~~~~~~~~")

    def display(self):
        for i in range(self.front, self.rear + 1):
            print(f"{i + 1}).{self.array[i]}")


class ChoiceCollege1:
    def __init__(self, a):
        self.size = a
        self.front = 0
        self.rear = -1
        self.array = [None] * self.size

    def add(self, data):
        if self.rear < self.size - 1:
            self.rear += 1
            self.array[self.rear] = data
        else:
            print("~~~~~~~~~ YOU ENTER ALL COLLEGES NOW YOU CAN'T ENTER MORE  ~~~~~~~~~")

    def display(self):
        for i in range(self.front, self.rear + 1):
            print(f"{i + 1}).{self.array[i]}")


class Student:
    def __init__(self):
        print(" ______________________________________________")
        print("|                                              |")
        print("|                   WELCOME                    |")
        print("|               ADMISSION SYSTEM               |")
        print("|                                              |")
        print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


class Default:
    def __init__(self):
        rank = 0
        q = CollegeQueue(10)
        q.add("LD")
        q.add("DDU")
        q.add("BVM")
        q.add("ADANI")
        q.add("GH")
        q.add("NIRMA")
        q.add("LJ")
        q.add("PDEU")
        q.add("PARUL")
        q.add("SAL")

        college_rank = [500, 1000, 1500, 2000, 2200, 2500, 3000, 3500, 4000, 4500]

        print("ENTER YOUR RANK = ", end="")
        rank = int(input())
        print()

        print("__________________________________________________")
        print("====== IF YOU WANT TO GO FOR CHOICE FILLING ======")
        print("==             PRESS 1 FOR CONTINUE             ==")
        print("==         OR PRESS ANY NUMBER FOR EXIT         ==")
        print()
        ch = int(input())
        c = ChoiceCollege(10)
        c1 = ChoiceCollege1(10)

        if ch == 1:
            print()
            q.display()
            print()

            print("****  YOU HAVE TO ENTER MORE THAN 1 CHOICE  ****")
            print()
            for i in range(10):
                print("ENTER COLLEGE NAME (PRESS 'QUIET' FOR EXIT) = ", end="")
                s = input()
                if s.lower() == "quiet":
                    break
                c.add(s)

            print()
            print("-------------------------------------")
            print("|    SUCCESSFULLY CHOICE FILLING    |")
            print("-------------------------------------")
            print()

            print("=====  YOUR COLLEGE CHOICES  =====")
            c.display()
            print()
        else:
            exit()

        a = q.array
        b = c.array
        count = 0
        count1 = len(b)
        k = 0
        for j in range(count1):
            for i in range(len(a)):
                if a[i].lower() != b[j].lower():
                    count += 1
                if a[i].lower() == b[j].lower():
                    break
            if count < 10:
                d = college_rank[count]
                if d == rank or d > rank:
                    k = 1
                    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                    print("|               CONGRATULATIONS                 |")
                    print(f"|           {a[count]} COLLEGE ALLOTTED TO YOU")
                    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                    print()
                    break

        if k == 0:
            print("===============================================================")
            print("|                           SORRY                             |")
            print("|  YOU ARE NOT ELIGIBLE FOR ANY COLLEGE ACCORDING TO YOUR CHOICE  |")
            print("===============================================================")

        print()
        print()
        print(" =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("|                                                              |")
        print("|     1).Press 1 for confirm your admission :                  |")
        print("|     2).Press 2 for book admission and go for the last round :    |")
        print("|     3).Press 3 for cancel admission and exit :               |")
        print("|                                                              |")
        print(" =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print()
        print("~~~~~ ENTER YOUR CHOICE = ", end="")
        ch1 = int(input())
        pin = 1234
        payment = 0
        if ch1 == 1:
            if k == 1:
                print()
                print("-------- PLEASE : PAY 20000 --------")
                payment = Payment(pin)
                print("<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>")
                print("||                                      ||")
                print("||   FINALLY YOUR ADMISSION CONFIRM IN  ||")
                print(f"                 {a[count]}             ")
                print("||                                      ||")
                print("<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>")
                exit()
            else:
                print("===== SORRY : COLLEGE NOT ALLOTTED TO YOU =====")
                exit()

        elif ch1 == 2:
            print()
            print()
            print("======= WELCOME TO THE LAST ROUND =======")
            print(
                "======= NOTICE : FURTHER " + a[count] + " COLLEGE ALLOTTED TO YOU ======="
            )
            print(
                "======= NOTICE : IF YOU HAVE ALLOTTED A NEW COLLEGE, THEN THE OLD COLLEGE WILL BE REMOVED  ======="
            )
            print()
            q.display()
            print()

            print("****  YOU HAVE TO ENTER MORE THAN 1 CHOICE  ****")
            print()
            for i in range(10):
                print("ENTER COLLEGE NAME (PRESS 'QUIET' FOR EXIT) = ", end="")
                s = input()
                if s.lower() == "quiet":
                    break
                c1.add(s)

            print()
            print("-------------------------------------")
            print("|    SUCCESSFULLY CHOICE FILLING    |")
            print("-------------------------------------")
            print()

            print("=====  YOUR COLLEGE CHOICES  =====")
            c1.display()
            print()

            a1 = q.array
            b1 = c1.array
            count3 = len(b1)
            k1 = 0
            for j in range(count3):
                count2 = 0
                for i in range(len(a1)):
                    if a1[i].lower() == b1[j].lower():
                        break
                    count2 += 1
                if count2 < 10:
                    d = college_rank[count2]
                    if d == rank or d > rank:
                        k1 = 1
                        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                        print("|               CONGRATULATIONS                 |")
                        print(f"|           {a1[count2]} COLLEGE ALLOTTED TO YOU")
                        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

                        print()
                        print("*****  PRESS 1 FOR CONFIRM NEW ADMISSION  *****")
                        o = int(input())
                        if o == 1:
                            payment = Payment(pin)
                            print()
                            print("<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>")
                            print("||                                      ||")
                            print("||   FINALLY YOUR ADMISSION CONFIRM IN  ||")
                            print(f"                 {a1[count2]}             ")
                            print("||                                      ||")
                            print("<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>")
                            exit()
                        break

            if k1 == 0:
                print("===============================================================")
                print("|                           SORRY                             |")
                print("|  YOU ARE NOT ELIGIBLE FOR ANY COLLEGE ACCORDING TO YOUR CHOICE  |")
                print("===============================================================")

                if k == 1:
                    print()
                    print("*****  PRESS 1 FOR CONFIRM YOUR OLD ADMISSION  *****")
                    ch3 = int(input())
                    if ch3 == 1:
                        payment = Payment(pin)
                        print()
                        print("<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>")
                        print("||                                      ||")
                        print("||   FINALLY YOUR ADMISSION CONFIRM IN  ||")
                        print(f"                 {a[count]}             ")
                        print("||                                      ||")
                        print("<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>")
                        exit()
                else:
                    exit()
        elif ch1 == 3:
            print()
            print(" +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            print("|                                             |")
            print("|            YOUR ADMISSION CANCEL            |")
            print("|       THANK YOU FOR USING OUR SYSTEM        |")
            print("|                                             |")
            print(" +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            exit()
        else:
            print("++++ SORRY : I CAN'T FIND YOUR CHOICE,")
            print("             PLEASE ENTER THE RIGHT CHOICE ")


def Payment(pin):
    while True:
        print("~~~~ ENTER PIN = ", end="")
        i = int(input())
        if i == pin:
            print("=========================")
            print("|    PAYMENT SUCCESS    |")
            print("=========================")
            print()
            return
        else:
            print("....... ENTER THE RIGHT PIN .......")


class Admission:
    def __init__(self):
        s = Student()
        d = Default()


if __name__ == "__main__":
    Admission()