# Adım 4 - Svm modeli oluşturularak sınıflandırma yapıldı.

#Import Libraries
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from joblib import dump, load
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from word_embedding import word_embedding
     

class model_SVM():
    def __init__(self,X,y,svm_type='linear',test_rate=0.2):
        self.X = X
        self.y = y
        self.svm_type = svm_type
        self.test_rate = test_rate

    def model_train(self):
        word_vectors = word_embedding(self.X).word_vector()

        svm_model = SVC(kernel=self.svm_type)

        X_train, X_test, y_train, y_test = train_test_split(word_vectors, self.y, test_size=self.test_rate, random_state=42)

        svm_model.fit(X_train, y_train)
        y_pred = svm_model.predict(X_test)

        #Calculate accuracy
        accuracy = accuracy_score(y_test, y_pred)*100
        #Calculate precision
        precision = precision_score(y_test, y_pred, average='weighted',zero_division=0)*100
        #Calculate recall
        recall = recall_score(y_test, y_pred, average='weighted')*100
        #Calculate F1 score
        f1 = f1_score(y_test, y_pred, average='weighted')*100

        print("Model Accuracy:", accuracy)
        print("Precision:", precision)
        print("Recall:", recall)
        print("F1 Score:", f1)
        dump(svm_model, 'svm_model.joblib')

    def model_test(self):
        #bu fonksiyon ile eğitilen model, verilen metinlerle sınıflandırma yapar
        word_vectors =word_embedding(self.X).word_vector()
        #kaydedilen model içeri aktarılarak kullanılır
        svm_model = load('svm_model.joblib')
        y_pred = svm_model.predict(word_vectors)
        return y_pred