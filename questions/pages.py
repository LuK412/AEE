from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Questions(Page):

	form_model = "player"
	form_fields = ["question_1", "question_2", "question_3", "question_4", "question_5", ]


class Results(Page):
	pass


page_sequence = [
	Questions,
	Results
]
