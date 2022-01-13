import csv
import random
import sys
from sys import argv

def create_mentee_lst(csvfile):
    all_mentees_lst = []
    mentee_topic_dct = {}
    mentees_reader = csv.reader(csvfile)
    next(mentees_reader)
    for row in mentees_reader:
        all_mentees_lst.append(row[2])
        mentee_topic_dct[row[2]] = row[6]
    return all_mentees_lst, mentee_topic_dct

def create_mentor_lst(csvfile):
    all_mentors_lst = []
    mentor_topic_dct = {}
    count_mentee_dct = {}
    mentors_reader = csv.reader(csvfile)
    next(mentors_reader)
    for row in mentors_reader:           
        all_mentors_lst.append(row[2])
        mentor_topic_dct[row[2]] = row[5]
        count_mentee_dct[row[2]] = int(row[6])
    return all_mentors_lst, mentor_topic_dct, count_mentee_dct

def create_mentee_mentor_dct(all_mentees, all_mentors, count_mentee_dct):
    new_all_mentors = all_mentors.copy()
    mentee_mentor_dct = {}
    for mentee in all_mentees:
            rand_mentor = random.choice(new_all_mentors)
            mentee_mentor_dct[mentee] = rand_mentor
            count_mentee_dct[rand_mentor]= count_mentee_dct[rand_mentor]-1

            if count_mentee_dct[rand_mentor] == 0:
                new_all_mentors.remove(rand_mentor)

                if len(new_all_mentors) == 0:
                    return None, all_mentees[all_mentees.index(mentee):len(all_mentees)], "  "

    return " ", " ", mentee_mentor_dct

def  number_coincid_interests(mentee_mentor_dct):
    number_coincid = 0
    for mentee, mentor  in mentee_mentor_dct.items():

            for topic_mentor in mentor_topic_dct[mentor].split(';'):

                for topic_mentee in mentee_topic_dct[mentee].split(';'):
                    if topic_mentor == topic_mentee:
                        number_coincid += 1

    return  number_coincid

attempt = int(argv[1])
mentee_f = argv[2]
mentor_f = argv[3]      

with open(mentee_f, newline = '') as csvfile:
    all_mentees_lst, mentee_topic_dct = create_mentee_lst(csvfile)
with open(mentor_f, newline = '') as csvfile:
    all_mentors_lst, mentor_topic_dct, count_mentee_dct = create_mentor_lst(csvfile)

err, notcovered_mentee_lst, mentee_mentor_dct = create_mentee_mentor_dct(all_mentees_lst, all_mentors_lst, count_mentee_dct)
if err == None:
    sys.exit('NOT ENOUGH MENTORS!!!' + "REMAIN WITHOUT MENTORS: " +str(notcovered_mentee_lst))

optimal_coincidences = 0
while attempt != 0:
    number_coincid  = number_coincid_interests(mentee_mentor_dct)
    if number_coincid > optimal_coincidences:
        optimal_coincidences = number_coincid
        optimal_lst = mentee_mentor_dct
    attempt -= 1

print(optimal_coincidences)
print(optimal_lst)