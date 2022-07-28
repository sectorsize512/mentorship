import csv
import sys
from sys import argv
import argparse
import data_visual
import mentee_mentor_class
import table
import random
import copy

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
            return notcovered_mentee, None
    
    return None, mentee_mentor_dct

def  number_coincid_interests(mentee_mentor_dct):
    
    mentee_mentor_coincid_dct = {}
    
    for mentee, mentor  in mentee_mentor_dct.items():
                  
          
##      topic match
               
        topic_Flag = False
        for mentee_topic in mentee_dct[mentee].techtopicsinterest .split(';'):             
            for mentor_topic in mentor_dct[mentor].techtopicsinterest .split(';'):
                
                if mentee_topic == mentor_topic:
                       
                        mentee_mentor_coincid_dct[mentee] = [mentor, '*']
                        topic_Flag = True
                        break
           
            if topic_Flag == True:
                break
            else:
                if argv.t == None:
                    mentee_mentor_coincid_dct[mentee] = [mentor, ' ']
            
                     
        # way of visiting conference
        if argv.v == True:
                if mentee in mentee_mentor_coincid_dct:        
                    if mentee_dct[mentee].virtperson != mentor_dct[mentor].virtperson:
                        del mentee_mentor_coincid_dct[mentee]
                   
                  
        # academy/industry match
        if argv.r == True:
               
                if mentee in mentee_mentor_coincid_dct:
                          
                    if mentor_dct[mentor].represent_academindust not in  mentee_dct[mentee].interest_academindust.split(';'):
                       
                        del mentee_mentor_coincid_dct[mentee]                
                    
        # no match institution       
        if argv.u == True and mentor_dct[mentor].represent_academindust == 'Academia':
                    if mentee in mentee_mentor_coincid_dct:        
                        if mentee_dct[mentee].university == mentor_dct[mentor].affiliation:
                            del mentee_mentor_coincid_dct[mentee]
                              
    number_coincid = len(mentee_mentor_coincid_dct)
    
    return  number_coincid, mentee_mentor_coincid_dct



parser = argparse.ArgumentParser()

parser.add_argument('-n', dest="count", default=10000, type=int, help = 'number of attempts, default 10000')
parser.add_argument('-f_mentee', '--menteefile', help = 'csv file mentee')
parser.add_argument('-f_mentor', '--mentorfile', help = 'csv file mentor')
parser.add_argument ('-t', action='store_const', const=True, help='Implement matching based on topic of interest')
parser.add_argument ('-v', action='store_const', const=True, help='Set if virtual or in-person visits are to be counted')
parser.add_argument ('-r', action='store_const', const=True, help='Implement matching based on academy/industry preference')
parser.add_argument ('-u', action='store_const', const=True, help='Do not match mentors and mentees that are from the same institution')
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
       



optimal_coincidences = 0
number_attempts = argv.count
while number_attempts != 0:
   

    notcovered_mentee, mentee_mentor_dct = create_mentee_mentor_dct(mentor_dct, mentee_dct)
    if notcovered_mentee != None:

        sys.exit('NOT ENOUGH MENTORS!!!' + "REMAIN WITHOUT MENTORS: " + str(notcovered_mentee))

    #if number_coincid_interests(mentee_mentor_dct) == 'Dictionary is unsuccessful':      
        #print(111)
        #number_attempts -= 1
        #continue
        
    #else:
    number_coincid, mentee_mentor_coincid_dct = number_coincid_interests(mentee_mentor_dct)

    if number_coincid > optimal_coincidences:
        optimal_coincidences = number_coincid
        optimal_dct = mentee_mentor_coincid_dct
  
    number_attempts -= 1  


mentor_without_mentee_dct = copy.deepcopy(mentor_dct)
mentee_without_mentor_dct = copy.deepcopy(mentee_dct)

for mentee, mentor in optimal_dct.items():
    del mentee_without_mentor_dct[mentee]
    
    mentor_without_mentee_dct[mentor[0]].numb_students_to_mentor = mentor_without_mentee_dct[mentor[0]].numb_students_to_mentor - 1
    if mentor_without_mentee_dct[mentor[0]].numb_students_to_mentor == 0:
            del mentor_without_mentee_dct[mentor[0]]
    
#print(mentee_without_mentor_dct)
#print(mentor_without_mentee_dct)
create_mentee_mentor_dct(mentor_without_mentee_dct, mentee_without_mentor_dct,)

  
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


#table.table(optimal_dct, mentee_dct, mentor_dct)
table.table_opt(optimal_dct, mentee_dct, mentor_dct)
table.table_unclaimed_mentors(mentor_without_mentee_dct)
table.table_menteewithoutmentor(mentee_without_mentor_dct)