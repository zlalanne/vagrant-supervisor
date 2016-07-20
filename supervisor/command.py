from enum import Enum
from pprint import pprint


class CommandType(Enum):
    status = 1
    destroy = 2
    up = 3
    suspend = 4
    halt = 5
    machine_add = 6
    machine_remove = 7


class Command:
    def __init__(self, command_type):
        self.command_type = command_type

    def run_cmd(self, config):
        print('Running {}'.format(self.command_type))


def parse_cmd_args(args):
    if args['status'] is True:
        cmd = Command(CommandType.status)
    elif args['destroy'] is True:
        cmd = Command(CommandType.destroy)
    elif args['up'] is True:
        cmd = Command(CommandType.up)
    elif args['suspend'] is True:
        cmd = Command(CommandType.suspend)
    elif args['halt'] is True:
        cmd = Command(CommandType.halt)
    elif args['machine'] is True and args['add'] is True:
        cmd = Command(CommandType.machine_add)
    elif args['machine'] is True and args['remove'] is True:
        cmd = Command(CommandType.machine_remove)
    pprint(args)

    return cmd
