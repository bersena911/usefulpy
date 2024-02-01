from typing import Any, Dict, Optional


def filter_important_services(
    event: Dict[str, Any], hint: Dict[str, Any]
) -> Optional[Dict[str, Any]]:
    """
    THIS METHOD IS DIRECTLY USED INSIDE COMPOSERS VARIABLES
    Filter out events which has filename of important dags
    Args:
        event: Sentry event
        hint: Sentry hint

    Returns:

    """
    if event.get("tags", {}).get("dag_id") not in [
        "v2_actions_engine",
        "v1_trigger_ads",
        "v1_finish_ads",
        "v1_trigger_ads_runner",
    ]:
        return None
    return event
