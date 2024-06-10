class Mobil:
    def __init__(self, roda, tipe, kecepatan):
        self.tipe = tipe
        self.roda = roda
        self.kecepatan = kecepatan

    def doMelaju(self):
        print("Melaju dengan kecepatan:", self.kecepatan)

    def doKlakson(self):
        print("Klakson")

    def doBelok(self, arah):
        print("Belok arah", arah)

# Contoh penggunaan class Mobil
mobilAvanza = Mobil(roda=4, tipe="Avanza", kecepatan=80)
mobilAvanza.doMelaju()  # Output: "Melaju dengan kecepatan: 80"
mobilAvanza.doKlakson()  # Output: "Klakson"
mobilAvanza.doBelok("kiri")  # Output: "Belok arah kiri"
