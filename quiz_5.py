# Written by *** for COMP9021
#
# Uses the file cardio_train.csv downloaded from
# https://www.kaggle.com/sulianova/cardiovascular-disease-dataset
#
# Implements a function analyse(gender, age)
# where gender is one of 'F' (for female) or 'M' (for male),
# and where age is any integer for which we have data in the file
# (nothing needs to be done if that is not the case).
#
# We assume that all years have 365 days;
# in particular, someone who is 365 days old is 0 year old,
# and someone who is 366 days old is 1 year old.
#
# We ignore records for which at least one of these conditions holds:
# - height < 150 or height > 200
# - weight < 50 or weight > 150
# - ap_hi < 80 or ap_hi > 200
# - ap_lo < 70 or ap_lo > 140
#
# For each of both classes "cardio problem" and "no cardio problem"
# (as given by the cardio attribute), we create 5 bins/categories for
# height, weight, ap_hi, ap_lo, of equal width,
# that span between smallest value and largest value
# for the attribute in the category.
# For instance, suppose that gender is 'F' and age is 48.
# - Suppose that for the category "cardio problem",
#   the shortest woman aged 48 is 150cm tall, and
#   the tallest woman aged 48 is 200cm tall.
#   Then each of the 5 categories for the class "cardio problem"
#   and for the attribute "height" spans 10cm.
# - Suppose that for the class "no cardio problem",
#   the shortest woman aged 48 is 158cm tall, and
#   the tallest woman aged 48 is 193cm tall.
#   Then each of the 5 categories for the class "no cardio problem"
#   and for the attribute "height" spans 7cm.
# To avoid boundary issues, add 0.1 to the maximum value
# (so with the previous example, the maximum heights would be
# considered to be 200.1 and 193.1, respectively).
# This applies to each of the 4 attributes height, weight,
# ap_hi and ap_lo.
#
# For each attribute and for each of its possible values,
# we compute the ratio of
# - the frequency of people under consideration with a "cardio problem"
#   having that value for that attribute, with
# - the frequency of people under consideration with "no cardio problem"
#   having that value for that attribute.
# Continuing the previous example:
# - Suppose that that there are 100 woman aged 48
#   who have a "cardio problem" and 20 of those are at most 160cm tall.
# - Suppose that that there are 150 woman aged 48
#   who have "no cardio problem" and 50 of those are at most 165cm tall.
# Then the ratio for the value "category 1" of the attribute "height"
# is 0.2 / 0.3...3...
#
# We keep only ratios that are strictly greater than 1 and order them
# from largest to smallest.
# A ratio might be infinite (see second sample test).
# In case two ratios are exactly the same, their order is determined
# by the order of the corresponding attributes in the csv file
# (first is height, last is being active or not), and in case the
# attributes are the same, their order is determined by the rank of
# the category (first is 1, last is 5; for booleans, False comes
# before True).
#
# We format ratios with 2 digits after the decimal point.
# After a ratio, the output is one of:
# - Height in category [1-5] (1 lowest, 5 highest)
# - Weight in category [1-5] (1 lowest, 5 highest)
# - Systolic blood pressure in category [1-5] (1 lowest, 5 highest)
# - Diastolic blood pressure in category [1-5] (1 lowest, 5 highest)
# - Cholesterol in category [1-3] (1 lowest, 3 highest)
# - Glucose in category [1-3] (1 lowest, 3 highest)
# - Smoking/Not smoking
# - Drinking/Not drinking
# - Not being active/Being active
#
# You are NOT allowed to use pandas. If you do, then your submission
# will NOT be assessed and you will score 0 to the quiz.

