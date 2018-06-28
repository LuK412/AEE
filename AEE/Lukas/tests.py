from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        yield (pages.Instructions)
        if self.player.id_in_group == 1:
            yield (pages.Testquestion, {'guess': 9})
        else:
            yield (pages.Testquestion, {'guess': 30})
        if self.player.id_in_group == 1:
            yield (pages.AcceptStrategyOne, {'esponse_0': True,
                                             'esponse_1': True,
                                             'esponse_2': True,
                                             'esponse_3': True,
                                             'esponse_4': True,
                                             'esponse_5': True,
                                             'esponse_6': True,
                                             'esponse_7': True,
                                             'esponse_8': True,
                                             'esponse_9': True,
                                             'esponse_10': True
                                             }
                   )
        else:
            yield (pages.AcceptStrategyTwo, {'response_0': False,
                                             'response_1': False,
                                             'response_2': False,
                                             'response_3': False,
                                             'response_4': True,
                                             'response_5': True,
                                             'response_6': True,
                                             'response_7': True,
                                             'response_8': True,
                                             'response_9': True,
                                             'response_10': True
                                             }
                   )
        yield (pages.ExpQuestion, {'experience': True,
                                   'played': True}
               )
        #yield (pages.Results)