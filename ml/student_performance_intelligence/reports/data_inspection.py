1.) we have 100,500 rows and 16 column
2.) we have a column names of [['student_id', 'age', 'department', 'level', 'study_hours',
       'attendance_rate', 'previous_gpa', 'assignment_average', 'quiz_average',
       'midterm_score', 'internet_access', 'library_visits', 'sleep_hours',
       'previous_failures', 'extracurricular_hours', 'final_score']]
3.) the columns types are:
student_id                 int64
age                      float64
department                   str
level                      int64
study_hours              float64
attendance_rate          float64
previous_gpa             float64
assignment_average       float64
quiz_average             float64
midterm_score            float64
internet_access              str
library_visits             int64
sleep_hours              float64
previous_failures          int64
extracurricular_hours    float64
final_score              float64


4.)

student_id                  0
age                         0
department                  0
level                       0
study_hours              2008
attendance_rate          2009
previous_gpa             2014
assignment_average       2009
quiz_average             2016
midterm_score               0
internet_access             0
library_visits              0
sleep_hours                 0
previous_failures           0
extracurricular_hours       0
final_score                 0

5.)

Duplicated:500

6.)Minum Value for each column

student_id                          100000
age                                    3.0
department               Civil Engineering
level                                  100
study_hours                           -5.0
attendance_rate                  27.820918
previous_gpa                           0.0
assignment_average               17.887189
quiz_average                      9.030365
midterm_score                    18.528565
internet_access                    Average
library_visits                           0
sleep_hours                            2.0
previous_failures                        0
extracurricular_hours             0.004456
final_score                       28.82354

maximum_value:

student_id                  199999
age                           32.0
department                 Physics
level                          500
study_hours                   15.0
attendance_rate              150.0
previous_gpa                   7.0
assignment_average           100.0
quiz_average                 100.0
midterm_score                100.0
internet_access               Poor
library_visits                  15
sleep_hours              11.604376
previous_failures                7
extracurricular_hours         15.0
final_score                  100.0

7.)attendance minimum houre -5 look suspicious, and also attendance maximum value is 150 i think it should be between 1-100 thou, i notice minimum gpa=0 doesn't that mean that the student was abscent

8.) Index(['department', 'internet_access'], dtype='str')

9.) final_score is our target

10.) duplicated_percentage=0.4975(df.duplicated().mean() * 100)
