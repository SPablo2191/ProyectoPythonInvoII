
from sys import stdout

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'

def echo(string, end='\r\n', color=None):
    if color:
        stdout.write("%s%s%s" % (
            color,
            string,
            Colors.END
        ))
    else:
        stdout.write(string)
    if end: 
        stdout.write("\n")

# echo('Dis is demo text')
# echo('Dis is demo text', color=Colors.BLUE)
# echo('=> ', color=Colors.RED, end='')
# echo('MEH', color=Colors.GREEN)
# echo('Dis is demo text', color=Colors.HEADER, end='')
# echo('Dis is demo text', color=Colors.BLUE)