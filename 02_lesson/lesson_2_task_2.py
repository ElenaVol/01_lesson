def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False 

year = 2000
is_vis_year = is_year_leap(year)
print("год", year, ": ", is_vis_year)

year = 2003
is_vis_year = is_year_leap(year)
print("год", year, ": ", is_vis_year)
   