"""
Utility functions for the Qt GUI.
"""


def update_combo_profiles(config, combo_profiles, current_profile_id):
    """
    Updates the combo box with profiles.

    :param config: Configuration object with access to profile data.
    :param combo_profiles: The combo box widget to be updated.
    :param current_profile_id: The ID of the current profile to be selected.
    """
    profiles = config.profilesSortedByName()
    for profile_id in profiles:
        combo_profiles.addProfileID(profile_id)
        if profile_id == current_profile_id:
            combo_profiles.setCurrentProfileID(profile_id)
