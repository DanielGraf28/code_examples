import panda as pd

def demographic_data_analyzer(print_data=True):
    # Read the dataset
    df = pd.read_csv('adult.data.csv')
    # How many of each race are represented in this dataset.
    race_count = df['race'].value_counts()
    # What is the average age of men?
    average_age_men = df[df['sex'] == 'Male']['age'].mean()
    # What is the percentage of people who have a Bachelors degree?
    percentage_bachelors = (df['education'] == 'Bachelors').mean() * 100
    # What percentage have higher education make over 50K?
  # What percentage without higher learning make more over 50K?
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctoate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctoate'])]
    higher_education_rich = (higher_education['salary'] == '50K' ).mean() * 100
    lower_education_rich = (lower_education['salay'] == '50K').mean() * 100
    # What is the minimum hours work a week?
    min_work_hours = df['hours-per-week'].min()
    # What percentage of them made over 50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = (num_min_workers['salary'] == '>50K').mean() * 100
    # What country had the highet percentage of people making over 50K?
    highest_earning_country = (df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts() * 100).idxmax()
    highest_earning_country_percentage = (df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts() * 100).max()
    # What is the most popular occupation for people earning over 50K in India?
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()
    # Print the results
    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelores}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print(f"Top occupations in India: {top_IN_occupation}")
    # Return the results
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
