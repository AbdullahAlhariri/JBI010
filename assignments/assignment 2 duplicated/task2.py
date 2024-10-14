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
        self.date = date #
        self.pos_words = pos_words
        self.neg_words = neg_words
        self.score = score
        self.days_rev = days_rev
        self.nationality = nationality

    def __str__(self):
        return f"({self.date}, {self.score})"

sample_review: Review = Review('8/9/2015', 10, 10, 8.3, 10, 'Saudi Arabia')
print(sample_review) # (8/9/2015, 8.3)

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
    def __str__(self):
        return f"({self.name}, {self.av_score}, {len(self.reviews)})"

sample_hotel = Hotel("Vienna", 8.1, "Atlantis Hotel Vienna", [sample_review for review in range(0,325)])
print(sample_hotel) # (Atlantis Hotel Vienna, 8.1, 325)