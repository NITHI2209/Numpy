#MINI PROJECT
Students mark analysis 
------------------------
# 1. Average by subject and student
# 2. Highest and lowest per subject
# 3. overall class topper
# 4. Pass count per subject
# 5. which subject is difficult?
# 6. Ranking students
-------------------------- 

import numpy as np
np.random.seed(25)
marks = np.random.randint(10,101,size=(20,5))
print(marks)
[[ 14  72 100  25  71]
 [ 33  54  60  18  38]
 [ 14  99  41  79  11]
 [ 49  13  98  65  13]
 [ 94  55  13  11  32]
 [ 41  58  57  83  26]
 [ 60  95  46  19  42]
 [ 20  70  57  11  96]
 [ 59  28  46  40  48]
 [ 12  15  67  83  32]
 [ 21  12  53 100  71]
 [ 94  93  84  27  24]
 [ 93  47  97  60  61]
 [ 24  81  72 100  25]
 [ 24  86  49  98  56]
 [ 63  39  23  56  63]
 [ 72  77  12  54  54]
 [ 73  55  34  19  77]
 [ 69  89  42  15  66]
 [ 46  93  29  21  47]]

1)average_by_subject = np.mean(marks,axis=0)
print("Average by subject:",average_by_subject)
average_by_student = np.mean(marks,axis=1)
print("Average by students:",average_by_student)
Average by subject: [48.75 61.55 54.   49.2  47.65]
Average by students: [56.4 40.6 48.8 47.6 41.  53.  52.4 50.8 44.2 41.8 51.4 64.4 71.6 60.4
 62.6 48.8 53.8 51.6 56.2 47.2]

2)highest = np.max(marks,axis=0)
lowest = np.min(marks,axis=0)
print("Highest mark per sub:",highest)
print("Lowest mark per sub:",lowest)
Highest mark per sub: [ 94  99 100 100  96]
Lowest mark per sub: [12 12 12 11 11]

3)total = np.sum(marks,axis =1)
topper = np.argmax(total) # argmax gives the index
print("overall topper:",topper,"with the total mark:",total[topper])

4)pass_fail = marks >= 40
pass_count = np.sum(pass_fail,axis = 0)
print("pass count by subject:",pass_count)

5)average_by_subject = np.mean(marks,axis=0)
diff_sub = np.argmin(average_by_subject)
print("Diff sub:",diff_sub,"with average of:",average_by_subject[diff_sub])

6)total = np.sum(marks,axis =1)
ranks = np.argsort(-total)
print(ranks)
[12 11 14 13  0 18 16  5  6 17 10  7  2 15  3 19  8  9  4  1]
print("First rank is in the index:",ranks[0])
First rank is in the index: 12


