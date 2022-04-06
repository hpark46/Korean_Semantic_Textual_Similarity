# !pip install transformers
# !pip install Flask
import pickle
from flask import request
from flask import Flask
import csv
from model_source import *
import codecs
import pandas as pd
import torch
import operator

app = Flask(__name__)


class CustomUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        try:
            return super().find_class(__name__, name)
        except AttributeError:
            return super().find_class(module, name)


tokenizer = CustomUnpickler(open('/content/drive/MyDrive/logs/roberta_large_tok', 'rb')).load()
model = CustomUnpickler(open('/content/drive/MyDrive/logs/whole_vx3', 'rb')).load()
device = torch.device('cuda')

model.eval()
model.to(device)


@app.route('/')
def sts():
    return 'STS score 0-5'


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        # we will get the file from the request
        sen_one = tokenize(tokenizer, request.args['sentence_one']).to(device)
        sen_two = tokenize(tokenizer, request.args['sentence_two']).to(device)
        score = model(sen_one, sen_two) * 5

        return str(score.tolist()[0])

    else:
        single = request.args['base_sen']
        uploaded = request.files['uploaded_file']
        all_score = []
        # reader = csv.DictReader(codecs.iterdecode(uploaded, 'utf-8'))
        sens = pd.read_csv(uploaded)['sentence'].tolist()
        print('-----------read!----------')
        for index in range(0, len(sens), 32):
            batch = prepare(tokenizer, single, sens[index:index+32])
            # batch = (bsen_one[index:index+32], bsen_two[index:index+32])
            batch = tuple(items.to(device) for items in batch)
            bsen_one, bsen_two = batch
            
            with torch.no_grad():
                pred = model(bsen_one, bsen_two)
            # print(type(pred))
            pred = pred * 5
            all_score = all_score + pred.cpu().tolist()
                
            
        
        score_dct = {i: all_score[i] for i in range(0, len(all_score))}
        return score_dct




# @app.route('/top', methods=['POST'])
# def top():
#     count = int(request.args['count'])
#     single = request.args['base_sen']
#     uploaded = request.files['uploaded']
#     scores = []
#     # for element in csv.DictReader(open(uploaded, 'r')):
#     #     sen_one = tokenize(tokenizer, single)
#     #     sen_two = tokenize(tokenizer, element)
#     #     score = model(sen_one, sen_two) * 5
#     #     scores.append(score.tolist()[0])
#     # score_dct = {i: scores[i] for i in range(0, len(scores))}
#     # return sorted(score_dct.items(), key = lambda item: item[1], reverse = True)[:count]
#     sens = pd.read_csv(uploaded)['sentence'].tolist()
#     # print(count)
#     # print(single)
#     print('-----------read!----------')
#     for index in range(0, len(sens), 32):
#         batch = prepare(tokenizer, single, sens[index:index+32])
#         # batch = (bsen_one[index:index+32], bsen_two[index:index+32])
#         batch = tuple(items.to(device) for items in batch)
#         bsen_one, bsen_two = batch
            
#         with torch.no_grad():
#             pred = model(bsen_one, bsen_two)
#         # print(type(pred))
#         pred = pred * 5
#         scores = scores + pred.cpu().tolist()
#     for i in range(len(scores)):
#         scores[i] = (i, float(scores[i]))
#     # print(scores[:10])
#     # print(type(scores))
#     scores = sorted(scores, key=operator.itemgetter(1), reverse=True)
#     # print(type(scores))
                
            
        
#     score_dct = {x: y for (x,y) in scores[:count]}
#     return score_dct
