from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer, util
import torch

app = Flask(__name__)

model = SentenceTransformer('all-MiniLM-L6-v2')

@app.route('/cari-investor', methods=['POST'])
def cari_investor():
    data = request.get_json()

    deskripsi_supplier = data.get('deskripsi_supplier')
    deskripsi_investor_list = data.get('deskripsi_investor_list')

    if not deskripsi_supplier or not deskripsi_investor_list:
        return jsonify({'error': 'deskripsi_supplier dan deskripsi_investor_list harus diisi'}), 400

    embedding_supplier = model.encode(deskripsi_supplier, convert_to_tensor=True)
    embedding_investor_list = model.encode(deskripsi_investor_list, convert_to_tensor=True)

    similarities = util.cos_sim(embedding_supplier, embedding_investor_list)

    best_match_idx = torch.argmax(similarities)

    result = {
        'investor_cocok': deskripsi_investor_list[best_match_idx],
        'similarity_score': float(similarities[0][best_match_idx])
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
