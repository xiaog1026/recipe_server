from flask_restx import Resource
from ..dto.card import CardDto
from ..business import card as card_service

api = CardDto.api
_cards = CardDto.cards


@api.route('/card_page=<card_page>/n_cards=<n_cards>/n_dishs=<n_dishs>')
@api.param('card_page', 'head card page no')
@api.param('n_cards', 'how many cards wanted')
@api.param('n_dishs', 'how many dishes wanted in each cards')
@api.response(404, 'Dish not found.')
class Card(Resource):
    @api.doc('get a card list, each card show some dish')
    @api.marshal_with(_cards)
    def get(self, card_page, n_cards, n_dishs):
        """get a dish given its identifier"""
        try:
            card_page = int(card_page)
            n_cards = int(n_cards)
            n_dishs = int(n_dishs)
        except Exception as e:
            api.abort(400, custom=f'invalid input {e.__str__()}')

        cards = None
        try:
            cards = card_service.get_cards(card_page, n_cards, n_dishs)
        except Exception as e:
            api.abort(400, custom=f'extract card info error {e.__str__()}')

        return cards

