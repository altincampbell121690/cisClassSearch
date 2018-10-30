class CourseInfo:
    '''
    course info class
    '''
    def __init__(self, classNum, className, className2 = "", fall=False, winter=False, spring=False, summer=False):
        '''
        course info constructor
        :param classNum: class number -String
        :param className: class name -String
        :param Optional className2: for any class names that have two lines -String
        :param Optional fall: QTR -Bool
        :param Optional winter: QTR -Bool
        :param Optional spring: QTR -Bool
        :param Optional summer: QTR -Bool
        '''
        qtrF = qtrW = qtrSp = qtrSu = ""
        if className2:
            self._className = className + " " + className2
        else:
            self._className = className
        self._classNum = classNum
        self.__qtrsOffered = 0
        if fall:
            qtrF = "Fall"
            self.__qtrsOffered += 1
        if winter:
            qtrW += "Winter"
            self.__qtrsOffered += 1
        if spring:
            qtrSp += "Spring"
            self.__qtrsOffered += 1
        if summer:
            qtrSu += "Summer"
            self.__qtrsOffered += 1
        self._Quarter = (qtrF, qtrW, qtrSp, qtrSu)


    def getclassName(self):
        '''
        access function
        :return: class name
        '''
        return str(self._className)

    def getclassNum(self):
        '''
        access function
        :return: class num
        '''
        return str(self._classNum)

    def getAllQtr(self):
        '''
        access function
        :return: Qtr tuple
        '''
        return self._Quarter

    def printAllQtr(self):
        '''
        creates a string of the qtrs that a class is offered
        :return: a string of QTR tuple
        '''
        count = self.__qtrsOffered - 1
        qtrString = ""
        for item in self._Quarter:
            qtrString += item
            if count > 0 and item:
                qtrString += ","
                count -= 1
        return qtrString

    def __repr__(self):
        '''
        :return: a string representing the object
        '''
        courseInfo = "CIS " + self._classNum + " " + self._className
        return courseInfo

    def __lt__(self, rhs):
        '''
        overloading the < operator
        :param rhs: object to be compared
        :return: bool
        '''
        return self._className < rhs.getclassName()

