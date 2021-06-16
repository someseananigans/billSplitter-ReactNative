from flask import Flask, jsonify, request
from venmo_api import Client
from flask_restful import Resource, Api, reqparse
import requests

# Intialize Flask
app = Flask(__name__)
# app.config["DEBUG"] = True

# Add Resources
api = Api(app)

host_api = 'https://api.venmo.com/v1/'


class Venmo(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('username', type=str, required=False, help="this field can not be left blank")
  parser.add_argument('password', type=str, required=False, help="this field can not be left blank")
  parser.add_argument('token', type=str, required=False, help="this field can not be left blank")
  
  # get user token
  def post(self):
    api_url = host_api + 'oauth/access_token'
    data = Venmo.parser.parse_args()
    headers = {
          "device-id": "88884260-05O3-8U81-58I1-2WA76F357GR9", 
          "Content-Type": 'application/json',
          "User-Agent": 'PostmanRuntime/7.28.0'
          }
    login_info = {
            "phone_email_or_username": data['username'],
            "password": data['password'],
            "client_id": "1"
            }
    try:
      user = requests.post(url=api_url, headers=headers, json=login_info)
      return user.json(), 200

    except:
      return {
        'message': "Unable to login", 
        'username': data['username'], 
        'password': data['password']
        }, 400
  
  # get extensive user info
  def get(self):
    api_url = host_api + 'me'
    data = Venmo.parser.parse_args()
    headers = {
      'Authorization': "Bearer {}".format(data['token']),
      "User-Agent": 'PostmanRuntime/7.28.0'
      }
    user = requests.get(url=api_url, headers=headers)
    return(user.json(), 200)

  # log out of user
  def delete(self):
    api_url = host_api + 'oauth/access_token'
    data = Venmo.parser.parse_args()
    headers = {
      'Authorization': "Bearer {}".format(data['token']),
      "User-Agent": 'PostmanRuntime/7.28.0'
      }
    user = requests.delete(url=api_url, headers=headers)
    return(user.json())



class VenmoSearch(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('token', type=str, required=False, help="this field can not be left blank")


  def get(self, user_id): 
    api_url = host_api + 'users/{}/friends?limit=5'.format(user_id)
    data = Venmo.parser.parse_args()
    headers = {
      'Authorization': "Bearer {}".format(data['token']),
      "User-Agent": 'PostmanRuntime/7.28.0'
      }
    user = requests.get(url=api_url, headers=headers)

    return(user.json())

    # client = Client(access_token='e719d4cec8da8cdcfd01328405f21dc9c8d66bc9f9c76c77df22019690630d90')
    # # Search for users. You get a maximum of 50 results per request.
    # users = client.user.search_for_users(query=name, limit=2)
    # for user in users:
    #   print(user.username)
        
    # users = client.user.get_user_friends_list(user_id='seaniepai')
    # friends_list = []
    # print (users[0])
    


api.add_resource(Venmo, '/venmo')
api.add_resource(VenmoSearch, '/venmo/<string:user_id>')

app.run(port=3000)
