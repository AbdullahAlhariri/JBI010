"""
JBI010: Booking.com Review Analyzer
Authors: Nora Bouwman, Emanuela Dumitru and Leon Willems

Copyright (c) 2024 - Eindhoven University of Technology, The Netherlands
This software is made available under the terms of the MIT License.
"""
from datetime import datetime
from typing import Any, List, Tuple, Dict
import csv
import statistics
from collections import defaultdict

# // BEGIN_TODO [Task 2] Create the Review and Hotel class
class Review:
    def __init__(self, date: str, neg_words: int, pos_words: int, score: float, days_rev: int, nationality: str):
        """
        :param date: Date as string i.e. 8/9/2015
        :param neg_words: Number of negative words as integer
        :param pos_words: Number of positive words as integer
        :param score: Score of the review as float
        :param days_rev: Days since review as integer
        :param nationality: Nationality of the reviewer as string
        """
        self.date = date
        self.pos_words = pos_words
        self.neg_words = neg_words
        self.score = score
        self.days_rev = days_rev
        self.nationality = nationality

    def __str__(self) -> str:
        return f"({self.date}, {self.score})"

# sample_review: Review = Review('8/9/2015', 10, 10, 8.3, 10, 'Saudi Arabia')
# print(sample_review) # (8/9/2015, 8.3)

class Hotel:
    def __init__(self, address: str, av_score: float, name: str, reviews: list[Review]):
        """
        :param address: Address as string
        :param av_score: Average review score as float
        :param name: Hotel name as string
        :param reviews: List of reviews as list[Review]
        """
        self.address = address
        self.av_score = av_score
        self.name = name
        self.reviews = reviews
        self.improved: bool = False
        self.median: float = 0
    def __str__(self) -> str:
        return f"({self.name}, {self.av_score}, {len(self.reviews)})"

# sample_hotel = Hotel("Vienna", 8.1, "Atlantis Hotel Vienna", [sample_review for review in range(0,325)])
# print(sample_hotel) # (Atlantis Hotel Vienna, 8.1, 325)
# // END_TODO [Task 2]


