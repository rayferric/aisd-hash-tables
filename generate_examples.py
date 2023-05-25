import random
import subprocess
import os

EXAMPLES = 100
MAX_SIZE = 100
MAX_ELEMENT = 100
MAX_OPS = 100

HARD_CODED_EXAMPLE_INITS = [
    (0, 1, [], ['-1']),
    (0, 2, [], ['-1']),
    (0, 3, [], ['-1']),
    (0, 4, [], ['-1']),
    (1, 1, [], ['0 0', '-1']),
    (1, 2, [], ['0 0', '-1']),
    (1, 3, [], ['0 0', '-1']),
    (1, 4, [], ['0 0', '-1']),
]

if __name__ == '__main__':
    for i in range(EXAMPLES):
        if i < len(HARD_CODED_EXAMPLE_INITS):
            size = HARD_CODED_EXAMPLE_INITS[i][0]
            collision_resolver = HARD_CODED_EXAMPLE_INITS[i][1]
            array = HARD_CODED_EXAMPLE_INITS[i][2]
            ops = HARD_CODED_EXAMPLE_INITS[i][3]
        else:
            # Generate initial input.
            size = random.randint(1, max(MAX_SIZE * i // EXAMPLES, 5))
            collision_resolver = random.choice([1, 2, 3, 4])
            array = [random.randint(1, MAX_ELEMENT) for _ in range(random.randint(1, size))]

            # Generate OPs.
            ops = []
            max_length = len(array)
            possible_values = set(array)
            for _ in range(random.randint(0, max(MAX_OPS * i // EXAMPLES, 5))):
                op = random.randint(0, 2)
                if op == 0:
                    if max_length == size:
                        continue
                    max_length += 1

                    x = random.randint(1, MAX_ELEMENT)
                    ops.append(f'0 {x}')
                    possible_values.add(x)
                elif op == 1:
                    if len(possible_values) == 0:
                        continue
                    
                    x = random.choice(list(possible_values))
                    ops.append(f'1 {x}')
                elif op == 2:
                    if len(possible_values) == 0:
                        continue

                    x = random.choice(list(possible_values))
                    ops.append(f'2 {x}')
                    max_length -= 1
                    possible_values.remove(x)
            ops.append('-1')
        
        print(f'Example #{i + 1}: Size = {size} Resolver = {collision_resolver} Array Size = {len(array)} OPs = {len(ops)}')

        # Write input to "in/i.txt".
        os.makedirs('in', exist_ok=True)
        os.makedirs('out', exist_ok=True)
        with open(f'in/{i + 1}.txt', 'w') as f_in:
            f_in.writelines([
                f'{size} {collision_resolver} {" ".join([str(x) for x in array])}\n',
                *[f'{op}\n' for op in ops]
            ])
        
        # Write output to "out/i.txt".
        # Use "python ./example_solver.py" to generate stdout.
        with open(f'in/{i + 1}.txt', 'r') as f_in:
            with open(f'out/{i + 1}.txt', 'w') as f_out:
                stdout = subprocess.run(['python', './example_solver.py'], stdin=f_in, stdout=subprocess.PIPE, text=True)
                f_out.write(stdout.stdout)
            