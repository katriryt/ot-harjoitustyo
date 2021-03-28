import unittest
from maksukortti import Maksukortti

# Tiivistetty tapa tehdä testejä

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kortti = Maksukortti(10)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10 euroa")

    def test_syo_edullisesti_vahentaa_saldoa_oikein(self):
        self.kortti.syo_edullisesti()
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 7.5 euroa")

    def test_syo_maukkaasti_vahentaa_saldoa_oikein(self):
        self.kortti.syo_maukkaasti()
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 6 euroa")

    def test_syo_edullisesti_ei_vie_saldoa_negatiiviseksi(self): 
        self.kortti.syo_maukkaasti()
        self.kortti.syo_maukkaasti()
        self.kortti.syo_edullisesti()
#        self.assertEqual("Kortilla on rahaa 2 euroa", str(self.kortti)) # vaihdettu suunta ohjeen mukaan
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 2 euroa")

    def test_kortille_voi_ladata_rahaa(self):
        self.kortti.lataa_rahaa(25)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 35 euroa")

    def test_kortin_saldo_ei_ylita_maksimiarvoa(self):
        self.kortti.lataa_rahaa(200)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 150 euroa")
    
    # Oman testin lisäys 1: Maukkaan lounaan syöminen ei vie saldo negatiiviseksi 

    def test_syo_maukkaasti_ei_vie_saldoa_negatiiviseksi(self): # yritetään syödä kolme kertaa maukkaasti eli 3 * EUR 4, ei pitäisi sallia viimeistä kertaa
        self.kortti.syo_maukkaasti()
        self.kortti.syo_maukkaasti()
        self.kortti.syo_maukkaasti()
#        self.assertEqual("Kortilla on rahaa 2 euroa", str(self.kortti)) # vaihdettu suunta ohjeen mukaan
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 2 euroa")


    # Oman testin lisäys 2: Negatiivisen suman lataaminen ei muuta kortin saldoa 
    def test_negatiivinen_lataus_ei_muuta_arvoa(self): 
        self.kortti.lataa_rahaa(-5)
#        self.assertEqual("Kortilla on rahaa 10 euroa", str(self.kortti)), suunta vaihdettu ohjeen mukaan 
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10 euroa")

    # Oman testin lisäys 3: Kortilla voi ostaa edullisen lounaan, kun rahaa on vain edullisen lounaan verran 
    def test_syo_edullisesti_nelja_kertaa(self):
        self.kortti.syo_edullisesti()
        self.kortti.syo_edullisesti()
        self.kortti.syo_edullisesti()
        self.kortti.syo_edullisesti()
#        self.assertEqual("Kortilla on rahaa 0.0 euroa", str(self.kortti)) # suunta vaihdettu
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 0.0 euroa")
    
    # Oman testin lisäys 4: Kortilla pystyy ostamaan maukkaan lounaan, kun kortilla vain maukkana lounaan verran rahaa (eli 4 e)
    def test_syo_maukkaasti_kun_kortilla_nelja_euroa(self):
        self.kortti.syo_maukkaasti()
        self.kortti.syo_maukkaasti()
        self.kortti.lataa_rahaa(2)
        self.kortti.syo_maukkaasti()
#        self.assertEqual("Kortilla on rahaa 0 euroa", str(self.kortti)) # suunta vaihdettu ohjeen mukaan
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 0 euroa")

