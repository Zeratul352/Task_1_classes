# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from enum import Enum
import uuid
import random

class Status(Enum):
    Available = 1
    Borrowed = 2
    Restauration = 3
    Lost = 4

class Genre(Enum):
    Fantastic = 1
    Adventure = 2
    Detective = 3
    Travels = 4


class Data_storage():

    def __init__(self, name, status, genre):
        #self.__serial_number = uuid.uuid4()
        self.__serial_number = random.randint(0, 100000)
        self.__name = name
        if not isinstance(status, Status):
            raise ValueError("Unknown object status")
        if not isinstance(genre, Genre):
            raise ValueError("Unknown object genre")
        self.__status = status
        self.__genre = genre

    @property
    def serial_number(self):
        return self.__serial_number

    @property
    def name(self):
        return self.__name

    @property
    def status(self):
        return self.__status

    @property
    def genre(self):
        return self.__genre

    def __repr__(self):
        return f"Name: {self.__name}, Genre: {self.__genre}, Status: {self.__status}, Serial_number: {self.__serial_number}"


class Book(Data_storage):

    def __init__(self, name, status, genre, author, publisher, issue_year):
        Data_storage.__init__(self, name, status, genre)
        self.__author = author
        self.__publisher = publisher
        self.__issue_year = issue_year


    @property
    def author(self):
        return self.__author

    @property
    def publisher(self):
        return self.__publisher

    @property
    def issue_year(self):
        return self.__issue_year

    def __repr__(self):
        return f"Name: {self.name}, Genre: {self.genre}, Status: {self.status}, Author: {self.author}, Publisher: {self.publisher}, Issue_year: {self.issue_year}, Serial_number: {self.serial_number}"


class Journal(Data_storage):
    def __init__(self, name, status, genre, issue_month):
        Data_storage.__init__(self, name, status, genre)
        self.__issue_month = issue_month

    @property
    def issue_month(self):
        return self.__issue_month

    def __repr__(self):
        return f"Name: {self.name}, Genre: {self.genre}, Status: {self.status}, Issue_month: {self.issue_month}, Serial_number: {self.serial_number}"

class DVD(Data_storage):
    def __init__(self, name, status, genre, lenght):
        Data_storage.__init__(self, name, status, genre)
        self.__length = lenght

    @property
    def length(self):
        return self.__length

    def __repr__(self):
        return f"Name: {self.name}, Genre: {self.genre}, Status: {self.status}, Lenght: {self.length}, Serial_number: {self.serial_number}"

def Print_menu():
    print("Available commands:")
    print("1 : Add Data_storage")
    print("2 : Add Book")
    print("3 : Add Journal")
    print("4 : Add DVD")
    print("5 : Print library")
    print("6 : Find name with id")
    print("7 : Find status with id")
    print("8 : Exit library")
    print("9 : Repeat this list")



def Library():
    Print_menu()
    command = 0
    library = []
    while command != 8:

        try:
            print("Please enter command:")
            command = int(input())
            if command == 1 or command == 2 or command == 3 or command == 4:
                print("Enter name, status, genre")
                name = str(input())
                status = int(input())
                genre = int(input())
                if command == 1:
                    library.append(Data_storage(name, Status(status), Genre(genre)))
                if command == 2:
                    print("Enter author, publisher, issue_year")
                    author = str(input())
                    publisher = str(input())
                    issue_year = str(input())
                    library.append(Book(name, Status(status), Genre(genre), author, publisher, issue_year))
                if command == 3:
                    print("Enter issue month")
                    month = input()
                    library.append(Journal(name, Status(status), Genre(genre), month))
                if command == 4:
                    print("Enter dvd length")
                    length = input()
                    library.append(DVD(name, Status(status), Genre(genre), length))

            if command == 5:
                if len(library) == 0:
                    print("Library is empty!")
                else:
                    for storage in library:
                        print(storage)
            if command == 6 or command == 7:
                if len(library) == 0:
                    print("Nowhere to search, library is empty")
                    continue
                print("Enter ID")
                serial = int(input())
                for storage in library:
                    if serial == storage.serial_number:
                        if command == 6:
                            print(f"Status: {storage.status}")
                        if command == 7:
                            print(f"Genre: {storage.genre}")
            if command == 8:
                break
            if command == 9:
                Print_menu()

        except ValueError:
            print("Unpropriate status or genre")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print(Genre(1))
    #print(Status(1))

    Library()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
