# <u>Home Sweet Home</u>

## <u>About this project</u>

This is the course project for CS5228 (Knowledge Discovery & Data Mining) @ NUS where the task is to predict the rental rates for HDB flats in Singapore.


## <u>Project Structure</u>

<b>1 ./config</b> : Contains yaml files/json files with hyperparameters for each specific experiment
<br>
<b>2 ./data</b> : Contains code related to loading/manipulating the dataset.
<br>
<b>5 ./experiments</b> : Contains ipynb files for showcasing each model experiment
<br>
<b>3 ./models</b> : For every experiment is a python package(i.e. directory with a init.py file) and contains the specific architectures needed
<br>
<b>4. ./resources: For storing graphs, visualizations and outputs from experiments in its respective folder.
<br>
<b>5 ./scripts</b> : Contains generic scripts for training, testing and visualizations.
<br>
<b>6 ./utils</b> : Contains util functions needed throughout the project (e.g. manipulating google drive from colab/matplotlib code)
<br>

## <u> TODO </u>

1. Find out the ordinal encoding for flat_type
2. Redo the report generation part for the whole dataset ( Report_generation_after_EDA)
3. See the correlation matrix
4. Start with KNN

Reviewing Backlog and Next Action Items (27th October):

Key comments from Prof:

1) target encoding nominal attributes with a large number of values - Adi will look into this

2) before fine-tuning KNN, try other sklearn models such as lin reg, random forests, xgboost.

My thoughts:

Find "Importance" of an Area or a Town - consolidate MRTs, Schools, Shopping Malls using "Centrality"

EDA code looks good (just some deprecated warning somewhere)
EDA flow  - normalization -> sklearn min-max?

check haversine implementation again - Parashara

Use Spearman Correlation apart from Pearson Coefficient (Pearson checks linear corr. Spearman gives an idea of transitive/non-linear corr too.) -> Sriram

two algos per person - one algo per person wont be enough.

KNN
Lin Reg(*)
Random Forests (*)
XG Boost (*)
Neural Nets
Another Algo
Another Algo

* - mentioned by Prof