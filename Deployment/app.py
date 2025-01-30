    import os
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template, send_from_directory
from DeepPurpose import utils
from DeepPurpose import DTI as models
from rdkit import Chem
from rdkit.Chem import Draw

app = Flask(__name__)

# Read and parse the CSV file
file_path = 'static/data/Modified Data.csv'
data = pd.read_csv(file_path)

# Handle potential NaN values and format the data
data['uniqueDri'] = data['uniqueDri'].fillna('').astype(str).str.strip()
data['drugName'] = data['drugName'].fillna('').astype(str).str.strip()
data['uniqueTa'] = data['uniqueTa'].fillna('').astype(str).str.strip()
data['targetName'] = data['targetName'].fillna('').astype(str).str.strip()
data['organism'] = data['organism'].fillna('').astype(str).str.strip()

# Extract unique drug and target information
drugs = data[['uniqueDri', 'drugName', 'organism']].drop_duplicates().to_dict('records')
targets = data[['uniqueTa', 'targetName', 'organism']].drop_duplicates().to_dict('records')

formatted_drugs = [{"id": row['uniqueDri'], "name": row['drugName'], "organism": row['organism']} for row in drugs]
formatted_targets = [{"id": row['uniqueTa'], "name": row['targetName'], "organism": row['organism']} for row in targets]

@app.route('/')
def home():
    return render_template('index.html', drugs=formatted_drugs, targets=formatted_targets)

@app.route('/predict', methods=['POST'])
def predict():
    drug_encoding, target_encoding = 'Transformer', 'CNN'

    drug_name = request.form['drug_name']
    target_name = request.form['target_name']

    drug_data = next(item for item in formatted_drugs if item["name"] == drug_name)
    target_data = next(item for item in formatted_targets if item["name"] == target_name)

    drug_id = drug_data['id']
    target_id = target_data['id']

    X_drug = [drug_id]
    X_target = [target_id]
    y = [1]  # Dummy value for y

    X_pred = utils.data_process(X_drug, X_target, y, drug_encoding, target_encoding, split_method='no_split')

    dti_model = models.model_pretrained(path_dir='DTI_Model')
    y_pred = dti_model.predict(X_pred)

    drug_smiles = drug_id
    mol = Chem.MolFromSmiles(drug_smiles)
    img_path = os.path.join('static', 'images', f'{drug_name}.png')
    if mol:
        # Set drawing options for black bonds and background
        drawing_options = Draw.MolDrawOptions()
        drawing_options.backgroundColor = None
        img = Draw.MolToImage(mol, options=drawing_options)
        img.save(img_path)
        num_atoms = mol.GetNumAtoms()
    else:
        img_path = None
        num_atoms = 0

    output = str(y_pred[0])

    return render_template('index.html', drugs=formatted_drugs, targets=formatted_targets, prediction_text='Binding Affinity = {}'.format(output), drug_img=f'{drug_name}.png', num_atoms=num_atoms, organism=drug_data['organism'])

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.get_json(force=True)
    drug_name = data['drug_name']
    target_name = data['target_name']

    drug_data = next(item for item in formatted_drugs if item["name"] == drug_name)
    target_data = next(item for item in formatted_targets if item["name"] == target_name)

    drug_id = drug_data['id']
    target_id = target_data['id']

    X_drug = [drug_id]
    X_target = [target_id]
    y = [1]  # Dummy value for y

    X_pred = utils.data_process(X_drug, X_target, y, 'Transformer', 'CNN', split_method='no_split')

    dti_model = models.model_pretrained(path_dir='DTI_Model')
    y_pred = dti_model.predict(X_pred)

    output = str(y_pred[0])
    return jsonify(output)

# Route to serve images from the drugs, target, and pairs folders
@app.route('/images/<folder>/<filename>')
def serve_image(folder, filename):
    valid_folders = ['drugs', 'target', 'pairs']
    if folder not in valid_folders:
        return "Invalid folder", 404
    return send_from_directory(os.path.join('static', folder), filename)

@app.route('/visualization')
def visualization():
    drugs_images = os.listdir(os.path.join('static', 'drugs'))
    target_images = os.listdir(os.path.join('static', 'target'))
    pairs_images = os.listdir(os.path.join('static', 'pairs'))
    return render_template('Visualization.html', drugs_images=drugs_images, target_images=target_images, pairs_images=pairs_images)

if __name__ == "__main__":
    os.makedirs(os.path.join('static', 'images'), exist_ok=True)
    app.run(debug=True)