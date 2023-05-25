import os
import subprocess
import sys

if __name__ == '__main__':
    # Read command to run from arguments.
    if len(sys.argv) < 2:
        print('Użycie: python ./test_examples.py <polecenie uruchamiające solver>')
        sys.exit(1)
    command = sys.argv[1:]
    print(f'Polecenie uruchamiające solver: {" ".join(command)}')

    # Find examples in "./in".
    examples = [f for f in os.listdir(os.path.join(os.path.dirname(__file__), 'in')) if os.path.isfile(os.path.join(os.path.dirname(__file__), 'in', f))]
    examples.sort(key=lambda x: int(x[:-4]))
    print(f'Sprawdzanie {len(examples)} testów...')

    # Run solver on each example.
    passed = 0
    printed_first_failed = False
    for example in examples:
        with open(os.path.join(os.path.dirname(__file__), f'in/{example}'), 'r') as f_in:
            try:
                result = subprocess.run(command, stdin=f_in, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            except:
                print(f'\nCoś poszło nie tak!')
                print(f'Upewnij się, że podane przez ciebie polecenie jest poprawne i można je uruchomić w terminalu:')
                print(f'$ {" ".join(command)}')
                sys.exit(1)

        # Compare stdout with expected output.
        with open(os.path.join(os.path.dirname(__file__), f'out/{example}'), 'r') as f_out:
            expected = f_out.read()
            if result.stdout != expected:
                if not printed_first_failed:
                    print(f'\nTEST #{example[:-4]} NIE ZALICZONY')
                    print(f'\n-------------------- Co powinno być --------------------\n{expected}')
                    print(f'\n--------------------  Co otrzymano  --------------------\n{result.stdout}')
                    print('Błędy w kolejnych testach nie będą już wyświetlane. Napraw ten test by zobaczyć resztę komunikatów.')
                    printed_first_failed = True
            else:
                passed += 1

    print(f'\nZakończono sprawdzanie {len(examples)} testów. Przeszło {passed} na {len(examples)}.')