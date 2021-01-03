broi_pak_himikali = int(input()) * 5.80
broi_pak_markeri = int(input()) * 7.20
litur_preparat = float(input()) * 1.20
procent_namalenie = int(input())

resultat = broi_pak_himikali + broi_pak_markeri + litur_preparat
resultat_s_namalenie = resultat - ((resultat * procent_namalenie) / 100)
print(f"{resultat_s_namalenie:.3f}")
