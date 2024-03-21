"""
  This module contains a Flask web application for adopting pets.

  The web application allows users to browse and adopt pets of different types, such as dogs, cats, and rabbits.

  Usage:
    - Run the application using the `python app.py` command.
    - Access the web application in a web browser at http://localhost:5000.

  Routes:
    - `/`: Renders the index page of the web application.
    - `/animals/<pet_type>`: Renders the list of animals of the specified pet type.
    - `/animals/<pet_type>/<int:pet_id>/`: Renders the details of a specific pet.

  Example:
    To view the details of a dog with ID 1, visit http://localhost:5000/animals/dog/1/

  Dependencies:
    - Flask: A micro web framework for Python.

"""

from flask import Flask

from helper import pets

app = Flask(__name__)


@app.route('/')
def index():
  """
  Renders the index page of the web application.

  Returns:
    str: HTML content of the index page.
  """
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
  """
  Renders the list of animals of the specified pet type.

  Args:
    pet_type (str): The type of pet.

  Returns:
    str: HTML content of the list of animals.
  """
  html = f'<h1>List of {pet_type}</h1>'
  html += '<ul>'
  for pet in pets[pet_type]:
    html += f'<li>{pet}</li>'
  html += '</ul>'
  return html


@app.route('/animals/<pet_type>/<int:pet_id>/')
def pet(pet_type, pet_id):
  """
  Renders the details of a specific pet.

  Args:
    pet_type (str): The type of pet.
    pet_id (int): The ID of the pet.

  Returns:
    str: HTML content of the pet details.

  Raises:
    KeyError: If the pet type or ID is not found in the pet data.

  Example:
    >>> pet('dog', 1)
    '<h1>Buddy</h1><img src="https://example.com/buddy.jpg" alt="Buddy"><p>Buddy is a friendly dog.</p><ul><li>breed:Golden Retriever</li><li>age:3</li></ul>'
  """
  pet_data = pets[pet_type][pet_id]
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
