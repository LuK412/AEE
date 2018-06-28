from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

from django import forms

import random


author = 'Marek'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'eco_label'
    players_per_group = None
    num_rounds = 1
    endowment = 4
    eco_price = 1.1
    conv_price = 0.8
    probability = 0.18



class Subsession(BaseSubsession):
    def before_session_starts(self):
    	for player in self.get_players():
    		player.BDM_eco_price = round(random.uniform(0, 4) , 2)
    		player.BDM_conventional_price = round(random.uniform(0, 4) , 2)
    		player.Role = random.choice(['treatment', 'control'])


class Group(BaseGroup):
    def calculate_payment(self):
    	for player in self.get_players():
    		player.relevant_decision = random.choice(["erste", "zweite", "dritte"])
    		player.prob = round(random.random() , 2)
    		if player.relevant_decision == "erste" and player.chocolate_choice == "Bio":
    			player.payment = Constants.endowment - Constants.eco_price
    			player.chocolate = "Bio"
    		elif player.relevant_decision == "erste" and player.chocolate_choice == "Konventionell":
    			player.payment = Constants.endowment - Constants.conv_price
    			player.chocolate = "Konventionelle"
    		elif player.relevant_decision == "zweite" and player.BDM_eco_buy == "kaufen" and player.Role == "treatment" and player.prob>=Constants.probability:
    			player.payment = Constants.endowment - player.BDM_eco_price
    			player.chocolate = "Bio"
    		elif player.relevant_decision == "zweite" and player.BDM_eco_buy == "kaufen" and player.Role == "treatment" and player.prob<=Constants.probability:
    			player.payment = Constants.endowment - player.BDM_eco_price
    			player.chocolate = "Konventionelle"
    		elif player.relevant_decision == "zweite" and player.BDM_eco_buy == "kaufen" and player.Role == "control":
    			player.payment = Constants.endowment - player.BDM_eco_price
    			player.chocolate = "Bio"
    		elif player.relevant_decision == "zweite" and player.BDM_eco_buy == "nicht kaufen":
    			player.payment = Constants.endowment
    			player.chocolate = "keine"
    		elif player.relevant_decision == "dritte" and player.BDM_conventional_buy == "kaufen":
    			player.payment = Constants.endowment - player.BDM_conventional_price
    			player.chocolate = "Konventionelle"
    		else:
    			player.payment = Constants.endowment
    			player.chocolate = "keine"



class Player(BasePlayer):

    payment = models.FloatField(
    	doc="Participant's payment"
    	)

    chocolate = models.CharField(
    	doc="which chocolate will participant get"
    	)

    prob = models.FloatField(
		doc="if larger .7 eco is conv."
		)

    Role = models.CharField(
    	doc="role of participant, treatment or control"
    	)
    
    chocolate_choice = models.CharField(
    	choices=["Bio" , "Konventionell"],
    	widget=widgets.RadioSelect(),
    	verbose_name="Welche Schokolade möchten Sie kaufen?",
    	doc="participant's chocolate choice"
    	)

    BDM_eco_WTP = models.FloatField(
    	min=0,
    	max=2,
    	widget=widgets.SliderInput(attrs={'step': '0.01'}),
    	verbose_name="Höchster Preis, den ich für Bio-Schokolade zahlen würde",
    	doc="Participant's WTP for eco chocolate"
    	)

    BDM_eco_price = models.FloatField(
    	doc="Randomly chosen price for eco"
    	)

    BDM_conventional_WTP = models.FloatField(
    	min=0,
    	max=2,
    	widget=widgets.SliderInput(attrs={'step': '0.01'}),
    	verbose_name="Höchster Preis, den ich für konventionelle Schokolade zahlen würde",
    	doc="Participant's WTP for conventional chocolate"
    	)

    BDM_conventional_price = models.FloatField(
    	doc="Randomly chosen price for conv"
    	)

    
    BDM_eco_buy = models.CharField(
    	doc="indicates whether participant will or will not buy at BDM price eco"
    	)

    BDM_conventional_buy = models.CharField(
    	doc="indicates whether participant will or will not buy at BDM price conv"
    	)

    relevant_decision = models.CharField(
    	doc="which decision determines payment"
    	)

    eco_buy = models.IntegerField(
    	min=1,
    	max=7,
    	verbose_name="Auf einer Skala von 1 bis 7, wie wichtig finden Sie es, Bio Produkte zu kaufen? (1 bedeutet 'gar nicht wichtig', 7 bedeutet 'sehr wichtig')",
    	doc="Participant's perceived importance of buying eco"
    	)

    eco_belief = models.IntegerField(
    	min=0,
    	max=100,
    	verbose_name="Schätzen Sie: Wie viel Prozent der Produkte im Handel mit Bio-Zertifikat erfüllen auch die Bio-Standards?",
    	doc="Participant's belief about how many eco are eco"
    	)

    eco_belief_experiment = models.IntegerField(
        min=0,
        max=100,
        verbose_name="Schätzen Sie: Wie hoch (in Prozent) war in diesem Experiment die Wahrscheinlichkeit, dass Sie bei der ersten Entscheidung konventionelle Schokolade bekommen, obwohl Sie Bio-Schokolade gekauft haben?",
        blank=True,
        doc="Participant's belief about how many eco are eco in experiment"
        )

