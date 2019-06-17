# ValidDex
Nesne algılama(Derin Öğrenme) da yapılan etiketlemeler için belli doğrulamaları yapan bir araçtır.

# Description

Bu araç nesne algılama için yapılan etiketlemelerde (https://github.com/tzutalin/labelImg) etiketlenen resimlerin temel olarak seçilmiş nesne isimlerin ile olan doğruluğunu bulur. Bunun dışında yapılan tüm etiketleme sonunda hangi nesneden ne kadar etiketlenmiş bunu csv formatında size sunar. Genelde uygulanan bir etiketleme sistemi olan resimleri mevcut kurmuş olduğunuz nesne algılama api ile çağrı yaparak dönen json nesnesini PascalVoc xml çevirir ve sürekliği olan etiketleme işinde size zaman kazandırır. Bir diğer özellik ise nesne ismini yazarak hangi resimde ve xml dosyasında bulunduğunu size gösterir.


# Requirements
- Python3
- PyQt5 Kuruluması (pip3 install pyqt5)
- Requests (pip3 install requests)


# Usage
- python dex.py

# TODO
- Json Pascal voc xml dönüştürürken resmin width ve height dinamik yapmak.

