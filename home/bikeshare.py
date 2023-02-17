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
    city=input("Please , Choose City To Analyze 'chicago,new york city,washington' ")
    while(city  not in CITY_DATA):
           print("please, Enter avalible city 'chicago,new york    city,washington' ")
           city=input("again , Choose City To Analyze 'chicago,new   york city,washington' ")
            
            

    # TO DO: get user input for month (all, january, february, ... , june)
    month=input("Please,Enter the month to filter by it or all \n ")
    months=['january','february','march','april','may','june']
    while (month not in months ):
        
        print("please,Enter vaild month")
        month=input("again,Enter the month to filter by it or all \n") 
              
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=input("Please,Enter the day to filter by it or all \n ")
    days=['monday', 'tuesday', 'wednesday','thursday','friday','saturday','sunday'] 
 
    while(day not in days ):  
            print("please, Enter vaild day 'monday', 'tuesday', 'wednesday','thursday','friday','saturday','sunday' ")
            day=input("again,Enter the day to filter by it or all ")

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
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day']=df['Start Time'].dt.weekday_name
    if month!=all:
        months=['january','february','march','april','may','june']
        month=months.index(month)+1
        df=df[df['month']==month]
    
    if day!=all:
        df=df[df['day']==day.title()]
            
    return df


def display_data(df):
    show_data = input('Would you like to view 5 rows from your data? Enter yes or no\n')
    start_loc = 0
    while (show_data !='no'):
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        show_data = input("Do you wish to continue?: ").lower()

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month= df['month'].mode()[0]

    # TO DO: display the most common day of week
    most_common_day= df['day'].mode()[0]
    
    # TO DO: display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    most_common_st_hour=df['hour'].mode()[0]

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    most_common_st_station=df['Start Station'].mode()[0]
    print("most_common_start_station : "+str(most_common_st_station))
    # TO DO: display most commonly used end station
    most_common_en_station=df['End Station'].mode()[0]
    print("most_common_end_station : "+str(most_common_en_station))

    # TO DO: display most frequent combination of start station and end station trip
       
    combination_common=df[['Start Time','End Time']].mode()
    print("most_common : "+str(combination_common))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print("total_travel_time : "+str(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()   
    print("mean_travel_time : "+str(mean_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type=df['User Type'].value_counts() 
    print("counts_of_user_types : "+str(user_type))        


    # TO DO: Display counts of gender
    if city!='washington':
        
        gender_count=df['Gender'].value_counts()
        print("counts_of _gender : "+str(gender_count))        

    # TO DO: Display earliest, most recent, and most common year of birth
    if city!='washington':
            early_year=min(df['Birth Year'])
            most_recent=max(df['Birth Year'])        
            most_common_year=df['Birth Year'].mode()[0]
            print("earliest year of birth : "+str(early_year) )
            print("most recent year of birth : "+str(most_recent))
            print("most common year of birth : "+str(most_common_year))        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_data(df)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
