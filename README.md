# Toko Anisa (Tugas Mata Kuliah Pemrograman Berbasis Platform Gasal 2023/2024)
Dibuat oleh:
Rizki Ariffudin
2206082612
PBP E

Tautan menuju aplikasi adaptable Toko Anisa dapat diakses melalui [tautan ini](https://tokoanisa.adaptable.app/main/).

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Dalam tugas kali ini, saya menggunakan OS Windows 11, sehingga semua perintah valid untuk versi Windows bukan Linux atau yang lainnya.
### **Membuat sebuah proyek Django baru**
1. Buat direktori baru dengan nama `toko_anisa` di local disk (C:) lalu buka command prompt, masuk ke dalam direktori tersebut menggunakan perintah `cd toko_anisa`.

2. Buat virtual environment dengan perintah `python -m venv env` untuk mengisolasi proyek Python kita dan aktifkan virtual environment dengan perintah `env\Scripts\activate.bat`.

3. Buat file `requirements.txt` di dalam direktori proyek dan isi dengan daftar dependencies yang dibutuhkan untuk proyek Anda.

4. Install dependencies dengan perintah `pip install -r requirements.txt`, kemudian buat proyek Django dengan menjalankan perintah `django-admin startproject (nama_app) .`. Nama_app disesuaikan dengan keinginan (kasus kali ini diisi dengan toko_anisa), dan ini akan membuat folder baru dengan nama tersebut.

5. Buka file `settings.py` yang ada di dalam folder proyek, cari variabel `ALLOWED_HOSTS` dan ubah nilainya menjadi `["*"]` untuk mengizinkan akses dari semua host.

6. Kembali ke command prompt atau terminal dan jalankan server dengan perintah `python manage.py runserver` di dalam direktori proyek (pastikan ada file `manage.py` di sana).

7. Kita dapat membuka proyek Django baru di browser dengan mengakses http://localhost:8000. Jika melihat animasi roket, maka proyek Django sudah berhasil.

8. Untuk menghentikan server, cukup tekan `Ctrl+C` di command prompt atau terminal. Jangan lupa untuk nonaktifkan virtual environment dengan perintah `deactivate`.

> [!NOTE]
> Jika ingin mengunggah proyek ke github, disarankan membuat file `.gitignore` untuk menentukan berkas dan direktori yang harus diabaikan oleh Git.


### **Membuat aplikasi dengan nama `main` pada proyek**
1. Buka command prompt pada direktori utama dan aktifkan virtual environment dengan perintah `env\Scripts\activate.bat`.

2. Jalankan perintah `python manage.py startapp main` untuk membuat aplikasi bernama `main`, secara otomatis folder `main` juga akan terbentuk.

3. Mendaftarkan aplikasi `main` ke proyek `toko_anisa` dengan membuka file `settings.py` dalam direktori proyek dan menambahkan `'main'` pada list `INSTALLED_APPS`.
    ```python
    INSTALLED_APPS = [
        ...,
        "main",
        ...
    ]
    ```
4. Membuat direktori `templates` di dalam direktori `main` dan membuat file ```main.html``` lalu isi file dengan kode berikut.
    ```html
    <h1>Toko Anisa Page</h1>

    <h5>Name: </h5>
    <p>{{ name }}<p>
    <h5>Class: </h5>
    <p>{{ class }}<p>
    ```

### **Melakukan routing pada proyek agar dapat menjalankan aplikasi ```main```**
1. Membuat file `urls.py` di dalam direktori `toko_anisa` untuk melakukan konfigurasi routing tampilan `main`, file diisi dengan kode berikut.
    ```python
    """
    URL configuration for toko_anisa project.

    The `urlpatterns` list routes URLs to views. For more information please see:
        https://docs.djangoproject.com/en/4.2/topics/http/urls/
    Examples:
    Function views
        1. Add an import:  from my_app import views
        2. Add a URL to urlpatterns:  path('', views.home, name='home')
    Class-based views
        1. Add an import:  from other_app.views import Home
        2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
    Including another URLconf
        1. Import the include() function: from django.urls import include, path
        2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
    """
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('main/', include('main.urls')),
        path('', include('main.urls')),
    ]
    ```
### **Membuat model pada aplikasi main dengan nama Item**
1. Buka file `models.py` dan isi file tersebut dengan Class `Item` dan atribut-atribut dan tipe data yang ingin digunakan. Dalam program ini, ada 3 atribut wajib (name, amount, description).
``` python
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
```

2. Jalankan perintah `python manage.py makemigrations` untuk mempersiapkan migrasi skema model ke dalam database Django lokal.

3. Jalankan perintah `python manage.py migrate` untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal.

> [!IMPORTANT]
> Setiap kali ada perubahan pada model (menambahkan / mengurangi / mengganti atribut), wajib untuk melakukan migrasi untuk merefleksikan perubahan itu


### **Cara membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML**
1. Buat direktori baru bernama `templates` di dalam direktori aplikasi `main` dan buat file `main.html` di dalamnya

2. Buka file `views.py` dalam direktori `main` dan tambahkan `from django.shortcuts import render` untuk mengimpor fungsi render dari modul django.shortcuts untuk me-render tampilan HTML dengan menggunakan data yang diberikan.
```
from django.shortcuts import render
```

3. Buat fungsi `show_main` dengan 1 parameter (anggap namanya `request`) dan di dalam fungsinya, buat sebuah dictionary yang berisi data yang akan dikirimkan ke tampilan yang kemudian di return dengan fungsi `render` dengan 3 argumennya, yaitu `request` (objek permintaan HTTP yang dikirim oleh pengguna), nama file html yang digunakan untuk me-_render_ tampilan, dan `context` (dictionary yang berisi data untuk digunakan dalam penampilan dinamis)
```python
def show_main(request):
    context = {
        'name': 'Rizki Ariffudin',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)
```

### **Membuat sebuah routing pada urls.py aplikasi `main` untuk memetakan fungsi yang telah dibuat pada views.py**
1. Melakukan konfigurasi routing URL aplikasi ```main``` dengan memodifikasi file ```urls.py``` di direktori ```main```.
```python
from django.urls import path
from main.views import show_main
```

2. Tambahkan urlpatterns untuk menghubungkan path dengan fungsi yang telah Anda buat di `views.py`, yaitu `show_main`
```python
app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```


### **Cara _deployment_ aplikasi ke Adaptable**
1. Pastikan proyek sudah diunggah ke GitHub dengan perintah ```git add .``` ```git commit -m "<pesan_commit>"``` ```git push -u origin <branch_utama>``` secara berurutan

2. Pertama - tama sign in akun Adaptable (jika belum punya) menggunakan akun GitHub, lalu log in pilih opsi "New App" dan "Connect an Existing Repository".

3. Hubungkan Adaptable.io dengan GitHub, pilih "All Repositories" (jika baru pertama kali menghubungkan).

4. Pilih repositori proyek aplikasi yang telah diunggah ke github dan branch untuk _deployment_.

5. Pilih template deployment "Python App Template" dan pilih PostgreSQL sebagai tipe basis data.

6. Sesuaikan versi Python dengan yang dibutuhkan (cek menggunakan perintah `python --version` pada command prompt).

7. Isi Start Command dengan `python manage.py migrate && gunicorn <nama_projek_django_kamu>.wsgi`.

8. Tentukan nama aplikasi yang juga akan menjadi nama domain situs web.

9. Centang "HTTP Listener on PORT" dan klik "Deploy App" untuk memulai proses deployment aplikasi.


## **Bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya**
![Bagan](Images/Bagan-request-client.jpg)
1. Client mengakses situs web dengan membuka browser
2. Client mengunjungi situs web, kemudian web server melayani permintaan dari Client 
3. URL Router mengalihkan URL proyek berdasarkan permintaan Client (```urls.py```), kemudian dialihkan ke fungsi yang sesuai berada di ```views.py``` 
4. Views (```views.py```) mengompilasi semua yang nantinya akan ditampilkan ke template ```html```
5. Context processor mengirimkan data dari ```views.py``` ke template ```html```
6. Template ```html``` menampilkan antarmuka depan proyek berdasarkan data konteks yang diambil dari ```views.py``` dan logika dari tag-tag template
7. ```models.py``` akan mengirim data yang diminta oleh ```views.py``` yang diambil dari database
8. ```views.py``` mengembalikan data yang didapat ke Client
9. Web server menampilkan respons dari server untuk disampaikan ke Client 
10. Client mendapatkan respons dari server web

## **Mengapa kita menggunakan virtual environment?**
Virtual environment adalah bagian penting dari pengembangan perangkat lunak Python, termasuk aplikasi web berbasis Django, karena mereka menyelesaikan tantangan pengelolaan proyek dengan spesifikasi yang bervariasi. Dengan menggunakan virtual environment, kami membuat lingkungan Python yang terisolasi untuk setiap proyek,  memungkinkan kami mengelola dependensi, versi Python, dan konfigurasi yang sesuai untuk proyek tersebut tanpa mengkhawatirkan konflik dengan proyek lain atau memengaruhi instalasi Python sistem. File 'requirements.txt' memungkinkan Anda menyimpan daftar dependensi yang diperlukan oleh proyek, sehingga memfasilitasi replikasi lingkungan pengembangan pada mesin yang berbeda. Hal ini tidak hanya penting bagi tim pengembangan dalam  menjaga konsistensi konfigurasi, tetapi juga membantu  manajemen ketergantungan yang efektif. Selain itu, virtual environment  membantu menjaga keamanan proyek dengan mengisolasi lingkungan dari perpustakaan atau komponen lain yang diinstal secara global atau di proyek lain, serta mencegah konflik yang mungkin timbul akibat penggunaan yang tidak diinginkan.


## **Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?**
Meskipun secara teknis ini memungkinkan kita untuk membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, ini tidak disarankan. Penggunaan virtual environment  dalam pengembangan Django merupakan standar yang sangat penting. Tanpa virtual environment, proyek akan bergantung pada sistem instalasi Python  yang ada di komputer Anda, yang dapat menyebabkan komplikasi. Salah satunya adalah konflik ketergantungan, dimana proyek yang berbeda memerlukan versi perpustakaan yang berbeda. Selain itu,  tanpa menggunakan virtual environment, Anda akan menghadapi tantangan dengan manajemen ketergantungan, ketergantungan keseluruhan pada lingkungan Python sistem, dan potensi masalah keamanan. Dengan menggunakan virtual environment, kami membuat lingkungan Python yang terisolasi untuk setiap proyek, memungkinkan  dependensi, versi Python, dan keamanan proyek dikelola secara independen. Hal ini juga mempermudah pengelolaan ketergantungan dan menghindari konflik antar proyek kami, sehingga menjaga kebersihan, stabilitas, dan keamanan selama pengembangan proyek di masa mendatang.


## **Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya**
MVC (Model-View-Controller), MVT (Model-View-Template) dan MVVM (Model-View-ViewModel) adalah pola arsitektur perangkat lunak yang digunakan dalam pengembangan aplikasi untuk memisahkan komponen aplikasi dari berbagai aplikasi  agar lebih terstruktur dan sederhana. untuk mengelola. Meskipun keduanya memiliki kesamaan dalam alokasi tugas, namun digunakan dalam konteks yang berbeda dan terdapat perbedaan dalam cara pengorganisasian komponen-komponen ini.

Pada MVC, MVT, dan MVVM ketiganya memiliki kesamaan dalam struktur, yaitu terdapat model dan view:
1. Model --> Bagian yang mengelola data dari aplikasi. Mulai dari mengakses, memanipulasi, validasi, hingga perhitungan dari data yang dimiliki aplikasi maupun dari sumber lain.
2. View --> Bagian yang mengelola tampilan untuk diberikan kepada pengguna ketika menggunakan aplikasi. View akan mengakses data-data melalui model lalu data tersebut ditampilkan ke layar pengguna.


### MVC (Model - View - Controller)
| **Model** | **View** | **Controller** |
| --- | --- | --- |
| Menyajikan data aplikasi dan aturan bisnis. Ini adalah pihak yang bertanggung jawab untuk mengakses dan memanipulasi data, baik dari database atau sumber lain. Model juga mendefinisikan logika bisnis, seperti validasi  dan perhitungan data. Misalnya, jika kita ingin mengembangkan aplikasi e-commerce, modelnya mengatur bagaimana data produk, pelanggan, dan pesanan disimpan dan diakses. | Bagian manajemen ditampilkan kepada pengguna. Inilah yang dilihat pengguna saat berinteraksi dengan aplikasi yang kita buat. Tugas View hanyalah mengekstrak data dari model dan menampilkannya di layar. Misalnya, dalam aplikasi e-commerce, tampilan akan menampilkan daftar produk dan detail pesanan kepada pengguna. | Bagian  perantara antara model dan tampilan. Ini mengelola aliran informasi dalam aplikasi. Controller menangani permintaan pengguna, memprosesnya, dan mengirimkannya ke model untuk memperbarui data atau mengambil data yang diperlukan. Misalnya pada aplikasi e-commerce. Jika pengguna menambahkan produk ke keranjang, controller akan meminta model untuk menyimpan data ini dan kemudian meminta tampilan untuk memperbarui tampilan. |

### MVT (Model - View - Template)
| **Model** | **View** | **Template** |
| --- | --- | --- |
| Seperti MVC, model adalah komponen konsep MVT yang bertanggung jawab untuk mengatur dan mengelola data aplikasi. Model mewakili struktur data dan logika aplikasi di balik tampilan. Model menghubungkan aplikasi ke database dan mengelola interaksi dengan data tersebut. | Logika presentasi disusun berdasarkan komponen-komponen dalam konsep MVT. Tampilan ini mengontrol cara data yang dikelola model ditampilkan kepada pengguna. Dalam konteks MVT, tampilan bertindak sebagai pengatur yang menampilkan dan mengambil informasi dari model untuk disajikan kepada pengguna. | Bagian yang bertanggung jawab untuk mengelola layar pengguna, misalnya halaman web. Dalam kerangka kerja seperti Django, template digunakan untuk merancang tata letak halaman web dan menggabungkan data dari template sehingga pengguna dapat melihat data yang dihasilkan melalui tampilan. |

### MVVM (Model - View - ViewModel)
| **Model** | **View** | **ViewModel** |
| --- | --- | --- |
| Komponen yang mengelola data dan logika aplikasi, mirip dengan pola MVC dan MVT. Model dan ViewModel di MVVM  bekerja sama untuk mengambil dan menyimpan data | Komponen yang  menampilkan tampilan dan memberi tahu ViewModel tentang tindakan pengguna. Namun, di MVVM, View bertindak sebagai penampil pasif yang hanya menampilkan data dan tidak berisi logika aplikasi apa pun. | Salah satu komponen utama MVVM, yang bertindak sebagai jembatan antara model dan view. ViewModel mengonversi data model ke dalam format yang dapat ditampilkan oleh view dan mengelola logika tampilan. Misalnya, jika kita memiliki program cuaca, ViewModel  mengambil informasi cuaca dari model dan mengubahnya menjadi format yang dapat ditampilkan oleh tampilan, seperti simbol cuaca, suhu, dan deskripsi. |

### Perbedaan MVC, MVT, dan MVVM
#### MVC
MVC adalah pola desain yang  digunakan dalam berbagai aplikasi termasuk aplikasi desktop, web, dan seluler. Ini adalah konsep yang serbaguna dan tersebar luas. Di MVC, Controller memainkan peran yang cukup aktif dalam mengelola aliran data antara Model dan View. Dalam beberapa kasus, model dan view juga dapat berinteraksi secara langsung. Dengan kata lain, MVC berfokus pada pemisahan tugas dengan model yang mengelola data dan logika bisnis, view yang menampilkan data, dan pengontrol yang mengelola aliran data. Dengan MVC, pengembang sering kali harus  mengelola pembaruan tampilan secara manual saat data berubah. Ini mungkin memerlukan kode tambahan untuk menghubungkan model ke view.

#### MVT
MVT adalah konsep yang terutama digunakan dalam pengembangan web  menggunakan kerangka  Django  berbasis Python. Salah satu komponen khusus, yaitu Template (dalam MVT (Django)), didedikasikan untuk mengelola tampilan halaman web, sedangkan Model dan View berfungsi seperti di MVC. Template adalah komponen tambahan yang tidak ada di MVC tradisional, dan (_frameworks_) ini memiliki alat bawaan yang memastikan tampilan diperbarui secara otomatis ketika data berubah.

#### MVVM
MVVM banyak digunakan pada aplikasi berbasis UI seperti aplikasi mobile atau desktop. Fokusnya adalah memisahkan  tampilan dan tugas logis di antarmuka pengguna. ViewModel  bertindak sebagai perantara antara Model dan View, menjaga keduanya  tetap terpisah dan mengurangi ketergantungan di antara keduanya. MVVM ini didasarkan pada sistem pengikatan data yang secara otomatis memperbarui tampilan ketika data dalam ViewModel berubah. Hal ini mengurangi kode tambahan yang diperlukan untuk melihat pembaruan. Namun, jika pengikatan data sangat rumit, proses debug aplikasi bisa menjadi sedikit lebih sulit.

## BONUS
Saya menambahkan satu testing, yaitu unit testing. Tujuan dari testing ini adalah untuk mengecek model dan attribut yang dimiliki oleh aplikasi dapat berjalan atau tidak. Berikut adalah kode yang saya terapkan di ```test.py```
```python
from django.test import TestCase, Client
from main.models import Item

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    def test_create_instance(self):
        # Create an instance of Item
        my_model = Item(name="Roti", amount=10, description="Roti bakar enak")

        # Verify that the attributes match what you set
        self.assertEqual(my_model.name, "Roti")
        self.assertEqual(my_model.amount, 10)
        self.assertEqual(my_model.description, "Roti bakar enak")

    def test_save_and_retrieve(self):
        # Create an instance of Item
        my_model = Item(name="Pisang", amount=15, description="Pisang coklat")

        # Save it to the database
        my_model.save()

        # Retrieve the object from the database
        retrieved_model = Item.objects.get(name="Pisang")

        # Verify that the retrieved object matches the saved object
        self.assertEqual(retrieved_model.name, "Pisang")
        self.assertEqual(retrieved_model.amount, 15)
        self.assertEqual(retrieved_model.description, "Pisang coklat")
```

# Tugas 3: Implementasi Form dan Data Delivery pada Django
## Membuat input ```form``` untuk menambahkan objek model pada app sebelumnya.
1. Menyalakan _virtual environment_ menggunakan command prompt pada direktori dengan perintah ```env\Scripts\activate.bat```
2. Sebelum membuat input form, kita harus membuat suatu _skeleton_ yang berfungsi sebagai kerangka views dari web yang kita buat. Tujuan dari pembuatan kerangka ini adalah untuk menghindari redundansi kode dan mempertahankan konsistensi desain web kita. Berikut akan dijelaskan cara membuat _skeleton_.
3. Buat folder `templates` di folder utama atau terluar (toko_anisa). Lalu buat berkas HTML bernama `base.html` yang berfungsi sebagai _template_ dasar untuk halaman web lainnya di dalam proyek. Masukan kode berikut ke `base.html`
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta
            name="viewport"
            content="width=device-width, initial-scale=1.0"
        />
        {% block meta %}
        {% endblock meta %}
    </head>

    <body>
        {% block content %}
        {% endblock content %}
    </body>
</html>
```
4. Buka `settings.py` yang ada di subdirektori `toko_anisa` lalu tambahkan kode berikut pada baris `TEMPLATES` agar `base.html` dapat terdeteksi.
```html
...
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # Tambahkan kode ini
        'APP_DIRS': True,
        ...
    }
]
...
```
5. Buka berkas `main.html` yang ada di direktori `main/templates` dan ubah isinya menjadi kode berikut.
```html
{% extends 'base.html' %}

