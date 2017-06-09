__author__ = 'Sudo Pnet'
import random

"""                     The MONTY HALL Statistics problem APP
                        --------------------------------------
    the monte carlo problem problem presents a simple conundrum where in a gaming show; a person
    is asked to pick one of three doors each of which holds either a car or  nothing. Now there is only one car
    in the game and thus only one door holds the car while the others have nothing behind them. the game's host
    opens and reveals one of the empty doors and asks the participant if he / she wishes to change his door pick
    or go with their first choice.

"""

# logic: so the app should show a representation of three doors
# : then the user gets to pick on of the doors
# : then the application gets to pick and either reveal or remove one of the doors that
#   hold nothing
# : the user then gets the chance to choose whether they want to change their first pick
#   or stick with the new choice.
# : the last step is to show the user what is behind the door of their choice
# : and maybe we can also put in a tally that shows the probability if winning the car should you change your choice
#   as opposed to when u don't


class Room(object):
    # properties
    def __init__(self):
        self.door = ""  # Door() maybe should be an object
        self.prize = "goat"
        self.state = "closed"  # either open or closed


class Door(object):
    def __init__(self):
        self.color = ""

class Counter(object):

    same_counter = 0
    diff_counter = 0
    total = 0

    def __init__(self):
        pass

def randomisation_engine(a_list):
    """ returns an extremely random value:
     quiz? is there not a way that we can nest or combine random functions in a manner that would render it double
      random then we can set the picked room prize to a car and all the others are assigned goats."""

    first_random_choice = random.choice(a_list)
    bool_counter = True
    while bool_counter:
        second_random_choice = random.choice(a_list)
        if first_random_choice == second_random_choice:
            bool_counter = True
        else:
            second_random_choice.prize = "car"
            bool_counter = False

def main():
    # initialize the game:

    # initialize the three rooms:
    room1 = Room()
    room2 = Room()
    room3 = Room()
    rooms_list = list()
    rooms_list.append(room1)
    rooms_list.append(room2)
    rooms_list.append(room3)

    # set one of the rooms prizes to hold a car
    randomisation_engine(rooms_list)

    # ask for the user's first choice
    first_choice = int(input("please type in first door choice(0|1|2): "))

    # here is where we choose the one door with a goat and set its state to opened

    # for room in rooms_list:
    #     if room.prize == "goat" and rooms_list.index(room) != first_choice:
    #         pc_open_index = rooms_list.index(room)
    #         break

    # i would prefer if we randomized the room holding a goat as opposed to the above
    goat_popped_room = random.choice([ room for room in rooms_list if room.prize == "goat" and
                                       rooms_list.index(room) != first_choice])
    pc_open_index = rooms_list.index(goat_popped_room)
    rooms_list[pc_open_index].state = "open"

    print("Room%s was opened and thus unavailable for selection." % pc_open_index)

    # popped_room = rooms_list.pop(rooms_list[pc_open_index])
    # compute a string containing the indices of rooms that are still closed
    def generator(a_list):
        for room in a_list:
            if room.state == "closed":
                yield rooms_list.index(room)
    string_list = [ str(room_index) for room_index in generator(rooms_list)]
    stringified = "|".join(string_list)
    second_choice = int(input("please type in second door choice(%s): " % stringified))

    print("you have won : ", rooms_list[second_choice].prize)

    same_choice = Counter()

    if first_choice == second_choice:
        same_choice.total += 1
        if rooms_list[second_choice].prize == "car":
            same_choice.same_counter += 1
    elif first_choice != second_choice:
        same_choice.total += 1
        if rooms_list[second_choice].prize == "car":
            same_choice.diff_counter += 1
    return  same_choice

    # and now for an analysis:


def loop_main():
    while True:
        choice = input("Press any key to proceed(**q to quit**): ")
        if choice == "q":
            return
        else:
            same_choice = main()
            print(same_choice.total, same_choice.same_counter, same_choice.diff_counter)
            if same_choice.total > 0:
                same_perc = int(same_choice.same_counter // same_choice.total * 100)
                print("Your win percentage after sticking with the same choice: %s" % (same_perc))
                diff_perc = int(same_choice.diff_counter // same_choice.total * 100)
                print("Your win percentage after choosing to switch choices: %s" % diff_perc)


if __name__ == "__main__":
    loop_main()