##### Any other demographics? Other experiments also include that?#######
##### Riskaversion??####

    
    def BDM_eco_choice(self):
    	#self.BDM_eco_price = random.uniform(0, 4)
    	if self.BDM_eco_price <= self.BDM_eco_WTP:
    		self.BDM_eco_buy = "kaufen"
    	else:
    		self.BDM_eco_buy = "nicht kaufen"

    def BDM_conventional_choice(self):
    	#self.BDM_conventional_price = random.uniform(0, 4)
    	if self.BDM_conventional_price <= self.BDM_conventional_WTP:
    		self.BDM_conventional_buy = "kaufen"
    	else:
    		self.BDM_conventional_buy = "nicht kaufen"

    #def BDM_maybe_eco_choice(self):
    #	#self.BDM_maybe_eco_price = random.uniform(0, 4)
    #	if self.BDM_maybe_eco_price <= self.BDM_maybe_eco_WTP:
    #		BDM_maybe_eco_buy = "kaufen"
    #	else:
    #		BDM_maybe_eco_buy = "nicht kaufen"

    #def calculate_payment(self):
    #	self.relevant_decision = random.choice("choice", "BDM_eco", "BDM_conv")
    #	if self.relevant_decision == "choice" and self.chocolate_choice == "Bio":
    #		self.payment = Constants.endowment - Constants.eco_price
    #	elif self.relevant_decision == "choice" and self.chocolate_choice == "Konventionell":
    #		self.payment = Constants.endowment - Constants.conv_price
    #	elif self.relevant_decision == "BDM_eco" and self.BDM_eco_buy == "kaufen":
    #		self.payment = Constants.endowment - self.BDM_eco_price
    #	elif self.relevant_decision == "BDM_eco" and self.BDM_eco_buy == "nicht kaufen":
    #		self.payment = Constants.endowment
    #	elif self.relevant_decision == "BDM_conv" and self.BDM_conventional_buy == "kaufen":
    #		self.payment = Constants.endowment - self.BDM_conventional_price
    #	else:
    #		self.payment = Constants.endowment


   



    #BDM_maybe_eco_WTP = models.CurrencyField(
    #	min=0,
    #	max=Constants.endowment,
    #	widget=widgets.SliderInput(attrs={'step': '0.01'}),
    #	verbose_name="Hoechster Preis, den ich für Schokolade zahlen wuerde, bei der ich nicht genau weiss, ob sie wirklich bio ist",
    #	doc="Participant's WTP for eco chocolate with maybe conventional"
    #	)

    #BDM_maybe_eco_price = models.CurrencyField(
    #	doc="Randomly chosen price for maybe eco"
    #	)

    #BDM_maybe_eco_buy = models.CharField(
    #	doc="indicates whether participant will or will not buy at BDM price maybe eco"
    #	)