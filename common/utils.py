import platform

from common.enums import Platform


def get_current_platform() -> Platform:
    print(platform.system())
    return Platform.from_str(platform.system())
