"""Model domain: petugas yang mengelola layanan UPJA."""


class Petugas:
    """Mewakili petugas yang bekerja pada UPJA."""

    def __init__(
        self,
        nip: str,
        nama: str,
        jabatan: str,
        nomor_telepon: str = "-",
    ) -> None:
        self._nip = nip
        self._nama = nama
        self._jabatan = jabatan
        self._nomor_telepon = nomor_telepon

    def identitas(self) -> str:
        """Mengembalikan identitas petugas."""
        return f"{self._nama} ({self._nip}) — {self._jabatan}"

    def kontak(self) -> str:
        """Mengembalikan informasi kontak petugas."""
        if self._nomor_telepon == "-":
            return f"{self._nama} belum mencantumkan nomor telepon"
        return f"{self._nama} dapat dihubungi di {self._nomor_telepon}"