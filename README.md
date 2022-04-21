# Word-level AutoCompletion (WLAC)
This is a Shared task in WMT 2022. 


# Data
This year the training/dev datasets are provided in the data directory. 

# Data Preprocessing
## Tokenization
Assuming that we want to **do tokenization** for `data/zh-en` .

At first, the folder should contain following files:
```bash
zh-en
├── train.en
└── train.zh

0 directories, 2 files
```

To tokenize, we should do following operations:
1. `cd WLAC`
2. Install `jieba` for Chinese tokenization:
   ```bash
   pip install jieba
   ```
3. Download `mosesdecoder` for English/German tokenization:
    ```bash
    git clone https://github.com/moses-smt/mosesdecoder.git
    ```
4. run `python data/tokenize.py --source-lang zh --target-lang en --file-prefix data/zh-en/train`

After above operations, we get two more tokenized files:
```bash
zh-en
├── train.en
├── train.en.tok
├── train.zh
└── train.zh.tok

0 directories, 4 files
```
For more details about tokenization, you can check `data/tokenize.py` and `data/run_mosesdecoder.sh`.


## Generate Samples
**After tokenization**, if we want to **generate samples** for `data/zh-en` .

Just run following commands:
1. Install `pypinyin`:
    ```bash
    pip install pypinyin
    ```
2. Run `generate_samples.py`:
    ```bash
    python data/generate_samples.py --source-lang zh --target-lang en --file-prefix data/zh-en/train
    ```
After above command, we get one more file in folder `zh-en`:
```bash
zh-en
├── train.en
├── train.en.tok
├── train.samples
├── train.zh
└── train.zh.tok

0 directories, 5 files
```

for more details, you can check the `data/generate_samples.py`