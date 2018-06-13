from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Welcome(Page):

	pass


class Questions(Page):

	form_model = "player"
	form_fields = ["question_1", "question_2", "question_3", "question_4"]

class WaitForGroup(WaitPage):

	def after_all_players_arrive(self):
		self.group.get_score()

class Agree(Page):

	pass
		

class Person_A(Page):
	
	form_model = "player"
	form_fields = ["sent_amount_players"]

	def before_next_page(self):
		self.player.get_values_A()

#	def is_displayed(self):
#		return self.player.id_in_group == 1

class WaitForPersonA(WaitPage):
	
	def after_all_players_arrive(self):
		self.group.after_decision_A()

class Person_B(Page):
	
	form_model = "player"
	form_fields = ["sent_back_amount_players"]

#	def is_displayed(self):
#		return self.player.id_in_group == 2

	def vars_for_template(self):
		return {
		"tripled_amount": self.player.sent_by_other * Constants.multiplication_factor
		}

	def sent_back_amount_players_choices(self):
		return currency_range(
			c(0),
			self.player.sent_by_other * Constants.multiplication_factor,
			c(1)
			)


class ResultsWaitPage(WaitPage):

	def after_all_players_arrive(self):
		self.group.after_decision_B()
		self.group.get_correct_roles()
		self.group.get_payoffs()
		self.group.before_results()


class Results(Page):
	pass


page_sequence = [
	Welcome,
	Questions,
	WaitForGroup,
	Agree,
	Person_A,
	WaitForPersonA,
	Person_B,
	ResultsWaitPage,
	Results
]
