from flask import Flask, g, redirect
from flask_restful import Resource, Api, reqparse
from payment_registry import check_card
import shelve
import markdown
import os

# Create an instance of flask
app = Flask(__name__)
api = Api(app)

def get_db():
	db = getattr(g, '_database', None)
	if db is None:
		db = g._database = shelve.open('payments.db')
	return db

@app.teardown_appcontext
def teardown_db(exception):
	db = getattr(g,'_database', None)
	if db is not None:
		db.close()



class PaymentList(Resource):

	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('session_id', required=True)
		parser.add_argument('amount', required=True)
		parser.add_argument('currency', required=True)
		parser.add_argument('redirect', required=True)

		args = parser.parse_args()

		shelf = get_db()
		if not (args['session_id'] in shelf):
			shelf[args['session_id']] = args
			return {'message':'Payment added!', 'data':args}, 201
		return {'message':'Payment failed! ID already exists', 'data':{}}, 404



class Payment(Resource):
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('session_id', required=True)
		parser.add_argument('cardnumber', required=True)
		parser.add_argument('expiration[month]', required=True)
		parser.add_argument('expiration[year]', required=True)
		parser.add_argument('cvd', required=True)

		args = parser.parse_args()

		shelf = get_db()


		if not (args['session_id'] in shelf):
			return {'message':'Payment incomplete! No payment pending!', 'data':0}, 404
		# DO SOME MAGIC TRANSACTION SHIT

		if not (check_card.qvS923GxFE2VPWBH9UJsSw(args['cardnumber']) == True):
			return {'message':'Payment incomplete! Card not valid!', 'data':0}, 404


		#Get the redirect_url

		redirect_url = shelf[args['session_id']].redirect

		# Delete payment from system and redirect
		del shelf[args['session_id']]

		return {'message':'Payment complete!', 'data':1}, 404


api.add_resource(PaymentList, '/payments')
api.add_resource(Payment, '/payment')