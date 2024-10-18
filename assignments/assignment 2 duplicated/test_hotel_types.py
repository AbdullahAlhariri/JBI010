"""
JBI010: Booking.com Review Analyzer
Authors: Nora Bouwman, Emanuela Dumitru and Leon Willems

Copyright (c) 2024 - Eindhoven University of Technology, The Netherlands
This software is made available under the terms of the MIT License.
"""

import pytest
import os
from booking.hotel_types import Booking, Review, Hotel, average_score_per_country, highest_nationalities_average_score


@pytest.fixture
def hotels_and_reviews():
    path = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)),
                        'data/Hotel_Reviews_EU.csv')

    hotels_and_reviews = Booking([], [])
    hotels_and_reviews.read_csv(path)

    return hotels_and_reviews


@pytest.fixture
def hotels(hotels_and_reviews):
    list_hotels = hotels_and_reviews.hotels
    return list_hotels


@pytest.fixture
def reviews(hotels_and_reviews):
    list_reviews = hotels_and_reviews.reviews
    return list_reviews


def test_read_csv(hotels, reviews):
    msg_len_hotels = 'You have an incorrect number of Hotel objects!'
    msg_len_reviews = 'You have an incorrect number of Review objects!'
    msg_hotel_type = 'Your hotels entries are not Hotel objects!'
    msg_review_type = 'Your reviews entries are not Review objects!'

    assert len(hotels) == 1493, msg_len_hotels
    assert len(reviews) == 515738, msg_len_reviews
    assert type(hotels[0]) == Hotel, msg_hotel_type
    assert type(reviews[0]) == Review, msg_review_type


def test_perform_eda(hotels_and_reviews):
    booking_instance = hotels_and_reviews
    output = booking_instance.perform_eda()

    msg_len_output = 'Your EDA output dictionary does not contain the correct number of entries!'
    msg_neg_words =  'Your neg_word list does not contain the correct number of items '
    msg_neg_words_len = 'The total number of data points is too high or low'
    msg_pos_words_median = 'The median of the number of positive words is too high or low'
    msg_score_std = 'The standard deviation of score is too high or low'
    msg_days_rev_mean = 'The mean of days_rev is too high or low'

    assert len(output) == 4, msg_len_output
    assert len(output['neg_words']) == 2, msg_neg_words
    assert output['neg_words'][0]  == 515738, msg_neg_words_len
    assert round(output['pos_words'][1]['median'], 2) == round(11.0, 2), msg_pos_words_median
    assert round(output['score'][1]['std'], 2) == round(1.6378, 2), msg_score_std
    assert round(output['days_rev'][1]['mean'], 2) == round(354.4419317560467, 2), msg_days_rev_mean



def test_check_improvement(hotels_and_reviews):
    booking_instance = hotels_and_reviews
    hotels_improvement = booking_instance.check_improvement()

    msg_improvement_len = 'The number of entries in your hotels_improvement list is incorrect!'
    msg_improved = 'Your entry for Hotel Arena is (probably) incorrectly formatted!'
    msg_not_improved = 'Your entry for One Aldwych is (probably) incorrectly formatted!'

    assert len(hotels_improvement) == 1491, msg_improvement_len
    assert hotels_improvement['Hotel Arena'] == (7.515, 8.156, True), msg_improved # Doesn't work, see canvas clarifications
    assert hotels_improvement['One Aldwych'] == (9.181, 9.109, False), msg_not_improved # Doesn't work, see canvas clarifications


def test_get_top_and_bottom_top(hotels_and_reviews):
    booking_instance = hotels_and_reviews
    sorting_order = True
    output = booking_instance.get_top_and_bottom(sorting_order)

    msg_len_output = 'Your output list has too many or little entries!'
    msg_top_incorrect = 'Your top 10 hotels has/have incorrect median rating(s)!'

    assert len(output) == 10, msg_len_output
    assert all(value == 10.0 for _, value in output), msg_top_incorrect

def test_get_top_and_bottom_bottom(hotels_and_reviews):
    booking_instance = hotels_and_reviews
    sorting_order = False  # or False based on your needs
    output = booking_instance.get_top_and_bottom(sorting_order)

    msg_len_output = 'Your output list has too many or little entries!'
    msg_bottom_incorrect = 'Your bottom  10 hotels has/have incorrect median rating(s)!'

    assert len(output) == 10, msg_len_output
    assert all(value < 7 for _, value in output), msg_bottom_incorrect

def test_average_score_per_country(hotels_and_reviews):
    booking_instance = hotels_and_reviews
    output = average_score_per_country(booking_instance)

    msg_len_output = 'Your output dict has too many or little entries!'
    msg_values_output = 'Your output values aren\'t correct'

    assert len(output.values()) == 6, msg_len_output
    assert sum(output.values()) == 50.73, msg_values_output


def test_highest_nationalities_average_score(hotels_and_reviews):
    booking_instance = hotels_and_reviews
    output = highest_nationalities_average_score(booking_instance)
    lines: list = output.split("\n")

    msg_average_output = 'Your output average is not correct'
    msg_len_output = 'Your output list is too short or is too long'

    assert float(lines[0][47:-2]) == 10.0, msg_average_output
    assert len(lines)-1 == 4, msg_len_output
