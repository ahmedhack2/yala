from flask import Flask ,request,jsonify

from chat import get_response
from search_amazon_product import extract_product_name,newsearch_amazon
app = Flask(__name__)

@app.get("/")
def index_get():
    return '<h1>E-Commerce Chat Bot</h1>'


@app.route('/api')
def api():
    # input you will find in the end of url
    user_input = request.args.get('input')
    product_name = extract_product_name(user_input)
    #if user input contain products
    if product_name != "" :
        print("User input contains a product: "+product_name)
        print("ok, i will search on amazon about "+product_name +"...")
        result = newsearch_amazon("https://www.amazon.com/s?k="+product_name)
        print(result)
        # response = get_response(user_input)
        json = {
            'input': user_input,
            'response': result,
            # 'accuracy': response.accuracy
        }
        return json
    else:
        response = get_response(user_input)
        json = {
            'input': user_input,
            'response': response,
            # 'accuracy': response.accuracy
        }
        return json

if __name__ == "__main__":
    app.run(debug=True)