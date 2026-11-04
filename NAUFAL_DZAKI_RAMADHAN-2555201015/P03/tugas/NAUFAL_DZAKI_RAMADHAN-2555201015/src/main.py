"""Titik masuk program. Satu-satunya berkas yang boleh mencetak."""

from src.mahasiswa import Mahasiswa
from src.model.alat_tani import AlatTani
from src.model.alamat import Alamat
from src.model.penyewa import Penyewa


def main() -> None:
    # P01: Identitas mahasiswa
    saya = Mahasiswa(
        "Naufal Dzaki Ramadhan",
        "2555201015",
        "Bangkinang Seberang",
    )
    print(saya.perkenalan())

    # P02: Data penyewa
    budi = Penyewa(
        "1406012509900001",
        "Budi Santoso",
        Alamat("Melati", "Kuok", "Bangkinang"),
        "0812-3456-7890",
    )

    siti = Penyewa(
        "1406014403950002",
        "Siti Aminah",
        Alamat("Mawar", "Salo", "Bangkinang"),
    )

    # P02: Data alat pertanian
    traktor = AlatTani(
        "TR-01",
        "Traktor Roda Dua Kubota",
        150000,
    )

    pompa = AlatTani(
        "PA-01",
        "Pompa Air 3 Inci",
        75000,
    )

    print(budi.identitas())
    print(budi.kontak())
    print(siti.kontak())

    print("\nDaftar Tarif Alat Pertanian:")
    daftar_alat = [traktor, pompa]

    for alat in daftar_alat:
        print(f"{alat.nama:<30} {alat.tarif_harian:>14,}")


if __name__ == "__main__":
    main()