# Dokładnie 75 godzin. Tyle czasu wg. naukowców potrzeba, aby nabyć nową umiejętność.
# Oblicz ile pełnych tygodni zajmie Ci zdobycie nowej umiejętności,
# w zależności o tego, ile czasu jesteś wstanie poświęcić na naukę w tygodniu.


tyle_godzin_trzeba = 75
ile_h_w_t_chcesz = float(input('Ile godzin w tygodniu możesz się uczyć'))
tyle_t = 75 / ile_h_w_t_chcesz

print('Nauka zajmie Ci', int(tyle_t), 'pełnych tygodni.')