# year =int(input('put a year to determine if is leap or not: '))
years = [1988, 1989, 1990, 1991, 1992, 1993, 1994,1995,1996,1997, 1998, 1999, 2000, 2001, 2002, 2003,2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012,2013, 2014,2015,2016, 2017, 2018,2019,2020, 2021, 2022]
for year in years:
    if(year % 4 == 0 and year%100 !=0 or year%400==0):
        print(f"El año {year} es bisiesto")
        print(f"{year%100}")
    else:
        print(f"El año {year} no es bisiesto")