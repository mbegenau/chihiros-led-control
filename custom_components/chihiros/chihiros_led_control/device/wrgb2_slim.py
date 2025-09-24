"""WRGB II Slim device Model."""

from .base_device import BaseDevice


class WRGBIISlim(BaseDevice):
    """Chihiros WRGB II Slim device Class."""

    _model_name = "WRGB II Slim"
    _model_codes = ["DYSILN","DYSL60"]
    _colors: dict[str, int] = {
        "red": 0,
        "green": 1,
        "blue": 2,
    }
