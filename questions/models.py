from otree.api import (
	models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
	Currency as c, currency_range
)


author = 'Luisa KLing'

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
	
	frauen = models.BooleanField(
		choices=(
			(True, "Ich stimme zu"),
			(False, "Ich stimme nicht zu"),
			),
		widget=widgets.RadioSelectHorizontal(),
		verbose_name="1. Wir brauchen eine Frauenquote für Führungspositionen.",
		doc="Turns True if the participant agrees."
		)

	atom = models.BooleanField(
		choices=(
			(True, "Ich stimme zu"),
			(False, "Ich stimme nicht zu"),
			),
		widget=widgets.RadioSelectHorizontal(),
		verbose_name="2. Langfristig sollte jedes Land aus der Atomkraft aussteigen.",
		doc="Turns True if the participant agrees."
		)

	grundek = models.BooleanField(
		choices=(
			(True, "Ich stimme zu"),
			(False, "Ich stimme nicht zu"),
			),
		widget=widgets.RadioSelectHorizontal(),
		verbose_name="3. In Deutschland sollte es ein bedingungsloses Grundeinkommen geben.",
		doc="Turns True if the participant agrees."
		)

	impfen = models.BooleanField(
		choices=(
			(True, "Ich stimme zu"),
			(False, "Ich stimme nicht zu"),
			),
		widget=widgets.RadioSelectHorizontal(),
		verbose_name="4. Für Kinder sollte eine Impfpflicht bestehen.",
		doc="Turns True if the participant agrees."
		)

	video = models.BooleanField(
		choices=(
			(True, "Ich stimme zu"),
			(False, "Ich stimme nicht zu"),
			),
		widget=widgets.RadioSelectHorizontal(),
		verbose_name="5. Zur Terrorismusbekämpfung sollte es mehr Videoüberwachung im öffentlichen Raum geben.",
		doc="Turns True if the participant agrees."
		)

	ruestung = models.BooleanField(
		choices=(
			(True, "Ich stimme zu"),
			(False, "Ich stimme nicht zu"),
			),
		widget=widgets.RadioSelectHorizontal(),
		verbose_name="6. Rüstungsexporte sollten ohne Ausnahmen verboten werden.",
		doc="Turns True if the participant agrees."
		)

	tempo = models.BooleanField(
		choices=(
			(True, "Ich stimme zu"),
			(False, "Ich stimme nicht zu"),
			),
		widget=widgets.RadioSelectHorizontal(),
		verbose_name="7. Auf deutschen Autobahnen sollte ein generelles Tempolimit eingeführt werden.",
		doc="Turns True if the participant agrees."
		)

	aktivesh = models.BooleanField(
		choices=(
			(True, "Ich stimme zu"),
			(False, "Ich stimme nicht zu"),
			),
		widget=widgets.RadioSelectHorizontal(),
		verbose_name="8. Aktive Sterbehilfe sollte in Deutschland erlaubt sein.",
		doc="Turns True if the participant agrees."
		)
