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
    template_content = """
        config.version=6
        profile1.snapshots.include.1.type={snapshot_type}
        profile1.snapshots.include.1.value={snapshot_value}
        profile1.snapshots.include.size={snapshot_size}
        profile1.snapshots.no_on_battery={no_on_battery}
        profile1.snapshots.notify.enabled={notify_enabled}
        profile1.snapshots.path={snapshot_path}
        profile1.snapshots.path.host={snapshot_host}
        profile1.snapshots.path.profile={snapshot_profile}
        profile1.snapshots.path.user={snapshot_user}
        profile1.snapshots.preserve_acl={preserve_acl}
        profile1.snapshots.preserve_xattr={preserve_xattr}
        profile1.snapshots.remove_old_snapshots.enabled={remove_old_snapshots_enabled}
        profile1.snapshots.remove_old_snapshots.unit={remove_old_snapshots_unit}
        profile1.snapshots.remove_old_snapshots.value={remove_old_snapshots_value}
        profile1.snapshots.rsync_options.enabled={rsync_options_enabled}
        profile1.snapshots.rsync_options.value={rsync_options_value}
        profiles.version={profiles_version}
    """
    return template_content.format(**snapshot_config._asdict())


def kill_subprocess(proc):
    """Kill a process and wait for it to terminate."""
    if proc:
        proc.kill()
        proc.wait()
