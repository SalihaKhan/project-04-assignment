def main():

    days_in_year = 365
    hours_in_a_day = 24
    min_in_an_hour = 60
    sec_in_a_min = 60

    seconds_in_year = days_in_year*hours_in_a_day*min_in_an_hour*sec_in_a_min
    print(f"There are {seconds_in_year} seconds in a year")


if __name__ == '__main__':
    main()