# Written by *** for COMP9021
#
# Uses the file cardio_train.csv downloaded from
# https://www.kaggle.com/sulianova/cardiovascular-disease-dataset
#
# Implements a function analyse(gender, age)
# where gender is one of 'F' (for female) or 'M' (for male),
# and where age is any integer for which we have data in the file
# (nothing needs to be done if that is not the case).
#
# We assume that all years have 365 days;
# in particular, someone who is 365 days old is 0 year old,
# and someone who is 366 days old is 1 year old.
#
# We ignore records for which at least one of these conditions holds:
# - height < 150 or height > 200
# - weight < 50 or weight > 150
# - ap_hi < 80 or ap_hi > 200
# - ap_lo < 70 or ap_lo > 140
#
# For each of both classes "cardio problem" and "no cardio problem"
# (as given by the cardio attribute), we create 5 bins/categories for
# height, weight, ap_hi, ap_lo, of equal width,
# that span between smallest value and largest value
# for the attribute in the category.
# For instance, suppose that gender is 'F' and age is 48.
# - Suppose that for the category "cardio problem",
#   the shortest woman aged 48 is 150cm tall, and
#   the tallest woman aged 48 is 200cm tall.
#   Then each of the 5 categories for the class "cardio problem"
#   and for the attribute "height" spans 10cm.
# - Suppose that for the class "no cardio problem",
#   the shortest woman aged 48 is 158cm tall, and
#   the tallest woman aged 48 is 193cm tall.
#   Then each of the 5 ctagories for the class "no cardio problem"
#   and for the attribute "height" spans 7cm.
# To avoid bounday issues, add 0.1 to the maximum value
# (so with the previous example, the maximum heights would be
# considered to be 210.1 and 193.1, respectively).
# This applies to each of the 4 attributes height, weight,
# ap_hi and ap_lo.
#
# For each attribute and for each of its possible values,
# we compute the ratio of
# - the frequency of people under consideration with a "cardio problem"
#   having that value for that attribute, with
# - the frequency of people under consideration with "no cardio problem"
#   having that value for that attribute.
# Continuing the previous example:
# - Suppose that that there are 100 woman aged 48
#   who have a "cardio problem" and 20 of those are at most 160cm tall.
# - Suppose that that there are 150 woman aged 48
#   who have "no cardio problem" and 50 of those are at most 165cm tall.
# Then the ratio for the value "category 1" of the attribute "height"
# is 0.2 / 0.3...3...
#
# We keep only ratios that are strictly greater than 1 and order them
# from largest to smallest.
# We format ratios with 2 digits after the decimal point.
# After a ratio, the output is one of:
# - Height in category [1-5] (1 lowest, 5 highest)
# - Weight in category [1-5] (1 lowest, 5 highest)
# - Systolic blood pressure in category [1-5] (1 lowest, 5 highest)
# - Diastolic blood pressure in category [1-5] (1 lowest, 5 highest)
# - Cholesterol in category [1-3] (1 lowest, 3 highest)
# - Glucose in category [1-3] (1 lowest, 3 highest)
# - Smoking/Not smoking
# - Drinking/Not drinking
# - Not being active/Being active
#
# You are NOT allowed to use pandas. If you do, then your submission
# will NOT be assessed and you will score 0 to the quiz.

import csv
from collections import defaultdict
from operator import itemgetter


# Samples
# ['id', 'age', 'gender', 'height', 'weight', 'ap_hi', 'ap_lo', 'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'cardio']
#     0; 18393;        2;      168;     62.0;     110;      80;             1;      1;       0;      0;        1;        0
#     1; 20228;        1;      156;     85.0;     140;      90;             3;      1;       0;      0;        1;        1
#     2; 18857;        1;      165;     64.0;     130;      70;             3;      1;       0;      0;        0;        1
#     3; 17623;        2;      169;     82.0;     150;     100;             1;      1;       0;      0;        1;        1
#     4; 17474;        1;      156;     56.0;     100;      60;             1;      1;       0;      0;        0;        0
#     8; 21914;        1;      151;     67.0;     120;      80;             2;      2;       0;      0;        0;        0
#     9; 22113;        1;      157;     93.0;     130;      80;             3;      1;       0;      0;        1;        0

col_age = 1
col_gender = 2

# 5 category
col_height = 3
col_weight = 4
col_ap_hi = 5
col_ap_lo = 6

# 3 category
col_cholesterol = 7
col_gluc = 8

# 2 category
col_smoke = 9
col_alco = 10
col_active = 11

col_cardio = 12

samples = list()

def calc_frequency_2(col, cardio):
    count = 0
    person = [0, 0]

    for row in samples:
        if int(row[col_cardio]) == cardio:
            i = int(row[col])
            person[i] += 1
            count += 1

    frequency = [0.0, 0.0]

    frequency[0] = person[0] / count
    frequency[1] = person[1] / count

    return frequency


def calc_frequency_3(col, cardio):
    count = 0
    person = [0, 0, 0]

    for row in samples:
        if int(row[col_cardio]) == cardio:
            i = int(row[col]) - 1
            person[i] += 1
            count += 1

    frequency = [0.0, 0.0, 0.0]

    for i in range(3):
        frequency[i] = person[i] / count

    return frequency


