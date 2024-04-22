# Git Strategies
## 1. Trunk-Based Development
![](/documentation/01-Trunk-Based.png)
---
![](/documentation/02-Trunk-Based.png)
 

## 2. Feature-Branching
![](/documentation/01-Feature-Branching.png)
---
![](/documentation/02-Feature-Branching.png)


## 3. Git Flow
![](/documentation/01-Git-Flow.png)
---
![](/documentation/02-Git-Flow.png)

## Extended Functionality with Python
Example of a scheduled job running a Python-script

```yml
name: run script.py

on:
  schedule:
    - cron: '0 0 * * 1' # At 00:00 on Monday

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: checkout repo content
        uses: actions/checkout@v4 # checkout the repository content

      - name: setup python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11' # install the python version needed

      - name: install python packages
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: execute py script # run script.py
        run: python script.py
```