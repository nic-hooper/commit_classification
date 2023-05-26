from flask import Flask, render_template, url_for, request
import fasttext
import re, string


def preprocess(text):
    text = text.lower() 
    text=text.strip()  
    text=re.compile('<.*?>').sub('', text) 
    text = re.sub(r'https*\S+', ' ', text) # remove links
    text = re.sub(r'http*\S+', ' ', text)
    text = re.compile('[%s]' % re.escape(string.punctuation)).sub(' ', text)  
    text = re.sub('\s+', ' ', text)  
    text = re.sub(r'\[[0-9]*\]',' ',text) 
    text=re.sub(r'[^\w\s]', '', str(text).lower().strip())
    text = re.sub(r'\d',' ',text) 
    text = re.sub(r'\s+',' ',text) 
    return text

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def main():
    
    if request.method == 'GET':
        return(render_template('main.html'))
    
    if request.method == 'POST':
        
        message = request.form['message']
        input = preprocess(message)
        model = fasttext.load_model('fasttext_model_quantized.ftz')
        prediction = model.predict(input, k=3)
        ngrams = model.get_subwords(input)
        neighbors = model.get_nearest_neighbors(input)

        
        
        return render_template('main.html', 
                               input = input, 
                               prediction = prediction, 
                               ngrams=ngrams,
                               neighbors=neighbors)

if __name__ == '__main__':
    app.run(debug=True)