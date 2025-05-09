# 🧠 Stroke Risk Prediction App

Aplikasi ini merupakan proyek **Dashboard Prediksi Risiko Stroke** berbasis *machine learning* menggunakan algoritma **Naive Bayes** dan dibangun dengan **Streamlit**. Tujuannya adalah untuk membantu tenaga medis mengenali risiko stroke pada pasien berdasarkan data klinis dan demografis.

---

## 📌 Fitur Aplikasi

- 🎯 **Prediksi Risiko Stroke**: Masukkan data pasien dan dapatkan hasil prediksi apakah pasien berpotensi terkena stroke.
- 📊 **Evaluasi Model**: Menampilkan metrik performa seperti akurasi, precision, recall, F1-score, dan ROC AUC.
- 📈 **Visualisasi Interaktif**: ROC Curve dan Confusion Matrix untuk memahami performa model.

---

## 🧾 Dataset

Dataset yang digunakan berisi informasi sebagai berikut:

| Fitur               | Deskripsi                                      |
|---------------------|-----------------------------------------------|
| `age`               | Usia pasien                                   |
| `gender`            | Jenis kelamin (`Male` / `Female`)             |
| `hypertension`      | Riwayat hipertensi (0 = Tidak, 1 = Ya)        |
| `heart_disease`     | Riwayat penyakit jantung (0 = Tidak, 1 = Ya)  |
| `ever_married`      | Pernah menikah (`Yes` / `No`)                 |
| `work_type`         | Jenis pekerjaan                               |
| `Residence_type`    | Tipe tempat tinggal (`Urban` / `Rural`)       |
| `avg_glucose_level` | Rata-rata kadar glukosa darah                 |
| `bmi`               | Indeks Massa Tubuh                            |
| `smoking_status`    | Status merokok                                |
| `stroke`            | Target (0 = Tidak stroke, 1 = Stroke)         |

---

## 🧠 Model

Model yang digunakan adalah **Naive Bayes** yang telah dilatih pada dataset seimbang (undersampling pada kelas mayoritas). Model disimpan dalam file `model_stroke.pkl`.

---

## 🚀 Cara Menjalankan Aplikasi

### 1. Clone Repository

```bash
git clone https://github.com/username/stroke-prediction-app.git
cd stroke-prediction-app
```

### 2. Install Dependensi
Pastikan Python 3.x telah terinstal, lalu jalankan:

``` bash
pip install -r requirements.txt
```


### 3. Struktur Folder
``` bash
stroke-prediction-app/
│
├── app.py                    # File utama aplikasi Streamlit
├── model_stroke.pkl          # File model ML yang telah dilatih
├── dataset_StrokePredicton.csv  # Dataset yang digunakan
├── requirements.txt          # Daftar dependensi Python
└── README.md                 # Dokumentasi proyek ini
```

### 4. Dependensi
Tambahkan ini ke file requirements.txt:

``` bash
nginx
Copy
Edit
streamlit
pandas
numpy
scikit-learn
matplotlib
seaborn
joblib
```