# // BEGIN_TODO [Task 3] Read in the dataset
class Booking:
    pass
    def __init__(self, hotels: list[Hotel], reviews: list[Review]):
        """
        :param hotels: List of hotels as list[Hotel]
        :param reviews: List of reviews as list[Review]
        """
        self.hotels = hotels
        self.reviews = reviews

    def read_csv(self, reviews_path: str) -> None:
        """
        Reads the csv given by reviews_path and updates self.hotels and self.reviews

        :param reviews_path: Path to reviews csv file as string
        :return: None. Updates self hotels and reviews lists according to the reviews csv file
        """

        with open(reviews_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                hotel_address: str = row[0].strip() # Address of the hotel.
                review_date: str = row[2] # Date when the reviewer posted the corresponding review.
                average_score: float = float(row[3]) # Average score of the hotel, calculated based on the latest comments in the last year.
                hotel_name: str = row[4] # Name of the hotel.
                review_total_negative_word_counts: int = int(row[7]) # Total number of words in the negative review.
                review_total_positive_word_counts: int = int(row[10]) # Total number of words in the positive review.
                reviewer_score: float = float(row[12]) # Score the reviewer has given to the hotel, based on their experience.
                days_since_review: int = int(row[14].split(' ')[0]) # Duration between the review date and the date it was collected into this dataset.
                reviewer_nationality: str = row[5]  # Nationality of the reviewer.

                hotel_addresses: list = [hotel.address for hotel in self.hotels]
                if hotel_address in hotel_addresses:
                    hotel: Hotel = self.hotels[hotel_addresses.index(hotel_address)]
                else:
                    hotel: Hotel = Hotel(hotel_address, average_score, hotel_name, [])
                    self.hotels.append(hotel)
                    hotel_addresses.append(hotel_address)

                review: Review = Review(review_date, review_total_negative_word_counts, review_total_positive_word_counts, reviewer_score, days_since_review, reviewer_nationality)
                self.reviews.append(review)
                hotel.reviews.append(review)

                self.hotels[hotel_addresses.index(hotel_address)] = hotel
# // END_TODO [Task 3]


# // BEGIN_TODO [Task 4] Exploratory data analysis
def perform_eda(self) -> dict[str,list]:
    """
    Performing exploratory data analysis on booking reviews and returning the results.

    :returns: The mean, median, and std computed of all the neg_words, pos_words, score, and days_rev attributes of review class.
    """
    neg_words = [review.neg_words for review in self.reviews]
    pos_words = [review.pos_words for review in self.reviews]
    score = [review.score for review in self.reviews]
    days_rev = [review.days_rev for review in self.reviews]

    output_dict: dict[str,list] = {
        "neg_words": [len(neg_words), {
            "mean": round(statistics.mean(neg_words), 2),
            "median": round(statistics.median(neg_words), 2),
            "std": round(statistics.stdev(neg_words), 2)
        }],
        "pos_words": [len(pos_words), {
            "mean": round(statistics.mean(pos_words), 2),
            "median": round(statistics.median(pos_words), 2),
            "std": round(statistics.stdev(pos_words), 2)
        }],
        "score": [len(score), {
            "mean": round(statistics.mean(score), 2),
            "median": round(statistics.median(score), 2),
            "std": round(statistics.stdev(score), 2)
        }],
        "days_rev": [len(days_rev), {
            "mean": round(statistics.mean(days_rev), 2),
            "median": round(statistics.median(days_rev), 2),
            "std": round(statistics.stdev(days_rev), 2)
        }],
    }

    return output_dict

Booking.perform_eda = perform_eda
# // END_TODO [Task 4]


# // BEGIN_TODO [Task 5] Own analysis
# See the report for the reason behind choosing these analyses.
# We made two analyses instead of one :-)

def average_score_per_country(booking: Booking) -> dict[str, float]:
    """
    Find the average score per country where the hotel is based and returns them.

    :param booking: Booking instance where the dataset has been loaded.
    :returns: Average score per country where the hotel is based as a dictionary.
    """
    reviews_per_country: dict = {}

    for hotel in booking.hotels:
        country: str = hotel.address.split(' ')[-1]
        if country not in reviews_per_country:
            reviews_per_country[country] = []

        (reviews_per_country[country].append(hotel.av_score))

    for country, reviews in reviews_per_country.items():
        reviews_per_country[country] = round(statistics.mean(reviews), 2)

    # Fixing for United Kingdom
    if 'Kingdom' in reviews_per_country:
        reviews_per_country['United Kingdom'] = reviews_per_country['Kingdom']
        del reviews_per_country['Kingdom']

    return reviews_per_country

def highest_nationalities_average_score(booking: Booking) -> str:
    """
    Determines the nationalities that gives the highest scores and returning them as string.

    :param booking: Booking instance where the dataset has been loaded.
    :returns: Highest nationalities average score as string.
    """

    av_score_per_nationality: dict = {}
    for review in booking.reviews:
        nationality: str = review.nationality.strip()
        if nationality == '':
            continue

        if nationality not in av_score_per_nationality:
            av_score_per_nationality[nationality] = []

        av_score_per_nationality[nationality].append(review.score)

    for nationality, av_scores in av_score_per_nationality.items():
        av_score_per_nationality[nationality] = round(statistics.mean(av_scores),2)

    highest_av_score: float = av_score_per_nationality[max(av_score_per_nationality, key=av_score_per_nationality.get)]
    highest_av_nationalities: dict = {nationality:av_score for nationality, av_score in av_score_per_nationality.items() if av_score == highest_av_score}
    return f"All the following nationalities had average of {highest_av_score}: \n" + "\n".join(highest_av_nationalities.keys())
# // END_TODO [Task 5] 


# // BEGIN_TODO [Task 6] Check score improvement
def check_improvement(self) -> dict[str, tuple]:
    """
    Checks every hotel given as param if it's reviews score in the second half has been improved compared to the first one by taking the mean. And returning the results.

    :param hotels: Hotels where checks for improvements will be done as list[Hotel].
    :returns: Returns a dict with hotel name(str) as key and first and second half mean and whether the second half has been an improvements over the fist one all as a value (tuple).
    """
    output_dict: dict = {}
    for hotel in self.hotels:
        reviews: list = sorted(hotel.reviews, key=lambda review: review.days_rev, reverse=True)
        half_point: int = round(len(reviews) / 2)

        review_scores: list = [review.score for review in reviews]

        reviews_first_half_mean: int = statistics.mean(review_scores[:half_point])
        reviews_second_half_mean: int = statistics.mean(review_scores[half_point:])

        if reviews_first_half_mean < reviews_second_half_mean:
            hotel.improved = True

        output_dict[hotel.name] = (reviews_first_half_mean, reviews_second_half_mean, hotel.improved)

    return output_dict

Booking.check_improvement = check_improvement # From canvas:  In task 6), check_improvement() should be a method of the Booking class, not a function.
# // END_TODO [Task 6]


# // BEGIN_TODO [Bonus task] Retrieve top and bottom 10 hotels
def get_top_and_bottom(self, sorting_order: bool) -> list[tuple[str, float]]:
    """
    Computes the top and bottom 10 hotels based on the review scores median of the hotels, and returns the top 10 or the bottom 10 based on sorting_order param.

    :param sorting_order: If True, returns bottom 10 hotels else top 10 hotels.
    :returns: Returns a list of tuple with the hotel name(string) as first entry and review scores(float) as second entry.
    """
    hotel_m_scores: list = []

    for hotel in booking.hotels:
        review_scores: list = [review.score for review in hotel.reviews]
        median_score: int = round(statistics.median(review_scores), 1)
        hotel_m_scores.append((hotel.name, median_score))

    hotel_m_scores_sorted: list = sorted(hotel_m_scores, key=lambda hotel_m_score: hotel_m_score[1], reverse=True)
    top_10: list = hotel_m_scores_sorted[:10]
    bottom_10: list = hotel_m_scores_sorted[-10:]

    return top_10 if sorting_order else bottom_10

Booking.get_top_and_bottom = get_top_and_bottom # From canvas: In task 7), get_top_and_bottom() should be a method of the Booking class, not a function. A list of hotels should not be a parameter.
# // END_TODO [Bonus task]

booking = Booking([], [])
booking.read_csv("data/Hotel_Reviews_EU.csv")
