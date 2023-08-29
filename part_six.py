# Load model directly
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("SamLowe/roberta-base-go_emotions")
model = AutoModelForSequenceClassification.from_pretrained("SamLowe/roberta-base-go_emotions")

labels = model.config.id2label
labels = list(labels.values())

from torch import nn
import numpy as np
import pandas as pd


#write function here to automate:
sequence = "type in a sequence "

tokens = tokenizer(sequence, return_tensors = 'pt')
output = model(**tokens)

probabilities = nn.functional.softmax(output.logits, dim=-1)
probabilities = [np.round(x,2) for x in probabilities.detach().numpy()[0]]

results_series = pd.Series(probabilities)
results_series.index = labels
results_series = results_series.sort_values(ascending = False)[0:5]

for i, prob in enumerate(results_series):
    print(f'{results_series.index[i]}: {prob:.2f}')