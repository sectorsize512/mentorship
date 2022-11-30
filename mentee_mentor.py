import csv
import sys
from sys import argv
import argparse
#import data_visual
import mentee_mentor_class
import table
import random
import copy


def create_mentee_mentor_dct(mentee_dct, mentor_dct):

    new_mentee_dct = copy.deepcopy(mentee_dct)
    new_mentor_dct = copy.deepcopy(mentor_dct)
    mentee_mentor_dct = {}
    for mentee in mentee_dct:
        rand_mentor = random.choice(list(new_mentor_dct.items()))[0]
        mentee_mentor_dct[mentee] = rand_mentor

        new_mentor_dct[rand_mentor].numb_students_to_mentor = new_mentor_dct[rand_mentor].numb_students_to_mentor - 1

        if new_mentor_dct[rand_mentor].numb_students_to_mentor == 0:
            del new_mentor_dct[rand_mentor]

        if len(new_mentor_dct) == 0:
            notcovered_mentee = list(new_mentee_dct.keys())
            return notcovered_mentee, None

    return None, mentee_mentor_dct

#  mentor_dct, mentee_dct   - global

def  compute_rating(mentee_mentor_dct):
    unclaimed_mentors = copy.deepcopy(mentor_dct)
    mentee_mentor_coincid_dct = copy.deepcopy(mentee_mentor_dct)
    for mentee, mentor  in mentee_mentor_dct.items():

        if mentor in unclaimed_mentors:
            del unclaimed_mentors[mentor]

##      topic match
        if argv.matching_on_topic == True:
            topic_Flag = False
            for mentee_topic in mentee_dct[mentee].techtopicsinterest:
                for mentor_topic in mentor_dct[mentor].techtopicsinterest:

                    if mentee_topic == mentor_topic:
                        topic_Flag = True
                        break

                if topic_Flag == True:
                    break

            if topic_Flag == False:
                del mentee_mentor_coincid_dct[mentee]

#       way of visiting conference

        if argv.accept_virtperson_visits == True:
            if mentee in mentee_mentor_coincid_dct:
                    if mentee_dct[mentee].virtperson != mentor_dct[mentor].virtperson:
                        del mentee_mentor_coincid_dct[mentee]

#       no match institution

        if argv.mentormentee_different_institution == True:
            if mentor_dct[mentor].represent_academindust == 'Academia':
                if mentee in mentee_mentor_coincid_dct:
                    if mentee_dct[mentee].university == mentor_dct[mentor].affiliation:
                        del mentee_mentor_coincid_dct[mentee]

#       academy/industry match
        if argv.academic_industry_preference == True:
            if mentee in mentee_mentor_coincid_dct:
                    if mentor_dct[mentor].represent_academindust not in  mentee_dct[mentee].interest_academindust:
                        del mentee_mentor_coincid_dct[mentee]

#       consider previous mentoring
        if argv.consid_prev_mentor == True:
             if (mentee, mentor) in mentee_mentor_prev_dct.items():
               del mentee_mentor_coincid_dct[mentee]

#   all mentors are involved
    if argv.all_mentors == True:
        if len(unclaimed_mentors) != 0:
            return  0

    rating = len(mentee_mentor_coincid_dct)
    return  rating


parser = argparse.ArgumentParser()

parser.add_argument('-n', dest = "count", default = 10000, type = int, help = 'number of attempts, default 10000')

