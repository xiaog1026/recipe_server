from flask import request
from flask_restx import Resource

from ..dto._replica import ReplicaDto
from ..service.replica import save_new_replica, get_all_replicas, get_a_replica, get_all_replicas_of_dish

api = ReplicaDto.api
_replica = ReplicaDto.replica
_new_replica = ReplicaDto.new_replica


@api.route('/')
class ReplicaList(Resource):
    @api.doc('list up all replicas')
    @api.marshal_list_with(_replica, envelope='data')
    def get(self):
        """List all registered repicas"""
        return get_all_replicas()

    @api.response(201, 'Replica successfully created.')
    @api.doc('create a new replica')
    @api.expect(_new_replica, validate=True)
    def post(self):
        """Creates a new Replica """
        data = request.json
        return save_new_replica(data=data)


@api.route('/dish_id=<dish_id>')
@api.param('dish_id', 'dish id')
@api.response(404, 'Replica not found.')
class ReplicaListInDish(Resource):
    @api.doc('get all replicas of a dish')
    @api.marshal_list_with(_replica)
    def get(self, dish_id):
        """get a replica given its identifier"""
        return get_all_replicas_of_dish(dish_id)


@api.route('/id=<id>')
@api.param('id', 'replica id')
@api.response(404, 'Replica not found.')
class Replica(Resource):
    @api.doc('get a replica by id')
    @api.marshal_with(_replica)
    def get(self, id):
        """get a replica given its identifier"""
        replica = get_a_replica(id)
        if not replica:
            api.abort(404)
        else:
            return replica