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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    #show_raw_data = False
    while True:
        city = input('Would you like to see data for Chicago, New York City, or Washington?\n').lower()
        if city in CITY_DATA:
            break
        else:
            print('Invalid input. Please enter a valid city name.')
    
            
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("What month's data would you like to filter by? Or type 'all' to get all data\n").lower()
        if month == 'all':
            months = ['january', 'february', 'march', 'april', 'may', 'june']
            break
           
        elif month in ['january', 'february', 'march', 'april', 'may', 'june']:
            months = ['january', 'february', 'march', 'april', 'may', 'june']
            month = months.index(month) + 1
            break
        
        else:
            print('Invalid input. Please enter a valid month')
        


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("What day of the week data would you like to see? all, monday, tuesday.... sunday?\n").lower()
        if day == 'all':
            days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        # filter by day of week to create the new dataframe
            break
        elif day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
            day = days.index(day) + 1
            break
        else:
             print('Invalid input. Please enter a valid day of the week')
        # Ask the user if they want to see raw data
    while True:
        raw_data_request = input('Would you like to see 5 lines of raw data? Enter yes or no.\n').lower()
        if raw_data_request == 'yes':
            df = pd.read_csv(CITY_DATA[city])
            start, end = 0, 5
            while True:
                print(df.iloc[start:end])
                start += 5
                end +=5
                more_data_request = input('Would you like to see more? Enter yes or no.\n').lower()
                if more_data_request != 'yes':
                    break
            break
                           
        elif raw_data_request == 'no':
            break
            
        else:
            print('Invalid input. Please enter either yes or no')
                
            
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
    path_file = CITY_DATA[city]
   
    df = pd.read_csv(path_file)
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    #df['Start Time'] = pd.to_datetime(df['Start Time'])
    #df['month'] = df['Start Time'].dt.month
    #df['day_of_week'] = df['Start Time'].dt.day_name()
    #df['hour'] = df['Start Time'].dt.hour

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print("The most common month is: ", common_month)

    # TO DO: display the most common day of week
    common_dayofweek = df['day_of_week'].mode()[0]
    print("The most common day of the week is: ", common_dayofweek)


    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print("The most common hour is: ", common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    

    # TO DO: display most commonly used start station
    common_startstation = df['Start Station'].mode()[0]
    print("The most popular Start station is: ", common_startstation)


    # TO DO: display most commonly used end station
    common_endstation = df['End Station'].mode()[0]
    print("The most popular end station is: ", common_endstation)

    # TO DO: display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + 'To' + df['End Station']
    common_trip = df['Trip'].mode()[0]

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total time travelled is: ', total_travel_time)


    # TO DO: display mean travel time
    mean_time_travel = df['Trip Duration'].mean()
    print('The average time travelled is: ', mean_time_travel)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_type = df['User Type'].value_counts()
    print('The count of users type is:', count_user_type)


    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_count = df['Gender'].value_counts()
        print('The gender count is:', gender_count)
    else:
        print("\nGender data is not available for this city.")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        common_birth_year = df['Birth Year'].mode()[0]
        print("\nEarliest Birth Year: {}".format(int(earliest_birth_year)))
        print("Most Recent Birth Year: {}".format(int(most_recent_birth_year)))
        print("Most Common Birth Year: {}".format(int(common_birth_year)))
    else:
        print("\nBirth Year data is not available for this city.")


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
        # Prompt the user if they want to see raw data
        #start_idx = 0
        #while show_raw_data:
         #   print(df.iloc[start_idx:start_idx + 5])
          #  start_idx += 5
           # raw_data_request = input('Would you like to see the next 5 lines of raw data? Enter yes or no.\n').lower()
            #if raw_data_request != 'yes':
             #   break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
