# Written by *** for COMP9021

# Defines a class Building that defines a few special methods,
# as well as the two methods:
# - go_to_floor_from_entry()
# - leave_floor_from_entry()
# and an atribute, number_created, to keep track of
# the number of Building objects that have been created.
#
# Also defines a function compare_occupancies() meant to take
# as arguments two Building objects.
#
# Building objects are created with statements of the form
# Building(height, entries) where height is a positive integer
# (possibly equal to 0) and entries is a nonempty string that
# denotes all access doors to the building, with at least
# one space within the string to separate entries.
# You can assume that height and entries are as expected.
#
# If building denotes a Building object, then
# building.go_to_floor_from_entry(floor, entry, nb_of_people)
# takes as argument an integer, a string, and an integer.
# An error of type BuildingError is raised,
# all with the same message, if:
# - floor is not between 0 and the building's height, or
# - entry is not one of the building's entries, or
# - nb_of_people is not strictly positive.
# If the lift at that entry has to go down,
# then by how many floors it has to go down is printed out.
#
# If building denotes a Building object, then
# building.leave_floor_from_entry(floor, entry, nb_of_people)
# takes as argument an integer, a string, and an integer.
# An error of type BuildingError is raised if:
# - floor is not between 0 and the building's height, or
# - entry is not one of the building's entries, or
# - nb_of_people is not strictly positive, or
# - there are not at least nb_of_people on that floor.
# The same error message is used for the first 3 issues,
# and another error message is used for the last issue.
# If the lift at that entry has to go up or down, then
# by how many floors it has to go up or down is printed out.
#
# For the description of objects and for the number of floors
# to go up or down, use "1 floor..." or "n floors..." for n > 1.


# DEFINE AN ERROR CLASS HERE

class BuildingError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class Building:
    number_created = 0

    # 构造函数
    def __init__(self, height, entries):
        self.height = height
        self.entries = entries
        Building.number_created += 1
        self.recent_floor = 0
        self.sum = 0


        # floor & entry. Record the number of ppl on each floor.
        self.mylist = []
        self.people_each_floor = []
        for n in range(height + 1):
            for m in entries.replace(" ", ""):
                self.mylist.append(str(n) + m)
                self.people_each_floor.append(0)

    def __repr__(self):
        return (f"Building({self.height}, '{self.entries}')")

    def __str__(self):
        list = ""
        index = 0
        for i in self.entries:
            if index % 2 == 0 and index != (len(self.entries) - 1):
                list = list + i + "," + " "
            index += 1
        list = list + i

        return (f"Building with {self.height + 1} floors accessible from entries: {list}")

    def go_to_floor_from_entry(self, floor, entry, nb_of_people):
        self.floor = floor
        self.entry = entry
        self.nb_of_people = nb_of_people

        if not 0 <= floor <= self.height:
            raise BuildingError("That makes no sense!")
        if not entry in self.entries:
            raise BuildingError("That makes no sense!")
        if nb_of_people <= 0:
            raise BuildingError("That makes no sense!")


        else:
            # record the number of ppl on each floor in the list.
            # people_each_floor[index] = number of people on each floor
            index = self.mylist.index(str(floor) + entry)
            self.people_each_floor[index] += self.nb_of_people
            self.sum += self.nb_of_people

            if self.recent_floor != 0:
                print(f"Wait, lift has to go down {self.recent_floor} floors...")
            # record the position of the elevator.
            self.recent_floor = floor


    def leave_floor_from_entry(self, floor, entry, nb_of_people):

        self.floor = floor
        self.entry = entry
        self.nb_of_people = nb_of_people
        index = self.mylist.index(str(floor) + entry)

        if not 0 <= floor <= self.height:
            raise BuildingError("That makes no sense!")
        if not entry in self.entries:
            raise BuildingError("That makes no sense!")
        if nb_of_people <= 0:
            raise BuildingError("That makes no sense!")
        if self.people_each_floor[index] < nb_of_people:
            raise BuildingError("There aren't that many people on that floor!")

        else:
            self.people_each_floor[index] -= self.nb_of_people
            self.sum -= self.nb_of_people
            # record the position of the elevator.
            if self.recent_floor < floor:
                print(f"Wait, lift has to go up {floor - self.recent_floor} floors...")
            if self.recent_floor > floor:
                print(f"Wait, lift has to go down {self.recent_floor - floor} floors...")
            self.recent_floor = 0


    

def compare_occupancies(building_1, building_2):
    if building_1.sum > building_2.sum:
        print("There are more occupants in the first building.")
    if building_1.sum < building_2.sum:
        print("There are more occupants in the second building.")
    if building_1.sum == building_2.sum:
        print("There is the same number of occupants in both buildings.")
        
