import torch
import torch.nn as nn
from transformers import AutoModel


def tokenize(tokenizer, sentence):
    return tokenizer(sentence, add_special_tokens=True, padding='max_length',
                                truncation=True, max_length=128, return_tensors='pt')


class CustomPooling(nn.Module):
    def __init__(self):
        super(CustomPooling, self).__init__()

        self.robert = AutoModel.from_pretrained("klue/roberta-large")

        self.cos_score = nn.Sequential(
            nn.Identity()
        )

    def forward(self, senone, sentwo):
        output_one = self.robert(input_ids=senone['input_ids'], attention_mask=senone['attention_mask'],
                                 token_type_ids=senone['token_type_ids'])
        output_two = self.robert(input_ids=sentwo['input_ids'], attention_mask=sentwo['attention_mask'],
                                 token_type_ids=sentwo['token_type_ids'])

        pooled_one = mean_pooling_fn(output_one, senone['attention_mask'])
        pooled_two = mean_pooling_fn(output_two, sentwo['attention_mask'])

        cos_sim = torch.cosine_similarity(pooled_one, pooled_two)
        logit = self.cos_score(cos_sim)

        return logit


def mean_pooling_fn(output, attention_mask):
    att_msk = attention_mask # (batch_len, 1024)
    mask = att_msk.unsqueeze(-1).expand(output.last_hidden_state.size()).float() # (batch len, longest sentence length, 1024)
    masked_embedding = output.last_hidden_state * mask # (batch_len, longest sen len, 1024)
    me_sum = torch.sum(masked_embedding, 1) # (batch_len, 1024)
    ms_sum = torch.clamp(mask.sum(1), min=1e-9) # (batch_len, 1024)
    mean_pool = me_sum/ms_sum # batch_len, 1024
    return mean_pool
    
    
def prepare(tokenizer, sentence_one, batch):
    sen_one_list = []

    for sen_two in batch:
        sen_one_list.append(sentence_one)

    tokenized_sen_one = tokenizer(sen_one_list, add_special_tokens=True, padding='max_length',
                                truncation=True, max_length=128, return_tensors='pt')
    tokenized_sen_two = tokenizer(batch, add_special_tokens=True, padding='max_length',
                                truncation=True, max_length=128, return_tensors='pt')

    return (tokenized_sen_one, tokenized_sen_two)