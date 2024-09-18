Web: http://affandi-shafwan-ecommerce.pbp.cs.ui.ac.id/

## Tugas 2 - PBP 2024/2025
Langkah-langkah yang dilakukan:
1. Membuat direktori utama, saya menamakannya e-commerce
2. Mengaktifkan virtual environment melalui command prompt
3. Menjalankan perintah di command prompt untuk membuat aplikasi bernama main di dalam proyek e-commerce
4. Mendaftarkan aplikasi main dengan menambahkan 'main' ke variable INSTALLED_APPS di file setting.py
5. Membuat direktori bernama templates didalam aplikasi main, kemudian membuat dan mengisi file main.html
   yang berisi:
   name sebagai nama item dengan tipe CharField,
   price sebagai harga item dengan tipe IntegerField, dan
   description sebagai deskripsi item dengan tipe TextField.
6. Menghubungkan view dengan template dengan cara membuka file views.py di file aplikasi main
7. Kemudian menambahkan fungsi show_main dibawah impor, contoh:
    def show_main(request):
    context = {
        'name' : 'Old Book',
        'price': 'Rp259.000,00',
        'description': 'Old book found in my backyard'
    }
    return render(request, "main.html", context)
8. Modifikasi template, ubah template main.html dengan mengubah name, price, dan 
   description menjadi struktur kode Django yang sesuai untuk menampilkan data. 
   Contoh:
   {{ name }}, {{ price }} dan {{ description }}

9. Mengonfigurasi Routing URL Aplikasi main, dengan mengubah urls.py dengan kode berikut:
   from django.urls import path
   from main.views import show_main
   app_name = 'main'
   urlpatterns = [
    path('', show_main, name='show_main'),
   ]
10. Menambahkan rute URL dalam urls.py proyek untuk menghubungkannya ke tampilan main
11. Buka berkas urls.py di dalam direktori proyek e_commerce, 
    bukan yang ada di dalam direktori aplikasi main. 
12. Lalu menambahkan import, from django.urls import path, include
13. Menambahkan rute url untuk mengarahkan ke tampilan main di dalam variabel urlpatterns
   urlpatterns = [
    ...
    path('', include('main.urls')),
    ...
    ]
14. Berkas urls.py ini bertanggung jawab untuk mengatur rute URL tingkat proyek
15. Menjalankan proyek Django dengan perintah python manage.py runserver
16. Kemudian buka link http://localhost:8000/ di web browser untuk melihat halaman yang sudah dibuat
17. Kemudian membuat proyek baru di pws
18. Pada settings.py di proyek Django yang sudah kamu buat tadi,
    tambahkan URL deployment PWS pada ALLOWED_HOSTS. ...
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "affandi-shafwan-ecommerce.pbp.cs.ui.ac.id"]
19. Setelah mendapatkan Project Credentials dan Project Command, jalankan instruksi project command


**Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.**
Check out the live version here: [Layot Store](https://github.com/Affandi21/e-commerce/blob/262a41a2d4b8b37d896adec86daa9672d41f971a/src/IMG_1090.jpg)

**Jelaskan fungsi git dalam pengembangan perangkat lunak!**
1. Git adalah tools yang bersifat open source, sehingga dapat digunakan untuk membuat perangkat lunak secara open source. 
2. untuk kolaborasi dengan banyak orang, kita dapat memanfaatkan Git untuk mengerjakan proyek yang sama (kerja tim). 
3. Sebagai platform fleksibilitas karena dapat digunakan sebagai solusi untuk hosting pada semua proyek. 
4. Sebagai backup, Git dapat dengan mudah mengembalikan ke dalam versi sebelumnya.

**Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?**
Karena Django memiliki fitur lengkap ("batteries included"), dokumentasi yang baik, arsitektur terstruktur (MVT), keamanan bawaan, ORM mudah digunakan, dan komunitas besar. Ini memberikan pemahaman menyeluruh tentang pengembangan web serta mendukung skalabilitas dari proyek kecil hingga besar.

**Mengapa model pada Django disebut sebagai ORM?**
Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena memungkinkan pengembang untuk berinteraksi dengan database menggunakan objek Python, tanpa perlu menulis kode SQL secara langsung. ORM menghubungkan kelas Python (model) dengan tabel dalam database, sehingga operasi seperti insert, update, delete, dan query dapat dilakukan melalui metode Python yang mudah dipahami, sementara ORM secara otomatis menerjemahkannya menjadi perintah SQL.

## Tugas 2 - PBP 2024/2025 - END

---

## Tugas 3 - PBP 2024/2025

### Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Data delivery sangat penting dalam pengimplementasian platform karena alasan berikut:
1.	**Aksesibilitas Data**: Memungkinkan pengguna mengakses informasi yang relevan dan tepat waktu dari mana saja.
2.	**Integrasi Sistem**: Memfasilitasi komunikasi antar sistem yang berbeda, mendukung operasional yang lancar.
3.	**Analitik dan Keputusan**: Data yang dikirimkan dengan efektif mendukung analisis lanjutan dan pengambilan keputusan berbasis data.
4.	**Performa dan Skalabilitas**: Esensial untuk mempertahankan performa platform saat skala penggunaan bertambah.
5.	**Keamanan Data**: Menjamin data dikirimkan dengan aman untuk melindungi dari akses tidak sah.
6.	**Kepatuhan Regulasi**: Memastikan platform mematuhi aturan pengelolaan dan pengiriman data yang diatur oleh regulasi.
Fungsi-fungsi ini membantu dalam membangun platform yang responsif, aman, dan efisien.

---


### Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Menurut saya JSON lebih baik daripada XML dan JSON bisa lebih populer daripada XML karena beberapa alasan utama:
1.	**Kesederhanaan**: JSON lebih sederhana dan mudah dibaca dibandingkan XML.
2.	**Ukuran**: JSON menggunakan bandwidth lebih sedikit karena ukurannya yang lebih ringkas.
3.	**Pemrosesan Data**: Struktur JSON lebih alami bagi banyak bahasa pemrograman modern, memudahkan manipulasi data.
4.	**Dukungan Browser**: JSON didukung secara native oleh browser modern, yang memfasilitasi penggunaannya dalam aplikasi web.
5.	**Interoperabilitas**: JSON menyediakan pertukaran data yang cepat dan efisien, sesuai untuk aplikasi web dan mobile.

---


### Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?

Method `is_valid()` pada form Django berfungsi untuk memvalidasi data yang di input ke dalam form. Fungsi utamanya adalah:
1. **Validasi Data**: Memeriksa apakah data memenuhi semua kriteria validasi yang telah ditetapkan.
2. **Konversi Tipe Data**: Mengubah input mentah menjadi tipe data Python yang sesuai.
3. **Pembersihan Data**: Memungkinkan pembersihan atau validasi data kustom melalui method `clean()`.

Kita membutuhkan `is_valid()` karena:

1. **Keamanan**: Mencegah masuknya data yang bisa merusak atau mengganggu sistem.
2. **Integritas Data**: Menjaga kualitas dan keakuratan data dalam aplikasi.
3. **Efisiensi Pengembangan**: Mengurangi kebutuhan untuk menulis validasi data secara manual.
4. **Pengalaman Pengguna**: Memberikan feedback kesalahan yang jelas, memudahkan pengguna untuk memperbaiki masukan.

Method ini esensial dalam Django untuk memastikan data yang diterima oleh aplikasi adalah valid dan aman.

---

### Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

`csrf_token` dalam Django digunakan untuk melindungi aplikasi dari serangan Cross-Site Request Forgery (CSRF). 
**Peran penting csrf_token**:
1.	**Perlindungan dari CSRF**: Memastikan permintaan hanya berasal dari sumber sah.
2.	**Validasi Asal Permintaan**: Mencegah permintaan palsu dari situs berbahaya.

**Risiko Tanpa csrf_token**:
•	Aplikasi menjadi rentan terhadap serangan CSRF, memungkinkan penyerang memaksa pengguna melakukan tindakan berbahaya.

**Eksploitasi Penyerang**:
•	Memanfaatkan sesi aktif pengguna untuk mengirim permintaan palsu yang tampak sah.
•	Memicu tindakan tidak diinginkan dengan menyembunyikan permintaan berbahaya dalam halaman yang dikunjungi pengguna.
csrf_token memastikan permintaan ke server berasal dari sumber yang sah, menambahkan lapisan keamanan penting untuk aplikasi web.

---

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step

1. **Membuat form di Django**
    ```python
    from django.forms import ModelForm
    from main.models import AddCart

    class AddCart(ModelForm):
        class Meta:
            model = AddCart
            fields = ["name", "description", "total"]
    ```

2. **Buka berkas `views.py` yang ada pada direktori main dan tambahkan beberapa import dan fungsi, serta tambahkan potongan kode di bawah ini untuk menghasilkan form yang dapat menambahkan data Mood Entry secara otomatis ketika data di-submit dari form.**
    ```python
    def create_mood_entry(request):
    form = AddCartForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "add_to_cart.html", context)

    ```

3. **Buat berkas HTML baru untuk menampilkan form**
     ```html
    {% extends 'base.html' %} 
    {% block content %}
    <h1>Add To Cart</h1>

    <form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
        <td></td>
        <td>
            <input type="submit" value="Add To Cart" />
        </td>
        </tr>
    </table>
    </form>

    {% endblock %}
    ```

4. **Tambahkan URL Routing untuk Form**
    ```python
    from django.urls import path
    from main.views import show_model, add_to_cart, show_all_json, show_all_xml, show_id_json, show_id_xml
    
    app_name = 'main'
    
    urlpatterns = [
        path('', show_model, name='show_model'),
        path('add-to-cart', add_to_cart, name='add_to_cart'),
    ]
    ```

5. **Menambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.**
     **Buat View untuk Format JSON dan XML**:
    - **View untuk JSON**:
      ```python
      def show_all_json(_):
          data = AddCart.objects.all()
          return HttpResponse(serializers.serialize("json", data), content_type="application/json")
      ```

    - **View untuk XML**:
      ```python
      def show_all_xml(_):
          data = AddCart.objects.all()
          return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
      ```

    - **View untuk JSON by ID**:
      ```python
      def show_id_json(_, id: str):
          data = AddCart.objects.filter(id=id)
          return HttpResponse(serializers.serialize("json", data), content_type="application/json")
      ```

    - **View untuk XML by ID**:
      ```python
      def show_id_xml(_, id: str):
          data = AddCart.objects.filter(id=id)
          return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
      ```

    **Membuat Routing URL**
    ```python
    # urls.py
    from django.urls import path
    from . import views
    
    urlpatterns = [
        path('', show_model, name='show_model'),
        path('add-to-cart', add_to_cart, name='add_to_cart'),
        path('xml/', show_all_xml, name='show_all_xml'),
        path('xml/<str:id>/', show_id_xml, name='show_id_xml'),
        path('json/', show_all_json, name='show_all_json'),
        path('json/<str:id>/', show_id_json, name='show_id_json'),
    ]
    ```
     
### Contoh Hasil API Call dengan Postman
**XML All**


