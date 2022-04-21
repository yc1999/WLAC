import argparse
import jieba
import os

def tokenize_zh(filename):

    sentences = [] 
    dst_file = filename + ".tok"

    # read sentences from file
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            sentences.append(line.rstrip("\n"))
    
    # tokenize sentences
    tokenized_sentences = []
    for sentence in sentences:
        words = jieba.cut(sentence)
        tokenized_sentences.append(" ".join(words))

    # write segmented sentences to file
    with open(dst_file, "w", encoding="utf-8") as f:
        for sentence in tokenized_sentences:
            f.write(sentence + "\n")

def tokenize_en_de(filename, lang):

    # in this function, we will invoke scripts to tokenize sentences.
    os.system(f"bash data/run_mosesdecoder.sh {filename} {lang}")

    # read from file
    tokenized_sentences = []
    with open(filename+".tok", "r", encoding="utf-8") as f:
        for line in f:
            tokenized_sentences.append( line.rstrip("\n"))
    
    # remove file
    os.system(f"rm {filename}.norm")
    os.system(f"rm {filename}.np")
    os.system(f"rm {filename}.lc")

    return tokenized_sentences

def tokenize(lang, filename):
    
    if lang == "zh":
        tokenize_zh(filename)
    elif lang in ["de", "en"]:
        tokenize_en_de(filename, lang)
    else:
        raise ValueError("Unknown language: {}".format(lang))
    
if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--source-lang", default="zh", type=str, required=False, help="source language")
    parser.add_argument("--target-lang", default="en", type=str, required=False, help="target language")
    parser.add_argument("--file-prefix", default="data/zh-en/train", type=str, required=False, help="file prefix")
    args = parser.parse_args()

    src_file = args.file_prefix + "." + args.source_lang
    tgt_file = args.file_prefix + "." + args.target_lang

    # do tokenization for src_file and tgt_file
    print("Start tokenizing source language : {} ...".format(args.source_lang))
    tokenize(args.source_lang, src_file)
    print("Tokenization finished !")

    print("Start tokenizing target language : {} ...".format(args.target_lang))
    tokenize(args.target_lang, tgt_file)
    print("Tokenization finished !")
