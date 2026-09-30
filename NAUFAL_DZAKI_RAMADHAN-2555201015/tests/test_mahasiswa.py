"""Pengujian untuk kelas Mahasiswa.""" 

from src.mahasiswa import Mahasiswa 

def test_perkenalan_memuat_nama() -> None:    
    saya = Mahasiswa("Budi Santoso", "2410123456", "Kuok")    
    assert "Budi Santoso" in saya.perkenalan() 

def test_atribut_dibaca_lewat_property() -> None:    
    saya = Mahasiswa("Andi", "2410123458", "Bangkinang")    
    assert saya.nama == "Andi"    
    assert saya.asal_desa == "Bangkinang"