import warnings
warnings.filterwarnings("ignore")
import pickle
import streamlit as st
import pandas as pd
import torch
import logging
import pandas as pd
from simpletransformers.seq2seq import (
    Seq2SeqModel,
    Seq2SeqArgs,
)


def count_matches(labels, preds):
    print(labels)
    print(preds)
    return sum(
        [
            1 if label == pred else 0
            for label, pred in zip(labels, preds)
        ]
    )

logging.basicConfig(level=logging.INFO)
transformers_logger = logging.getLogger("transformers")
transformers_logger.setLevel(logging.WARNING)

model_args = Seq2SeqArgs()
model_args.silent=True

path_1= "https://talentprofile.s3.amazonaws.com/data-science-model/checkpoint-3610-epoch-2/"
model = Seq2SeqModel(
    encoder_decoder_type="bart",
    encoder_decoder_name=path_1,
    args=model_args,
    use_cuda=False,
)

st.title("Job Title Normalization")
st.header("Raw Title")
raw_title = st.text_input('Raw Title',label_visibility="collapsed")
if '/' not in raw_title:
    input_title=" ".join( w.capitalize() for w in raw_title.split())
else:
    lst1=[]
    for word in raw_title.split():
        if '/' in word:
            word="/".join(w.capitalize() for w in word.split("/"))
            lst1.append(word)
        else:
            word=word.capitalize()
            lst1.append(word)
    input_title=" ".join(lst1)
    
  
with open("input_output.pickle", "rb") as file:
     input_output_dict = pickle.load(file)

if input_title:
    st.header("Normalized Job Title")
    if input_title in input_output_dict.keys():
        output_title=input_output_dict[input_title]
    else:
        output_title=model.predict([i])[0]
    st.write(output_title)
    if input_title not in input_output_dict:
        input_output_dict[input_title]=output_title
        with open('input_output.pickle', 'wb') as file:
            pickle.dump(input_output_dict,file)