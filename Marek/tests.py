from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        yield (views.Introduction)
        #yield (views.Instruction)
        yield (views.Choice, {"chocolate_choice": "Bio"})
        yield (views.BDM_eco, {"BDM_eco_WTP": 1.44})
        yield (views.BDM_conventional, {"BDM_conventional_WTP": 1.3})
        yield (views.Questionaire, {"eco_buy": 5, "eco_belief": 50})
        #yield (views.Results)