{% block content %}
    <h1>Shopping List Page</h1>

    <h5>Name:</h5>
    <p>{{name}}</p>

    <h5>Class:</h5>
    <p>{{class}}</p>
{% endblock content %}
```
6. Step 5 adalah akhir dari pembuatan _skeleton_. Selanjutnya untuk membuat input form, pertama-tama buat berkas baru di direktori `main` dengan nama `forms.py` untuk membuat struktur form yang menerima data produk baru. Isi berkas dengan kode berikut.
```python
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "Amount", "description"]
```
7. Buka `views.py` di direktori `main` lalu tambahkan beberapa _import_ dan fungsi `create_product` serta ubah fungsi `show_main`. Sehingga isi dari berkas adalah sebagai berikut.
```python
from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
from main.forms import Item
from main.models import Item  # Import your Product model

# Ubah show_main
def show_main(request):
    products = Item.objects.all()

    context = {
        'name': 'Rizki Ariffudin', # Nama kamu
        'class': 'PBP E', # Kelas PBP kamu
        'products': products,
        'total_items': len(products) # Untuk BONUS, membaca total items di database yang sudah disimpan 
    }

    return render(request, "main.html", context)

# Fungsi baru
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)
```
8. Buka `urls.py` di direktori `main` import fungsi `create_product` yang dibuat dan tambahkan _path url_ ke `urlpatterns`. Berikut kode yang perlu ditambahkan.
```python
from main.views import show_main, create_product # import fungsi create_product

