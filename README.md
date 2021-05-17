# Data Gempabumi Terbuka BMKG
Data Gempabumi Terbuka BMKG telah tersedia di portal https://data.bmkg.go.id/gempabumi yang terdiri atas:
1. Gempabumi Terbaru (`autogempa.xml`)
2. Daftar 15 Gempabumi M 5.0+ (`gempaterkini.xml`)
3. Daftar 15 Gempabumi Dirasakan (`gempadirasakan.xml`)

Berikut kode baris pemrograman PHP yang digunakan dalam mengolah data-data XML gempabumi tersebut.

### Kode Baris PHP untuk Mengolah Data `autogempa.xml`
```php
<?php
  $data = simplexml_load_file("https://data.bmkg.go.id/DataMKG/TEWS/autogempa.xml") or die("Gagal mengakses!");
  echo "<h2>Gempabumi Terbaru</h2>";
  echo "Tanggal: " . $data->gempa->Tanggal . "<br>";
  echo "Jam: " .  $data->gempa->Jam . "<br>";
  echo "DateTime: " . $data->gempa->DateTime . "<br>";
  echo "Magnitudo: " . $data->gempa->Magnitude . "<br>";
  echo "Kedalaman: " . $data->gempa->Kedalaman . "<br>";
  echo "Koordinat: " . $data->gempa->point->coordinates . "<br>";
  echo "Lintang: " . $data->gempa->Lintang . "<br>";
  echo "Bujur: " . $data->gempa->Bujur . "<br>";
  echo "Lokasi: " . $data->gempa->Wilayah . "<br>";
  echo "Potensi: " . $data->gempa->Potensi . "<br>";
  echo "Dirasakan: " . $data->gempa->Dirasakan . "<br>";
  echo "Shakemap: <br><img src=\"https://data.bmkg.go.id/DataMKG/TEWS/" . $data->gempa->Shakemap . "\" alt=\"Gempabumi Terbaru\">";
?>
```

### Kode Baris PHP untuk Mengolah Data `gempaterkini.xml`
```php
<?php
  $data = simplexml_load_file("https://data.bmkg.go.id/DataMKG/TEWS/gempaterkini.xml") or die ("Gagal ambil!");
  echo "<h2>Daftar 15 Gempabumi M 5.0+</h2>";
  $i = 1;
  foreach($data->gempa as $gempaM5) {
    echo "No: " . $i . "<br>";
    echo "Tanggal: " . $gempaM5->Tanggal . "<br>";
    echo "Jam: " .  $gempaM5->Jam . "<br>";
    echo "DateTime: " . $gempaM5->DateTime . "<br>";
    echo "Magnitudo: " . $gempaM5->Magnitude . "<br>";
    echo "Kedalaman: " . $gempaM5->Kedalaman . "<br>";
    echo "Koordinat: " . $gempaM5->point->coordinates . "<br>";
    echo "Lintang: " . $gempaM5->Lintang . "<br>";
    echo "Bujur: " . $gempaM5->Bujur . "<br>";
    echo "Lokasi: " . $gempaM5->Wilayah . "<br>";
    echo "Potensi: " . $gempaM5->Potensi . "<br><br>";
    $i++;
  }
?>
```

### Kode Baris PHP untuk Mengolah Data `gempadirasakan.xml`
```php
<?php
  $data = simplexml_load_file("https://data.bmkg.go.id/DataMKG/TEWS/gempadirasakan.xml") or die ("Gagal ambil!");
  echo "<h2>Daftar 15 Gempabumi Dirasakan</h2>";
  $i = 1;
  foreach($data->gempa as $gempaDirasakan) {
    echo "No: " . $i . "<br>";
    echo "Tanggal: " . $gempaDirasakan->Tanggal . "<br>";
    echo "Jam: " .  $gempaDirasakan->Jam . "<br>";
    echo "DateTime: " . $gempaDirasakan->DateTime . "<br>";
    echo "Magnitudo: " . $gempaDirasakan->Magnitude . "<br>";
    echo "Kedalaman: " . $gempaDirasakan->Kedalaman . "<br>";
    echo "Koordinat: " . $gempaDirasakan->point->coordinates . "<br>";
    echo "Lintang: " . $gempaDirasakan->Lintang . "<br>";
    echo "Bujur: " . $gempaDirasakan->Bujur . "<br>";
    echo "Lokasi: " . $gempaDirasakan->Wilayah . "<br>";
    echo "Dirasakan di Wilayah: " . $gempaDirasakan->Dirasakan . "<br><br>";
    $i++;
  }
?>
```


# Data Gempa Bumi JSON
Konversi tipe data gempa bumi BMKG dari XML ke JSON

Sumber data dari https://data.bmkg.go.id/gempabumi 

### Berikut ini kode Python 3 untuk mengolah data XML dan data JSON
1. Function (`function.py`)
2. Gempabumi Terbaru (`autogempa.py`)
3. Daftar 15 Gempabumi M 5.0+ (`gempaterkini.py`)
4. Daftar 15 Gempabumi Dirasakan (`gempadirasakan.py`)

## Parameter (key)
* Tanggal dan Jam dalam WIB
* DateTime sesuai ISO 8601 dalam UTC (+00:00)
* Magnitude atau magnitudo merupakan kekuatan gempa
* Kedalaman dalam kilometer (km)
* Koordinat Lintang dan Bujur
* Susunan key coordinates adalah latitude kemudian longitude
* Wilayah terdekat dengan lokasi episenter gempabumi
* Potensi tsunami atau tidak, dan status gempa dirasakan
* Dirasakan merupakan wilayah yang merasakan gempa dalam skala MMI
* Gambar Shakemap (peta guncangan) diawali dengan URL https://data.bmkg.go.id/DataMKG/TEWS/

### Kode Baris Python 3 `autogempa.py` untuk Mengolah Data dari JSON `function.py`
```python
import function
import json
result = json.loads(function.autogempa())
mapURL = result["Shakemap"]
result.pop("Shakemap")
print("")
for x in result:
    print("{:<15} : ".format(x) + result[x])

print("{:<15} :".format("Shakemap"))
import IPython
IPython.display.Image(mapURL)

```
### Kode Baris Python 3 `gempaterkini.py` untuk Mengolah Data dari JSON `function.py`
```python
import function
import json
result = json.loads(function.gempaterkini())
for x in result:
    for y in result[x]:
        print("{:<15} : ".format(y) + result[x][y])
    print("\n")

```
### Kode Baris Python 3 `gempadirasakan.py` untuk Mengolah Data dari JSON `function.py`
```python
import function
import json
result = json.loads(function.gempadirasakan())
for x in result:
    for y in result[x]:
        print("{:<15} : ".format(y) + result[x][y])
    print("\n")

```
