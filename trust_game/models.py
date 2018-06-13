from otree.api import (
	models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
	Currency as c, currency_range
)

import random

author = 'Luisa Kling'

doc = """
A simple trust game with a measure of similarity according to the same answers to five questions.
"""


class Constants(BaseConstants):
	name_in_url = 'trust_game'
	players_per_group = 2
	num_rounds = 1

	endowment = c(10)
	multiplication_factor = 3


class Subsession(BaseSubsession):

	
	def creating_session(self):
		self.group_randomly()
		random_number = random.randint(1,2)
		for player in self.get_players():
			player.exchange_rate = self.session.config["real_world_currency_per_point"]
			player.payment = self.session.config["payment"]
			player.exchange_rate_sweets = self.session.config["exchange_rate_sweets"]
			player.random_number = random_number


class Group(BaseGroup):

	agree_q1 = models.IntegerField()
	agree_q2 = models.IntegerField()
	agree_q3 = models.IntegerField()
	agree_q4 = models.IntegerField()
#	agree_q5 = models.IntegerField()


	score = models.PositiveIntegerField()
	
	sent_amount = models.CurrencyField(
		choices=currency_range(0,Constants.endowment, c(1)),
		doc="amount sent from Person A to Person B",
		)

	sent_back_amount = models.CurrencyField()

	def get_score(self):
		p1 = self.get_player_by_id(1)
		p2 = self.get_player_by_id(2)
		
		if p1.question_1 == p2.question_1:
			self.agree_q1 = 1
		elif p1.question_1 != p2.question_1:
			self.agree_q1 = 0
		if p1.question_2 == p2.question_2:
			self.agree_q2 = 1
		elif p1.question_2 != p2.question_2:
			self.agree_q2 = 0
		if p1.question_3 == p2.question_3:
			self.agree_q3 = 1
		elif p1.question_3 != p2.question_3:
			self.agree_q3 = 0
		if p1.question_4 == p2.question_4:
			self.agree_q4 = 1
		elif p1.question_4 != p2.question_4:
			self.agree_q4 = 0
#		if p1.question_5 == p2.question_5:
#			self.agree_q5 = 1
#		elif p1.question_5 != p2.question_5:
#			self.agree_q5 = 0

		self.score = self.agree_q1 + self.agree_q2 + self.agree_q3 + self.agree_q4

	def get_correct_roles(self):
		p1 = self.get_player_by_role("A")
		p2 = self.get_player_by_role("B")
		self.sent_amount = p1.sent_amount_players
		self.sent_back_amount = p2.sent_back_amount_players

	def get_payoffs(self):
		p1 = self.get_player_by_role("A")
		p2 = self.get_player_by_role("B")
		p1.payoff = Constants.endowment - self.sent_amount + self.sent_back_amount
		p2.payoff = self.sent_amount * Constants.multiplication_factor - self.sent_back_amount

	def after_decision_A(self):
		for player in self.get_players():
			player.get_values_A()

	def after_decision_B(self):
		for player in self.get_players():
			player.get_values_B()

	def before_results(self):
		for player in self.get_players():
			player.det_final_payoff()


class Player(BasePlayer):

	random_number = models.IntegerField(doc="Turns either 1 or 2 (see subsession) and is used to randomly assign roles in the experiment (see def role).")

	# Determines the payoff relevant roles:
	def role(self):
		return "A" if self.id_in_group == self.random_number else "B"

	sent_amount_players = models.CurrencyField(
		choices=currency_range(0,Constants.endowment, c(1)),
		doc="amount sent from Person A to Person B",
		)

	sent_back_amount_players = models.CurrencyField()

	def get_values_A(self):
		self.sent_by_other = self.get_others_in_group()[0].sent_amount_players

	sent_by_other = models.CurrencyField(
		doc="amount that each player sends to the other one as person A."
		)
	
	def get_values_B(self):
		self.sent_back_by_other = self.get_others_in_group()[0].sent_back_amount_players

	sent_back_by_other = models.CurrencyField(
		doc="amount that each player sends to the other one as person A."
		)

	question_1 = models.BooleanField(
		choices=(
			(True, "Ich stimme zu"),
			(False, "Ich stimme nicht zu"),
			),
		widget=widgets.RadioSelectHorizontal(),
		verbose_name="1. Wir brauchen eine Frauenquote für Führungspositionen.",
		doc="Turns True if the participant agrees."
		)

	question_2 = models.BooleanField(
		choices=(
			(True, "Ich stimme zu"),
			(False, "Ich stimme nicht zu"),
			),
		widget=widgets.RadioSelectHorizontal(),
		verbose_name="2. In Deutschland sollte es ein bedingungsloses Grundeinkommen geben.",
		doc="Turns True if the participant agrees."
		)

	question_3 = models.BooleanField(
		choices=(
			(True, "Ich stimme zu"),
			(False, "Ich stimme nicht zu"),
			),
		widget=widgets.RadioSelectHorizontal(),
		verbose_name="3. Zur Terrorismusbekämpfung sollte es mehr Videoüberwachung im öffentlichen Raum geben.",
		doc="Turns True if the participant agrees."
		)

	question_4 = models.BooleanField(
		choices=(
			(True, "Ich stimme zu"),
			(False, "Ich stimme nicht zu"),
			),
		widget=widgets.RadioSelectHorizontal(),
		verbose_name="4. Rüstungsexporte sollten ohne Ausnahmen verboten werden.",
		doc="Turns True if the participant agrees."
		)

#	question_5 = models.BooleanField(
#		choices=(
#			(True, "Ich stimme zu"),
#			(False, "Ich stimme nicht zu"),
#			),
#		widget=widgets.RadioSelectHorizontal(),
#		verbose_name="5. We should employ more public video surveillance.",
#		doc="Turns True if the participant agrees."
#		)

	exchange_rate = models.FloatField()

	exchange_rate_sweets = models.PositiveIntegerField()

	payment = models.CharField(
		doc="indicates whether payment is in money or in sweets."
		)

	final_payoff = models.DecimalField(max_digits=5, decimal_places=2)

	def det_final_payoff(self):
		if self.payment == "money":
			self.final_payoff = float(self.payoff) * self.exchange_rate
		elif self.payment == "sweets":
			self.final_payoff = float(self.payoff) / self.exchange_rate_sweets