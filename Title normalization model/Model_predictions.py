import numpy as np
import pandas as pd
import time
import warnings
warnings.filterwarnings("ignore")
import torch
import time
import logging
from tqdm import tqdm
from simpletransformers.seq2seq import (
    Seq2SeqModel,
    Seq2SeqArgs,
)
from tqdm import tqdm

model_path = "https://talentprofile.s3.amazonaws.com/data-science-model/checkpoint-3610-epoch-2/"

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
cuda_available = torch.cuda.is_available()


start=time.time()
model_args = Seq2SeqArgs()
model_args.silent=True


model = Seq2SeqModel(
    encoder_decoder_type="bart",
    encoder_decoder_name= model_path,
    args=model_args,
    use_cuda=False,
)
print(time.time()-start)


norm_title = model.predict(["sr. data scientist"])
print(norm_title)
