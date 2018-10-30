'''
Lab 8
Name: Sjaakar * ALTIN * Campbell
Class: CIS41A PYTHON
Professor: The Awesome Mrs.Clare Nguyen
Week: 8
Date 17MAR2018
Description: This program is an application that helps a user look up CIS classes.
             The app uses data from this CIS web page.
'''
import re
from course import CourseInfo


class CISclasses:
    def __init__(self):
        '''
        CISclass constructer
        Uses reg ex to capture desired information from HTML
        '''
        file = "lab8input.txt"
        listofClasses = []
        found = False
        while not found:
            try:
                with open(file) as inFile:
                    found = True
                    for line in inFile:
                        line = line.strip()
                        if re.findall("CIS\s\d+[a-zA-Z]*", line):
                            classNumber = re.search("CIS\s(\d+[A-Z]*)", line)
                            print(classNumber.group(1))
                            inFile.__next__()
                            line2 = inFile.__next__()
                            if re.search(">([A-Z].+?)<[b|/]", line2):
                                className = re.findall(">([A-Z].+?)<[b|/]", line2)
                                inFile.__next__()
                                line3 = inFile.__next__()
                                fall = True if re.search(">(x)<", line3) else False
                                inFile.__next__()
                                line4 = inFile.__next__()
                                winter = True if re.search(">(x)<", line4) else False
                                inFile.__next__()
                                line5 = inFile.__next__()
                                spring = True if re.search(">(x)<", line5) else False
                                inFile.__next__()
                                line6 = inFile.__next__()
                                summer = True if re.search(">(x)<", line6) else False
                                if len(className) > 1:
                                    cisCourse = CourseInfo(classNumber.group(1), className[0], className[1], fall, winter,
                                                           spring, summer)
                                else:
                                    cisCourse = CourseInfo(classNumber.group(1), className[0], "", fall, winter,
                                                           spring, summer)
                                listofClasses.append(cisCourse) #!!!!!! This is the only CHANGE
                self._tupleOfClasses = tuple(listofClasses)
                print(self._tupleOfClasses)
                del listofClasses
            except FileNotFoundError:
                print(file, "not found")
                file = input("Please enter a file name: ")
                if ".txt" not in file:
                    file += ".txt"


    def getTupleofClasses(self):
        '''
        access function
        :return: the tuple of classes
        '''
        return self._tupleOfClasses

    def searchByNumber(self, classNumber):
        '''
        searches the tuple for class number
        :param classNumber: number associated with the course
        prints result
        :return: None
        '''
        found = False
        for item in self._tupleOfClasses:
            #print(item, ":", classNumber)
            if classNumber == item.getclassNum():
                print(item, end="")
                if item.printAllQtr() == "":
                    print()
                else:
                    print(":", item.printAllQtr())
                found = True
        if not found:
            print("There is no class with this Number")

    def searchByTopic(self, topic):
        '''
        searches the tuple by and input string (if the string contains special characters regex is used
        prints result
        :param topic: user input
        :return: None
        '''
        found = False
        catchC = "C"
        topic = topic.title()
        myRegex = "\\b(" + topic + ")\\b"
        # if re.search(myRegex, item.getclassName().title()):
        for item in sorted(self._tupleOfClasses):
            if re.search("[+.#]+", topic):
                if topic in item.getclassName().title():
                    print(item)
                    found = True
            elif topic == "C":
                if "C " in item.getclassName():
                    print(item)
                    found = True
            else:
                if re.search(myRegex, item.getclassName().title()):
                    print(item)
                    found = True
        if not found:
            print("There are no classes with this topic")

    def searchByTopicQuarter(self, topic, qtr):
        '''
        searches by both topic and qtr
        prints result
        :param topic: string searched for
        :param qtr: Qtr that the class is offered
        :return: None
        '''
        found = False
        topic = topic.title()
        qtr = qtr.title()
        myRegex = "\\b(" + topic + ")\\b"
        for item in sorted(self._tupleOfClasses):
            if re.search("[+.#]+", topic):
                if topic in item.getclassName().title() and qtr in item.getAllQtr():
                    print(item)
                    found = True
            elif topic == "C":
                if "C " in item.getclassName() and qtr in item.getAllQtr():
                    print(item)
                    found = True
            else:
                if re.search(myRegex, item.getclassName().title()) and qtr in item.getAllQtr():
                    print(item)
                    found = True
        if not found:
            print("There are no classes that match this search")


