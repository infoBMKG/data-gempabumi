<?php
  // Kode Baris PHP untuk Mengolah Data autogempa.xml
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
