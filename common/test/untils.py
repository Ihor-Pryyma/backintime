"""Utilities for testing"""
from pathlib import Path
from collections import namedtuple

SnapshotConfig = namedtuple('SnapshotConfig', [
    'config_version',
    'snapshot_type',
    'snapshot_value',
    'snapshot_size',
    'no_on_battery',
    'notify_enabled',
    'snapshot_path',
    'snapshot_host',
    'snapshot_profile',
    'snapshot_user',
    'preserve_acl',
    'preserve_xattr',
    'remove_old_snapshots_enabled',
    'remove_old_snapshots_unit',
    'remove_old_snapshots_value',
    'rsync_options_enabled',
    'rsync_options_value',
    'profiles_version'
])


def generate_temp_config(snapshot_config: SnapshotConfig) -> str:
    """Generate a temporary config file with the given snapshot values."""
    template_path = Path(__file__).parent / 'config_template'

    with open(template_path, 'r', encoding='utf-8') as template:
        return template.read().format(**snapshot_config._asdict())


def kill_subprocess(proc):
    """Kill a process and wait for it to terminate."""
    if proc:
        proc.kill()
        proc.wait()
