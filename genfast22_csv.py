import csv
import random
from sys import argv

mentor_namelst =[('Heon Y. Yeom', 'tarasov@vasily.name', 'Stony Brook University', 'Industry'),
('Ravi Chitloor', 'tarasov@vasily.name', 'Stony Brook University', 'Industry'),
('Uday Kiran Jonnala', 'tarasov@vasily.name', 'Stony Brook University', 'Industry'),
('Zhaoyan Shen', 'tarasov@vasily.name', 'Stony Brook University', 'Industry'),
('Feng Chen', 'tarasov@vasily.name', 'Stony Brook University', 'Industry'),
('Yichen Jia','tarasov@vasily.name', 'Stony Brook University', 'Industry'),
('Zili Shao', 'tarasov@vasily.name', 'Stony Brook University', 'Industry'),
('Mansour Shafaei', 'tarasov@vasily.name', 'Stony Brook University', 'Industry'),
('Peter Desnoyers', 'tarasov@vasily.name', 'Stony Brook University', 'Industry'),
('Jim Fitzpatrick', 'tarasov@vasily.name', 'Stony Brook University', 'Industry'),
('Leonardo Marmol', 'tarasov@vasily.name', 'Stony Brook University', 'Industry'),
('Jorge Guerra', 'tarasov@vasily.name', 'Stony Brook University', 'Industry')]



mentee_namelst =[('Sungyong Ahn', 'tarasov@vasily.name', 'Stony Brook University', 'Mid PhD (3-4 years)', 'Academia;Industry'),
('Kwanghyun La', 'tarasov@vasily.name', 'Stony Brook University', 'Mid PhD (3-4 years)', 'Academia;Industry'),
('Richard Black', 'tarasov@vasily.name', 'Stony Brook University', 'Mid PhD (3-4 years)', 'Academia;Industry'),
('Austin Donnelly', 'tarasov@vasily.name', 'Stony Brook University', 'Mid PhD (3-4 years)', 'Academia;Industry'),
('Dave Harper', 'tarasov@vasily.name', 'Stony Brook University', 'Mid PhD (3-4 years)', 'Academia;Industry'),
('Aaron Ogus', 'tarasov@vasily.name', 'Stony Brook University', 'Mid PhD (3-4 years)', 'Academia;Industry'),
('Antony Rowstron', 'tarasov@vasily.name', 'Stony Brook University', 'Mid PhD (3-4 years)', 'Academia;Industry'),
('Zhichao Yan', 'tarasov@vasily.name', 'Stony Brook University', 'Mid PhD (3-4 years)', 'Academia;Industry'),
('Hong Jiang', 'tarasov@vasily.name', 'Stony Brook University', 'Mid PhD (3-4 years)', 'Academia;Industry'),
('Hao Luo', 'tarasov@vasily.name', 'Stony Brook University', 'Mid PhD (3-4 years)', 'Academia;Industry'),
('Gala Yadgar', 'tarasov@vasily.name', 'Stony Brook University', 'Mid PhD (3-4 years)', 'Academia;Industry'),
('Moshe Gabel', 'tarasov@vasily.name', 'Stony Brook University', 'Mid PhD (3-4 years)', 'Academia;Industry'),
('Erci Xu', 'tarasov@vasily.name', 'Stony Brook University', 'Mid PhD (3-4 years)', 'Academia;Industry'),
('Mohit Saxena', 'tarasov@vasily.name', 'University of Crete', 'Mid PhD (3-4 years)', 'Academia;Industry'),
('Lawrence Chiu', 'tarasov@vasily.name', 'University of Crete', 'Mid PhD (3-4 years)', 'Academia;Industry'),
('Fenggang Wu', 'tarasov@vasily.name', 'University of Crete', 'Mid PhD (3-4 years)', 'Academia;Industry'),
('Ming-Chang Yang', 'tarasov@vasily.name', 'University of Crete', 'Mid PhD (3-4 years)', 'Academia;Industry'),
('Ziqi Fan', 'tarasov@vasily.name', 'University of Crete', 'Mid PhD (3-4 years)', 'Academia;Industry'),
('Baoquan Zhang', 'tarasov@vasily.name', 'University of Crete', 'Mid PhD (3-4 years)', 'Academia;Industry'),
('Xiongzi Ge', 'tarasov@vasily.name', 'University of Crete', 'Mid PhD (3-4 years)', 'Academia;Industry'),
('David H.C. Du', 'tarasov@vasily.name', 'University of Crete', 'Mid PhD (3-4 years)', 'Academia;Industry'),
('Michael Wei', 'tarasov@vasily.name', 'University of Crete', 'Mid PhD (3-4 years)', 'Academia;Industry'),
('Amy Tai', 'tarasov@vasily.name', 'University of Crete', 'Mid PhD (3-4 years)','Academia;Industry'),
('Chris Rossbach', 'tarasov@vasily.name', 'University of Crete', 'Mid PhD (3-4 years)', 'Academia;Industry'),
('Ittai Abraham', 'tarasov@vasily.name', 'University of Crete', 'Mid PhD (3-4 years)', 'Academia;Industry'),
('Udi Wieder', 'tarasov@vasily.name', 'University of Crete', 'Mid PhD (3-4 years)', 'Academia;Industry'),
('Steven Swanson', 'tarasov@vasily.name', 'University of Crete', 'Mid PhD (3-4 years)', 'Academia;Industry'),
('Dahlia Malkhi', 'tarasov@vasily.name', 'University of Crete', 'Mid PhD (3-4 years)', 'Academia;Industry'),
('Richard P. Spillane', 'tarasov@vasily.name', 'University of Crete', 'Mid PhD (3-4 years)', 'Academia;Industry'),
('Wenguang Wang', 'tarasov@vasily.name', 'University of Crete', 'Mid PhD (3-4 years)', 'Academia;Industry'),
('Luke Lu', 'tarasov@vasily.name', 'University of Crete', 'Mid PhD (3-4 years)', 'Academia;Industry'),
('Maxime Austruy', 'tarasov@vasily.name', 'University of Crete', 'Mid PhD (3-4 years)', 'Academia;Industry'),
('Christos Karamanolis', 'tarasov@vasily.name', 'University of Crete', 'Mid PhD (3-4 years)', 'Academia;Industry'),
('Rawlinson Rivera', 'tarasov@vasily.name', 'University of Crete', 'Mid PhD (3-4 years)', 'Academia;Industry'),
('Woong Shin', 'tarasov@vasily.name', 'University of Crete', 'Mid PhD (3-4 years)', 'Academia;Industry'),
('Jaehyun Park', 'tarasov@vasily.name', 'University of Crete', 'Mid PhD (3-4 years)', 'Academia;Industry')]

