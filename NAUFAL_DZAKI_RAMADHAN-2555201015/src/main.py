"""Titik masuk program. Satu-satunya berkas yang boleh mencetak ke layar.""" 

from src.mahasiswa import Mahasiswa 

def main() -> None:    
    saya = Mahasiswa("Naufal Dzaki Ramadhan", "2555201015", "Bangkinang Seberang")    
    print(saya.perkenalan()) 
    
if __name__ == "__main__":    
    main()