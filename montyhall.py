__author__ = 'Sudo Pnet'
import random

"""                     The MONTY HALL Statistics problem APP
                        --------------------------------------
    the monte Hall problem problem presents a simple conundrum where in a gaming show; a person
    is asked to pick one of three doors, each of which holds either a car or nothing. Now there is only one car
    in the game and thus only one door holds the car while the others have nothing behind them. the game's host
    opens one door and reveals one of the empty doors and asks the participant if he / she wishes to change his door
    pick or go with their first choice.

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
        self.prize = "nothing"
        self.state = "closed"  # either open or closed


class Door(object):
    def __init__(self):
        self.color = ""


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


def main(total=0, same_counter=0, diff_counter=0):
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

    def except_room_str(listing):
        string = ""
        if len(listing) > 0:
            string += str(listing[0])
        for number in range(1, len(listing)):
            string += "|" + str(listing[number])
        return string

    first_choice, second_choice = 0, 0

    def input_choice(choice, listing):
        temp_choice = int(input("please type in door choice(%s): " % except_room_str(listing)))
        if temp_choice not in listing:
            raise Exception('Choice does not exist')
        else:
            choice = temp_choice
    first_choice = input_choice(first_choice, [0, 1, 2])
    # ask for the user's first choice

    popped_room = random.choice([room for room in rooms_list if room.prize == "nothing" and
                                 rooms_list.index(room) != first_choice])
    pc_open_index = rooms_list.index(popped_room)
    rooms_list[pc_open_index].state = "open"

    print("Room %s was opened and thus unavailable for selection." % pc_open_index)

    # compute a string containing the indices of rooms that are still closed
    def generator(a_list):
        for room in a_list:
            if room.state == "closed":
                yield rooms_list.index(room)
    string_list = [int(room_index) for room_index in generator(rooms_list)]
    input_choice(second_choice, string_list)

    if rooms_list[second_choice].prize == "car":
        print("you have won : ", rooms_list[second_choice].prize)
    else:
        print("You have did not get the car this tym round!")


    if first_choice == second_choice:
        total += 1
        if rooms_list[second_choice].prize == "car":
            same_counter += 1
    elif first_choice != second_choice:
        total += 1
        if rooms_list[second_choice].prize == "car":
            diff_counter += 1

    return [total, same_counter, diff_counter]

    # and now for an analysis:


def loop_main():
    total, same_counter, diff_counter = 0, 0, 0
    while True:
        choice = input("Press any key to proceed(**q to quit**): ")
        if choice == "q":
            break
        else:
            same_choice = main()
            total += same_choice[0]
            same_counter += same_choice[1]
            diff_counter += same_choice[2]

    if total > 0:
        if same_counter > 0:
            same_perc = int(same_counter // total * 100)
            print("Your win percentage after sticking with the same choice: %s" % (same_perc))
        if diff_counter > 0:
            diff_perc = int(diff_counter // total * 100)
            print("Your win percentage after choosing to switch choices: %s" % diff_perc)


if __name__ == "__main__":
    loop_main()
