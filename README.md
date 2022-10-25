[![N|Solid](https://github.com/fahmiyufrizal/ea-apps/blob/main/Screenshot%20(1).png)](#)

# EA Apps Loader (Portable)
Designed for Diskless

## Fitur
[-] Menjalankan EA Apps tanpa perlu install dan superuser di client

[-] Toolkit untuk membantu agar EA Apps berjalan semestinya

## Pre-Configured
[-] Base EA Apps' Games Registry

[-] Patch Unicode DisplayName (still testing)

## Penjelasan Fitur
[-] Base Game Registry adalah Registry dasar yang akan diimport. Jika owner warnet sudah melakukan instalasi ke dalam folder _ Games _, owner sudah tidak perlu membuka toolkit dan melakukan 'Find EA Apps Games Registry' lagi. Base Registry hanya berisi sebagian kecil game saja dikarenakan keterbatasan riset dan dana untuk membeli semua game dan DLC di dalam EA Apps.

[-] Find EA Apps' Registry = Melakukan scanning registry melalui pattern tertentu yang selanjutnya akan mensupport registry base game. Sangat berguna bila game terinstall di folder lain dan tidak disupport oleh base registry. Misal warnet A membeli game FIFA23 yang tidak disupport Base Registry maka owner warnet A wajib melakukan scanning melalui fitur ini agar registry yang dibutuhkan dapat dibaca di client.

[-] Unload EA Apps Loader = Fitur ini digunakan bila akan memindahkan EA Apps Loader ke folder/drive lain. Setelah melakukan unload, silahkan lakukan 'Toggle Configured Mark' agar EA Apps Loader menginisiasi ulang symlink.

[-] Toggle Configured Mark = Digunakan untuk menghapus/menandakan mark yang dibutuhkan EA Apps Loader

[-] Clean Unused EA Apps Files = Digunakan untuk menghapus file-file lama EA Apps setelah update. Bisa menghemat sampai ~300MB

## Known Issues
[-] EA Loader mungkin tidak dapat mendeteksi game dengan benar diluar folder _ Games _ bila drive-letter gamedisk server dan client berbeda
[-] Find EA Apps Game Registry mungkin bermasalah untuk beberapa game di Origin karena perbedaan struktur (murni kerjaannya EA), masih perlu riset untuk ini

## Cara Pakai
1. Jalankan Launch_EApps_Loader.exe di server
2. Jika sebelumnya belum menginstall game EA apapun elalui EA Apps/Origin, Install ke dalam folder _ Games _
3. Jika sudah menginstall game di folder/drive lain, gunakan toolkit lalu lakukan find EA Games Apps Registry

## Thank's to
- Allah SWT
- Senna WaLker Wibowo
- AyraGaming Pacitan
- XGC Manisrejo Madiun
- dan semua yang telah memanfaatkan project ini^^

## Download Link
- [Disini](https://github.com/fahmiyufrizal/ea-apps/releases)
