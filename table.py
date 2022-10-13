import csv


def table_opt(optimal_menteementor_dct, mentee_dct, mentor_dct, рrevtable):

    with open(рrevtable, 'w', newline = '') as csvfile:
        writer = csv.writer(csvfile,  delimiter = ';')
        writer.writerow(["MENTEE", "MENTOR", "TOPIC MATCH", "PERSVIRT MATCH", "INDACAD MATCH", "ISTIT MATCH"])

        for mentee, mentor in optimal_menteementor_dct.items():

            topic_Flag = False 

            for mentee_topic in mentee_dct[mentee].techtopicsinterest:
                for mentor_topic in mentor_dct[mentor].techtopicsinterest:

                    if mentee_topic == mentor_topic:
                                          
                        topic_match = '*'
                        topic_Flag = True
                        break

                if topic_Flag == True:
                    break
                else:
                    topic_match = ' '



            persvirt_match = '*' if mentor_dct[mentor].virtperson == mentee_dct[mentee].virtperson else ' '
            indacad_match = '*' if mentor_dct[mentor].represent_academindust in mentee_dct[mentee].interest_academindust else ' '
            instit_match_no = '*' if mentor_dct[mentor].affiliation != mentee_dct[mentee].university else ' '
            writer.writerow([mentee, mentor, topic_match, persvirt_match, indacad_match, instit_match_no ])


def table_unclaimed_mentors(mentors_unclaimed_slots_dct):
    with open('rez_table_mentor.csv', 'w', newline = '') as csvfile:
        writer = csv.writer(csvfile,  delimiter = ';')
        writer.writerow(["MENTOR", "TOPIC MATCH", "PERSVIRT MATCH", "INDACAD MATCH", "ISTIT MATCH", "FREE SLOTS"])
        for mentor, inform_mentor in mentors_unclaimed_slots_dct.items():
            writer.writerow([mentor, inform_mentor.techtopicsinterest, inform_mentor.virtperson, inform_mentor.represent_academindust, inform_mentor.affiliation, inform_mentor.numb_students_to_mentor])

def table_menteewithoutmentor(mentee_without_mentor_dct):
    with open('rez_table_mentee.csv', 'w', newline = '') as csvfile:
        writer = csv.writer(csvfile,  delimiter = ';')
        writer.writerow(["MENTEE", "TOPIC MATCH", "PERSVIRT MATCH", "INDACAD MATCH", "ISTIT MATCH"])
        for mentee, inform_mentee in mentee_without_mentor_dct.items():
            writer.writerow([mentee, inform_mentee.techtopicsinterest, inform_mentee.virtperson, inform_mentee.interest_academindust, inform_mentee.university])