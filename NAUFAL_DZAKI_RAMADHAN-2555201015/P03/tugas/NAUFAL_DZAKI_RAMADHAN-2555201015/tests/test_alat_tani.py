import pytest

from src.model.alat_tani import AlatTani


def test_tarif_wajar_tanpa_objek():
    assert AlatTani.tarif_wajar(10000) is True
    assert AlatTani.tarif_wajar(5000000) is True
    assert AlatTani.tarif_wajar(5000) is False


def test_format_rupiah():
    assert AlatTani.format_rupiah(150000) == "Rp150.000"


def test_tarif_di_bawah_minimum_ditolak():
    with pytest.raises(ValueError):
        AlatTani("TR-01", "Traktor", 5000)


def test_tarif_di_atas_maksimum_ditolak():
    with pytest.raises(ValueError):
        AlatTani("TR-01", "Traktor", 6000000)


def test_jumlah_terdaftar_bertambah():
    sebelum = AlatTani.jumlah_terdaftar()

    AlatTani("TR-02", "Traktor Baru", 150000)

    sesudah = AlatTani.jumlah_terdaftar()

    assert sesudah == sebelum + 1


def test_dari_baris_csv_berhasil():
    alat = AlatTani.dari_baris_csv(
        "TR-03;Traktor Besar;250000"
    )

    assert alat.kode == "TR-03"
    assert alat.nama == "Traktor Besar"
    assert alat.tarif_harian == 250000


def test_csv_tarif_bukan_angka_ditolak():
    with pytest.raises(ValueError):
        AlatTani.dari_baris_csv(
            "TR-04;Traktor;abc"
        )


def test_csv_format_salah_ditolak():
    with pytest.raises(ValueError):
        AlatTani.dari_baris_csv(
            "TR-05;Traktor"
        )


def test_denda_keterlambatan():
    alat = AlatTani("TR-06", "Traktor", 150000)

    assert alat.denda_keterlambatan(2) == 30000


def test_hari_terlambat_negatif_ditolak():
    alat = AlatTani("TR-07", "Traktor", 150000)

    with pytest.raises(ValueError):
        alat.denda_keterlambatan(-1)