def calc_frequency_5(col, cardio):
    max_val = 0.0
    min_val = 1000.0
    count = 0

    for row in samples:
        if int(row[col_cardio]) == cardio:
            val = float(row[col])
            max_val = max(max_val, val)
            min_val = min(min_val, val)
            count += 1

    span = (max_val + 0.1 - min_val) / 5

    #print("max {} min {} span {}".format(max_val, min_val, span))

    person = [0, 0, 0, 0, 0]

    for row in samples:
        if int(row[col_cardio]) == cardio:
            val = float(row[col])

            i = int((val - min_val) / span)
            person[i] += 1;

            #val = val - min_val

            #if val < span:
            #    table[0] += 1
            #elif val > span and val < span * 2:
            #    table[1] += 1
            #elif val > span * 2 and val < span * 3:
            #    table[2] += 1
            #elif val > span * 3 and val < span * 4:
            #    table[3] += 1
            #elif val > span * 4 and val < span * 5:
            #    table[4] += 1


    frequency = [0.0, 0.0, 0.0, 0.0, 0.0]

    for i in range(5):
        frequency[i] = person[i] / count

    return frequency


def calc_ratio_2(table, col, title_zero, title_one):
    frequency_0 = calc_frequency_2(col, 0)
    frequency_1 = calc_frequency_2(col, 1)

    for i in range(2):
        desc = title_zero if i == 0 else title_one
        ratio = float("inf")
        if frequency_0[i] > 0:
            ratio = frequency_1[i] / frequency_0[i]

        table.append((desc, ratio, col, i))


def calc_ratio_3(table, col, title):
    frequency_0 = calc_frequency_3(col, 0)
    frequency_1 = calc_frequency_3(col, 1)

    for i in range(3):
        desc = "{} {} (1 lowest, 3 highest)".format(title, i + 1)
        ratio = float("inf")
        if frequency_0[i] > 0:
            ratio = frequency_1[i] / frequency_0[i]

        table.append((desc, ratio, col, i))

def calc_ratio_5(table, col, title):
    frequency_0 = calc_frequency_5(col, 0)
    frequency_1 = calc_frequency_5(col, 1)

    for i in range(5):
        desc = "{} {} (1 lowest, 5 highest)".format(title, i + 1)
        ratio = float("inf")
        if frequency_0[i] > 0:
            ratio = frequency_1[i] / frequency_0[i]

        table.append((desc, ratio, col, i))


def analyse(gender, age):
    cvsfile = open('cardio_train.csv')

    cardio_train = csv.reader(cvsfile, delimiter=';')

    # skip first line
    next(cardio_train)

    if gender == 'F':
        gender_mask = 1
    elif gender == 'M':
        gender_mask = 2

    samples.clear()

    for row in cardio_train:

        age_of_day = int(row[col_age])
        #if int((age_of_day + 1) / 365) == age and int(row[col_gender]) == gender_mask:
        if age_of_day > (age) * 365 and age_of_day <= (age + 1) * 365 and int(row[col_gender]) == gender_mask:
            height = float(row[col_height])
            weight = float(row[col_weight])
            ap_hi = float(row[col_ap_hi])
            ap_lo = float(row[col_ap_lo])

            # ignore some conditions
            if height < 150 or height > 200 or weight < 50 or weight > 150 or ap_hi < 80 or ap_hi > 200 or ap_lo < 70 or ap_lo > 140:
                continue

            samples.append(row)

    if len(samples) == 0:
        return

    table = list()
    
    calc_ratio_5(table, col_ap_hi, 'Systolic blood pressure in category')
    calc_ratio_5(table, col_ap_lo, 'Diastolic blood pressure in category')
    calc_ratio_5(table, col_height, 'Height in category')
    calc_ratio_5(table, col_weight, 'Weight in category')

    calc_ratio_3(table, col_cholesterol, 'Cholesterol in category')
    calc_ratio_3(table, col_gluc, 'Glucose in category')

    calc_ratio_2(table, col_smoke, 'Smoking', 'Not smoking')
    calc_ratio_2(table, col_alco, 'Drinking', 'Not drinking')
    calc_ratio_2(table, col_active, 'Not being active', 'Being active')

    print('The following might particularly contribute to cardio problems for {} aged {}:'.format('females' if gender == 'F' else 'males', age))

    table = sorted(table, key=itemgetter(3), reverse=True)
    table = sorted(table, key=itemgetter(2), reverse=False)
    table = sorted(table, key=itemgetter(1), reverse=True)
    for item in table:
        if item[1] >= 1.0:
            print("   {:.2f}: {}".format(item[1], item[0]))

        
if __name__ == "__main__":
    print('----------------')
    analyse('F', 43)
    print('----------------')
    analyse('M', 58)
    print('----------------')




