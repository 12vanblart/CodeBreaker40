####Tyler VanBlargan####
####January 5th, 2015###
####ACRE Conversions####


def get_nums(row):
    ###covert each item using a loop: ###
    item = 0
    while item < len(row):
        row[item] = int(row[item])
        item += 1
    return row
