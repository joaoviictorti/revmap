from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.application import run_in_terminal
import sys

bindings = KeyBindings()

@bindings.add('c-c')
def _(event):
    def quit() -> None:
        print("Interrupt detected. Closing the program...")
        sys.exit(-1)
    run_in_terminal(quit())