...

path('create-product', create_product, name='create_product'), # tambahkan ke urlpatterns
```
9. Buat berkas HTML baru dengan nama `create_product.html` di direktori `main/templates`. Isi berkas dengan kode berikut.
```html
{% extends 'base.html' %} 

{% block content %}
<h1>Add New Product</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Product"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```
10. Buka `main.html` tambahkan kode berikut ke dalam block `{% block content %}` agar data produk dalam bentuk tabel serta tombol *Add New Product* yang akan _redirect_ ke halaman form.
```html
    <table>
        <tr>
            <th>Name</th>
            <th>Amount</th>
            <th>Description</th>
            <th>Date Added</th>
        </tr>
    
        {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini {% endcomment %}
    
        {% for product in products %}
            <tr>
                <td>{{product.name}}</td>
                <td>{{product.amount}}</td>
                <td>{{product.description}}</td>
                <td>{{product.date_added}}</td>
            </tr>
        {% endfor %}
    </table>
    
    <br />
    
    <a href="{% url 'main:create_product' %}">
        <button>
            Add New Product
        </button>
    </a>
{% endblock content %}
```

## Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID. Serta routing URL untuk masing-masing views yang telah ditambahkan.
### XML
1. Buka file `main/views.py`, kemudian import `HttpResponse` dan `Serializer` dan tambahkan function `show_xml`
```py
from django.http import HttpResponse
from django.core import serializers
...
def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
> [!NOTE]
> serializers digunakan untuk translate objek model menjadi format lain.

2. Buka `main/urls.py` untuk import function `show_xml` dan tambahkan routing url ke url patterns sebagai akses menuju fungsi tersebut
```py
from main.views import show_main, create_item, show_xml
...
urlpatterns = [
    ...
    path('xml/', show_xml, name='show_xml'),
    ...
]
```

### JSON
1. Buka file `views.py` pada folder `main` dan buat fungsi `show_json` yang menerima parameter `request`
```py
def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

