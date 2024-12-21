from app import app, db, Product  # app nesnesini ve diğer modelleri içe aktar

# Veritabanını oluştur ve ürünleri ekle
with app.app_context():
    db.create_all()

    # Örnek ürünler
    products = [
        # Televizyonlar
        Product(name="Samsung Smart TV", description="4K UHD HDR Smart TV.", price=15000, city="İstanbul", category="Televizyon", image_url="https://static.ticimax.cloud/33268/uploads/urunresimleri/buyuk/samsung-tv--102-ekran--40-inc--smart-tv--7008.jpeg"),
        Product(name="LG OLED TV", description="OLED ekran, üstün görüntü kalitesi.", price=20000, city="Ankara", category="Televizyon", image_url="https://www.lg.com/content/dam/channel/wcms/tr/images/tv/oled65c34la_apd_emtk_tr_c/gallery/medium05.jpg"),
        Product(name="Sony Bravia", description="4K HDR Görüntü Kalitesi.", price=18000, city="İzmir", category="Televizyon", image_url="https://www.sony.com.tr/image/60fc808004d6860e433b5a4cafeb60d2?fmt=png-alpha&resMode=bisharp&wid=384"),
        Product(name="Philips Ambilight", description="Ambilight özellikli TV.", price=17000, city="Antalya", category="Televizyon", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSZCAVKXKXb_w4qwCZKzHwojRTwnyqoK9Mvsw&s"),
        Product(name="Toshiba Smart TV", description="Akıllı TV özellikli.", price=14000, city="Bursa", category="Televizyon", image_url="https://toshiba-tv.com/assets/img/smart-tv-logos/smart-tv-banner.png"),
        Product(name="Sharp Aquos", description="Yüksek kontrast ve netlik.", price=16000, city="İstanbul", category="Televizyon", image_url="https://m.media-amazon.com/images/I/717ko3Sx+qL.jpg"),
        Product(name="Panasonic Viera", description="Gelişmiş HDR teknolojisi.", price=16500, city="Ankara", category="Televizyon", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcShmVVHSoOUGBL2vtuAUVl1qWTwypD3RmWTCA&s"),
        Product(name="Vestel Smart TV", description="Yerli üretim Smart TV.", price=12000, city="İzmir", category="Televizyon", image_url="https://statics.vestel.com.tr/productimages/20278777_r1_1000_1000.jpg"),
        Product(name="Arçelik UHD TV", description="UHD görüntü kalitesi.", price=13000, city="Antalya", category="Televizyon", image_url="https://cdn.akakce.com/z/arcelik/arcelik-a50-c-885-a-4k-ultra-hd-50-127-ekran-uydu-alicili-android-smart-led-tv.jpg"),
        Product(name="Grundig Smart TV", description="Smart özellikli LED TV.", price=11000, city="Bursa", category="Televizyon", image_url="https://assets.mmsrg.com/isr/166325/c1/-/ASSET_MMS_108382366?x=536&y=402&format=jpg&quality=80&sp=yes&strip=yes&trim&ex=536&ey=402&align=center&resizesource&unsharp=1.5x1+0.7+0.02&cox=0&coy=0&cdx=536&cdy=402"),

        # Tabletler
        Product(name="iPad Pro", description="11 inç, güçlü performans.", price=18000, city="İzmir", category="Tablet", image_url="https://m.media-amazon.com/images/I/81c+9BOQNWL.jpg"),
        Product(name="Samsung Galaxy Tab S7", description="Yüksek performanslı tablet.", price=14000, city="Ankara", category="Tablet", image_url="https://cdn.akakce.com/z/samsung/samsung-tab-s7-fe-wi-fi-sm-t733-64-gb-12-4.jpg"),
        Product(name="Huawei MatePad Pro", description="Premium tablet.", price=13000, city="İstanbul", category="Tablet", image_url="https://img01.huaweifile.com/eu/tr/huawei/uomcdn/TRHW/pms/202410/gbom/6942103131561/group/428_428_BDC215A9F5FEFCC1E1967CB18447E2B0.png"),
        Product(name="Lenovo Tab P11 Pro", description="Ekran kalitesi yüksek.", price=12000, city="Bursa", category="Tablet", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSw1B-qYVIxYTzfFexwVCedM2ExYoA_VMxIAA&s"),
        Product(name="Xiaomi Mi Pad 5", description="Fiyat performans tableti.", price=11000, city="Antalya", category="Tablet", image_url="https://cdn.akakce.com/z/xiaomi/xiaomi-mi-pad-5-256-gb-11.jpg"),
        Product(name="Microsoft Surface Go", description="2'si 1 arada özellik.", price=16000, city="Ankara", category="Tablet", image_url="https://support.content.office.net/tr-tr/media/bdc49c71-5bee-e2e2-6f5e-2a81c235f232.png"),
        Product(name="Amazon Fire HD 10", description="Uygun fiyatlı tablet.", price=9000, city="İstanbul", category="Tablet", image_url="https://resim.epey.com/682125/m_amazon-fire-hd-10-alexa-20129-1.jpg"),
        Product(name="Apple iPad Mini", description="Kompakt ve güçlü.", price=15000, city="İzmir", category="Tablet", image_url="https://store.storeimages.cdn-apple.com/4668/as-images.apple.com/is/ipad-mini-finish-unselect-gallery-1-202410_FMT_WHH?wid=1280&hei=720&fmt=jpeg&qlt=95&.v=1727219498681"),
        Product(name="Realme Pad", description="Şık ve ekonomik tablet.", price=8500, city="Antalya", category="Tablet", image_url="https://m.media-amazon.com/images/I/51VBgr0llWL.jpg"),
        Product(name="TCL NXTPAPER 10s", description="Kağıt hissiyatı veren ekran.", price=10500, city="Bursa", category="Tablet", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTW5t0PAInGAY57lvgkyJEfxTYQUAjtNxDJDg&s"),

        # Laptoplar
        Product(name="MacBook Air", description="M1 çip ile üstün performans.", price=25000, city="Antalya", category="Laptop", image_url="https://store.storeimages.cdn-apple.com/4668/as-images.apple.com/is/mba13-midnight-select-202402?wid=904&hei=840&fmt=jpeg&qlt=90&.v=1708367688034"),
        Product(name="Dell XPS 13", description="Premium ultrabook.", price=22000, city="İstanbul", category="Laptop", image_url="https://m.media-amazon.com/images/I/51YbNtAUKxL._AC_UF1000,1000_QL80_.jpg"),
        Product(name="Lenovo ThinkPad X1 Carbon", description="İş dünyası için tasarlandı.", price=24000, city="Ankara", category="Laptop", image_url="https://cdn.akakce.com/z/lenovo/lenovo-thinkpad-x1-carbon-21ccs03p00-i7-1260p-16-gb-512-gb-ssd-iris-xe-graphics-14-full-hd-notebook.jpg"),
        Product(name="HP Spectre x360", description="Şık ve dönüştürülebilir laptop.", price=23000, city="İzmir", category="Laptop", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcScdrCWKcFJCfMpT91kqDYB4vo4fF-xZGryyg&s"),
        Product(name="Acer Swift 3", description="Uygun fiyatlı ultrabook.", price=20000, city="Antalya", category="Laptop", image_url="https://resim.epey.com/779413/m_acer-swift-3-sf314-43-r0ab-7.png"),
        Product(name="Asus ZenBook 14", description="İnce ve hafif.", price=21000, city="İstanbul", category="Laptop", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcToSwqMdVBn65rrvB6g7ms4WN0Ir90rrC02RA&s"),
        Product(name="MSI Prestige 14", description="Performans odaklı tasarım.", price=22000, city="Ankara", category="Laptop", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQXm_1npDjlpfCnyaFAKgRQ5If6QMnUc7nv7g&s"),
        Product(name="Razer Blade 14", description="Oyun ve iş için güçlü laptop.", price=28000, city="İzmir", category="Laptop", image_url="https://m.media-amazon.com/images/I/712g5R0vkbL._AC_UF1000,1000_QL80_.jpg"),
        Product(name="Microsoft Surface Laptop 4", description="Windows deneyimi.", price=26000, city="Antalya", category="Laptop", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTRrCGKAuagkGHmv6_cS9uRN0K9GFnfj-OlYA&s"),
        Product(name="Apple MacBook Pro", description="Profesyonel işler için tasarlandı.", price=30000, city="İstanbul", category="Laptop", image_url="https://ideacdn.net/trsh/op/33/myassets/products/858/mbp-spacegray-gallery2-202206-geo-tr.jpg?revision=1705912224"),

        # Monitörler
        Product(name="Dell UltraSharp", description="4K çözünürlüklü monitör.", price=10000, city="İstanbul", category="Monitör", image_url="https://m.media-amazon.com/images/I/A1Iqr2v1SIL._AC_UF1000,1000_QL80_.jpg"),
        Product(name="LG UltraFine", description="HDR özellikli monitör.", price=9000, city="Ankara", category="Monitör", image_url="https://m.media-amazon.com/images/I/71Vo+dKKTkL.jpg"),
        Product(name="Samsung Smart Monitor", description="Akıllı monitör.", price=12000, city="İzmir", category="Monitör", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTCKOx7cgo17l43fMCNXXhEUS4z2c4qh9Dj3A&s"),
        Product(name="Acer Predator", description="Oyun için 240Hz monitör.", price=11000, city="Bursa", category="Monitör", image_url="https://m.media-amazon.com/images/I/71HdHQuk+TL.jpg"),
        Product(name="HP EliteDisplay", description="İş odaklı monitör.", price=8000, city="Antalya", category="Monitör", image_url="https://m.media-amazon.com/images/I/71M89MyMsZL._AC_UF1000,1000_QL80_.jpg"),
        Product(name="Philips 276E", description="IPS ekranlı monitör.", price=8500, city="İstanbul", category="Monitör", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT6qpaLMLy6xTIpqKPq0SKC-SyB4GsF7SV8yA&s"),
        Product(name="MSI Optix", description="E-spor oyuncuları için monitör.", price=9500, city="Ankara", category="Monitör", image_url="https://cdn.akakce.com/_static/574415691/msi-optix-g24c4.png"),
        Product(name="ViewSonic VX", description="Geniş renk yelpazesi.", price=7000, city="İzmir", category="Monitör", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVXT_bNDRB9RzGU8XA5eNYTNv6mxFGodXErA&s"),
        Product(name="BenQ EX", description="Video düzenleme için monitör.", price=9800, city="Antalya", category="Monitör", image_url="https://cdn.akakce.com/z/benq/benq-ex2710q-27ips-qhd-2k-1ms-165hz-freesync-hdmi-dp-usb3-0-subwoofer-oyun-u.jpg"),
        Product(name="Asus TUF Gaming", description="Oyun için ideal.", price=9400, city="Bursa", category="Monitör", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRd3MGcLBfUUOgkKMyQtV6Eenq-caBjct6ldA&s"),

        # Kulaklıklar
        Product(name="Sony WH-1000XM4", description="Gürültü önleyici kablosuz kulaklık.", price=5000, city="İstanbul", category="Kulaklık", image_url="https://cdn.dsmcdn.com/ty1551/product/media/images/ty1552/prod/QC/20240917/11/b2245b4c-b7a5-34c5-8eab-5e4e42c4cdb6/1_org_zoom.jpg"),
        Product(name="Apple AirPods Pro", description="ANC özellikli kulaklık.", price=3500, city="Ankara", category="Kulaklık", image_url="https://assets.mmsrg.com/isr/166325/c1/-/ASSET_MMS_120875347"),
        Product(name="Bose QC35 II", description="Konforlu gürültü önleyici kulaklık.", price=4500, city="İzmir", category="Kulaklık", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRUB1lfKiehZMl5E2DhIyi6O6zRWAx6VzEC9Q&s"),
        Product(name="Jabra Elite 85h", description="Suya dayanıklı kulaklık.", price=4000, city="Antalya", category="Kulaklık", image_url="https://i0.shbdn.com/photos/34/83/40/x5_1196348340iuj.jpg"),
        Product(name="Sennheiser Momentum", description="Hi-Fi ses kalitesi.", price=4800, city="Bursa", category="Kulaklık", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQJ7_qGmqHIaxKS0OlxkhKQO3JAu_CBWCMfGQ&s"),
        Product(name="SteelSeries Arctis Pro", description="Oyun kulaklığı.", price=3000, city="İstanbul", category="Kulaklık", image_url="https://media.steelseriescdn.com/thumbs/filer_public/f4/96/f496026d-385b-4623-9d7e-d63cbac30da9/arctis_pro_wl_white_livingroom_wide_4k_001.jpg__1920x1080_q100_crop-fit_optimize_subsampling-2.jpg"),
        Product(name="Logitech G Pro X", description="Mikrofonlu oyun kulaklığı.", price=3200, city="Ankara", category="Kulaklık", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-WHiBkPJ3bj-h0RTnzfq91y-biQwkDlUv3w&s"),
        Product(name="HyperX Cloud II", description="Oyuncular için kulaklık.", price=2800, city="İzmir", category="Kulaklık", image_url="https://img.joomcdn.net/2c01824a1de9acdb4ff8022dd2eb91471ec9498e_original.jpeg"),
        Product(name="Razer Kraken", description="RGB ışıklı kulaklık.", price=2600, city="Antalya", category="Kulaklık", image_url="https://cdn.akakce.com/razer/razer-kraken-tournament-edition-7-1-mikrofonlu-oyuncu-kulakligi-z.jpg"),
        Product(name="Plantronics BackBeat", description="Bluetooth özellikli.", price=2000, city="Bursa", category="Kulaklık", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSyRdP7nAbnYbWndstp2E-A6awG0nOK88iuBA&s"),
    ]

    db.session.add_all(products)
    db.session.commit()
    print("Veritabanı ve ürünler başarıyla oluşturuldu.")
