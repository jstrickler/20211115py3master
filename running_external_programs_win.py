from subprocess import run, PIPE, CalledProcessError

cmd = "netstat -n"

try:
    proc = run(cmd, stdout=PIPE, stderr=PIPE)
except CalledProcessError as err:
    print(err.return_code)
else:
    output_lines = proc.stdout.decode().splitlines()
    for line in output_lines:
        print(line)
print("-" * 60)

cmd = "icacls DATA"

try:
    proc = run(cmd, stdout=PIPE, stderr=PIPE)
except CalledProcessError as err:
    print(err.return_code)
else:
    output_lines = proc.stdout.decode().splitlines()
    for line in output_lines:
        print(line)
