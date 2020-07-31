# attendance-solver
In this software students can see that  how many classes will required to make their attendance sufficient for the exams.

i.e. if any student have 30% attendance up to end of the February  month then the student can see their attendance what will be their attendance after 1 month,

if he will attend the classes in present manner.

#NOW YOU CAN KNOW WHAT WILL BE YOUR ATTENDANCE AFTER 1 MONTH #ATTENDANCE PROBLEMN SOLVE..

NOW AI CAN SOLVE UR PROBLEMN

The Process are :-
1. Use Pandas to read Excel sheet
2. Take the columns that are necessary
3. Train the Model. Devide it to train and test set
4. Then i use Standard-Scaler that transform my data such that its distribution will have a mean value 0 and standard deviation of 1.
4. Then i use PCA(Principal component analysis) because PCA finds a vector that "best represents" your data set in a much lower dimension
5. Then i use RandomForest Regressor algorithm to fit the train and test set
6. And use this algorithm to predict 
