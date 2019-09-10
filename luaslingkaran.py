class lingkaran(object):
   def __init__(self, p, r):
      self.phi = p
      self.jarijari = r
   def hitungluas(self):
      return self.phi * self.jarijari * self.jarijari

def main():
   lingkaranBesar = lingkaran(3.14, 24)

   print('Objek lingkaran Besar')
   print('phi       : ', lingkaranBesar.phi)
   print('jari-jari : ', lingkaranBesar.jarijari)
   print('Luas lingkaran  = ', lingkaranBesar.hitungluas())

   lingkaranKecil = lingkaran(3.14, 4)

   print("\nObjek lingkaran Kecil")
   print('phi       : ', lingkaranKecil.phi)
   print('jari-jari : ', lingkaranKecil.jarijari)
   print("Luas lingkaran  = ", lingkaranKecil.hitungluas())

if __name__ == "__main__":
   main()
