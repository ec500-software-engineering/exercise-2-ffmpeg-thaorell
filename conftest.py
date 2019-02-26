import subprocess
from pathlib import Path
import pytest

length = '1'


if subprocess.call(["ffmpeg"]):
    cmd = 'ffmpeg'
else:
    raise FileNotFoundError('ffmpeg not found')


@pytest.fixture
def genpat(tmpdir) -> Path:
    """
    generate test video
    """
    vidfn = tmpdir / 'bars.avi'
    subprocess.check_call([cmd, '-v', 'warning', '-f', 'lavfi', '-i', 'smptebars', '-t', length, str(vidfn)])

    return vidfn