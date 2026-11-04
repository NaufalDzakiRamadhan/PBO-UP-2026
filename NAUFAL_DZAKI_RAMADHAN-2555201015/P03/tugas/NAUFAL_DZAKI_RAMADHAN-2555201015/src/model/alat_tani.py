
"""Model domain: alat yang disewakan UPJA."""
from typing import Final

class AlatTani:
    """Satu unit alat pertanian beserta tarif hariannya."""

    TARIF_MINIMUM: Final[int] = 10_000
    TARIF_MAKSIMUM: Final[int] = 5_000_000
    PERSEN_DENDA_HARIAN: Final[int] = 10
    PEMISAH_BARIS: Final[str] = ";"
    _jumlah_terdaftar: int = 0

    @classmethod
    def dari_baris_csv(cls, baris: str) -> "AlatTani":
        bagian = baris.split(cls.PEMISAH_BARIS)

        if len(bagian) != 3:
            raise ValueError("Format baris CSV harus terdiri dari 3 bagian.")

        kode, nama, tarif_teks = [item.strip() for item in bagian]

        try:
            tarif = int(tarif_teks)
        except ValueError as exc:
            raise ValueError("Tarif harus berupa bilangan bulat.") from exc

        return cls(kode, nama, tarif)
    def denda_keterlambatan(self, hari_terlambat: int) -> int:
        if hari_terlambat < 0:
            raise ValueError("Hari keterlambatan tidak boleh negatif.")

        return (
            self._tarif_harian
            * AlatTani.PERSEN_DENDA_HARIAN
            * hari_terlambat
            // 100
        )
    @classmethod
    def jumlah_terdaftar(cls) -> int:
        return cls._jumlah_terdaftar
    def __init__(
        self,
        kode: str,
        nama: str,
        tarif_harian: int,
    ) -> None:
        self._kode = kode
        self._nama = nama
        self._tarif_harian = 0
        self.tarif_harian = tarif_harian
        AlatTani._jumlah_terdaftar += 1

    @staticmethod
    def tarif_wajar(nilai: int) -> bool:
        return AlatTani.TARIF_MINIMUM <= nilai <= AlatTani.TARIF_MAKSIMUM
    @staticmethod
    def format_rupiah(nilai: int) -> str:
        rupiah = f"{nilai:,}".replace(",", ".")
        return f"Rp{rupiah}"
    @property
    def kode(self) -> str:
        """Kode alat yang hanya bisa dibaca."""
        return self._kode

    @property
    def nama(self) -> str:
        """Nama alat yang hanya bisa dibaca."""
        return self._nama

    @property
    def tarif_harian(self) -> int:
        """Tarif sewa harian alat."""
        return self._tarif_harian

    @tarif_harian.setter
    def tarif_harian(self, nilai: int) -> None:
        if not AlatTani.tarif_wajar(nilai):
            raise ValueError(
                f"Tarif harus antara "
                f"{AlatTani.format_rupiah(AlatTani.TARIF_MINIMUM)} "
                f"dan {AlatTani.format_rupiah(AlatTani.TARIF_MAKSIMUM)}."
            )
        self._tarif_harian = nilai

    def biaya_sewa(self, jumlah_hari: int) -> int:
        """Menghitung biaya sewa untuk sejumlah hari tertentu."""
        return self._tarif_harian * jumlah_hari

    def keterangan(self) -> str:
        """Mengembalikan baris keterangan alat untuk daftar sewa."""
        rupiah = self.format_rupiah(self._tarif_harian)
        return f"[{self._kode}] {self._nama} ΓÇö {rupiah}/hari"

    