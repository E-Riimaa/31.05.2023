

"""
 kirjuta funktsioon ,mis arvutab juhusliku aja etteantud
 vahemikus. Vahemik on sekundites ja kaasa arvatud.Lõpp
 tulemusena näitab lisaks sekundile ja tuhandikke. Näiteks:
 Kui vahemik on 47-59 sekundit, siis juhuslik aeg on 52.432 sekundit.
 siis juhuslik aeg on 52.432 sekundit.
Tee list viie eesnimega kes võistlevad. Genereeri igale ühele
 kolm sektori aega vahemikus 23 kuni 26 k.a. Väljasta iga isiku järgi
 kolm aega.

 Näiteks:
 Lewis 25.12 25.286 25.935
 Valtteri 25.96 26.858 26.993

Väljasta ajad ühel joonel. Nime max pikkus on 10 märki. Näiteks:
Lewis      25.12 25.286 25.935
Valtteri   25.96 26.858 26.993

Kõige esimeseks tuleb kogu aeg ja siis s1,s2,s3.
Lewis     72.778  25.12 25.286 25.935
Valtteri  77.952  25.96 26.858 26.993

Kogu aeg vormindada kujule 00:00:00.000 ehk 77.987 => 00:01:17.987
Lewis    00:01:15.414  25.12 25.286 25.935
Valtteri 00:01:12.485  25.96 26.858 26.993

Kirjuta funktsioon, mis arvutab täisringi aja kasutades esimeses
punktis tehtud funktsiooni  uue funktsiooni sees! Aegade vahemik
sektorites on sama ,mis alguses(23 ja 26). Sektori aeg sel korral
meeles pidama ei pea. Ainult täisringi aeg.

Nüüd kui on peaaegu kogu vajalik info olemas tuleb teha "Võistlus"
Võistlus on 10 ringi .Meeles tuleb pidada igal ringil sõitja aega(ringi)
ja kogu aega (sisse sõidetud ringinde summa ).Kogu info peab olema listis (nimi ja sõidetud ringide summa )
Kogu info peab olema listis (nimi ja sõidetud ringide aegade summa ). Kui info olemas näita lõpus lõpp tulemust.
Ära unusta listi sorteerida aja järgi kasvavalt.

Valtteri    00:08:18.204
Lewis       00:08:27.252

Võistlusel on ikka nii ,et kõik ringid ei tule hästi välja. Seega
mõnel ringil võiks juhtuda äpardus. See tähendab, et sektori aeg
poleks enam 23 ja 26 sek., vahel vaid 30 ja 90 sek. vahel ka. Enne
ringi aja arvutamist tehke lihtne loogiline kontroll. Genereerige
juhuslik number vahemikus 1-10 või 0-9 ja kui see number on 2,
siis juhtus midagi ja arvutage sektori aeg nüüd vahemikus 30-90 k.a.
Lewis       00:09:11.433
Valtteri    00:12:36.756

Sõit ja kõik "koperdamised" pane listi - ringi number. Ja kui
väljastatakse sõitja info, siis näita ringi numbreid kasutaja järgi.
Valtteri  00:08:17.793
Lewis     00:10:10.002 7 10

VÕI

Valtteri  00:08:17.793 []
Lewis     00:10:10.002 [7, 10]

Arvuta alates teisest sõitjast vahe esimesega. Aega näita
põhiaja järgi enne vigaseid ringide numbreid näiteks:
Evelin    00:08:17.793 []
Lewis     00:10:10.002  00:00:09.182[]
Sten      00:09:04.019  00:00:44.041[1]
Karl      00:09:38.634  00:01:18.656[3]
David     00:10:41.443  00:02:21.465[4, 5, 6]

Igal võidusõidul tuvastatakse ka kiirema ringi tegija (kolme sektori summa). Teie ülesandeks on tuvastada
kes on kiirema ringi teinud. Aega näita isiku järgi peale "koperdatud ringe".

Valtteri 00:12:23.430 [] 00:01:10.037
Lewis 00:14:51.852 00:02:28.422 [3]

"""

import random

racers = ["Karlana", "Rannar", "Liise", "Kreete", "Sten"]
alg, lopp = 23, 26
times = []


def suvalineaeg(a, b):
    aeg = round(random.uniform(a, b), 3)
    return aeg


def taisringi_aeg():
    total = 0
    messed_up_laps = []
    fastest_lap = float('inf')  # Kiireima ringi algväärtus kõrgeim võimalik
    for lap in range(1, 11):
        s1 = suvalineaeg(alg, lopp)
        s2 = suvalineaeg(alg, lopp)
        s3 = suvalineaeg(alg, lopp)

        number = random.randint(1, 10)
        if number == 2:
            s1 = suvalineaeg(30, 90)
            s2 = suvalineaeg(30, 90)
            s3 = suvalineaeg(30, 90)
            messed_up_laps.append(lap)

        kokku = round(s1 + s2 + s3, 3)
        total += kokku

        # Kontrollime, kas see ring on seni kiireim
        if kokku < fastest_lap:
            fastest_lap = kokku

    return total, messed_up_laps, fastest_lap


for racer in racers:
    total_time, messed_up_laps, fastest_lap = taisringi_aeg()
    times.append([racer, total_time, messed_up_laps, fastest_lap])

sorted_times = sorted(times, key=lambda x: x[1])


def format_time(total_time):
    hours, minutes = divmod(int(float(total_time)) // 60, 60)
    seconds = int(float(total_time)) % 60
    milliseconds = int(total_time.split(".")[1][:3])
    return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:03}"


first_racer_time = sorted_times[0][1]

for i, (racer, time, koperdused, fastest_lap) in enumerate(sorted_times):
    total_time = str(time)
    time_formatted = format_time(total_time)
    koperdused_formatted = " ".join(map(str, koperdused))
    fastest_lap_formatted = format_time(str(fastest_lap))
    if i == 0:
        print(f"{racer:10}{time_formatted:13}[{koperdused_formatted}] {fastest_lap_formatted}")
    else:
        difference = time - sorted_times[0][1]
        difference_formatted = format_time(str(difference))
        print(f"{racer:10}{time_formatted:13}{difference_formatted:13}[{koperdused_formatted}] {fastest_lap_formatted}")

