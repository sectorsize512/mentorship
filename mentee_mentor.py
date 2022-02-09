import csv
import random
import sys
from sys import argv
import argparse




def create_mentee_lst(csvfile):
    all_mentees_lst = []
    mentee_topicmail_dct = {}
    mentees_reader = csv.reader(csvfile)
    next(mentees_reader)
    for row in mentees_reader:
        all_mentees_lst.append(row[2])
        mentee_topicmail_dct[row[2]] = (row[6], row[1], row[7])


    return all_mentees_lst, mentee_topicmail_dct

def create_mentor_lst(csvfile):
    all_mentors_lst = []
    mentor_topicmail_dct = {}
    count_mentee_dct = {}
    mentors_reader = csv.reader(csvfile)
    next(mentors_reader)
    for row in mentors_reader:
        all_mentors_lst.append(row[2])
        mentor_topicmail_dct[row[2]] = row[6], row[1], row[8]
        count_mentee_dct[row[2]] = int(row[7])

    return all_mentors_lst, mentor_topicmail_dct, count_mentee_dct


def create_mentee_mentor_dct(all_mentees, all_mentors):
    new_all_mentors = all_mentors.copy()
    mentee_mentor_dct = {}
    for mentee in all_mentees:
            rand_mentor = random.choice(new_all_mentors)
            mentee_mentor_dct[mentee] = rand_mentor
            count_mentee_dct[rand_mentor] = count_mentee_dct[rand_mentor] - 1
            if count_mentee_dct[rand_mentor] == 0:
                new_all_mentors.remove(rand_mentor)
                if len(new_all_mentors) == 0:

                    return None, all_mentees[all_mentees.index(mentee):len(all_mentees)], "  "


    return " ", " ", mentee_mentor_dct

def  number_coincid_interests(mentee_mentor_dct):
    number_coincid = 0
    for mentee, mentor  in mentee_mentor_dct.items():

            for topic_mentor in mentor_topicmail_dct[mentor][0].split(';'):

                for topic_mentee in mentee_topicmail_dct[mentee][0].split(';'):
                       if topic_mentor == topic_mentee and mentee_topicmail_dct[mentee][2] == mentor_topicmail_dct[mentor][2]:
                        number_coincid += 1

                        
                        
    
    return  number_coincid

parser = argparse.ArgumentParser()

parser.add_argument('-n', '--attempt', type = int, help = 'number of attempts')
parser.add_argument('-f', '--menteefile', help = 'csv file mentee')
parser.add_argument('-f1', '--mentorfile', help = 'csv file mentor')
argv = parser.parse_args()

    

with open(argv.menteefile, newline = '') as csvfile:
    all_mentees_lst, mentee_topicmail_dct = create_mentee_lst(csvfile)
with open(argv.mentorfile, newline = '') as csvfile:
    all_mentors_lst, mentor_topicmail_dct, count_mentee_dct = create_mentor_lst(csvfile)

optimal_coincidences = 0
while argv.attempt != 0:
    err, notcovered_mentee_lst, mentee_mentor_dct = create_mentee_mentor_dct(all_mentees_lst, all_mentors_lst)
    if err == None:
        sys.exit('NOT ENOUGH MENTORS!!!' + "REMAIN WITHOUT MENTORS: " +str(notcovered_mentee_lst))
    number_coincid  = number_coincid_interests(mentee_mentor_dct)
    if number_coincid > optimal_coincidences:
        optimal_coincidences = number_coincid
        optimal_dct = mentee_mentor_dct
    argv.attempt -= 1

print(optimal_coincidences)
print(len(optimal_dct))
print(optimal_dct)
for pair in optimal_dct.items():
    print("To:  " + mentee_topicmail_dct[pair[0]][1] + ";  " +  mentor_topicmail_dct[pair[1]][1])
    print("CC:  " + "tarasov@vasily.name")
    print("Subject: FAST'22 Mentorship Program: Mentor and mentee assignment")
    print("Dear " + pair[0] + " and " + pair[1] + ",")
    print("Thank you for participating in FAST'22! You were assigned as a mentor-mentee pair. Please, schedule a time to meet with each other.")
    print("Mentorship Program Chair,")
    print("Vasily Tarasov")
    print()
    print()