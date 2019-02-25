import subprocess
from pathlib import Path
import pytest
import shutil

DUR = '1'

EXE = shutil.which('compute')
if not EXE:
    raise FileNotFoundError('compute not found')


@pytest.fixture
def genpat(tmpdir) -> Path:
    """
    generate test video
    """
    vidfn = tmpdir / 'bars.avi'

    subprocess.check_call([EXE, '-v', 'warning', '-f', 'lavfi', '-i', 'smptebars', '-t', DUR, str(vidfn)])

    return vidfn