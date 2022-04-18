import csv
import sys
from sys import argv
import argparse
#import data_visual
import mentee_mentor_class
import random
import copy

parser = argparse.ArgumentParser()

parser.add_argument('-n', dest="count", default=10000, type=int, help = 'number of attempts, default 10000')
parser.add_argument('-f', '--menteefile', help = 'csv file mentee')
parser.add_argument('-f1', '--mentorfile', help = 'csv file mentor')
parser.add_argument ('-v', action='store_const', const=True, help='Set if virtual or in-person visits are to be counted')
argv = parser.parse_args()


with open(argv.menteefile, newline = '') as csvfile:
    mentees_reader = csv.reader(csvfile)
    next(mentees_reader)
    mentee_dct = {}
    for row in mentees_reader:
        mentee = mentee_mentor_class.Mentee.parse_mentee(row)
        mentee_dct[mentee.fullname] = mentee

with open(argv.mentorfile, newline = '') as csvfile:
    mentors_reader = csv.reader(csvfile)
    next(mentors_reader)
    mentor_dct = {}
    for row in mentors_reader:
        mentor = mentee_mentor_class.Mentor.parse_mentor(row)
        mentor_dct[mentor.fullname] = mentor

def create_mentee_mentor_dct(mentor_dct, mentee_dct):
    new_mentee_dct = copy.deepcopy(mentee_dct)
    new_mentor_dct = copy.deepcopy(mentor_dct)
    mentee_mentor_dct = {}
    for mentee in mentee_dct:
        rand_mentor = random.choice(list(new_mentor_dct.items()))[0]
        mentee_mentor_dct[mentee] = rand_mentor
        new_mentor_dct[rand_mentor].numb_students_to_mentor = new_mentor_dct[rand_mentor].numb_students_to_mentor - 1
        del new_mentee_dct[mentee]

        if new_mentor_dct[rand_mentor].numb_students_to_mentor == 0:
            del new_mentor_dct[rand_mentor]

        if len(new_mentor_dct) == 0:
            notcovered_mentee = list(new_mentee_dct.keys())
            return None, notcovered_mentee, "  "

    return " ", " ", mentee_mentor_dct

def  number_coincid_interests(mentee_mentor_dct):
    number_coincid = 0
    mentee_mentor_coincid_dct = {}
    for mentee, mentor  in mentee_mentor_dct.items():
        for mentee_topic in mentee_dct[mentee].techtopicsinterest .split(';'):
            for mentor_topic in mentor_dct[mentor].techtopicsinterest .split(';'):

                if argv.v == True:
                    if mentee_topic == mentor_topic and mentee_dct[mentee].virtperson == mentor_dct[mentor].virtperson:
                        number_coincid += 1
                        mentee_mentor_coincid_dct[mentee] = mentor
                else:
                    if mentee_topic == mentor_topic:
                        number_coincid += 1
                        mentee_mentor_coincid_dct[mentee] = mentor

    return  number_coincid, mentee_mentor_coincid_dct

optimal_coincidences = 0
while argv.count != 0:
    err, notcovered_mentee, mentee_mentor_dct = create_mentee_mentor_dct(mentor_dct, mentee_dct)

    if err == None:
        sys.exit('NOT ENOUGH MENTORS!!!' + "REMAIN WITHOUT MENTORS: " + str(notcovered_mentee))
    number_coincid, mentee_mentor_coincid_dct   = number_coincid_interests(mentee_mentor_dct)

    if number_coincid > optimal_coincidences:
        optimal_coincidences = number_coincid
        optimal_dct = mentee_mentor_coincid_dct        
    argv.count -= 1

for pair in optimal_dct.items():
    print("To:  " + mentee_dct[pair[0]].interest_academindust + ";  " +  mentor_dct[pair[1]].username)
    print("CC:  " + "tarasov@vasily.name")
    print("Subject: FAST'22 Mentorship Program: Mentor and mentee assignment")
    print("Dear " + mentee_dct[pair[0]].fullname + " and " + mentor_dct[pair[1]].fullname + ",")
    print("Thank you for participating in FAST'22! You were assigned as a mentor-mentee pair. Please, schedule a time to meet with each other.")
    print("Mentorship Program Chair,")
    print("Vasily Tarasov")
    print()
    print()

#data_visual.coincid_graph(optimal_dct, mentor_dct)