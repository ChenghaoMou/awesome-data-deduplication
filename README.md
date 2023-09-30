

# Awesome Data Deduplication

An awesome list of data deduplication use cases, papers, tools, and methods.

## How to contribute

1. Fork this repository;
2. Install the dependencies `pip install -r requirements.txt` and `pre-commit install`;
3. Add your data to the corresponding folder by copying the `template.json` file;
4. Run `pre-commit run --all-files` to format the data;
5. Commit your changes and open a pull request to this repository.

## Textual Data

| Paper                                         | Dataset                                                                                                       | Final Data Size   | Method                    | Hardware                             | License    | Comments   |
|:----------------------------------------------|:--------------------------------------------------------------------------------------------------------------|:------------------|:--------------------------|:-------------------------------------|:-----------|:-----------|
| [NA]()                                        | [RedPajama](https://github.com/togethercomputer/RedPajama-Data)                                               | 1.2T Tokens       | SimHash (partial)         | NA                                   | Apache 2.0 |            |
| [NA]()                                        | [RedPajama](https://github.com/togethercomputer/RedPajama-Data)                                               | 1.2T Tokens       | SimHash (partial)         | NA                                   | Apache 2.0 |            |
| [NA]()                                        | [SlimPajama](https://github.com/Cerebras/modelzoo/tree/main/modelzoo/transformers/data_processing/slimpajama) | 627B Tokens       | MinHash + LSH             | NA                                   | Apache 2.0 |            |
| [Arxiv](https://arxiv.org/pdf/2309.09400.pdf) | [CulturaX](https://arxiv.org/abs/2309.09400)                                                                  | 6.3T Tokens       | MinHashLSH (per language) | 600 AWS c5.24xlarge (96/192GB * 600) |            | [^1]       |

## Image Data



## Multi-modal Data



[^1]: This uses a variant of the spark script from [text-dedup](https://github.com/ChenghaoMou/text-dedup) 🎉️;