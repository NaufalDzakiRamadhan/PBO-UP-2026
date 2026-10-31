
"""Pengujian untuk kelas Penyewa."""

from src.model.penyewa import Penyewa


def test_identitas_penyewa() -> None:
    penyewa = Penyewa("12345", "Budi", "Kuok")
    assert penyewa.identitas() == "Budi (12345) — Desa Kuok"


def test_kontak_dengan_telepon() -> None:
    penyewa = Penyewa("12345", "Budi", "Kuok", "08123456789")
    assert penyewa.kontak() == "Budi dapat dihubungi di 08123456789"


def test_kontak_tanpa_telepon() -> None:
    penyewa = Penyewa("67890", "Siti", "Salo")
    assert penyewa.kontak() == "Siti belum mencantumkan nomor telepon"


def test_dua_penyewa_memiliki_data_sendiri() -> None:
    budi = Penyewa("12345", "Budi", "Kuok")
    siti = Penyewa("67890", "Siti", "Salo")
    assert budi.identitas() != siti.identitas()
