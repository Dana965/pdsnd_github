import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }




# This is the first change  
# This is the second change 

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
    cities=['chicago', 'new york city', 'washington']
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    
    while True:
        try:
           city=input('Would you like to see the data for Chicago, New York City or Washington?\n').lower()
           if city in cities:
                print('Ok!')
                break
           elif city not in cities:
            print('Wrong city. Try again!')
        except:
            pass
       
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
           month=input('Which month? All, January, February, March, April, May or June?\n').lower()
           if month in months:
                print('Ok!')
                break
           elif month not in months:
            print('Wrong month. Try again!')
        except:
            pass


    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
           day=input('Which day? All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday ?\n').lower()
           if day in days:
                print('Ok!')
                break
           elif days not in days:
            print('Wrong day. Try again!')
        except:
            pass

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
 # load data file into a dataframe

    df = pd.read_csv(CITY_DATA[city])

# convert the Start Time column to datetime

    df['Start Time'] = pd.to_datetime(df['Start Time'])

# extract month and day of week from Start Time to create new columns

    df['month'] = df['Start Time'].dt.month

    df['day_of_week'] = df['Start Time'].dt.weekday_name

    df['hour'] = df['Start Time'].dt.hour
 # filter by month if applicable

    if month != 'all':

# use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']

        month = months.index(month) + 1

# filter by month to create the new dataframe

        df = df[df['month'] == month]

# filter by day of week if applicable

        if day != 'all':

# filter by day of week to create the new dataframe

            df = df[df['day_of_week'] == day.title()]
    print (df)
    return df
    
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month=df['month'].mode()[0]
    print('This is the most common month',most_common_month)

    # TO DO: display the most common day of week
    most_common_day=df['day_of_week'].mode()[0]
    print('This is the most common day of the week',most_common_day)

    # TO DO: display the most common start hour
    most_common_hour=df['hour'].mode()[0]
    print('This is the most common hour',most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station=df['Start Station'].mode()[0]
    print('This is the most common start station',most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station=df['End Station'].mode()[0]
    print('This is the most common end station : ',most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    
    df['start_end_station'] = df['Start Station'] + ' to ' + df['End Station']

    print('This is the most common combination of start and end station: ',df.start_end_station.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('This is the total travel time : ',total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('This is the mean of the travel time : ',mean_travel_time)

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_user_types=df['User Type'].value_counts()
    print('This is the count for user types : ',counts_user_types)

    # TO DO: Display counts of gender
    counts_gender=df['Gender'].value_counts()
    print('This is the count for gender : ',counts_gender)

    # TO DO: Display earliest, most recent, and most common year of birth

    earliest_year=df['Birth Year'].min()
    print('This is the earliest year : ',earliest_year)

    most_recent_year=df['Birth Year'].max()
    print('This is the most recent year : ',most_recent_year)

    most_common_year=df['Birth Year'].mode()[0]
    print('This is the most common year : ',most_common_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
   