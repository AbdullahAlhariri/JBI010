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
        :param reviews_path: Path to reviews csv file as string
        :return: None. Updates self hotels and reviews lists according to the reviews csv file
        """

        with open(reviews_path, 'r') as file:
            reader = csv.reader(file)
            hotel_names: list = [h.name for h in self.hotels]
            next(reader)
            for row in reader:
                hotel_address: str = row[0] # Address of the hotel.
                review_date: str = row[2] # Date when the reviewer posted the corresponding review.
                average_score: float = float(row[3]) # Average score of the hotel, calculated based on the latest comments in the last year.
                hotel_name: str = row[4] # Name of the hotel.
                review_total_negative_word_counts: int = int(row[7]) # Total number of words in the negative review.
                review_total_positive_word_counts: int = int(row[10]) # Total number of words in the positive review.
                reviewer_score: float = float(row[12]) # Score the reviewer has given to the hotel, based on their experience.
                days_since_review: int = int(row[14].split(' ')[0]) # Duration between the review date and the date it was collected into this dataset.
                reviewer_nationality: str = row[5]  # Nationality of the reviewer.

                if hotel_name in hotel_names:
                    current_hotel_index = hotel_names.index(hotel.name)
                    hotel: Hotel = self.hotels[current_hotel_index]
                else:
                    hotel: Hotel = Hotel(hotel_address, average_score, hotel_name, [])
                    self.hotels.append(hotel)
                    hotel_names.append(hotel.name)
                    current_hotel_index = hotel_names.index(hotel.name)

                review: Review = Review(review_date, review_total_negative_word_counts, review_total_positive_word_counts, reviewer_score, days_since_review, reviewer_nationality)
                self.reviews.append(review)
                hotel.reviews.append(review)

                self.hotels[current_hotel_index] = hotel