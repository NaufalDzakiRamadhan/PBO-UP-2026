"""Pengujian untuk kelas Petugas."""

from src.model.petugas import Petugas


def test_identitas_petugas() -> None:
    petugas = Petugas("PT-001", "Andi", "Operator")
    assert petugas.identitas() == "Andi (PT-001) — Operator"


def test_kontak_dengan_telepon() -> None:
    petugas = Petugas("PT-002", "Budi", "Admin", "08123456789")
    assert petugas.kontak() == "Budi dapat dihubungi di 08123456789"


def test_kontak_tanpa_telepon() -> None:
    petugas = Petugas("PT-003", "Siti", "Kasir")
    assert petugas.kontak() == "Siti belum mencantumkan nomor telepon"


def test_dua_petugas_memiliki_data_sendiri() -> None:
    andi = Petugas("PT-001", "Andi", "Operator")
    budi = Petugas("PT-002", "Budi", "Admin")

    assert andi.identitas() != budi.identitas()
    assert andi.kontak() != budi.kontak()