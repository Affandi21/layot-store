Web: http://affandi-shafwan-layotstore.pbp.cs.ui.ac.id/

## Tugas PBP 2024/2025
### Tugas 2
### Tugas 3

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
     
### Mengakses keempat URL di poin 2 menggunakan Postman
**XML All**
![image](https://github.com/Affandi21/layot-store/blob/c3595fb8c59819da704e78d7bfddbac5b3375a4a/src/Screenshot%20(39).png)


**JSON All**
![image](https://github.com/Affandi21/layot-store/blob/c3595fb8c59819da704e78d7bfddbac5b3375a4a/src/Screenshot%20(38).png)


**XML by ID**
![image](https://github.com/Affandi21/layot-store/blob/c3595fb8c59819da704e78d7bfddbac5b3375a4a/src/Screenshot%20(41).png)

**JSON by ID**
![image](https://github.com/Affandi21/layot-store/blob/c3595fb8c59819da704e78d7bfddbac5b3375a4a/src/Screenshot%20(40).png)



## Tugas 4 - PBP 2024/2025

### Perbedaan antara `HttpResponseRedirect()` dan `redirect()`
### HttpResponseRedirect()
Berfungsi untuk mengembalikan respons HTTP 302 yang memerintahkan browser untuk melakukan pengalihan ke URL yang ditentukan.
Contoh Penggunaan:

```python
from django.http import HttpResponseRedirect

def my_view(request):
    return HttpResponseRedirect('/some-url/')
```
Kelebihan: memiliki kendali penuh atas URL yang dituju, tapi ini hanya terbatas pada URL yang harus ditentukan sebagai string.

HttpResponseRedirect() cocok jika hanya ingin melakukan redirect ke URL tertentu dan tidak membutuhkan banyak fleksibilitas.


### redirect()
Merupakan shortcut (fungsi bantu) yang lebih fleksibel untuk melakukan redirect. Fungsi ini pada dasarnya adalah pembungkus (wrapper) dari HttpResponseRedirect().

Contoh penggunaan:
```python
from django.shortcuts import redirect

# Redirect dengan URL
def my_view(request):
    return redirect('/some-url/')

# Redirect dengan nama view
def my_view(request):
    return redirect('view-name')

# Redirect dengan model instance (memerlukan get_absolute_url di model)
def my_view(request):
    obj = MyModel.objects.get(pk=1)
    return redirect(obj)

```

Kelebihan: redirect() lebih mudah digunakan karena mendukung lebih banyak jenis argumen, sehingga tidak perlu khawatir dengan format URL secara eksplisit. Django akan secara otomatis menerjemahkan view name atau object instance menjadi URL yang benar.

redirect() lebih mudah dibaca dan ditulis, serta menawarkan lebih banyak opsi untuk pengalihan.
---

### Jelaskan cara kerja penghubungan model Product dengan User!
Kita dapat menggunakan field ForeignKey
## Relasi One-to-Many (ForeignKey)
Satu pengguna dapat memiliki banyak produk. Setiap produk hanya dimiliki oleh satu pengguna. Anda bisa menggunakan ForeignKey untuk membuat relasi ini.
Langkah-langkah:
1. Tambahkan ForeignKey ke model Product untuk menunjuk ke User.
2. Gunakan on_delete=models.CASCADE untuk memastikan jika pengguna dihapus, produk terkait juga dihapus.

```python
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  # Relasi ForeignKey

    def __str__(self):
        return self.name

```
Penjelasan: owner = models.ForeignKey(User, on_delete=models.CASCADE): Produk dihubungkan dengan pengguna yang menjadi pemiliknya. Jika pengguna dihapus, produk juga akan dihapus.

---

### Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
## Authentication (Autentikasi):
Proses verifikasi identitas pengguna, yaitu memeriksa apakah pengguna adalah orang yang mereka klaim,  proses ini terjadi saat pengguna memasukkan informasi login, dan Django memvalidasi kredensial mereka terhadap database.

Tujuan: Memastikan bahwa pengguna yang mencoba mengakses aplikasi atau sistem adalah pengguna yang sah.

Contoh: Saat pengguna memasukkan username dan password, aplikasi memeriksa apakah kredensial yang diberikan sesuai dengan data yang disimpan.

## Authorization (Otorisasi):
Proses pengaturan hak akses pengguna, yaitu menentukan apa yang boleh dilakukan oleh pengguna yang telah terotentikasi. Setelah pengguna terotentikasi, Django menggunakan izin (permissions) dan grup (groups) untuk memutuskan apakah pengguna diizinkan melakukan tindakan tertentu.

Tujuan: Menentukan tindakan atau sumber daya apa yang dapat diakses oleh pengguna tertentu, berdasarkan peran atau izin yang mereka miliki.

Contoh: Setelah pengguna login (terotentikasi), sistem memeriksa apakah pengguna tersebut memiliki hak untuk mengakses halaman admin atau melakukan tindakan tertentu.

## Proses yang Terjadi Saat Pengguna Login
Ketika pengguna login ke aplikasi Django:
1. Pengguna memasukkan kredensial (username dan password)
2. Django memverifikasi kredensial: Menggunakan sistem autentikasi, Django mencocokkan username dan password yang dimasukkan dengan data pengguna yang ada di database.
Jika kredensial benar, pengguna diotentikasi.
Jika salah, Django menampilkan pesan kesalahan.
3. Setelah terotentikasi, Django membuat sesi pengguna: Django menyimpan informasi tentang pengguna di sesi (session) agar pengguna tetap dianggap login selama sesi berlangsung.
4. Authorization: Setiap kali pengguna mengakses halaman atau mencoba melakukan tindakan, Django memeriksa apakah pengguna memiliki izin yang sesuai.

---

### Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
## Django mengingat pengguna yang telah login dengan menggunakan session dan cookies.
Sesi (Session): Setelah pengguna berhasil login, Django membuat sesi untuk pengguna tersebut. Django menyimpan data sesi di server dan menyimpan session ID (ID unik untuk sesi tersebut) di cookie di browser pengguna.

Cookies: Django menggunakan cookie untuk menyimpan session ID ini, sehingga setiap kali pengguna mengirim permintaan baru ke server, session ID dikirim bersama cookie, dan Django dapat mencocokkannya dengan data sesi yang tersimpan di server.

## Kegunaan lain dari cookies
1. Menyimpan preferensi pengguna: Cookies dapat menyimpan data seperti tema yang dipilih pengguna, bahasa yang diinginkan, atau pengaturan halaman.
2. Pelacakan dan analitik: Cookies sering digunakan oleh situs web untuk melacak aktivitas pengguna (seperti halaman yang dikunjungi) guna menganalisis perilaku pengguna atau memberikan rekomendasi.
3. Iklan dan retargeting: Cookies digunakan untuk menyimpan data tentang kebiasaan browsing pengguna, yang kemudian digunakan oleh pengiklan untuk menampilkan iklan yang relevan.
4. Otentikasi yang tersimpan: Beberapa situs menggunakan cookies untuk menyimpan status login jangka panjang, sehingga pengguna tetap login meskipun setelah browser ditutup.
5. Keranjang belanja (Shopping cart): Cookies bisa digunakan untuk menyimpan produk yang dipilih pengguna di keranjang belanja, bahkan jika mereka belum login.

## Apakah Semua Cookies Aman Digunakan?
Tidak semua cookies aman digunakan,
Risiko dan Keamanan Cookies:
1.  Cookies yang tidak dienkripsi: Jika cookies tidak dilindungi dengan baik, seperti tidak menggunakan HTTPS, data dalam cookies bisa dicegat oleh pihak ketiga melalui man-in-the-middle attacks.


2. Cookies yang tidak dienkripsi dengan baik di sisi klien: Jika informasi sensitif disimpan dalam cookies tanpa enkripsi, penyerang bisa memanipulasi atau mencuri data pengguna.

3. Cookies pihak ketiga (Third-party cookies): Cookies yang dibuat oleh situs lain selain situs yang Anda kunjungi (misalnya, untuk pelacakan iklan) dapat menimbulkan masalah privasi. Mereka memungkinkan pihak ketiga untuk melacak aktivitas pengguna di berbagai situs web.

---

### Langkah-langkah Implementasi Checklist

## 1. Membuat Fungsi dan Form Registrasi
Buka views.py yang ada pada subdirektori main, lalu tambahkan import UserCreationForm dan messages pada bagian paling atas, dan tambahkan  fungsi register di bawah ke dalam views.py.
```python
  # Authentication Views
  def register(request):
      form = UserCreationForm()
  
      if request.method == "POST":
          form = UserCreationForm(request.POST)
          if form.is_valid():
              form.save()
              messages.success(request, "Akun baru berhasil dibuat")
              return redirect('main:login')
          
      context = {'form': form}
      return render(request, 'auth/register.html', context)
```
Lalu buat template auth/register.html untuk menampilkan form pendaftaran.

## 2. Membuat Fungsi Login
Buka views.py yang ada pada subdirektori main, kemudianTambahkan import authenticate, login, dan AuthenticationForm. Lalu tambahkan fungsi login_user di bawah ini ke dalam views.py.
```python
def login_user(request):
   if request.user.is_authenticated:
        return redirect('main:show_main')
   
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse('main:show_main'))
            response.set_cookie('last_login', datetime.datetime.now())
            return response

   else:
      form = AuthenticationForm(request)

   context = {'form': form}
   return render(request, 'auth/login.html', context)

```
Lalu buat template auth/login.html untuk menampilkan form login.

## 3. Membuat Fungsi Logout
Buka views.py yang ada pada subdirektori main. Tambahkan import logout, lalu tambahkan fungsi logout_user
```python
def logout_user(request):
    logout(request)
    return redirect('main:login')
```
## 4. Hubungkan semua view melalui urls.py
```python
from django.urls import path
from main.views import show_main, add_to_cart, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user


app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('add-to-cart', add_to_cart, name='add_to_cart'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]
```

## 6. Membuat Dua Akun Pengguna dengan Dummy Data


## 7. Menggunakan Data Dari Cookies
Buka views.py yang ada pada subdirektori main. Tambahkan import HttpResponseRedirect, reverse, dan datetime.
Lalu Pada fungsi login_user,  tambahkan fungsionalitas menambahkan cookie yang bernama last_login untuk melihat kapan terakhir kali pengguna melakukan login. 
```python
if form.is_valid():
    user = form.get_user()
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main"))
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
```

## 8. Menghubungkan Model MoodEntry dengan User
Buka models.py yang ada pada subdirektori main dan tambahkan import user untuk mengimpor model, kemudian pada model LayotStore yang sudah dibuat, tambahkan potongan kode berikut:
```python
class LayotStore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ...
```
```python
class LayotStore(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    time = models.DateField(auto_now_add=True)
    description = models.TextField()
    total = models.IntegerField()
   
```
