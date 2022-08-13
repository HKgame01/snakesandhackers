from flask import Flask, render_template 
import cohere
app = Flask(name)

@app.route('/') 
def home_page(): 

g=input("Enter game name: ")
co = cohere.Client('zgwXd870rQz3cVQyzJqRcQITzKsIR8lx873qlmsZ')

response = co.generate(
  model='xlarge',
  prompt=f'This program will generate games based on played games.\n--\nPlayed games: billiards\nGames: bagatelle, balkline billiards, baseball, carom billiards, eight ball, golf, pocket billiards.\n--\nPlayed games: Monopoly\nGames: checkers, chess, Chinese chess, go, goose, Monopoly, Nine Men’s Morris\n--\nPlayed games: blackjack\nGames: baccarat, Casino War, Faro, Fan Tan,pai gow poker, poker, red dog, rummy, TexasHold’em poker.\n--\nPlayed games: dice\nGames: Bank Craps, barbooth, chuck-a-luck, crown and anchor, grand hazard, hazard, poker dice\n--\nPlayed games: {g}\nGames: \n',
  max_tokens=50,
  temperature=0.9,
  k=0,
  p=0.75,
  frequency_penalty=0,
  presence_penalty=0,
  stop_sequences=[],
  return_likelihoods='NONE')
print('Prediction: {}'.format(response.generations[0].text))
return ('Prediction: {}'.format(response.generations[0].text)

if name == "main": 
app.run(host="0.0.0.0",debug=True) 
