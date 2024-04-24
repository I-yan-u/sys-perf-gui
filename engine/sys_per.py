"""
System performance monitoring functions.

    functions:
    - cpu_per(percpu: bool = False) -> Union[float, List[float]]
    - mem_per() -> float
    - disk_per() -> float

    Example:
    >>> cpu_per()
    10.0
    >>> cpu_per(percpu=True)
    [10.0, 20.0, 30.0, 40.0]
    >>> mem_per()
    50.0
    >>> disk_per()
    60.0
"""

import psutil
from typing import Union, List


def sec2hours(secs: int) -> str:
    """
    Converts seconds to hours, minutes and seconds.

    Args:
        secs (int): Seconds to convert.

    Returns:
        str: Time in hh:mm:ss format.
    """
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%d:%02d:%02d" % (hh, mm, ss)


def cpu_per(percpu: bool = False) -> Union[float, List[float]]:
    """
    Returns the CPU usage percentage.

    Parameters:
    - percpu (bool): If True, returns the CPU usage percentage for each CPU core.
                     If False (default), returns the overall CPU usage percentage.

    Returns:
    - float or list: The CPU usage percentage(s).
    """
    return psutil.cpu_percent(interval=1, percpu=percpu)


def mem_per() -> float:
    """
    Returns the memory usage percentage.

    Returns:
    - float: The memory usage percentage.
    """
    return psutil.virtual_memory().percent


def disk_per() -> float:
    """
    Returns the disk usage percentage of the root directory.

    Returns:
    - float: The disk usage percentage.
    """
    return psutil.disk_usage('/').percent


def disk_usage() -> List[float]:
    """
    Returns the disk usage percentage of the root directory.

    Returns:
    - List[float]: A list of Total, used, free and percentage.
    """
    return psutil.disk_usage('/')


def cpu_count() -> int:
    """
    Returns the number of CPU cores.

    Returns:
    - int: The number of CPU cores.
    """
    return psutil.cpu_count()


def cpu_times(arg: str = None) -> float:
    """
    Returns the CPU times.

    Returns:
    - float: The CPU times.
    """
    times = psutil.cpu_times()
    obj = {
        'user': times.user,
        'system': times.system,
        'idle': times.idle,
    }
    if arg and arg in ['user', 'system', 'idle']:
        return obj[arg]
    return times


def battery_info() -> List[Union[float, str, bool]]:
    """
    Returns the battery information.

    Returns:
    - List[Union[float, str, bool]]: A list of battery percentage, time left and power status.
    """
    battery = psutil.sensors_battery()
    power = 'Battery' if not battery.power_plugged else 'AC'
    return [battery.percent, sec2hours(battery.secsleft), power]