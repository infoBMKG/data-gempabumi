<?php
  // Kode Baris PHP untuk Mengolah Data gempaterkini.xml
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
