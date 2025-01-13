"""
This is a very small 'tox' plugin.
'toxfile.py' is a special name for auto-loading a plugin without defining package
metadata.

For full doc, see: https://tox.wiki/en/latest/plugins.html

Methods decorated below with `tox.plugin.impl` are hook implementations.
We only implement hooks which we need.
"""

from __future__ import annotations

import logging
import pathlib
import shutil
import typing as t

from tox.plugin import impl

if t.TYPE_CHECKING:
    from tox.config.sets import EnvConfigSet
    from tox.session.state import State
    from tox.tox_env.api import ToxEnv

log = logging.getLogger(__name__)


@impl
def tox_add_env_config(env_conf: EnvConfigSet, state: State) -> None:
    env_conf.add_config(
        keys=["globus_cli_rmtree"],
        of_type=list[str],
        default=[],
        desc="A dir tree to remove before running the environment commands",
    )


@impl
def tox_before_run_commands(tox_env: ToxEnv) -> None:
    cli_rmtree = tox_env.conf.load("globus_cli_rmtree")
    for name in cli_rmtree:
        path = pathlib.Path(name)
        if path.exists():
            log.warning(f"globus_cli_rmtree: {path}")
            shutil.rmtree(path)
