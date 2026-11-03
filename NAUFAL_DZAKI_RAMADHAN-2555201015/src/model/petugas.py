
"""Model domain: petugas yang mengelola layanan UPJA."""

from dataclasses import dataclass


@dataclass(frozen=True)
class IdentitasPetugas:
    """Value object untuk identitas petugas."""

    nip: str
    nama: str
    jabatan: str

    def __post_init__(self) -> None:
        if not self.nip.strip():
            raise ValueError("NIP tidak boleh kosong.")
        if not self.nama.strip():
            raise ValueError("Nama tidak boleh kosong.")
        if not self.jabatan.strip():
            raise ValueError("Jabatan tidak boleh kosong.")


class Petugas:
    """Mewakili petugas yang bekerja pada UPJA."""

    def __init__(
        self,
        nip: str,
        nama: str,
        jabatan: str,
        nomor_telepon: str = "-",
    ) -> None:
        self._identitas = IdentitasPetugas(nip, nama, jabatan)
        self._nomor_telepon = "-"
        self.nomor_telepon = nomor_telepon

    # Readonly: identitas petugas tidak boleh diganti sembarangan.
    @property
    def nip(self) -> str:
        return self._identitas.nip

    @property
    def nama(self) -> str:
        return self._identitas.nama

    @property
    def jabatan(self) -> str:
        return self._identitas.jabatan

    # Validating setter: nomor telepon dapat diperbarui,
    # tetapi nilainya harus memenuhi aturan.
    @property
    def nomor_telepon(self) -> str:
        return self._nomor_telepon

    @nomor_telepon.setter
    def nomor_telepon(self, nilai: str) -> None:
        if nilai == "-":
            self._nomor_telepon = "-"
            return

        nomor = nilai.replace("-", "").replace(" ", "")

        if not nomor.isdigit() or len(nomor) < 10:
            raise ValueError(
                "Nomor telepon harus berupa angka minimal 10 digit."
            )

        self._nomor_telepon = nomor

    def identitas(self) -> str:
        """Mengembalikan identitas petugas."""
        return (
            f"{self.nama} ({self.nip}) — {self.jabatan}"
        )

    def kontak(self) -> str:
        """Mengembalikan informasi kontak petugas."""
        if self._nomor_telepon == "-":
            return f"{self.nama} belum mencantumkan nomor telepon"
        return (
            f"{self.nama} dapat dihubungi di "
            f"{self.nomor_telepon}"
        )
