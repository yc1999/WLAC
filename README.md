# Word-level AutoCompletion (WLAC)
This is a Shared task in WMT 2022. In this year, the shared task involves in two language pairs German-to-English (De-En) and Chinese-to-English (Zh-En) with two directions. 



# Steps 

- ❗❗❗Download the datasets for De-En and Zh-EN (see the details in next section)
- Download the scripts in the directory scripts/ to preprocess the data.
- Run the scripts to obtain the simulated training data for WLAC task from bilingual data.


# Data Preparation
## De-En Bilingual Data
The bilingual data is from WMT 14 preprocessed by Stanford NLP Group: [train.de](https://nlp.stanford.edu/projects/nmt/data/wmt14.en-de/train.de) and [train.en](https://nlp.stanford.edu/projects/nmt/data/wmt14.en-de/train.en).


## Zh-En Bilingual Data 
The bilingual data is ``UN Parallel Corpus V1.0" from WMT 17. To obtain the data, one can follow three steps: 
- Download two files [UNv1.0.en-zh.tar.gz.00](https://drive.google.com/uc?export=download&id=1rv2Yh5j-5da5RZO3DEaYvYRZKxE841hT) and
[UNv1.0.en-zh.tar.gz.01](https://drive.google.com/uc?export=download&id=1cfUezEOv5UPzF-d1uIm9-dkIUjtyZ9ys). You may also find both files yourself from [webpage](https://conferences.unite.un.org/UNCORPUS/en/DownloadOverview). 

- Run the following command to combine two files and decompress them: 
```
cat UNv1.0.en-zh.tar.gz.* | tar -xzf - 
```

- en-zh/UNv1.0.en-zh.en and en-zh/UNv1.0.en-zh.zh are source and target files. Note that both files should be preprocessed (word segmentation for zh and tokenization for en) by scripts/preprocess.py.

## Preparing the Simulated Training data for WLAC

Bilingual data can not be used to train WLAC models directly. Instead, one can obtain training data for WLAC from bilingual data via simulation following the reference [1] (See Section 3.2 in this paper). For example, this can be done by running the following cmd:


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

## Generate Samples
**After tokenization**, if we want to **generate samples** for `data/zh-en` .

Just run following commands:
1. Install `pypinyin`:
    ```bash
    pip install pypinyin
    ```
2. Run `generate_samples.py`:
    ```bash
    python data/generate_samples.py --source-lang zh --target-lang en --file-prefix data/zh-en/UNv1.0.en-zh.tok
    ```
After above command, we get one more file in folder `zh-en`:


for more details, you can check the `data/generate_samples.py`

```bash
zh-en
├── UNv1.0.en
├── train.en.tok
├── train.samples
├── train.zh
└── train.zh.tok

0 directories, 5 files
```