parser.add_argument('-F', '--prev_file', help = 'csv file from previous conference')
#parser.add_argument('-L', '--menteelatefile', help = 'csv file late mentee')
parser.add_argument ('-t', '--matching_on_topic', action = 'store_const', const = True, help = 'Implement matching based on topic of interest')
parser.add_argument ('-v', '--accept_virtperson_visits', action ='store_const', const = True, help = 'Set if virtual or in-person visits are to be counted')
parser.add_argument ('-r', '--academic_industry_preference', action = 'store_const', const = True, help = 'Implement matching based on academy/industry preference')
parser.add_argument ('-u', '--mentormentee_different_institution', action = 'store_const', const = True, help = 'Do not match mentors and mentees that are from the same institution')
parser.add_argument ('-a', '--all_mentors', action ='store_const', const = True, help = 'Support the mode where every mentor gets at least one mentee')
parser.add_argument ('-p', '--consid_prev_mentor', action = 'store_const', const = True, help ='Consider previous mentoring')
parser.add_argument ('-l', '--late_mentee', action = 'store_const', const = True, help ='Possibility to add more mentee without changing existing pairs')
parser.add_argument('-m', '--menteefile', required = True, help = 'csv file mentee' or 'csv file mentee with latecomers mentee')
parser.add_argument('-M', '--mentorfile', required = True, help = 'csv file mentor')
parser.add_argument('-T', '--tablefile', required = True, help = 'csv file, where to save the output table')
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

if argv.prev_file is not None:
        with open(argv.prev_file, newline = '') as csvfile:
            menteementor_reader = csv.reader(csvfile)
            next(menteementor_reader)
            mentee_mentor_prev_dct = {}
            for row in menteementor_reader:
                mentee = row[0].split(';')[0]
                mentor = row[0].split(';')[1]
                mentee_mentor_prev_dct[mentee] = mentor

if argv.late_mentee is not None:
    late_mentee_dct = {}                              ### forming a dictionary of latecomers mentee
    for key, values in mentee_dct.items():
        if key in mentee_mentor_prev_dct:
            continue
        else:
            late_mentee_dct[key] = values

    mentors_unclaimed_slots_dct = copy.deepcopy(mentor_dct)     ### forming a mentor dictionary with available slots
    for mentee, mentor in mentee_mentor_prev_dct.items():   
        if mentor in mentors_unclaimed_slots_dct:
            mentors_unclaimed_slots_dct[mentor].numb_students_to_mentor = mentors_unclaimed_slots_dct[mentor].numb_students_to_mentor - 1

            if mentors_unclaimed_slots_dct[mentor].numb_students_to_mentor == 0:
                del mentors_unclaimed_slots_dct[mentor]


optimal_rating = 0
while argv.count != 0:

    if argv.late_mentee is not None:
        notcovered_mentee, mentee_mentor_dct = create_mentee_mentor_dct(late_mentee_dct, mentors_unclaimed_slots_dct)
    else:
        notcovered_mentee, mentee_mentor_dct = create_mentee_mentor_dct(mentee_dct, mentor_dct)
    if notcovered_mentee != None:

        sys.exit('NOT ENOUGH MENTORS!!!' + "REMAIN WITHOUT MENTORS: " + str(notcovered_mentee))

    rating = compute_rating(mentee_mentor_dct)

    if rating >= optimal_rating:
        optimal_rating = rating
        optimal_menteementor_dct = mentee_mentor_dct

    argv.count -= 1

    if argv.late_mentee is not None:
        optimal_menteementor_dct.update(mentee_mentor_prev_dct)


#for pair in optimal_dct.items():
#    print("To:  " + mentee_dct[pair[0]].interest_academindust + ";  " +  mentor_dct[pair[1]].username)
#    print("CC:  " + "tarasov@vasily.name")
#    print("Subject: FAST'22 Mentorship Program: Mentor and mentee assignment")
#    print("Dear " + mentee_dct[pair[0]].fullname + " and " + mentor_dct[pair[1]].fullname + ",")
#    print("Thank you for participating in FAST'22! You were assigned as a mentor-mentee pair. Please, schedule a time to meet with each other.")
#    print("Mentorship Program Chair,")
#    print("Vasily Tarasov")
#    print()
#    print()



table.table_opt(optimal_menteementor_dct, mentee_dct, mentor_dct, argv.tablefile)

#table.table_unclaimed_mentors(mentors_unclaimed_slots_dct)
#table.table_menteewithoutmentor(mentee_without_mentor_dct)