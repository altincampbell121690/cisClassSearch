'''
Console UI for class search
Name: Sjaakar * ALTIN * Campbell
Date 17MAR2018
Description: This program is an application that helps a user look up CIS classes.
             The app uses data from this CIS web page.
'''

from cisclasses import CISclasses
'''
In this lab I used three classes UI, CIS classes, course info.
UI: contains all of the functions/methods used to search the course database
CIS classes: uses regex to capture all of the data needed to instantiate a courseinfo object and the methods to search
    all instantiated courseinfo objects will be stored in a tuple because there will be no need to change that data
Course Info: is where all of the major data is store.  
'''

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
        #print("***in Switch 2***")
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
        #print(choice)
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
