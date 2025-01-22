# 3 terms -> Training Data/Training set,Validation data/vaildation set,testing data?testing set

#Training data-----

#Ml involves the formulation of a mathematical model which is capable of predicting output for any given input
#To arrive upon a numeric value of the parameters presnt i n your ML model, your algo make use of some 
#data in this process and this data is called training data and the entire process is called "model training"

#validation data----

#after learning values of your parameter you migth want to check if your learnt model is accurate or not 
#before evaluating it with a completely different set of data.the part of data which you use for this
# process is called validation data/validation set and entire process is called model validation

#test data/model testing------

#before you deploy your modelyou need to extensively evaluate whether your model is performing output prediction correctly
#this testing is called model testing and data used for this purpose is called test data.once the results of your testing process is satsfactory
#you go and deploy your modelfor real life  use cases

#Overfitting vs Underfitting

#if your ML model fails to be generic for the given training data in itself,then you say tha t your model is underfitting
#one can say that the model is too simple and hence it fails to capture

#if your ML model is able to generalise on your training data but fails to generalise on testing data then you say
#that your model is overfitting.One can say that the model is too complex and fails to generalise and captur the relationship btw generic input and ouput

#types of machine learning

#      (a)             Based on amount of external supervison required for Ml algos during model training
# ->  Supervised learning :classification based learning and regression based learning
#->  unsupervised learning :Clustering,dimensionality reduction,anomaly detection and association rule based learning
# -> semi-supervised learning

# -> reinforcement learning
#by the amount of superviison ,we mean to convey aout the availability of output to your algorithm

#supervised learning
#(i)the data which is used to train /validate/test your algorithm consists of both input and output.usually ,you provide data to your model int he form of labels which consist of input colums and output columns

#(iii)lets consider a senario where we are supposed to predict whether the give student caN GET PLACED OR NOT,IN THIS CONTWXT,
#LETS ASSUME WE KNOW the following thimgs about the student ,ID,CGPA,aptitude score,and verbal ability scxore.the final column 
#would be treu/false indicating whether the student got polaced or not .
#(iii)so the output column can consist of a countable set of values or an uncountable set of values.in the former cASE it is termed as -----"Classification based learning problem"----,whereas in the latter case it is termed as ---"regression based learning problem"

#Unsupervised learning

#Semi supervised learning
#it is partialy supervised and partially unsupervised.developed to overcoming difficulties involved in obtaining the output values for your data.you must provide the outputvalues for some of your data points and the values for the rest of the data points are automatically assighned

#reinforcement Learning:
#you provide zero data to your model to learn in RL you dont exactly have a model,but an agent is made to continuosly interact with environmentand refine its policy rules

#     (b)                based on how your ML model is utilised at production
# -- Batch/offline Learning  -> model get trained before deployment.eg mainly we use libraries like scikit learn,pandas :: problen--not adaptable
# -- Online Machine Learning -> model after deployment is continiuosly being trained with data eg youtube :: problem--security

#     (c)                based on learning process
# -- Instance based ML
# -- Model based ML


