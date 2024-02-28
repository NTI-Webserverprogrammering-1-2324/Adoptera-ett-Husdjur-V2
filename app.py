from flask import Flask

from helper import pets

app = Flask(__name__)


@app.route('/')
def index():
  return '''
  <h1>Adopt a Pet!</h1>
  <p>Browse through the links below to find your new furry friend:</p>
  <ul> 
   <li><a href="/animals/dogs">Dogs</a></li>
   <li><a href="/animals/cats">Cats</a></li>
   <li><a href="/animals/rabbits">Rabbits</a></li>
  </ul>
   '''


@app.route('/animals/<pet_type>')
def animals(pet_type):
  html = f'<h1>List of {pet_type}</h1>'
  html += '<ul>'
  for pet in pets[pet_type]:
    html += f'<li>{pet}</li>'
  html += '</ul>'
  return html


@app.route('/animals/<pet_type>/<int:pet_id>/')
def pet(pet_type, pet_id):
  pet_data = pets[pet_type][pet_id]
  print(pet_data)
  html = ''''''
  html += f'<h1>{pet_data["name"]}</h1>'
  html += f'<img src="{pet_data["url"]}" alt="{pet_data["name"]}">'
  html += f'<p>{pet_data["description"]}</p>'
  html += '<ul>'
  html += f'<li>breed:{pet_data["breed"]}</li>'
  html += f'<li>breed:{pet_data["age"]}</li>'
  html += '</ul>'

  return html


if __name__ == '__main__':
  app.run(debug=True, host="0.0.0.0")
