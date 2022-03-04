



#Como? Criar um gerador de Qrcode.
import qrcode

lista_de_repositorios = ["CriadorDeArquivos",
                        "CotacoesDeCriptomoedas",
                        "Calculadora",
                        "GeradorDeSenhas",
                        "CriptoExcel",
                        ]

for lista in lista_de_repositorios:
    qr= qrcode.make(f'https://github.com/SamuelBarbosaDev/{lista}')
    qr.save(f"{lista}.png")

