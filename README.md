# commit_classification
Exploring word embedding models in the task of classifying commit messages.

This is a collection of notebooks extending the work of AlOmar et al. in 'On the documentation of refactoring types'[[1]](#1), in which the authors study the practices of programmers' commit messages in relation to the refactoring type the message is associated with. To do this, machine learning models are used to train and predict 6 distinct method refactoring types from a dataset of labeled commit messages.

In this work, several methods of word embedding techniques including BERT and fastText, are used to gain additional insight into the practices of commit messages. The same dataset was used for our study. One initial train/test split was performed so each model could be compared evenly. The models compared are a replication of AlOmar et al.'s model, a model vectorized with Word2Vec[[2]](#2), a BERT model[[3]](#3), and a fastText model[[4]](#4).

This was a group project created with fellow Data Science MS students at RIT, Connor Gallagher and Pulkit Saxena.

## References
<a id="1">[1]</a> 
AlOmar, E.A., Liu, J., Addo, K. et al. On the documentation of refactoring types. 
Autom Softw Eng 29, 9 (2022). 
https://doi.org/10.1007/s10515-021-00314-w

<a id="2">[2]</a> 
Le, Quoc & Mikolov, Tomas. (2014). Distributed Representations of Sentences and Documents. 
31st International Conference on Machine Learning, ICML 2014. 4. 

<a id="3">[3]</a> 
Kamath, Uday, et al. “Bidirectional Encoder Representations from Transformers (Bert).” 
Transformers for Machine Learning, 2022, pp. 43–70., 
https://doi.org/10.1201/9781003170082-3. 

<a id="4">[4]</a> 
A. Joulin, E. Grave, P. Bojanowski, T. Mikolov, 
Bag of Tricks for Efficient Text Classification
