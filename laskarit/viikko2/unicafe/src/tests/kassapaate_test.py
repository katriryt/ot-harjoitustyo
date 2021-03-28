import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
#        self.maksukortti = Maksukortti(1000)

    def test_luotu_kassapaate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    # Testi 1a: Onko luodun kassapaatteen rahamäärä on oikein 
    # Oletus: rahamäärän merkintä kuten maksukortti-luokassa, eli palautettu summa tulee jakaa 100:lla
    def test_konstruktori_kassan_rahamaara_alussa_oikein(self): 
        self.assertEqual(self.kassapaate.kassassa_rahaa/100, 1000)

    # Testi 1b: Edullisia lounaita on myyty nolla 
    def test_konstruktori_edullisia_myyty_alussa_nolla(self): 
        self.assertEqual(self.kassapaate.edulliset/100, 0.0)

    # Testi 1c: Maukkaita lounaita on myyty nolla 
    def test_konstruktori_maukkaita_myyty_alussa_nolla(self): 
        self.assertEqual(self.kassapaate.maukkaat/100, 0.0)

    # Testi 2: KÄTEISOSTO toimii EDULLISTEN lounaiden osalta
    # 2.1 Jos maksu on riittävä: kassassa oleva rahamäärä kasvaa lounaan hinnalla...
    def test_syo_edullisesti_kateisella_maksu_riittaa_kassa_oikein(self): 
        self.kassapaate.syo_edullisesti_kateisella(400)                     # annetaan 400, lounaan hinta 240
        self.assertEqual(self.kassapaate.kassassa_rahaa/100, 1002.4)        # kassan rahat kasvavat 1000 + 2.4

    # 2.2 Jos maksu on riittävä: vaihtorahan suuruus on oikea
    def test_syo_edullisesti_kateisella_maksu_riittaa_vaihtoraha_oikein(self): 
        palautus = self.kassapaate.syo_edullisesti_kateisella(400)          # annetaan 400
        self.assertEqual(palautus, (400-240))                               # palauttaa 400-240 lounaan hinta

    # 2.3 Jos maksu on riittävä: myytyjen lounaiden määrä kasvaa
    def test_syo_edullisesti_kateisella_maksu_riittaa_lounaiden_maara_kasvaa(self): 
        self.kassapaate.syo_edullisesti_kateisella(400)                     # annetaan 400, lounaan hinta 240
        self.assertEqual(self.kassapaate.edulliset, 1)                      # edullisia on myyty 1

    # 2.4 Jos maksu ei ole riittävä, kassassa oleva rahamäärä ei muutu
    def test_syo_edullisesti_kateisella_maksu_ei_riita_kassa_oikein(self): 
        self.kassapaate.syo_edullisesti_kateisella(200)                     # annetaan 200, lounaan hinta 240
        self.assertEqual(self.kassapaate.kassassa_rahaa/100, 1000)          # kassan rahat eivät muutu

    # 2.4 Jos maksu ei ole riittävä, kaikki rahat palautetaan vaihtorahana
    def test_syo_edullisesti_kateisella_maksu_ei_riita_vaihtoraha_oikein(self): 
        palautus = self.kassapaate.syo_edullisesti_kateisella(200)          # annetaan 200
        self.assertEqual(palautus, (200))                                   # palauttaa annetun summan

    # 2.4 Jos maksu ei ole riittävä, lounaiden määrässä ei muutosta
    def test_syo_edullisesti_kateisella_maksu_ei_riita_lounaiden_maara_ei_kasva(self): 
        self.kassapaate.syo_edullisesti_kateisella(200)                     # annetaan 200, lounaan hinta 240
        self.assertEqual(self.kassapaate.edulliset, 0)                      # edullisia on myyty 0

    # Testi 3: KÄTEISOSTO toimii MAUKKAIDEN lounaiden osalta
    # 3.1 Jos maksu on riittävä: kassassa oleva rahamäärä kasvaa lounaan hinnalla...
    def test_syo_maukkaasti_kateisella_maksu_riittaa_kassa_oikein(self): 
        self.kassapaate.syo_maukkaasti_kateisella(1000)                   # annetaan 1000, lounaan hinta 4000
        self.assertEqual(self.kassapaate.kassassa_rahaa/100, (1000+4))    

    # 3.2 Jos maksu on riittävä: vaihtorahan suuruus on oikea
    def test_syo_maukkaasti_kateisella_maksu_riittaa_vaihtoraha_oikein(self): 
        palautus = self.kassapaate.syo_maukkaasti_kateisella(1000)          # annetaan 1000
        self.assertEqual(palautus, (1000-400))                               # palauttaa 400-240 lounaan hinta

    # 3.3 Jos maksu on riittävä: myytyjen lounaiden määrä kasvaa
    def test_syo_maukkaasti_kateisella_maksu_riittaa_lounaiden_maara_kasvaa(self): 
        self.kassapaate.syo_maukkaasti_kateisella(1000)                     # annetaan 1000, lounaan hinta 400
        self.assertEqual(self.kassapaate.maukkaat, 1)                       # maukkaita on myyty 1

    # 3.4 Jos maksu ei ole riittävä, kassassa oleva rahamäärä ei muutu
    def test_syo_maukkaasti_kateisella_maksu_ei_riita_kassa_oikein(self): 
        self.kassapaate.syo_maukkaasti_kateisella(300)                      
        self.assertEqual(self.kassapaate.kassassa_rahaa/100, 1000)          

    # 3.4 Jos maksu ei ole riittävä, kaikki rahat palautetaan vaihtorahana
    def test_syo_maukkaasti_kateisella_maksu_ei_riita_vaihtoraha_oikein(self): 
        palautus = self.kassapaate.syo_maukkaasti_kateisella(300)          
        self.assertEqual(palautus, (300))                                   

    # 3.4 Jos maksu ei ole riittävä, lounaiden määrässä ei muutosta
    def test_syo_maukkaasti_kateisella_maksu_ei_riita_lounaiden_maara_ei_kasva(self): 
        self.kassapaate.syo_maukkaasti_kateisella(200)                     
        self.assertEqual(self.kassapaate.maukkaat, 0)                      

    # Testi 4: KORTTIOSTO toimii EDULLISTEN lounaiden osalta

    # 4.1 Kortilla on tarpeeksi rahaa, summa veloitetaan oikein kortilta
    def test_syo_edullisesti_kortilla_saldo_riittaa_kortin_saldo_oikein(self):
        self.maksukortti = Maksukortti(1000)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, (1000-240))

    # 4.2 Kortilla on tarpeeksi rahaa, funktio palauttaa True
    def test_syo_edullisesti_kortilla_saldo_riittaa_osto_onnistuu(self):
        self.maksukortti = Maksukortti(1000)
        vastaus = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(vastaus, True)
    
    # 4.3 Kortilla on tarpeeksi rahaa, myytyjen lounaiden määrä kasvaa
    def test_syo_edullisesti_kortilla_saldo_riittaa_lounaiden_maara_oikein(self):
        self.maksukortti = Maksukortti(1000)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    # 4.4 Kortilla ei ole tarpeeksi rahaa, kortin rahamäärä ei muutu
    def test_syo_edullisesti_kortilla_saldo_ei_riita_kortin_saldo_ei_muutu(self):
        self.maksukortti = Maksukortti(5)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 5)

    # 4.5 Kortilla ei ole tarpeeksi rahaa, lounaiden määrä ei muutu
    def test_syo_edullisesti_kortilla_saldo_ei_riita_lounaiden_maara_ei_muutu(self):
        self.maksukortti = Maksukortti(5)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 0)

    # 4.5 Kortilla ei ole tarpeeksi rahaa, funktio palauttaa False
    def test_syo_edullisesti_kortilla_saldo_ei_riita_osto_ei_onnistu(self):
        self.maksukortti = Maksukortti(5)
        vastaus = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(vastaus, False)

    # 4.6 Kortilla on rahaa, mutta kassassa oleva rahamäärä ei muutu
    def test_syo_edullisesti_kortilla_saldo_riittaa_kassa_ei_muutu(self):
        self.maksukortti = Maksukortti(1000)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    # 4.6 Kortilla ei ole rahaa, kassassa oleva rahamäärä ei muutu
    def test_syo_edullisesti_kortilla_saldo_ei_riita_kassa_ei_muutu(self):
        self.maksukortti = Maksukortti(5)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    # Testi 5: KORTTIOSTO toimii MAUKKAIDEN lounaiden osalta

    # 5.1 Kortilla on tarpeeksi rahaa, summa veloitetaan oikein kortilta
    def test_syo_maukkaasti_kortilla_saldo_riittaa_kortin_saldo_oikein(self):
        self.maksukortti = Maksukortti(1000)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, (1000-400))

    # 5.2 Kortilla on tarpeeksi rahaa, funktio palauttaa True
    def test_syo_maukkaasti_kortilla_saldo_riittaa_osto_onnistuu(self):
        self.maksukortti = Maksukortti(1000)
        vastaus = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(vastaus, True)
    
    # 5.3 Kortilla on tarpeeksi rahaa, myytyjen lounaiden määrä kasvaa
    def test_syo_maukkaasti_kortilla_saldo_riittaa_lounaiden_maara_oikein(self):
        self.maksukortti = Maksukortti(1000)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    # 5.4 Kortilla ei ole tarpeeksi rahaa, kortin rahamäärä ei muutu
    def test_syo_maukkaasti_kortilla_saldo_ei_riita_kortin_saldo_ei_muutu(self):
        self.maksukortti = Maksukortti(300)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 300)

    # 5.5 Kortilla ei ole tarpeeksi rahaa, lounaiden määrä ei muutu
    def test_syo_maukkaasti_kortilla_saldo_ei_riita_lounaiden_maara_ei_muutu(self):
        self.maksukortti = Maksukortti(300)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    # 5.5 Kortilla ei ole tarpeeksi rahaa, funktio palauttaa False
    def test_syo_maukkaasti_kortilla_saldo_ei_riita_osto_ei_onnistu(self):
        self.maksukortti = Maksukortti(300)
        vastaus = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(vastaus, False)

    # 5.6 Kortilla on rahaa, mutta kassassa oleva rahamäärä ei muutu
    def test_syo_maukkaasti_kortilla_saldo_riittaa_kassa_ei_muutu(self):
        self.maksukortti = Maksukortti(1000)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    # 5.6 Kortilla ei ole rahaa, kassassa oleva rahamäärä ei muutu
    def test_syo_edullisesti_kortilla_saldo_ei_riita_kassa_ei_muutu(self):
        self.maksukortti = Maksukortti(300)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    # 6a. Kortille ladataan rahaa positiivinen määrä. Kortin saldon muuttuu. 
    def test_lataa_rahaa_kortille_kortin_saldo_muuttuu(self):
        self.maksukortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(self.maksukortti.saldo, 2000)

    # 6b. Kortille ladataan rahaa positiivinen määrä. Kassan rahamäärä kasvaa
    def test_lataa_rahaa_kortille_kassa_muuttuu(self):
        self.maksukortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, (100000+1000))

    # 6c. Kortille ladataan rahaa NEGATIIVINEN määrä. Kortin saldo ei muutu. 
    def test_lataa_rahaa_nega_kortille_kortin_saldo_ei_muutu(self):
        self.maksukortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1000)
        self.assertEqual(self.maksukortti.saldo, 1000)

    # 66. Kortille ladataan rahaa NEGATIIVINEN määrä. Kassan rahamäärä kasvaa
    def test_lataa_rahaa_nega_kortille_kassa_ei_muutu(self):
        self.maksukortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
