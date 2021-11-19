from subprocess import run, PIPE, CalledProcessError
import shlex

cmd = "netstat -n"

cmd_words = shlex.split(cmd)

try:
    proc = run(cmd_words, stdout=PIPE)
except CalledProcessError as err:
    print(err.returncode)
else:
    output = proc.stdout.decode()
    output_lines = output.splitlines()
    print(len(output_lines))


