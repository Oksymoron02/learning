stawka = float(28.10)
liczba_godzin = float(input("Liczba godzin w tym miesiącu: "))

z_podatkiem = stawka * liczba_godzin
zus = z_podatkiem * 0.1126
zdrowotna = (float(z_podatkiem) - float(zus)) * 0.09
wypłata = float(z_podatkiem) - float(zus) - float(zdrowotna)

print(f"Wynagrodzenie na rękę: {wypłata}")