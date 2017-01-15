## Boosting NER
HORUS is meta-algorithm for Named Entity Recognition (NER) based on image processing and multi-level machine learning. It aims at boosting NER task by adding <i>apriori</i> information to the pipeline. 

Currently supports the identification of classical named-entity types (LOC, PER, ORG). It has been designed (specially) for short-texts.  
<p align="center">
<img src=http://dne5.com/whitney_example_peq.png />
</p>

## Setup
- setup [sqlite](https://sqlite.org/) database and run [our script](https://github.com/dnes85/horus-models/blob/master/horus/cache/database/horus.db.sql) to create the schema
- setup [openCV 3.1.0](http://docs.opencv.org/) or use [anaconda](https://anaconda.org/menpo/opencv3)
- get your [Microsoft Bing API](https://datamarket.azure.com/dataset/bing/search) and [Microsoft Translator API](https://datamarket.azure.com/developer/applications/register)
- set model parameters at the .ini file

## Usage 
```python
python main.py --input_text="whitney houston has been honored at nyc" --ds_format=0 --output_format="csv"

python main.py --input_file="sentences.txt" --ds_format=0

python main.py --input_file="ritter_ner.tsv" --ds_format=1 --output_file="metadata" --output_format="json"
```

## Output
```
0. IS_ENTITY ?
1. ID_SENT
2. ID_WORD
3. WORD/TERM
4. POS_UNI
5. POS
6. NER
7. COMPOUND
8. COMPOUND_SIZE
9. ID_TERM_TXT
10. ID_TERM_IMG
11. TOT_IMG
12. TOT_CV_LOC
13. TOT_CV_ORG
14. TOT_CV_PER
15. DIST_CV_I
16. PL_CV_I
17. CV_KLASS (y1)
18. TOT_RESULTS_TX 
19. TOT_TX_LOC
20. TOT_TX_ORG
21. TOT_TX_PER
22. TOT_ERR_TRANS
23. DIST_TX_I
24. TX_KLASS (y2)
25. HORUS_KLASS (y3)
```    
## Version
- 0.1.0 initial version
- 0.1.1 adding text classification
- 0.1.2 adding map detection