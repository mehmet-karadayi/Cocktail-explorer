import requests
from flask import Flask, render_template, request


def get_cocktails_by_letter(letter):
    url = f"https://www.thecocktaildb.com/api/json/v1/1/search.php?f={letter}"  # URL to send GET request.
    r = requests.get(url)
    data = r.json()  # Get data as a JSON.

    if data and (data['drinks'] and len(data['drinks'])):  # If API response has the data.
        docs = list()
        for doc in data['drinks']:
            # List of records to include in table.
            new_doc = [
                doc['strDrink'],
                doc['strDrinkThumb'],
                doc['strAlcoholic'],
            ]
            docs.append(new_doc)  # Put records for each cocktail into list.
        return docs


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")


@app.route('/cocktails', methods=["GET", "POST"])
def cocktails():
    cocktail_letter = request.form['cocktail_name']
    # Get list of cocktails data.
    result = get_cocktails_by_letter(cocktail_letter)
    if result:  # If data exists
        return render_template('cocktails.html', result=result)
    else:
        return render_template('error.html', result=cocktail_letter)


if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
