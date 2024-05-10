# Adım 1 - türkçe metin verisetleri kullanılarak sözlük oluşturuldu.(Bag of words)
# Adım 2 - eğitim ve test aşamasında verilen metinler için sözlüğe göre kelime vektörü oluşturuldu.

#Import Libraries
from sklearn.feature_extraction.text import CountVectorizer
import zeyrek
import pickle
import nltk
nltk.download('punkt')


class word_embedding():
    #Sözlük ve kelime vektörü oluşturan fonksiyonlar word_embedding sınıfı içerisine dahil edildi.

    def __init__(self, texts):
        #texts: girdi metinler listesi
        #dictionary: daha önce oluşturulan ya da oluşturulacak olan sözlük
            self.texts = texts
            self.dictionary = self.get_dictionary()

    def create_dict(self):
        #bu fonksiyon türkçe metin verilerini alarak sözlük oluşturur.
        texts = self.texts
        # CountVectorizer kullanarak özellik vektörlerini oluşturma
        vectorizer = CountVectorizer(binary=True)  # Kelimenin varlığına göre 1 veya 0 olarak kodla
        vectorizer.fit_transform(texts)  # Metinlerden kelime vektörlerini oluştur
        vocabulary = vectorizer.vocabulary_
        words = list(vocabulary.keys())

        # Adım 2 - sözlükteki kelimelerin ekleri çıkarılarak sözlük son haline getirilir
        analyzer = zeyrek.MorphAnalyzer()
        # Kelimenin köklerini tutacak bir liste oluşturalım:  stems
        stems = []

        for word in words:
            analysis = analyzer.analyze(word)
            for parse in analysis:
                if not parse:  # Eğer parse boş ise
                    continue  # Bir sonraki kelimeye geç
                else:
                    stem = parse[0].lemma
                    stems.append(stem)

        stems = list(set(stems))
        stems = {stem: indeks for indeks, stem in enumerate(stems)}
        file_path = 'dictionary.pkl'
        with open(file_path, 'wb') as file:
            pickle.dump(stems, file)
        return stems

    def word_vector(self):
       #bu fonksiyon girdi metninin kelime vektörünü oluşturur
        dictionary = self.dictionary
        texts = self.texts
        analyzer = zeyrek.MorphAnalyzer()
        #Cümleler köklerine ayrılır.
        word_vectors=[]
        for i in texts:
            words = i.split()
            word_vector = [0] * len(dictionary)  # Köklerin olduğu sayıda vektör oluşturulur
            for word in words:
                analysis = analyzer.analyze(word)
                for parse in analysis:
                    if not parse:  # Eğer parse boş ise
                        continue  # Bir sonraki kelimeye geç
                    else:
                        stem = parse[0].lemma
                        if stem in dictionary:  # Kök, kökler sözlüğünde varsa vektördeki karşılık gelen indeksi işaretleriz
                            indeks = dictionary[stem]
                            word_vector[indeks] = 1
            word_vectors.append(word_vector)
        return word_vectors

    def get_dictionary(self):
        #daha önce oluşturulan sözlük okunur
        file_path = 'dictionary.pkl'
        try:
            with open(file_path, 'rb') as file:
                dictionary = pickle.load(file)
                return dictionary
        except FileNotFoundError:
            print("File not found!")
            return None


