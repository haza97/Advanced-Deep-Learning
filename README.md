# Advanced-Deep-Learning
Repo for What does DistilBERT learn about the syntax and semantics of language?
The experiments in this paper can be replicated by running the notebook file for all 10 .txt files in [SentEval's probing task](https://github.com/facebookresearch/SentEval/tree/main/data/probing). <br/>
The extract-features.py and classifier.py files are slightly altered after from probing section of the [Jawahar et al. (2019) repo](https://github.com/ganeshjawahar/interpret_bert/tree/master/probing) in order to work with DistilBERT and to run a loop for all six DistilBERT layers. <br/> 
The plots in Figure 1 can be generated with plots.rmd, this also includes plots for the untrained BERT and DistilBERT models. <br/>
