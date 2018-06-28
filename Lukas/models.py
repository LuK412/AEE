from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


author = 'Lukas'

doc = """
Test, ob Leute die Instruktionen lesen.
Ultimatumspiel mit zwei Spielern und Computer.
"""


class Constants(BaseConstants):

    name_in_url = 'ultimatumgame'
    players_per_group = 2
    num_rounds = 1

    endowment = c(10)
    payoff_if_rejected = c(0)
    offer_increment = c(1)

    offer_choices = currency_range(0, endowment, offer_increment)
    offer_choices_count = len(offer_choices)

    keep_give_amounts = []
    for offer in offer_choices:
        keep_give_amounts.append((offer, endowment - offer))


class Subsession(BaseSubsession):
    pass


def question(amount):
        return 'Akzeptieren Sie ein Angebot von {}?'.format(c(amount))


class Group(BaseGroup):
    amount_offered = models.CurrencyField(min=0, max=10)

    offer_accepted = models.BooleanField(
        doc="if offered amount is accepted"
    )

    use_strategy_method = models.BooleanField(
        doc="what happens in strategy method"
    )

    # for strategy method one
    response_0 = models.BooleanField(
        widget=widgets.RadioSelectHorizontal, verbose_name=question(0))
    response_1 = models.BooleanField(
        widget=widgets.RadioSelectHorizontal, verbose_name=question(1))
    response_2 = models.BooleanField(
        widget=widgets.RadioSelectHorizontal, verbose_name=question(2))
    response_3 = models.BooleanField(
        widget=widgets.RadioSelectHorizontal, verbose_name=question(3))
    response_4 = models.BooleanField(
        widget=widgets.RadioSelectHorizontal, verbose_name=question(4))
    response_5 = models.BooleanField(
        widget=widgets.RadioSelectHorizontal, verbose_name=question(5))
    response_6 = models.BooleanField(
        widget=widgets.RadioSelectHorizontal, verbose_name=question(6))
    response_7 = models.BooleanField(
        widget=widgets.RadioSelectHorizontal, verbose_name=question(7))
    response_8 = models.BooleanField(
        widget=widgets.RadioSelectHorizontal, verbose_name=question(8))
    response_9 = models.BooleanField(
        widget=widgets.RadioSelectHorizontal, verbose_name=question(9))
    response_10 = models.BooleanField(
        widget=widgets.RadioSelectHorizontal, verbose_name=question(10))

    # for strategy method two
    esponse_0 = models.BooleanField(
        widget=widgets.RadioSelectHorizontal, verbose_name=question(0))
    esponse_1 = models.BooleanField(
        widget=widgets.RadioSelectHorizontal, verbose_name=question(1))
    esponse_2 = models.BooleanField(
        widget=widgets.RadioSelectHorizontal, verbose_name=question(2))
    esponse_3 = models.BooleanField(
        widget=widgets.RadioSelectHorizontal, verbose_name=question(3))
    esponse_4 = models.BooleanField(
        widget=widgets.RadioSelectHorizontal, verbose_name=question(4))
    esponse_5 = models.BooleanField(
        widget=widgets.RadioSelectHorizontal, verbose_name=question(5))
    esponse_6 = models.BooleanField(
        widget=widgets.RadioSelectHorizontal, verbose_name=question(6))
    esponse_7 = models.BooleanField(
        widget=widgets.RadioSelectHorizontal, verbose_name=question(7))
    esponse_8 = models.BooleanField(
        widget=widgets.RadioSelectHorizontal, verbose_name=question(8))
    esponse_9 = models.BooleanField(
        widget=widgets.RadioSelectHorizontal, verbose_name=question(9))
    esponse_10 = models.BooleanField(
        widget=widgets.RadioSelectHorizontal, verbose_name=question(10))

    def set_payoffs(self):
        p1, p2 = self.get_players()

        self.amount_offered = random.randint(0, 10)

        self.offer_accepted = getattr(self, 'response_{}'.format(
                int(self.amount_offered)))

        if self.offer_accepted:
            p1.payoff = Constants.endowment - self.amount_offered
            p2.payoff = self.amount_offered
        else:
            p1.payoff = Constants.payoff_if_rejected
            p2.payoff = Constants.payoff_if_rejected


class Player(BasePlayer):
    guess = models.IntegerField(
        min=0, max=100,
        doc="What the player guessed"
    )

    experience = models.BooleanField(
        widget=widgets.RadioSelectHorizontal, label="Haben Sie schon einmal an einem Experiment teilgenommen?"
    )

    played = models.BooleanField(
        widget=widgets.RadioSelectHorizontal, label="Kannten Sie das Ultimatumspiel bereits vorher?"
    )