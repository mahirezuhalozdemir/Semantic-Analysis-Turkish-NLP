# Adım 5 - Kullanıcı arayüzü oluşturuldu.

#Import Libraries
import sys
import random
import requests
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt
from model_classifier import model_SVM

class MyWindow(QWidget):
    #Kullanıcı arayüzü için
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Anlam Çıkar")
        self.setGeometry(100, 100, 1000, 750)

        # Metin girişi için QTextEdit oluştur
        self.text_input = QTextEdit(self)
        self.text_input.setFixedSize(400, 400)
        self.text_input.setAlignment(Qt.AlignTop)
        self.text_input.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)

        # Butonlar için yatay düzenleyici oluştur
        buttons_layout = QHBoxLayout()

        self.classifie_text_button = QPushButton("Anlam Çıkar", self)
        self.classifie_text_button.clicked.connect(self.classifie_text)
        self.classifie_text_button.setFixedSize(150, 50)
        buttons_layout.addWidget(self.classifie_text_button)

        # Rastgele Metin butonu
        self.random_text_button = QPushButton("Rastgele Metin", self)
        self.random_text_button.setFixedSize(150, 50)
        self.random_text_button.clicked.connect(self.random_text)
        buttons_layout.addWidget(self.random_text_button)

        # Metin girişi kutusunu düzenlemek için düzenleyici oluştur
        layout = QVBoxLayout()
        layout.addWidget(self.text_input)
        layout.addLayout(buttons_layout)

        # Sonuçları gösterecek düzenleyiciler
        results_layout = QVBoxLayout()

        self.olumlu_label = QLabel("Olumlu: 0", self)
        self.olumlu_label.setAlignment(Qt.AlignLeft)
        results_layout.addWidget(self.olumlu_label)

        self.olumsuz_label = QLabel("Olumsuz: 0", self)
        self.olumsuz_label.setAlignment(Qt.AlignLeft)
        results_layout.addWidget(self.olumsuz_label)

        self.nötr_label = QLabel("Nötr: 0", self)
        self.nötr_label.setAlignment(Qt.AlignLeft)
        results_layout.addWidget(self.nötr_label)

        layout.addLayout(results_layout)
        self.setLayout(layout)

    def classifie_text(self):
        # Metin girişi alınacak
        text = self.text_input.toPlainText()
        text = str(text)
        olumlu = 0
        olumsuz = 0
        nötr = 0
        liste = []
        liste.append(text)
        #model çıktı sonucu elde edilir
        result = model_SVM(list(liste),0).model_test()
        if result == -1:
            olumsuz += 1
        elif result == 0:
            nötr += 1
        elif result == 1:
            olumlu += 1
        # Sonuçları QLabel'lara yazdır
        self.olumlu_label.setText("Olumlu: " + str(olumlu))
        self.olumsuz_label.setText("Olumsuz: " + str(olumsuz))
        self.nötr_label.setText("Nötr: " + str(nötr))

    def random_text(self):
        # Web sitesinden yorumları çekme
        url = 'https://www.scrapethissite.com/pages/'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Metinleri içeren div etiketlerini seçme
        text_divs = soup.find_all('div', class_='col-md-6 col-md-offset-3')

        # Metinleri saklamak için bir liste oluşturma
        texts = []
        for yorum_div in text_divs:
            p_etiketleri = yorum_div.find_all('p')  # <p> etiketlerini bul
            for p in p_etiketleri:
                texts.append(p.text.strip())  # Metinleri listeye ekle

        # Rastgele bir metin seçme
        if texts:
            secilen_yorum = random.choice(texts)

            # Metin giriş kutusunu temizle ve seçilen yorumu yaz
            self.text_input.clear()
            self.text_input.append(secilen_yorum)
        else:
            self.text_input.clear()
            self.text_input.append("Metin bulunamadı.")
