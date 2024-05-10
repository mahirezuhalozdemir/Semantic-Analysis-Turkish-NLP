#Oluşturulan python dosyaları import edilir
from word_embedding import word_embedding
from user_gui import MyWindow
from model_classifier import model_SVM

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt
import sys

# sentences = [
#     'Ses kalitesi ergonomisi rezalet sony olduğu aldım  fiyatına çin replika ürün alsaydım iyiydi kesinlikle tavsiye etmiyorum',
#     'Hızlı teslimat teşekkürler',
#     'Ses olayı süper, gece çalıştır sıkıntı yok, kablo uzun işinizi rahat ettirir, çekme olayı son derece güzel içiniz rahat olsun, diğerlerini saymıyorum bile',
#     'Geldi bir gün, kullandık hemen bozuldu, hiç tavsiye etmem',
#     'Kulaklığın sesi kaliteli falan değil, aleti öve öve bitiremeyen yorumlar şüpheli, tizler yok, olan boğuk çıkıyor, bas kaba saba ben buradayım diyor, kalite yok, iyi ses arayanlara tavsiye etmem, hayatımda aldığım ilk snopy marka üründü, onu yorumlara güvenerek aldım, pişman oldum, hepsiburadanın sahte yorumlara karşı önlem alması gerekiyor artık',
#     ]

# labels= [-1,1,1,-1,-1]

sentence = ['Ses kalitesi ergonomisi rezalet sony olduğu aldım  fiyatına çin replika ürün alsaydım iyiydi kesinlikle tavsiye etmiyorum']
label= [-1]


if __name__ == "__main__":
    #1-) İlk olarak verisetlerinden sözlük oluştur.
    #2-) Sözlük ve yeni metin verileri ile modeli eğit.
    #3-) Eğitilen modeli tekrar kullanmak için dışarı aktar.
    #4-) Yeni veriler üzerinde model ile test işlemi gerçekleştir.

    # girdiler liste olmalıdır.
    # eğitim için  --->  model_SVM(sentences, label).model_train()
    # test için  --->  model_SVM(sentences,0).model_test()

    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())