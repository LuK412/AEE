from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Experiment_3(Page):
    pass

class Introduction(Page):
    pass

class Instruction(Page):
    pass

class Choice(Page):
    form_model = models.Player
    form_fields = ["chocolate_choice"]


class BDM_eco(Page):
    form_model = models.Player
    form_fields = ["BDM_eco_WTP"]

    def before_next_page(self):
    	self.player.BDM_eco_choice()


class BDM_conventional(Page):
    form_model = models.Player
    form_fields = ["BDM_conventional_WTP"]

    def before_next_page(self):
    	self.player.BDM_conventional_choice()


class Questionaire (Page):
	form_model = models.Player
	form_fields = ["eco_buy", "eco_belief", "eco_belief_experiment"]


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.calculate_payment()


class Results(Page):
    pass


page_sequence = [
    Introduction,
    #Instruction,
    Choice,
    BDM_eco,
    BDM_conventional,
    Questionaire,
    ResultsWaitPage,
    Results
]
