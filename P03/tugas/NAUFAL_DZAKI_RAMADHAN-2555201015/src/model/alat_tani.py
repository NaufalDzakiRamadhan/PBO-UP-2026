
"""Model domain: alat yang disewakan UPJA."""


class AlatTani:
    """Satu unit alat pertanian beserta tarif hariannya."""

    TARIF_MAKSIMUM = 5_000_000

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
        """Memvalidasi tarif sebelum disimpan."""
        if nilai <= 0:
            raise ValueError("Tarif harus lebih dari nol.")

        if nilai > self.TARIF_MAKSIMUM:
            raise ValueError(
                f"Tarif tidak boleh lebih dari "
                f"Rp{self.TARIF_MAKSIMUM:,}."
            )

        self._tarif_harian = nilai

    def biaya_sewa(self, jumlah_hari: int) -> int:
        """Menghitung biaya sewa untuk sejumlah hari tertentu."""
        return self._tarif_harian * jumlah_hari

    def keterangan(self) -> str:
        """Mengembalikan baris keterangan alat untuk daftar sewa."""
        rupiah = f"{self._tarif_harian:,}".replace(",", ".")
        return f"[{self._kode}] {self._nama} ΓÇö Rp{rupiah}/hari"