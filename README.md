# AiSD Tablice z Haszowaniem

🥴 Automatyczny tester rozwiązań do zadania domowego [Tablice z Haszowaniem](https://upel.agh.edu.pl/pluginfile.php/177684/mod_resource/content/8/Algorytmy_i_struktury_danych______-3.pdf).

## Użycie

Aby uruchomić sprawdzarkę z własnym kodem, należy wykonać następujące kroki:

- Sklonuj to repozytorium przy pomocy polecenia:

```bash
git clone https://github.com/rayferric/aisd-hash-tables.git
```

- Uruchom program:

```bash
python ./aisd-hash-tables/test_examples.py <polecenie uruchamiające twój program>
```
```
# Przykładowe polecenia uruchamiające:
# python ./aisd-hash-tables/test_examples.py python ./zadania-aisd/tablice_z_haszowaniem.py
# python ./aisd-hash-tables/test_examples.py ./zadania-aisd/hash-tables.exe
```

- Jeśli twoje rozwiązanie nie poradzi sobie z którymś z testów, informacje o tym co poszło nie tak pojawią się w terminalu:

```log
Polecenie uruchamiające solver: python ./example_solver.py
Sprawdzanie 100 testów...

TEST #8 NIE ZALICZONY

-------------------- Co powinno być --------------------
[None]
[0]


--------------------  Co otrzymano  --------------------
[None]
Traceback (most recent call last):
  File "/home/rayferric/Source/aisd-tester/./example_solver.py", line 208, in <module>
    table.insert(extra)
  File "/home/rayferric/Source/aisd-tester/./example_solver.py", line 105, in insert
    hash = self._hash(x, i)
  File "/home/rayferric/Source/aisd-tester/./example_solver.py", line 177, in _hash
    return int((self._hash1(x) + i * self._hash2(x)) % self._size)
  File "/home/rayferric/Source/aisd-tester/./example_solver.py", line 174, in _hash2
    return int(x % max(self._size - 1, 0)) + 1
ZeroDivisionError: integer division or modulo by zero

Błędy w kolejnych testach nie będą już wyświetlane. Napraw ten test by zobaczyć resztę komunikatów.
Zakończono sprawdzanie 100 testów. Przeszło 99 na 100.
```

## Struktura Projektu

- `in/` - folder zawierający dane wejściowe do każdego z testów
- `out/` - folder zawierający dane wyjściowe, które powinien zwrócić twój program otrzymawszy odpowiedni plik z folderu `in`
- `.gitignore` - plik wykluczający `example_solver.py` z modelowym rozwiązaniem zadania
- `generate_examples.py` - generator losowych danych testowych; Wymaga obecności pliku `example_solver.py`.
- `README.md` - ten plik
- `test_examples.py` - sprawdzarka itself

## Zgłaszanie Problemów AGH Helpdesk 2000

Jeśli uważasz, że znalazłeś błąd w testach, lub sprawdzarka u Ciebie nie działa, zgłoś się do mnie:

> Discord: rayferric#0169
>
> Messenger: Rafał Rafał
