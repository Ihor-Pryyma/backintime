"""Utilities for testing"""

config_template = """
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


def kill_subprocess(proc):
    """Kill a process and wait for it to terminate."""
    if proc:
        proc.kill()
        proc.wait()
