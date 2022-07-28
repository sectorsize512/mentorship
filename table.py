import csv

def table_opt(mentee_mentor_dct, mentee_dct, mentor_dct):
    with open('rez_table.csv', 'w', newline = '') as csvfile:
        writer = csv.writer(csvfile,  delimiter = ';')
        writer.writerow(["MENTEE", "MENTOR", "TOPIC MATCH", "PERSVIRT MATCH", "INDACAD MATCH", "ISTIT MATCH"])
        for pair in mentee_mentor_dct.items():
            
            topic_match = pair[1][1]           
            persvirt_match = '*' if mentor_dct[pair[1][0]].virtperson == mentee_dct[pair[0]].virtperson else ' '
            indacad_match = '*' if mentor_dct[pair[1][0]].represent_academindust in mentee_dct[pair[0]].interest_academindust.split(';') else ' '
            instit_match_no = '*' if mentor_dct[pair[1][0]].affiliation != mentee_dct[pair[0]].university else ' ' 
            writer.writerow([pair[0], pair[1][0], topic_match, persvirt_match, indacad_match, instit_match_no ])


def table_unclaimed_mentors(mentor_without_mentee_dct):
    with open('rez_table_mentor.csv', 'w', newline = '') as csvfile:
        writer = csv.writer(csvfile,  delimiter = ';')
        writer.writerow(["MENTOR", "TOPIC MATCH", "PERSVIRT MATCH", "INDACAD MATCH", "ISTIT MATCH", "FREE SLOTS"])
        for mentor, inform_mentor in mentor_without_mentee_dct.items():
            writer.writerow([mentor, inform_mentor.techtopicsinterest, inform_mentor.virtperson, inform_mentor.represent_academindust, inform_mentor.affiliation, inform_mentor.numb_students_to_mentor])
            
def table_menteewithoutmentor(mentee_without_mentor_dct):
    with open('rez_table_mentee.csv', 'w', newline = '') as csvfile:
        writer = csv.writer(csvfile,  delimiter = ';')
        writer.writerow(["MENEE", "TOPIC MATCH", "PERSVIRT MATCH", "INDACAD MATCH", "ISTIT MATCH"])
        for mentee, inform_mentee in mentee_without_mentor_dct.items():
            writer.writerow([mentee, inform_mentee.techtopicsinterest, inform_mentee.virtperson, inform_mentee.interest_academindust, inform_mentee.university])                        