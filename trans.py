#coded by kroemen, iam newbie
from googletrans import Translator
import googletrans
import time,sys

merah =('\033[31;1m')
kuning= ('\033[1;33m')
hijau = ('\033[0;32m')
dilangit = ('\033[37;1m')
yang = ('\033[32;1m')
biru = ('\033[0;36m')

def banner(lo):
    for i in lo:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.01)
banner(f"""    
{biru}[V.1[kroemen]]{kuning}▀█▀ █▀█ ▄▀█ █▄░█ █▀ █░░ ▄▀█ ▀█▀ █▀█ █▀█
{biru}[  15/02/21  ]{hijau}░█░ █▀▄ █▀█ █░▀█ ▄█ █▄▄ █▀█ ░█░ █▄█ █▀▄{dilangit}
\n""")


def main():
    try:
        tran = Translator()
        print('Kode Bahasanya'.center(50,'='))
        print(googletrans.LANGUAGES)
        print('='*50)
        print('Masukan Kode bahasa yg ingin kamu terjemahkan\n\text: B.jepang kodenya: ja ')
        ap = input("\nKode bahasa: ")
        apa = input("Kata yg mau diterjemahin:\n")
        her= tran.detect(
            apa)
        he = tran.translate(
            apa,
            dest=f'{ap}')
        print(f'{her}\nMenerjemahkan {apa} :\n\t',he.text)
        print(f'Romajinya: {he.pronunciation}')
        lagi = input('Lagi? y/n: ')
        print(lagi)
        if lagi == 'y' or lagi == 'Y':
            main()
    except ValueError:
        print("[!]Kode Bahasa tidak diketahui".center(20))
        print("[!]Mengulangi[!]".center(20))
        time.sleep(3)
        main()
main()