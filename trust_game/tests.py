from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

	def play_round(self):
		if self.player.id_in_group == self.player.random_number: 
			assert self.player.role() == "A"
		if self.player.id_in_group != self.player.random_number: 
			assert self.player.role() == "B"


		yield (pages.Welcome)
		yield (pages.Questions, {"question_1": True, "question_2": False, "question_3": False, "question_4": True})
		assert self.group.score == 4
		yield (pages.Agree)
		yield (pages.Person_A, {"sent_amount_players": 5})
		yield (pages.Person_B, {"sent_back_amount_players": 5})
		assert self.player.payoff == 10
#		Bot cannot submit the last page since I removed the next button.
#		yield (pages.Results)


