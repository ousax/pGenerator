import re # check is a given password is strong or not
import argparse # for prefix FB_STRONGPASSWORD
import random
import string
from pyfiglet import figlet_format
from rich.console import Console
from rich.table import Table
from rich import print

parser = argparse.ArgumentParser(
    description="Strong passwords generator"
)
parser.add_argument("-plen", help="The password's length [10 by default]", type=int, required=False, default=10)
parser.add_argument("-sf", help="Save to a file", type=str, required=False)
parser.add_argument("-pNumber", help="Number of passwords to generate", type=int, default=1000, required=False)
parser.add_argument("-all_", help="Use digits, strings, punctuation", type=str)
parser.add_argument("-eXD", help="Exclude digits [0] to exlude digits [1] to include digits", type=int, choices=[0, 1], required=False)
parser.add_argument("-eXP", help="Exclude, Include punctuations [0] exlude, [1] include", type=int, choices=[0, 1], required=False)
parser.add_argument("-eXS", help="Exclude, Include letters [lower, upper case] [0] exlude, [1] include", type=int, choices=[0, 1], required=False)
parser.add_argument("-prefix_", help="Add a prefix to a the passwords like [(fb, facebook), titktok, gmail, (twitter|xtwi), grok, openAI, ChatGpt...]", type=str, required=False, default="")
parser.add_argument("-passCheck", help="Check the complexity of the password", type=int, choices=[0, 1], required=False)
args = parser.parse_args()
PassLength = args.plen
SaveToFile = args.sf
PassNumber = args.pNumber
UseAll = args.all_
eXD = args.eXD
eXS = args.eXS
eXP = args.eXP
prefix_ = args.prefix_
passCheck = args.passCheck

class Password:
    def __init__(self, *argsH):
        self.PassLength = PassLength
        self.SaveToFile = SaveToFile
        self.pNumber = PassNumber
        self.UseAll = UseAll
        self.eXD = eXD
        self.eXS = eXS
        self.eXP = eXP
        self.prefix_ = prefix_
        self.passCheck = passCheck
        self.__Banner()
    def __Banner(self):
        Banner = figlet_format(
            "Password Generator",
            font="slant" 
            )
        print(f"[bold green] {Banner}[/ bold green]")
        print("[bold red]Treat your passwords as if they were your underwears[/ bold red]".center(60))
        console, table = Console(), Table(
            title="Information",
            style="bold green"
        )
        table.add_column("Length", highlight=True, justify="center", no_wrap=False)
        table.add_column("Number", highlight=True, justify="center", no_wrap=False)
        table.add_column("All", highlight=True, justify="center", no_wrap=False)
        table.add_column("Save", highlight=True, justify="center", no_wrap=False)
        table.add_column("eXD", highlight=True, justify="center", no_wrap=False)
        table.add_column("eXS", highlight=True, justify="center", no_wrap=False)
        table.add_column("eXP", highlight=True, justify="center", no_wrap=False)
        table.add_column("Prefix", highlight=True, justify="center", no_wrap=False)
        table.add_column("isCheck", highlight=True, justify="center", no_wrap=False)
        table.add_row(
            str(self.PassLength), 
            str(self.pNumber),
            "Y" if str(self.UseAll) == "1" else "N", 
            "Y" if str(self.SaveToFile) == "1" else "N",
            "Y" if str(self.eXD) == "1" else "N", 
            "Y" if str(self.eXS) == "1" else "N", 
            "Y" if str(self.eXP) == "1" else "N",
            str(self.prefix_),
            "Y" if  str(self.passCheck) == "1" else "N"
            )
        console.print(table)
    def Core_(self):
        FileName = self.SaveToFile
        PassList = []

        if self.eXS and self.eXP and self.eXD == 1:
            ALL = string.ascii_letters + string.digits + string.punctuation
        elif self.eXS == 0 and self.eXP == 0 and self.eXD == 0:
            ALL = string.ascii_letters + string.digits + string.punctuation
            print("[bold yellow]You need to specify a filter to apply[/ bold yellow]")
            ALL = string.ascii_letters
        elif self.eXS and self.eXP == 1 and self.eXP == 0:
            # exclude punctuation
            ALL = string.ascii_letters + string.digits
        elif self.eXS and self.eXP == 1 and self.eXD == 0:
            #exclude digits
            ALL = string.ascii_letters + string.punctuation
        elif self.eXS == 1 and self.eXD == 0 and self.eXP == 0:
            # include only ascii_letters
            ALL = string.ascii_letters
        elif self.eXS == 0 and self.eXP and self.eXD == 1:
            # exlude ascii_letters
            ALL = string.digits + string.punctuation 
        elif int(self.eXD) == 1 and int(self.eXP) == 0 and  int(self.eXS) == 0:
            ALL = string.digits
            print("[bold yellow]You've excluded both ascii_letters, punctuations[/bold yellow]")
            print("[bold yellow]So to avoid raising a [red]'ValueError: Sample larger than population or is negative'[/red][/bold yellow]")
            print("[bold yellow]'self.PassLength' has been assigned a new value (10)[/bold yellow]")
            self.PassLength = 10
        for password in range(self.pNumber):#self.pNumber):
            password = self.prefix_+"_"+''.join(random.sample(ALL, self.PassLength))
            PassList.append(password)
        print(PassList)
Password().Core_()
    
