<div id="top" align="center">
<img src=misc/taptap.png width=150 />

Generative Table Pre-training Empowers Models for Tabular Prediction
-----------------------------
<h3> |<a href="https://arxiv.org/abs/2305.09696"> Paper </a> | 
<a href="example.py"> Example </a> |  
<a href="https://huggingface.co/models?search=ztphs980/taptap"> 🤗 Pre-trained Model </a> |
<a href="https://huggingface.co/datasets/ztphs980/taptap_datasets"> 📚 Pre-training Dataset </a>
</h3>
</div>

This is the official Github repository for the paper "Generative Table Pre-training Empowers Models for Tabular Prediction" by Tianping Zhang, Shaowen Wang, Shuicheng Yan, Jian Li, and Qian Liu.

## Log
### 2024/3/19
os.environ["CUDA_VISIBLE_DEVICES"] = "0,1,2,3" Must give 4 gpu devices to this model (PS: I don't know why, but it work when 4 gpu all available while it dosen't work when only 2 available)

`TypeError: '<' not supported between instances of 'list' and 'int'` on `> /home/ruc/xiaotong/LLMDataGen/model/TapTap/taptap/taptap.py(167)fit() great_trainer.train(resume_from_checkpoint=resume_from_checkpoint)`
```bash
The score training by the original data is 0.8242972746040172
  0%|                                                                                                                                        | 0/1000 [00:00<?, ?it/s]Traceback (most recent call last):
  File "/home/ruc/xiaotong/LLMDataGen/model/TapTap/example.py", line 47, in <module>
    model.fit(train_data, target_col=target_col, task=task) # TypeError: '<' not supported between instances of 'list' and 'int'
  File "/home/ruc/xiaotong/LLMDataGen/model/TapTap/taptap/taptap.py", line 167, in fit
    great_trainer.train(resume_from_checkpoint=resume_from_checkpoint) # TypeError: '<' not supported between instances of 'list' and 'int'
  File "/home/ruc/.conda/envs/llmdatagen/lib/python3.9/site-packages/transformers/trainer.py", line 1624, in train
    return inner_training_loop( # TypeError: '<' not supported between instances of 'list' and 'int'
  File "/home/ruc/.conda/envs/llmdatagen/lib/python3.9/site-packages/transformers/trainer.py", line 1928, in _inner_training_loop
    for step, inputs in enumerate(epoch_iterator): # TypeError: '<' not supported between instances of 'list' and 'int'
  File "/home/ruc/.conda/envs/llmdatagen/lib/python3.9/site-packages/torch/utils/data/dataloader.py", line 631, in __next__
    data = self._next_data()
  File "/home/ruc/.conda/envs/llmdatagen/lib/python3.9/site-packages/torch/utils/data/dataloader.py", line 675, in _next_data
    data = self._dataset_fetcher.fetch(index)  # may raise StopIteration
  File "/home/ruc/.conda/envs/llmdatagen/lib/python3.9/site-packages/torch/utils/data/_utils/fetch.py", line 49, in fetch
    data = self.dataset.__getitems__(possibly_batched_index)
  File "/home/ruc/.conda/envs/llmdatagen/lib/python3.9/site-packages/datasets/arrow_dataset.py", line 2814, in __getitems__
    batch = self.__getitem__(keys)
  File "/home/ruc/.conda/envs/llmdatagen/lib/python3.9/site-packages/datasets/arrow_dataset.py", line 2810, in __getitem__
    return self._getitem(key)
  File "/home/ruc/xiaotong/LLMDataGen/model/TapTap/taptap/taptap_dataset.py", line 51, in _getitem
    row = self._data.fast_slice(key, 1)
  File "/home/ruc/.conda/envs/llmdatagen/lib/python3.9/site-packages/datasets/table.py", line 138, in fast_slice
    if offset < 0: # TypeError: '<' not supported between instances of 'list' and 'int'
TypeError: '<' not supported between instances of 'list' and 'int'
  0%|                                                                                                                                        | 0/1000 [00:00<?, ?it/s]
offset = [14968, 12277, 14741, 9199, 15070, 8155, 14868, 1908, 9803, 12628, 384, 4868, 14502, 7128, 167, 8621, 9047, 1064, 3302, 2347, 6806, 1360, 6211, 14100, 11536, 5531, 2645, 8485, 6999, 6779, 14466, 9604]
```

## Overview

Recently, the topic of table pre-training has attracted considerable research interest. However, how to employ table pre-training to boost the performance of tabular prediction (e.g., [Housing price prediction](https://www.coursera.org/projects/tensorflow-beginner-predicting-house-prices-regression)) remains an open challenge. In this project, we present **TapTap**, the first attempt that leverages table pre-training to empower models for tabular prediction.

<img src=misc/taptap_overview.jpg width=750 />

The TapTap model is firstly pre-trained on the pre-training corpus,
and then fine-tuned on the downstream table. During both pre-training and fine-tuning, tables are serialized into sequences via textual encoding, and TapTap is trained to predict them token by token. During inference, TapTap is prompted to sample values for “___” in data prompts, and the filled values build up a synthetic table. Finally, once the backbone model has yielded labels for the synthetic table, it can be used to strengthen the backbone model. In theory TapTap can be applied to any backbone model!

## Why TapTap?

TapTap can synthesize high-quality tabular data for data augmentation, privacy protection, missing value imputation, and imbalanced classification. For more details, please refer to our <a href="https://arxiv.org/abs/2305.09696"> paper </a>.

## Code

The <a href="example.py"> example </a> demonstrates the overall process of TapTap to synthesize high-quality data, including fine-tuning, sampling, and label generation.

## Datasets

### Pre-training Corpus

We have uploaded our pre-training corpus to Huggingface datasets. You can download it from [here](https://huggingface.co/datasets/ztphs980/taptap_datasets/) and use this [code](https://github.com/ZhangTP1996/TapTap/blob/master/load_pretraining_datasets.py) to load all the datasets into a dictionary of pd.DataFrame.

## Citation

If you find this repository useful in your research, please cite our paper:

```bibtex
@article{zhang2023generative,
  title={Generative Table Pre-training Empowers Models for Tabular Prediction},
  author={Zhang, Tianping and Wang, Shaowen and Yan, Shuicheng and Li, Jian and Liu, Qian},
  journal={arXiv preprint arXiv:2305.09696},
  year={2023}
}
```


## Acknowledgement

- [GreaT](https://github.com/kathrinse/be_great): TapTap is inspired a lot by the awesome work of GReaT. We thank the authors of GReaT for releasing their codebase.
- [Huggingface](https://huggingface.co/): We use the Huggingface transformers framework to pre-train / fine-tune our models. We thank the team of Huggingface for their great work.
- [DeepFloyd IF](https://huggingface.co/spaces/DeepFloyd/IF): We use the DeepFloyd IF to generate the project logo.
