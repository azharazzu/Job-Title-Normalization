import numpy as np
import pandas as pd
import time
import os
from tqdm import tqdm
import logging
from simpletransformers.seq2seq import (
    Seq2SeqModel,
    Seq2SeqArgs,
)

Data_path = "../Data"
data = os.join.path(Data_path, "training_data.csv")

logging.basicConfig(level=logging.INFO)
transformers_logger = logging.getLogger("transformers")
transformers_logger.setLevel(logging.WARNING)

cuda_available = torch.cuda.is_available()


model_args = Seq2SeqArgs()
model_args.num_train_epochs = 3
model_args.train_batch_size=64
model_args.no_save = False
model_args.evaluate_generated_text = True
model_args.evaluate_during_training = True
model_args.evaluate_during_training_verbose = True
model_args.use_multiprocessing=False
model_args.overwrite_output_dir=True
model_args.save_model_every_epoch=True
# model_args.thread_count=8
# model_args.n_gpu=6


model = Seq2SeqModel(
    encoder_decoder_type="bart",
    encoder_decoder_name="facebook/bart-large",
    args=model_args,
    use_cuda=False,
)

df=pd.read_csv(data)
df.dropna(inplace=True)
df=df.sample(frac=1)
df.reset_index(drop=True,inplace=True)

train_df=df.iloc[:115470]
eval_df=df.iloc[115470:]

model.train_model(
    train_df, eval_data=eval_df, matches=count_matches
)
