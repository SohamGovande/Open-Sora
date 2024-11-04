
from opensora.models.stdit import STDiT3
import pickle
import torch

model: STDiT3 = torch.load('../torchlog/debug_pickle/STDiT3_model.pt')
z_in, t, model_args = pickle.load(open('../torchlog/debug_pickle/fwd_params.pkl', 'rb'))
model(z_in, t, **model_args)