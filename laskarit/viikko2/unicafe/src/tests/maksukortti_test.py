import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    # Testi 1: Onko kortin saldo alussa oikein 
    def test_konstruktori_saldo_alussa_oikein(self): 
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    # Testi 2: Rahan lataaminen kasvattaa saldoa oikein, lisätään 5 rahaa
    def test_lataa_rahaa_kasvaa_oikein(self): 
        self.maksukortti.lataa_rahaa(5)
        self.assertEqual(str(self.maksukortti), "saldo: 0.15")
    
    # Testi 3a: Rahan ottaminen toimii oikein, saldo vähenee oikein, jos rahaa on tarpeeksi
    def test_ota_rahaa_saldo_vahenee_kun_on_rahaa(self): 
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(str(self.maksukortti), "saldo: 0.05")
    
    # Testi 3b: Rahan ottaminen toimii oikein: saldo ei muutu, jos rahaa ei ole tarpeeksi
    def test_ota_rahaa_saldo_ei_vahene_jos_ei_tarpeeksi_rahaa(self): 
        self.maksukortti.ota_rahaa(15)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    # Testi 3c: Rahan ottaminen toimii oikein: metodi palauttaa True, jos rahat riittivät
    def test_ota_rahaa_palauttaa_true_kun_raha_riittää(self): 
        vastaus = self.maksukortti.ota_rahaa(5)
        self.assertEqual(vastaus, True)

    # Testi 3d: Rahan ottaminen toimii oikein: metodi palauttaa False, jos rahat eivät riittäneet
    def test_ota_rahaa_palauttaa_false_kun_raha_ei_riitä(self): 
        vastaus = self.maksukortti.ota_rahaa(15)
        self.assertEqual(vastaus, False)