2. Buka `urls.py` yang ada pada folder `main` dan import fungsi yang sudah dibuat tadi `(show_json)` dan tambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang diimpor tadi
```py
from main.views import show_main, create_item, show_xml, show_json
...
urlpatterns = [
    ...
    path('json/', show_json, name='show_json'),
    ...
]
```

### XML and JSON by ID
1. Buka kembali folder `main` dan akses file `urls.py`, kemudian buat function baru, `show_xml_by_id` dan `show_json_by_id` dengan mengembalikan function berupa `HttpResponse` yang berisi parameter data hasil query yang sudah diserialisasi menjadi JSON atau XML dan parameter `content_type`
```py
...
def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
...
```

2. Buka `urls.py` yang ada pada folder `main` dan import fungsi yang sudah dibuat tadi, yaitu `show_xml_by_id` dan `show_json_by_id`, kemudian perbarui path url yang di dalam urlpatterns untuk mengakses kedua fungsi tersebut.
```py
from django.urls import path
from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id 

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
]
```
## Perbedaan antara form POST dan form GET dalam Django
Terdapat dua jenis method form yang dapat digunakan dalam Django, yaitu POST dan GET. Keduanya memiliki fungsi yang sama, yaitu mengambil data yang diisi user pada form lalu menyimpan data tersebut pada database. Akan tetapi, keduanya memiliki karakteristik masing-masing, yaitu sebagai berikut:
| **POST** | **GET** |
| --- | --- |
| Data pada _form_ akan dibaca dan dilakukan _encode_ kepada data tersebut untuk keperluan transmisi, lalu dikirim secara internal kepada server tanpa menampilkan parameter dari URL. Sehingga data lebih aman karena tidak sembarang orang dapat melakukan akses ke data tersebut. | Data pada form akan dibaca dan dikirim ke server sebagai _string_ yang merupakan parameter URL. Sehingga seluruh data yang dibaca menggunakan method GET bisa terlihat oleh siapapun melalui URL |
| Sebuah _request_ yang memberikan dampak kepada database dan system harus menggunakan POST | GET digunakan untuk _request_ yang tidak punya pengaruh kepada system. |
| Cocok digunakan untuk memperoleh _Login Data_ seperti _password_, data yang sangat besar, dan _binary data_ seperti gambar | Cocok digunakan untuk keperluan yang hanya mengakses sesuatu yang sudah ada di website seperti _web search form_. |

## Perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data
Secara singkat, XML cocok untuk pertukaran data yang sangat terstruktur dan ketat, JSON cocok untuk pertukaran data yang lebih sederhana dan efisien dalam konteks aplikasi web, sedangkan HTML adalah bahasa markup yang digunakan untuk membuat tampilan halaman web yang bisa diakses oleh manusia.

XML adalah bahasa markup yang dirancang untuk menyimpan dan mengirim data dengan struktur yang kuat dan sangat terstruktur. XML menggunakan tag-tag yang mendefinisikan elemen-elemen data dan atribut-atribut untuk memberikan informasi tambahan tentang elemen-elemen tersebut. XML sangat kuat dalam mendefinisikan skema data yang ketat, yang membuatnya cocok untuk pertukaran data yang kompleks seperti data konfigurasi, data yang harus divalidasi dengan ketat, atau dalam format data yang bisa dibaca oleh mesin. Namun, XML memiliki overhead dalam hal ukuran file karena strukturnya yang kuat, dan parsing XML memerlukan penggunaan sumber daya komputasi yang signifikan.

JSON adalah format pertukaran data yang lebih ringan dan mudah dibaca oleh mesin. JSON menggunakan struktur objek dan array yang lebih sederhana daripada XML, membuatnya ideal untuk pertukaran data yang cepat dan efisien. JSON sangat populer dalam pengembangan aplikasi web modern karena dapat diurai (parsed) dan dihasilkan (serialized) dengan mudah dalam banyak bahasa pemrograman. JSON juga mendukung berbagai jenis data, termasuk teks, angka, objek, array, dan boolean, menjadikannya format yang serbaguna untuk pertukaran data antara klien dan server. Namun, JSON tidak memiliki dukungan bawaan untuk definisi skema data yang kuat, yang dapat menyebabkan masalah kompatibilitas jika tidak dikelola dengan baik.

