from keras.models import load_model 
from keras.utils import image_dataset_from_directory

from flask import Flask, request, render_template
from PIL import Image
import numpy as np

from queue import PriorityQueue
import json

train_dir = r'...\plantnet_300K\images_train'
val_dir = r'...\plantnet_300K\images_val'
test_dir = r'...\plantnet_300K\images_test'

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/recognize')
def about():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['image']
    image = Image.open(file.stream)
    image = image.resize(size=(224, 224), )
    image_array = np.array(image)
    guess = model.predict(np.expand_dims(image_array/255, 0))
    
    return render_template('results.html', results= top_guesses(guess))

def top_guesses(guess, n:int = 5):
    q = PriorityQueue(1081)

    for i in range(len(guess[0])):
        q.put((guess[0][i]*(-1), i))
    
    results = []
            
    print("\n\nConfidence :  Species ")
    print("___________________________\n")
    for i in range(n):
        confidence, key = q.get()
        confidence = round(confidence*-(100), 1)
        key = list(species.values())[key]
        print(f'{confidence}%  : {key}  ')

        results.append((key, confidence))

    print(results)
    
    return results

def test():
    test_img = image_dataset_from_directory(
        test_dir,
        image_size=(224,224),
        batch_size=32
    )

    for images, labels in test_img.take(1):
        for i in range(1):
            key_s = test_img.class_names[labels[i]]
            print(f"\nSpecies: {species[key_s]}\n")
            
            q = predict(np.expand_dims(images[i]/255, 0))
            


with open(r"...\plantnet_300K\plantnet300K_species_names.json") as f:
    data = json.load(f)
    
species = {}
for key, value in data.items():
    species[key] = value


if __name__ == '__main__':
    model = load_model(r"...\plant_species.h5")
    
    app.run(host='127.0.0.1', port=5000, debug=True)
    #test()
