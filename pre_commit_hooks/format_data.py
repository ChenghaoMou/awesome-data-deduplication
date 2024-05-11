import glob
import json
import os
from typing import Sequence

import pandas as pd

template = """

# Awesome Data Deduplication

An awesome list of data deduplication use cases, papers, tools, and methods.

## How to contribute

1. Fork this repository;
2. Install the dependencies `pip install -r requirements.txt` and `pre-commit install`;
3. Add your data to the corresponding folder by copying the `template.json` file;
4. Run `pre-commit run --all-files` to format the data;
5. Commit your changes and open a pull request to this repository.

## Textual Data

{text_data}

## Image Data

{image_data}

## Multi-modal Data

{multi_modal_data}

"""
comments = []
seen_comments = {}

def load_data(path):
    global comments
    records = []
    for f in glob.glob(os.path.join(path, "*.json")):
        if f == "template.json":
            continue
        with open(f) as fp:
            data = json.load(fp)
        
        new_cell = []
        if data["Comments"]:
            for comment in data["Comments"]:
                if comment in seen_comments:
                    new_cell.append(seen_comments[comment])
                    continue
                seen_comments[comment] = f"[^{len(comments) + 1}]"
                new_cell.append(seen_comments[comment])
                comments.append(f"[^{len(comments) + 1}]: {comment}")
        data["Comments"] = ", ".join(new_cell)
        records.append(data)
    
    table = pd.DataFrame(records)
    table = table.fillna("")
    md_table = table.to_markdown(index=False)
    return md_table

def main(argv: Sequence[str] | None = None) -> int:
    
    text_data = load_data("text")
    image_data = load_data("image")
    multi_modal_data = load_data("multi-modal")

    with open("README.md", "w") as fp:
        fp.write(template.format(
            text_data=text_data,
            image_data=image_data,
            multi_modal_data=multi_modal_data
        ))

        fp.write("\n".join(comments))

    return 

if __name__ == '__main__':
    raise SystemExit(main())