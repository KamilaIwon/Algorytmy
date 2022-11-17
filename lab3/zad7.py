

def z7_dodaj_cyfry(c_tab_tab_we: list[list[int]], ile_cyfr: int) -> list[list[int]] :
    if (ile_cyfr < 1):
        return c_tab_tab_we
    c_tab_tab_wy = []
    for li in range(len(c_tab_tab_we)):
        c_tab_org = c_tab_tab_we[li]
        for cyfra in range(10):
            c_tab_nowa = c_tab_org.copy()  # trzeba sklonować tablicę, by nie modyfikować oryginału
            c_tab_nowa.append(cyfra)
            c_tab_tab_wy.append(c_tab_nowa)
    return z7_dodaj_cyfry(c_tab_tab_wy, ile_cyfr-1)


def z7_n_sums(n: int) -> list[int]:
    tab_wyn = []
    cyfry_tab_tab_pa = []; cyfry_tab_tab_np = []
    max_suma_cyfr = None
    cyfr_i_pa = 0; cyfr_i_np = 0  # cyfr o indexie (nie)parzystym
    assert (n >= 2)
    cyfr_i_pa = math.ceil(n/2)
    cyfr_i_np = math.floor(n/2)
    max_suma_cyfr = cyfr_i_np * 9
    for x in range(1, 10):  # pierwsza cyfra musi być > 0
        cyfry_tab_tab_pa.append([x])
    for x in range(0, 10):
        cyfry_tab_tab_np.append([x])
    # print(tab_pa); print(""); print(tab_np);
    cyfry_tab_tab_pa = z7_dodaj_cyfry(cyfry_tab_tab_pa, cyfr_i_pa - 1)
    cyfry_tab_tab_np = z7_dodaj_cyfry(cyfry_tab_tab_np, cyfr_i_np - 1)
    # print(cyfry_tab_tab_pa); print(cyfry_tab_tab_np)
    for c_tab_pa in cyfry_tab_tab_pa:  # list[int], składamy liczby wyjściowe
        l_pa_suma_cyfr = 0
        for cyfra in c_tab_pa:
            l_pa_suma_cyfr += cyfra
        if (l_pa_suma_cyfr > max_suma_cyfr):
            continue # nie da się stworzyć takiej liczby z cyfr w cyfry_tab_tab_np
        for c_tab_np in cyfry_tab_tab_np:  # list[int]
            liczba_wy = 0
            l_np_suma_cyfr = 0
            for cyfra in c_tab_np:
                l_np_suma_cyfr += cyfra
            if (l_np_suma_cyfr != l_pa_suma_cyfr):
                continue # nie zgadza się suma cyfr, nie da się złożyć cyfry
            for c_idx in range (cyfr_i_pa):  #składamy liczbę z cyfr,
                liczba_wy = liczba_wy * 10 + c_tab_pa[c_idx]
                if (c_idx < cyfr_i_np):
                    liczba_wy = liczba_wy * 10 + c_tab_np[c_idx]
            tab_wyn.append(liczba_wy)
    return tab_wyn


print(z7_n_sums(3));  print(z7_n_sums(4))