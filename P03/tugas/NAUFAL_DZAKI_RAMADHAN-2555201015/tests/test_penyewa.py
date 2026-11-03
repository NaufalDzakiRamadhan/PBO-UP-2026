"""Pengujian untuk kelas Penyewa."""

import pytest

from src.model.alamat import Alamat
from src.model.penyewa import Penyewa


def buat_alamat() -> Alamat:
    return Alamat("Melati", "Kuok", "Bangkinang")


def test_identitas_penyewa() -> None:
    penyewa = Penyewa("1234567890123456", "Budi", buat_alamat())
    assert penyewa.identitas() == (
        "Budi (1234567890123456) ΓÇö Desa Kuok"
    )


def test_kontak_dengan_telepon() -> None:
    penyewa = Penyewa(
        "1234567890123456", "Budi", buat_alamat(), "08123456789"
    )
    assert penyewa.kontak() == "Budi dapat dihubungi di 08123456789"


def test_kontak_tanpa_telepon() -> None:
    penyewa = Penyewa("6789012345678901", "Siti", buat_alamat())
    assert penyewa.kontak() == "Siti belum mencantumkan nomor telepon"


def test_dua_penyewa_memiliki_data_sendiri() -> None:
    budi = Penyewa("1234567890123456", "Budi", buat_alamat())
    siti = Penyewa("6789012345678901", "Siti", buat_alamat())
    assert budi.identitas() != siti.identitas()


def test_nik_harus_16_digit() -> None:
    with pytest.raises(ValueError):
        Penyewa("12345", "Budi", buat_alamat())


def test_nik_tidak_boleh_huruf() -> None:
    with pytest.raises(ValueError):
        Penyewa("123456789012345A", "Budi", buat_alamat())


def test_nik_tidak_bisa_diubah() -> None:
    penyewa = Penyewa("1234567890123456", "Budi", buat_alamat())

    with pytest.raises(AttributeError):
        setattr(penyewa, "nik", "9876543210987654")


def test_telepon_tidak_valid_ditolak() -> None:
    with pytest.raises(ValueError):
        Penyewa("1234567890123456", "Budi", buat_alamat(), "abc")


def test_telepon_minimal_10_digit() -> None:
    with pytest.raises(ValueError):
        Penyewa("1234567890123456", "Budi", buat_alamat(), "123456789")


def test_telepon_dinormalisasi() -> None:
    penyewa = Penyewa(
        "1234567890123456", "Budi", buat_alamat(), "0812-3456-7890"
    )
    assert penyewa.telepon == "081234567890"


def test_alamat_berupa_objek() -> None:
    penyewa = Penyewa("1234567890123456", "Budi", buat_alamat())
    assert isinstance(penyewa.alamat, Alamat)