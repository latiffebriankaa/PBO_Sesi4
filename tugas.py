#nama : latip
#NIM : 20240040036

class BankAccount:
    def __init__(self, akun, saldo, pin):
        # public 
        self.akun = akun
        # protected 
        self._saldo = saldo
        # private 
        self.__pin = pin

    # getter
    def get_saldo(self):
        return self._saldo

    # Setter 
    def set_saldo(self, jumlah):
        if jumlah > 0:
            self._saldo = jumlah
            print(f"Saldo berhasil diperbarui menjadi Rp {self._saldo}")
        else:
            print("Jumlah harus positif")

    # Verif PIN
    def verify_pin(self, pin):
        return self.__pin == pin


def menu_utama():
    print()
    print("  MENU UTAMA")
    print("1. Lihat Nama Pemilik Akun (public)")
    print("2. Akses Atribut Protected (protect)")
    print("3. Akses Atribut Private (private)")
    print("4. Lihat Saldo")
    print("5. Ubah Saldo")
    print("6. Verifikasi PIN")
    print("0. Keluar")


def main():
    # akun bank
    akun = BankAccount(
        akun="Latip",
        saldo=5_000_000,
        pin="1234"
    )

    # menu utama
    while True:
        menu_utama()
        pilihan = input("pilih menu:").strip()

        #Public 
        if pilihan == "1":
            print()
            print(f"  nama akun : '{akun.akun}'")
            print("ini adalah atribut public dapat diakses langsung dari luar kelas.")

        #Protected 
        elif pilihan == "2":
            print()
            print(f"  saldo akun = Rp {akun._saldo}")
            print("ini adalah atribut protected mmasih bisa di akses tapi tidak di sarankan di akses dari luar")

        #Private 
        elif pilihan == "3":
            print()
            print("mencoba mengakses harusnya erorr karena ini bersifat private")
            try:
                _ = akun.__pin          # sengaja memicu AttributeError
            except AttributeError as e:
                print(f" AttributeError: {e}")
            print()
            print(f"  pin akun = '{akun._BankAccount__pin}'")
            print("Tidak bisa diakses normal, hanya lewat method kelas.")

        #Lihat saldo (getter)
        elif pilihan == "4":
            print()
            pin_input = input("  Masukkan PIN Anda: ").strip()
            if akun.verify_pin(pin_input):
                saldo = akun.get_saldo()
                print(f"PIN benar, Saldo Anda: Rp {saldo}")
            else:
                print("PIN salah, Akses ditolak.")

        #Ubah saldo (setter) 
        elif pilihan == "5":
            print()
            try:
                nominal = float(input("  Masukkan saldo baru (Rp):").strip())
                akun.set_saldo(nominal)
            except ValueError:
                print("Masukkan angka yang benar")

        #Verifikasi PIN
        elif pilihan == "6":
            print()
            pin_input = input("Masukkan PIN untuk diverifikasi: ").strip()
            hasil = akun.verify_pin(pin_input)
            if hasil:
                print("PIN BENAR")
            else:
                print("PIN SALAH")

        #Keluar
        elif pilihan == "0":
            print()
            print("  Terima kasih telah menggunakan ATM latip ")
            print()
            break

        else:
            print("Pilihan tidak valid. Masukkan angka 0-6.")
        input("\nTekan Enter untuk kembali ke menu...")
if __name__ == "__main__":
    main()