HTML adalah bahasa markup yang dirancang khusus untuk membuat dan mengatur konten web yang dapat diakses oleh manusia melalui peramban web. HTML tidak biasanya digunakan untuk pertukaran data struktural antara aplikasi, tetapi digunakan untuk membuat tampilan dan struktur halaman web. Namun, HTML memiliki kemampuan untuk menyematkan data dalam atribut atau elemen tertentu dan, dengan bantuan JavaScript, data ini dapat diakses oleh aplikasi web dan digunakan untuk interaksi klien-sisi. HTML adalah dasar dari web, dan semua halaman web modern menggunakan HTML sebagai struktur dasarnya.

## Alasan JSON sering digunakan dalam pertukaran data antara aplikasi web modern
JSON dengan format teks ringan dan fleksibilitas struktur data, memudahkan pengembang dalam memahami, mengelola, dan merepresentasikan data kompleks. Dukungan interoperabilitasnya di banyak bahasa pemrograman dan platform membuatnya serbaguna, digunakan secara luas dalam aplikasi web modern, terutama dalam berinteraksi dengan layanan web dan API eksternal. JSON juga menawarkan fitur keamanan yang mengurangi risiko serangan injeksi kode. Dalam konteks aplikasi real-time, JSON memungkinkan pembaruan data efisien antara klien dan server, meningkatkan pengalaman pengguna. Dukungan luas dari kerangka kerja dan perpustakaan web menjadikannya alat penting dalam pengembangan aplikasi web.

