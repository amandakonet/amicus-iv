# Amicus IV

Purpose: To investigate how "important" the contents of amicus briefs are in a Supreme Court justice's vote in an abortion case. 


Notes: All data to be saved on Box **only** (Amicus IV - data)

## Goal

To build a model predicting a justice's vote (yes/no) on each of the ~40 Supreme Court cases reguarding abortion from the 1970s to present. Note these models will need to consider the clustering inherent in the data.

## Available Data

The main data source is the text of 954 amicus briefs across all ~40 S.C. cases. In the model, we want to include 1) metadata on the case, justices, society, etc. and 2) measures describing contents of the amicus brief.

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

