'''
| Make the project in edit mode

>>>  pip install -e .

>>> rfcentral -p 65.55 -d ttyACM0

| Note: Check the devicemanager from control panel for the port name
'''
import platform
from argparse import ArgumentParser, Namespace

from rfcentral import (
   __author__,  # type:ignore
   __description__,  # type:ignore
   __license__,  # type:ignore
   __title__,  # type:ignore
   __url__,  # type:ignore
   __version__,  # type:ignore
)
from rfcentral._help import bug_reporting
from rfcentral.broker import DataBroker
from rfcentral.displayer import ConsoleOutput
from rfcentral.receiver import Receiver


def get_cli_value()->tuple[float,float,str]:# type:ignore
   pass

def main()-> None:
     """
    This is the main function that executes the program.
    This function uses argparse to handle input from the command line.

    Command-line arguments
    ----------------------
    -p : float
        energy warning level; default to 50 dBm
    -d : str
        device name default to 'ttyACM0'

    Examples:
        >>> rfcentral -p 65.55 -d ttyACM0
    """
     parser = ArgumentParser(prog="rfcentral", usage="rfcentral -p 65.55 -d ttyACM0",description="RF Central Command Line Interface")


     parser.add_argument(
        '-p',
        help='frequency engergy power level; if exceeded will give beep as warning',
        type=float,
        nargs='?',
        default=50.00,
        metavar='power'
     )
     parser.add_argument(
        '-d',
        help= 'device name  or RF device receiver name',
        type= str,
        default = 'ttyACM0',
        nargs='?',
        metavar = 'device'

     )

     parser.add_argument("--version", action="store_true", help="Display current library version")
     parser.add_argument("--author", action="store_true", help="Display author information")
     parser.add_argument("--report-bug", action="store_true", help="Library detail information to report a bug")
     parser.add_argument("--description", action="store_true", help="Display description of the package")
     parser.add_argument("--license", action="store_true", help="Display license information")
     parser.add_argument("--title", action="store_true", help="Display title of the package")
     parser.add_argument("--url", action="store_true", help="Display read the docs url of the package")


     args : Namespace = parser.parse_args()

     if args.version:
            print(f"Version: {__version__}")
            return

     if args.author:
        print(f"Author: {__author__}")
        return

     if args.report_bug:
        bug_reporting()
        return

     if args.description:
        print(f"Description: {__description__}")
        return

     if args.license:
        print(f"License: {__license__}")
        return

     if args.title:
        print(f"Title: {__title__}")
        return

     if args.url:
        print(f"URL: {__url__}")
        return


     power:float = args.p
     device:str = args.d

     port:str
     if platform.system() == 'Windows':
         port = device
     else:
         port ='/dev/' + device

     out = ConsoleOutput(power)
     data_broker = DataBroker()
     data_broker.start()
     receiver = Receiver(out, port=port)
     receiver.start() # execute in a separate thread


# this is important so that it does not run from pytest
if __name__ == "__main__":
    main()

