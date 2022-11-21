
def years_leap(years):
    leaps = []
    for year in years:
        if ((year%400==0)or(year%100!=0)and(year%4==0)):
            leaps.append(year)
    return leaps


years = [i for i in range(1800,2023)]

my_leaps = years_leap(years)
print(my_leaps)

        