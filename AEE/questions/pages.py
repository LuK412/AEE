from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Questions(Page):

	form_model = "player"
	form_fields = ["frauen", "atom", "grundek", "impfen", "video", "ruestung", "tempo", "aktivesh" ]


class Results(Page):
	pass


page_sequence = [
	Questions,
	Results
]
