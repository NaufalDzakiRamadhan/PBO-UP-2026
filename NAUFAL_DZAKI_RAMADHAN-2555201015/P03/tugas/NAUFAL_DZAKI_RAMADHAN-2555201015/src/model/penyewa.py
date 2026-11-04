
"""Model domain: petani yang menyewa alat dari UPJA."""

from src.model.alamat import Alamat


class Penyewa:
    """Identitas seorang petani yang menyewa alat dari UPJA."""

    def __init__(
        self,
        nik: str,
        nama: str,
        alamat: Alamat,
        telepon: str = "-",
    ) -> None:
        if len(nik) != 16 or not nik.isdigit():
            raise ValueError("NIK harus terdiri dari tepat 16 digit.")

        self._nik = nik
        self._nama = nama
        self._alamat = alamat
        self._telepon = "-"
        self.telepon = telepon

    @property
    def nik(self) -> str:
        """NIK hanya boleh dibaca karena merupakan identitas tetap."""
        return self._nik

    @property
    def nama(self) -> str:
        """Nama penyewa hanya boleh dibaca melalui properti."""
        return self._nama

    @property
    def alamat(self) -> Alamat:
        """Alamat dikembalikan sebagai objek Alamat yang immutable."""
        return self._alamat

    @property
    def telepon(self) -> str:
        """Nomor telepon penyewa."""
        return self._telepon

    @telepon.setter
    def telepon(self, nilai: str) -> None:
        """Memvalidasi nomor telepon setelah normalisasi."""
        nomor = nilai.replace("-", "").replace(" ", "")

        if nilai == "-":
            self._telepon = "-"
            return

        if not nomor.isdigit() or len(nomor) < 10:
            raise ValueError(
                "Nomor telepon harus berupa angka minimal 10 digit."
            )

        self._telepon = nomor

    def identitas(self) -> str:
        """Mengembalikan baris identitas singkat untuk nota sewa."""
        return (
            f"{self._nama} ({self._nik}) ΓÇö "
            f"Desa {self._alamat.desa}"
        )

    def kontak(self) -> str:
        """Mengembalikan keterangan cara menghubungi penyewa."""
        if self._telepon == "-":
            return f"{self._nama} belum mencantumkan nomor telepon"
        return f"{self._nama} dapat dihubungi di {self._telepon}"