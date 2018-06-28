from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Experiment_2(Page):
    pass

class Testquestion(Page):
    form_model = 'player'
    form_fields = ['guess']


class Instructions(Page):
    pass


class AcceptStrategyOne(Page):
    form_model = 'group'
    form_fields = ['esponse_{}'.format(int(i)) for i in
                   Constants.offer_choices]

    def is_displayed(self):
        return self.player.id_in_group == 1


class AcceptStrategyTwo(Page):
    form_model = 'group'
    form_fields = ['response_{}'.format(int(i)) for i in
                   Constants.offer_choices]

    def is_displayed(self):
        return self.player.id_in_group == 2


class ExpQuestion(Page):

    form_model = 'player'
    form_fields = ['experience', 'played']


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):
    pass


page_sequence = [
    Experiment_2,
    Instructions,
    Testquestion,
    AcceptStrategyOne,
    AcceptStrategyTwo,
    ExpQuestion,
    ResultsWaitPage,
    Results,
]
