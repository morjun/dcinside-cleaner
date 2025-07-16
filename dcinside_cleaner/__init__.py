
RUNNING_MODE = 'cli' # 'gui' | 'cli'

def main():
    if RUNNING_MODE == 'cli':
        from .cli.cleaner_console import Console
        Console()

    if RUNNING_MODE == 'gui':
        from .gui.cleaner_gui import execute
        execute()

__all__ = ['main', 'dcinside_cleaner', 'proxy_checker', 'cli', 'gui']
