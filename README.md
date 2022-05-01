# Arguments in Abortion/Reproductive Rights Amicus Briefs

Purpose: To investigate how "important" the contents of amicus briefs are in a Supreme Court justice's vote in an abortion case. 

Note: All data to be saved on Box **only** (Amicus IV - data)

## Background

There is rich existing literature on the importance of "amicus curiae" (friend of the court) briefs submitted to the U.S. Supreme Court and their influence over decision outcomes. These briefs are submitted by parties, organizations, citizens, etc. who are interested in the outcome of a particular case. The purpose of these briefs is to 1) demonstrate to the Court that the impact of the decision extends beyond the involved parties and 2) to persuade the Court to vote in their favor. Decades of research indicates that, generally, the filing of such briefs influence the outcomes of decisions, regardless of "case issue." However, there is only one existing paper that dives into the contents of the briefs. In this project, we 1) investigate text analysis/nlp tasks to identify/measure amicus brief contents and 2) empirically test whether contents influence justice votes. 

## Goal

To build a model predicting a justice's vote (yes/no) on each of the ~40 Supreme Court cases reguarding abortion from the 1970s to present. Note the clustering inherent in the data by case: we have 40 groups with 9 observations each (one per justice vote). Models will need to handle inherent clustering and small data. 

## Available Data

The main data source is the text of 741 amicus briefs across all ~40 S.C. cases regarding abortion in the United States. This is a unique dataset collected by Dr. McCammon and previous graduate students in Vanderbilt's Sociology department. In the model, we want to include 1) metadata on the case, justices, society, etc. and 2) measures describing contents of the amicus briefs.

We have dozens of potential variables categorized by the "level" they belong to:

*Societal & Cultural*

* Public views on abortion over time (from GSS survey)
* Political context (party in pres, congress, state legislatures, women in office)
* Violence against abortion 

*Case Level*

* Decision Date
* Case type (minor's rights, late-term abortion, anti-abortion protestors, etc.)
* Whether the lower court decision was in favor of feminists (repro rights) side

*Justice Level*

* ideology (mq score)
* gender

*Amicus Level (characteristics/contents)*

* Count of amicus briefs per case
* Type (num of legal, medical, feminist, etc. amicus briefs per case)
* Topics (using topic modeling, what are the authors discussing in briefs?)
* Frames (Dr. McCammon's qualitatively constructed "topics" - we'd either include the topic modeling frames or these, whichever are more informative)

*Author Level*

* Author count
* Author diversity measures

## Potential Models

The type of data we have (clustered) belongs to a class of data where observations are grouped in some way. Other examples included panel and longitudinal data. 

1. Random effects (or multi-level or mixed effects) models (linear regression w/constraints for different levels)
    - Note: This is the model used in this projects. Further models will be explored at a later date. 
3. Bayesian models (hierarchical nature of these models suits clustered data)
4. Existing machine learning algorithms adapted with constraints 
    - GPBoost: tree boosting & mixed effects ([blog post which also links to research article](https://towardsdatascience.com/tree-boosted-mixed-effects-models-4df610b624cb) and [python implementation](https://github.com/fabsig/GPBoost))
    - MERF: Mixed Effects Random Forests ([blog post, links to research article](https://towardsdatascience.com/mixed-effects-random-forests-6ecbb85cb177) and [python implementation](https://pypi.org/project/merf/))
    - these have similar performance but GPBoost is much faster


## Repository Structure

The files can be perused in the following folder order:
1. Data Cleaning
     - Contains all files used to clean data for transformers finetuning, topic modeling, and multi-level modeling.
3. EDA
     - Files for exploratory analysis 
     - Includes file for generating capstone report graphics
5. MLM-Finetuning
     - Jupyter notebooks for fine-tuning transformers (BERT, DistilBERT, and LegalBERT) on the masked-language modeling task
7. NLP
     - Contains folders for topic modeling and for zero-shot classification using the finetuned models from above. Both tasks completed entirely in python/colab notebooks
9. Modeling
     - Rmd files for multi-level modeling to test whether presence of arguments influences justice decision-making


## Acknowledgements:

Special thank you to Dr. Holly McCammon for her guidance on this project and Sarah Torrence for her support. 

