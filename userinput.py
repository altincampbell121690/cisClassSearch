from LABS.Lab8.cisclasses import CISclasses


class UI:
    '''
    UI constructor
    '''
    def __init__(self):
        self._classList = CISclasses()
        self.switchCase = {1: self.case1,
                           2: self.case2,
                           3: self.case3}

    def case1(self):
        '''
        switch case 1:
            calls search by numbers
        :return: None
        '''
        print()
        classNumber = input("Enter a class number: ")
        self._classList.searchByNumber(classNumber.upper())
        print()

    def case2(self):
        '''
        switch case 2:
            calls search by topic
        '''
        print("***in Switch 2***")
        print()
        topic = input("Enter a CIS topic: ")
        self._classList.searchByTopic(topic.title())
        print()

    def case3(self):
        '''
        switch case 3:
            calls search by topic and Qtr
        '''
        print()
        topic = input("Enter a CIS topic: ")
        topic = topic.title()
        qtr = input("Enter a quarter: ")
        qtr = qtr.title()
        while qtr != "Fall" and qtr != "Winter" and qtr != "Spring" and qtr != "Summer":
            qtr = input("Please enter Fall, Winter, Spring or Summer: ")
            qtr = qtr.title()
        self._classList.searchByTopicQuarter(topic, qtr)
        print()

    def displayMenu(self):
        '''
        Provides the user witha menu that calls all the functions needed to search for classes
        :return: None
        '''
        choice = None
        print(choice)
        while choice != 4:
            print("1. Search by class number")
            print("2. Search by topic")
            print("3. Search by topic and quarter")
            print("4. End search")
            try:
                choice = int(input("Enter a number: "))
            except ValueError:
                print(choice, "is not a number. Please try again.")
            try:
                self.switchCase[choice]()
            except KeyError:
                if choice != 4:
                    print(choice, "must be a number between 1 and 4")
                else:
                    print("Thank you for searching with us")

    def run(self):
        '''
        starts the program
        :return: None
        '''
        self.displayMenu()


app = UI()
app.run()
