import sys
import os
import csv
import random

class Mentee:

  def __init__(self, timestamp, username, fullname, university, careerstage, interest_academindust, techtopicsinterest, virtperson):
    self.timestamp = timestamp
    self.username = username
    self.fullname = fullname
    self.university = university
    self.careerstage = careerstage
    self.interest_academindust = interest_academindust
    self.techtopicsinterest = techtopicsinterest
    self.virtperson = virtperson

  @classmethod
  def parse_mentee(cls, row):
    timestamp = row[0]
    username = row[1]
    fullname = row[2]
    university = row[3]
    careerstage = row[4]
    interest_academindust = row[5]
    techtopicsinterest = row[6]
    irtperson = row[7]

    return Mentee(timestamp, username, fullname, university, careerstage, interest_academindust, techtopicsinterest, irtperson)


class Mentor:

    def __init__(self, timestamp, username, fullname, affiliation, represent_academindust, techtopicsinterest, numb_students_to_mentor, virtperson):
        self.timestamp = timestamp
        self.username = username
        self.fullname = fullname
        self.affiliation = affiliation
        self.represent_academindust = represent_academindust
        self.techtopicsinterest = techtopicsinterest
        self.numb_students_to_mentor = int(numb_students_to_mentor)
        self.virtperson = virtperson

    @classmethod
    def parse_mentor(cls, row):
        timestamp = row[0]
        username = row[1]
        fullname = row[2]
        affiliation = row[3]
        represent_academindust = row[4]
        techtopicsinterest = row[5]
        numb_students_to_mentor = row[6]
        virtperson = row[7]
    
        return Mentor(timestamp, username, fullname, affiliation, represent_academindust, techtopicsinterest, numb_students_to_mentor, virtperson)