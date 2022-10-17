import time
import pandas as pd
import numpy as np
import calendar

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        print ("The avaliable cities are: chicago, new york city, washington")
        city= input("Choose which city do you want, please: ").lower()
        if city not in CITY_DATA :
            print ("This city is not avaliable, please try again")
        else :
            break 
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        print ("The avaliable months are: january,february ,march ,april ,may ,june")
        month= input("Choose which month do you want, or all: ").lower()
        all_monthes= ["january","february","march","april","may","june"]
        if month != "all" and month not in all_monthes : 
            print ("This Month is not available, please try again")
        else :
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day= input("Insert which day do you want, or all: ").lower()
        all_days= ["Monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
        if day != "all" and day not in all_days :
            print ("This Day is not available, please try again")
        else : 
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df= pd.read_csv(CITY_DATA[city])
    df [ "Start Time" ] = pd.to_datetime(df["Start Time"])
    df [ "month" ] = df["Start Time"].dt.month
    df [ "day_of_week" ] = df["Start Time"].dt.day_name()
    
    if month != "all" :
        all_monthes= ["january","february","march","april","may","june"]
        month = all_monthes.index(month) +1
        df = df [df ["month"] == month]
    
    if day != "all":
        df = df [df ["day_of_week"] == day.title()]
    
    return df


def line_data(df) :
    line = 0
    line_ask = input("Do you want the first 5 lines data?: ").lower()
    pd. set_option("display.max_columns",None)
    
    while True:
        if line_ask == "no" :
            break
        print(df [ line:line+5])
        line_ask = input("Do you want the next 5 lines data?: ").lower()
        line = line+5

        
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    com_month = df["month"] .mode()[0]
    print (" The Most Common Month is {}." .format(calendar.month_name[com_month]))

    # TO DO: display the most common day of week
    com_day = df["day_of_week"] .mode()[0]
    print (" The Most Common day is {}." .format(com_day))

    # TO DO: display the most common start hour
    df ["hour"] = df ["Start Time"] .dt.hour
    com_hour = df["hour"] .mode()[0]
    print (" The Most Common Start Hour is {}." .format(com_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    com_start_station = df["Start Station"] .mode()[0]
    print (" The Most Common Start Station is {}." .format(com_start_station))

    # TO DO: display most commonly used end station
    com_end_station = df["End Station"] .mode()[0]
    print (" The Most Common End Station is {}." .format(com_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    com_start_end = (df["Start Station"]+ " " +df["End Station"]) .mode()[0]
    print (" The Most Frequent Combination of Start Station and End Station trip is {}." .format(com_start_end)) 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df["Trip Duration"] .sum()
    print("Total Travel Time is {}." .format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df["Trip Duration"] .mean()
    print("Mean Travel Time is {}." .format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_type = df["User Type"] .value_counts()
    print("Count of User Types is {}." .format(count_user_type))

    # TO DO: Display counts of gender
    if "Gender" in df:
        gender= df ["Gender"] .value_counts()
        print ("The Counts of Gender is {}." .format(gender))

    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df:
        earliest= int( df["Birth Year"] .min() )
        print ("Earliest Year of Birth is {}." .format(earliest))
        most_recent= int( df["Birth Year"] .max() )
        print ("Most Recent Year of Birth is {}." .format(most_recent))
        most_common= int( df["Birth Year"] .mode()[0] )
        print ("Most Common Year of Birth is {}." .format(most_common))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        line_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
