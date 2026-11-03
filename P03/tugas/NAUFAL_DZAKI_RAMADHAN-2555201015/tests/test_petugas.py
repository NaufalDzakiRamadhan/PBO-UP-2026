"""Pengujian untuk class Petugas."""

import pytest

from src.model.petugas import Petugas, IdentitasPetugas


def test_identitas_petugas() -> None:
    petugas = Petugas("P001", "Budi", "Kasir")
    assert petugas.identitas() == "Budi (P001) ΓÇö Kasir"


def test_kontak_petugas() -> None:
    petugas = Petugas("P001", "Budi", "Kasir", "081234567890")
    assert petugas.kontak() == "Budi dapat dihubungi di 081234567890"


def test_kontak_tanpa_nomor() -> None:
    petugas = Petugas("P001", "Budi", "Kasir")
    assert petugas.kontak() == "Budi belum mencantumkan nomor telepon"


def test_dua_petugas_berbeda() -> None:
    budi = Petugas("P001", "Budi", "Kasir")
    siti = Petugas("P002", "Siti", "Admin")
    assert budi.identitas() != siti.identitas()


def test_nip_readonly() -> None:
    petugas = Petugas("P001", "Budi", "Kasir")
    with pytest.raises(AttributeError):
        setattr(petugas, "nip", "P002")


def test_nama_readonly() -> None:
    petugas = Petugas("P001", "Budi", "Kasir")
    with pytest.raises(AttributeError):
        setattr(petugas, "nama", "Siti")


def test_nomor_telepon_valid() -> None:
    petugas = Petugas("P001", "Budi", "Kasir", "0812-3456-7890")
    assert petugas.nomor_telepon == "081234567890"


def test_nomor_telepon_invalid() -> None:
    with pytest.raises(ValueError):
        Petugas("P001", "Budi", "Kasir", "12345")


def test_nomor_telepon_bisa_diubah() -> None:
    petugas = Petugas("P001", "Budi", "Kasir")
    petugas.nomor_telepon = "081234567890"
    assert petugas.nomor_telepon == "081234567890"


def test_identitas_petugas_frozen() -> None:
    identitas = IdentitasPetugas("P001", "Budi", "Kasir")
    with pytest.raises(AttributeError):
        setattr(identitas, "nama", "Siti")