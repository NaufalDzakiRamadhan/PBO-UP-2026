"""Model value object untuk alamat penyewa."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Alamat:
    """Mewakili alamat lengkap seorang penyewa."""

    dusun: str
    desa: str
    kecamatan: str

    def __post_init__(self) -> None:
        if not self.desa.strip():
            raise ValueError("Desa tidak boleh kosong.")

        if not self.kecamatan.strip():
            raise ValueError("Kecamatan tidak boleh kosong.")

    def lengkap(self) -> str:
        return (
            f"Dusun {self.dusun}, Desa {self.desa}, "
            f"Kecamatan {self.kecamatan}"
        )

    def singkat(self) -> str:
        return f"{self.desa}, {self.kecamatan}"