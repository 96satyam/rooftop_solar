def convert_pixels_to_m2(pixel_area: float, scale_per_pixel: float = 0.25) -> float:
    """Convert pixel area to square meters based on resolution scale."""
    return pixel_area * scale_per_pixel