from otree.api import (
	models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
	Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
	name_in_url = 'questions'
	players_per_group = None
	num_rounds = 1


class Subsession(BaseSubsession):
	pass


class Group(BaseGroup):
	pass


class Player(BasePlayer):
	
	question_1 = models.BooleanField(
		choices=(
			(True, "I agree"),
			(False, "I don't agree"),
			),
		widget=widgets.RadioSelectHorizontal(),
		verbose_name="1. We need mandatory quotas for women in leadership positions.",
		doc="Turns True if the participant agrees."
		)

	question_2 = models.BooleanField(
		choices=(
			(True, "I agree"),
			(False, "I don't agree"),
			),
		widget=widgets.RadioSelectHorizontal(),
		verbose_name="2. Every country should exit from nuclear power in the long run.",
		doc="Turns True if the participant agrees."
		)

	question_3 = models.BooleanField(
		choices=(
			(True, "I agree"),
			(False, "I don't agree"),
			),
		widget=widgets.RadioSelectHorizontal(),
		verbose_name="3. We should all have an unconditional basic income.",
		doc="Turns True if the participant agrees."
		)

	question_4 = models.BooleanField(
		choices=(
			(True, "I agree"),
			(False, "I don't agree"),
			),
		widget=widgets.RadioSelectHorizontal(),
		verbose_name="4. Vaccinations should be mandatory for children.",
		doc="Turns True if the participant agrees."
		)

	question_5 = models.BooleanField(
		choices=(
			(True, "I agree"),
			(False, "I don't agree"),
			),
		widget=widgets.RadioSelectHorizontal(),
		verbose_name="5. We should employ more public video surveillance.",
		doc="Turns True if the participant agrees."
		)
