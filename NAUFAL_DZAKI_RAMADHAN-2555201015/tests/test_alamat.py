"""Pengujian untuk class Alamat."""

import pytest

from src.model.alamat import Alamat


def test_membuat_alamat() -> None:
    alamat = Alamat("Melati", "Suka Maju", "Bangkinang")
    assert alamat.dusun == "Melati"
    assert alamat.desa == "Suka Maju"
    assert alamat.kecamatan == "Bangkinang"


def test_alamat_lengkap() -> None:
    alamat = Alamat("Melati", "Suka Maju", "Bangkinang")
    assert alamat.lengkap() == (
        "Dusun Melati, Desa Suka Maju, Kecamatan Bangkinang"
    )


def test_alamat_singkat() -> None:
    alamat = Alamat("Melati", "Suka Maju", "Bangkinang")
    assert alamat.singkat() == "Suka Maju, Bangkinang"


def test_desa_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Alamat("Melati", "", "Bangkinang")


def test_kecamatan_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Alamat("Melati", "Suka Maju", "")


def test_alamat_tidak_bisa_diubah() -> None:
    alamat = Alamat("Melati", "Suka Maju", "Bangkinang")
    with pytest.raises(AttributeError):
        setattr(alamat, "desa", "Desa Baru")