presence_lst = ['Virtually only', 'In person at least one day of the conference']

topic_lst = ['Archival systems', 'Auditing and provenance', 'Big data, analytics and data sciences',
'Caching, replication and consistency', 'Cloud, multi and hybrid-cloud environments', 'Data deduplication',
'Database storage', 'Distributed and networked storage (wide_area, grid, peer-to peer', 'Emerging memory hierarchy disign',
 'Empirical evaluation', 'Experience with deploiyd systems', 'File system design', 'HPC systems (including parallel I/O',
 'Key-value and NoSQL storage', 'Management', 'Memory-only storage systems', 'Mobile, personal, embedded, and home storage',
 'Networking', 'Noval and emerging storage technologies (e.g., byte-addressable NVM, flash, SMR, IMR, DNA storage, glass',
 'Performance and QoS', 'Power-aware storage architectures', 'RAID and erasure coding', 'Reliability, availabilit, and disaster tolerance',
 'Search and data retrieval', 'Security'] 

v =('Virtually only', 'In person at least one day of the conference')


# MENTEE

mentee_lst = []

for name in mentee_namelst:
    mentee = ['2021/11/08 3:15:12 PM PST']
    mentee.append(name[1])
    mentee.append(name[0])
    mentee.append(name[2])
    mentee.append(name[3])
    mentee.append(name[4])
    topic = random.sample(topic_lst, 3)
    mentee.append(str(topic[0])+';' +str(topic[1])+';'+str(topic[2]))
    mentee.append(random.choice(v))
    mentee_lst.append(mentee)

mentee_f = argv[1]
with open(mentee_f, 'w', newline = '') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
    writer.writerow(['Timestamp', 'Username', 'Full name', 'University', 'Career stage', 'Interested to be mentored by a member of', 'Technical topics of interest', 'Are you planning to attend the conference virtually or in person?'])
    for k in mentee_lst:
        writer.writerow(k)        

### MENTOR

mentor_lst = []

for name in mentor_namelst:
    mentor = ['2021/11/08 3:15:12 PM PST']
    mentor.append(name[1])
    mentor.append(name[0])
    mentor.append(name[2])
    mentor.append(name[3])
    topic = random.sample(topic_lst, 3)
    mentor.append(str(topic[0])+';' +str(topic[1])+';'+str(topic[2]))
    mentor.append(random.randint(1, 3))
    mentor.append(random.choice(v))
    mentor_lst.append(mentor)

mentor_f = argv[2]
with open(mentor_f, 'w', newline = '') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
    writer.writerow(['Timestamp', 'Username', 'Full name', 'Affiliation', 'Your reprezent', 'Career stage', 'Interested to be mentored by a member of', 'Technical topics of interest and expertise', 'How many students will you be able to mentor?', 'Are you planning to attend the conference virtually or in person?'])
    for k in mentor_lst:       
        writer.writerow(k)