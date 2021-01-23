import difflib
import os
import subprocess
import sys


def main():
    force = len(sys.argv) >= 2

    path = os.getcwd()
    extensions = {
        'javascript': 'js',
        'ruby': 'rb',
        'csharp': 'cs',
        'cpp': 'cpp',
        'go': 'go',
	'crystal': 'cr'
    }

    for exercise in os.listdir(path):
        if not os.path.isdir(exercise):
            continue

        file_name = f'{exercise}.{extensions[os.path.basename(path)]}'
        possible_path = f'{path}/{exercise}/{file_name}'
        f = possible_path if os.path.exists(possible_path) else f'{path}/{exercise}/{difflib.get_close_matches(file_name, os.listdir(exercise))[0]}'

        with open(f'{os.path.dirname(__file__)}/.uploaded', 'r+') as _f:
            if not force and f in _f.read():
                print(f'{exercise} already submited!\nSend anything in ARGV to force submittion.\n')
                continue

            if not force:
                _f.write(f'{f}\n')

        print(f'There was an error when submiting {exercise}' if(subprocess.run(['exercism', 'submit', f], stdout=subprocess.DEVNULL).returncode > 0) else f'{exercise} submitted successfully')



if __name__ == '__main__':
     main()
