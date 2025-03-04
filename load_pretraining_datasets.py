from datasets import load_dataset
import pandas as pd
import numpy as np
import os 
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'

# Load pre-training tables from huggingface
# This py can not run without connecting hugging face 24/3/19
if __name__ == '__main__':
    data = {}
    dataset = load_dataset(path='ztphs980/taptap_datasets')
    dataset = dataset['train'].to_dict()
    for table_name, table in zip(dataset['dataset_name'], dataset['table']):
        table = pd.DataFrame.from_dict(eval(table, {'nan': np.nan}))
        data[table_name] = table

    # The key-value pair of data corresponds to the table name and the table (in pd.DataFrame)
