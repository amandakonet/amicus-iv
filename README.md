# Amicus IV

Purpose: To investigate how "important" the contents of amicus briefs are in a Supreme Court justice's vote in an abortion case. 


Notes: All data to be saved on Box **only** (Amicus IV - data)

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

*Justice Level*

* ideology (mq score)
* gender

*Amicus Level (characteristics/contents)*

* Count of amicus briefs per case
* Type (num of legal, medical, feminist, etc. amicus briefs per case)
* Lexical diversity 
* Document similarity 
* Topics (using topic modeling, what are the authors discussing in briefs?)
* Frames (Dr. McCammon's qualitatively constructed "topics" - we'd either include the topic modeling frames or these, whichever are more informative)
* Sentiment around "women"
* Text "readability" or quality
* Overall sentiment 

*Author Level*

* Author count
* Author diversity measures


## Potential Models

The type of data we have (clustered) belongs to a class of data where observations are grouped in some way. Other examples included panel and longitudinal data. 

1. Random effects (or multi-level or mixed effects) models (linear regression w/constraints for different levels)
2. Bayesian models (hierarchical nature of these models suits clustered data)
3. Existing machine learning algorithms adapted with constraints 
    - GPBoost: tree boosting & mixed effects ([blog post which also links to research article](https://towardsdatascience.com/tree-boosted-mixed-effects-models-4df610b624cb) and [python implementation](https://github.com/fabsig/GPBoost))
    - MERF: Mixed Effects Random Forests ([blog post, links to research article](https://towardsdatascience.com/mixed-effects-random-forests-6ecbb85cb177) and [python implementation](https://pypi.org/project/merf/))
    - these have similar performance but GPBoost is much faster