## Screenshot hasil akses URL pada Postman
### HTML
![Alt text](tugas3-images/html.png)

### XML
![Alt text](tugas3-images/xml.png)

### JSON
![Alt text](tugas3-images/json.png)

### XML by ID (Case ID = 2)
![Alt text](tugas3-images/xmlbyid.png)

### JSON by ID (Case ID = 1)
![Alt text](tugas3-images/jsonbyid.png)

## BONUS: Menambahkan pesan "Kamu menyimpan X item pada aplikasi ini" (dengan X adalah jumlah data item yang tersimpan pada aplikasi) dan menampilkannya di atas tabel data.
Untuk melakukan hal ini, kita perlu mengambil total item yang sudah dibuat di database. tambahkan kode berikut di berkas `views.py` di direktori `main`
```python
from main.models import Item  # Import your Product model

# Ubah show_main
def show_main(request):
    products = Item.objects.all()

    context = {
        'name': 'Rizki Ariffudin', # Nama kamu
        'class': 'PBP E', # Kelas PBP kamu
        'products': products,
        'total_items': len(products) # Untuk BONUS, syntax len akan mereturn jumlah products yang ada di database
    }

    return render(request, "main.html", context)
```
Setelah itu, kita ke berkas `main.html` yang ada di direktori `main/templates` dan ubah berkas menjadi sebagai berikut/
```html
{% extends 'base.html' %}

{% block content %}
    <h1>Toko Anisa Page</h1>

    <h5>Name:</h5>
    <p>{{name}}</p>

    <h5>Class:</h5>
    <p>{{class}}</p>
    <h5>Kamu menyimpan {{total_items}} item pada aplikasi ini</h5> # Untuk BONUS, tambahkan kode ini untuk menampilkan total items di halaman web
    <table>
        <tr>
            <th>Name</th>
            <th>Amount</th>
            <th>Description</th>
            <th>Date Added</th>
        </tr>
    
        {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini {% endcomment %}
    
        {% for product in products %}
            <tr>
                <td>{{product.name}}</td>
                <td>{{product.amount}}</td>
                <td>{{product.description}}</td>
                <td>{{product.date_added}}</td>
            </tr>
        {% endfor %}
    </table>
    
    <br />
    
    <a href="{% url 'main:create_product' %}">
        <button>
            Add New Product
        </button>
    </a>
{% endblock content %}
```