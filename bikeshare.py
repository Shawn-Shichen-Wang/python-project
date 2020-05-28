import time
import pandas as pd
import numpy as np

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

    def input_mod(input_print,error_print,enterable_list):
        ret = input(input_print).lower()
        while ret not in enterable_list:
            ret = input(error_print).lower()
        return ret

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input_mod('Please input the city name:\n',
              'Error!Please input the correct city name:\n',
              CITY_DATA.keys())


    # TO DO: get user input for month (all, january, february, ... , june)
    month = input_mod('Which month? all, january, february, ... , june?\n',
                    'Please input correct month:\n',
                    ['all', 'january', 'february', 'march', 'april', 'may', 'june'])

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input_mod('Which day? all, monday, tuesday, ... sunday?\n',
                    'Please input correct day:\n',
                    ['all', 'monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday'])
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
    df['day_of_week'] = df['Start Time'].dt.day_name()
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


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('The most common month is ' + str(df['month'].mode()[0]))


    # TO DO: display the most common day of week
    print('The most common day of week is ' + str(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    print('The most common start hour is ' + str(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_most = df['Start Station'].mode()[0]
    print('The most commonly used start station is ' + start_most)

    # TO DO: display most commonly used end station
    end_most = df['End Station'].mode()[0]
    print('The most commonly used end station is ' + end_most)

    # TO DO: display most frequent combination of start station and end station trip
    top = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print("The most frequent combination of start station and end station trip is {} to {}".format(top[0], top[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('The total travel time is ' + str(df['Trip Duration'].sum()) + ' seconds')

    # TO DO: display mean travel time
    print('The mean travel time is ' + str(df['Trip Duration'].mean()) + ' seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('The counts of user types: ')
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    try :
        print('The counts of gender: ')
        print(df['Gender'].value_counts())
    # TO DO: Display earliest, most recent, and most common year of birth
        print('The earliest year of birth is ' + str(df['Birth Year'].max()))
        print('The most recent year of birth is ' + str(df['Birth Year'].min()))
        print('The most common year of birth is ' + str(df['Birth Year'].mode()[0]))

    except:
            print('error')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:

        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
