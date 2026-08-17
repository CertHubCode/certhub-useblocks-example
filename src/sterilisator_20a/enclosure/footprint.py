"""Footprint helpers for Sterilisator 20A."""

from __future__ import annotations

from dataclasses import dataclass

from sterilisator_20a.constants import MAX_DEPTH_CM, MAX_HEIGHT_CM, MAX_WIDTH_CM


@dataclass(frozen=True)
class DimensionsCm:
    width: float
    depth: float
    height: float


# @need-ids: DOUT_018
def device_dimensions_cm() -> DimensionsCm:
    """External envelope of the Sterilisator 20A enclosure."""
    return DimensionsCm(width=48.0, depth=38.0, height=34.0)


# @need-ids: DOUT_018
def footprint_within_limits(dimensions: DimensionsCm | None = None) -> bool:
    """Return True when overall dimensions do not exceed 50×40×35 cm."""
    dims = dimensions if dimensions is not None else device_dimensions_cm()
    return (
        dims.width <= MAX_WIDTH_CM
        and dims.depth <= MAX_DEPTH_CM
        and dims.height <= MAX_HEIGHT_CM
    )
