import colorsys


def text_color_generator(
    hex_code: str, light: str = "#FFFFFF", dark: str = "#000000"
) -> str:

    h = hex_code.lstrip("#")
    r, g, b = (int(h[i : i + 2], 16) / 255 for i in (0, 2, 4))

    def lin(c):
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4

    L = 0.2126 * lin(r) + 0.7152 * lin(g) + 0.0722 * lin(b)
    return dark if L > 0.5 else light


def complement_color_generator(hex_code: str) -> str:
    h = hex_code.lstrip("#")
    r, g, b = (int(h[i : i + 2], 16) / 255 for i in (0, 2, 4))
    hh, ll, ss = colorsys.rgb_to_hls(r, g, b)
    SAT_THRESHOLD = 0.05

    if ss < SAT_THRESHOLD:
        ll = 1.0 - ll
    else:
        hh = (hh + 0.5) % 1.0

    r2, g2, b2 = colorsys.hls_to_rgb(hh, ll, ss)
    return f"#{int(r2 * 255):02X}{int(g2 * 255):02X}{int(b2 * 255):02X}"


def reduce_color_saturation_and_lightness(
    hex_code: str,
    sat_factor: float = 0.30,
    light_factor: float = 0.30,
) -> str:
    h = hex_code.lstrip("#")
    r, g, b = (int(h[i : i + 2], 16) / 255 for i in (0, 2, 4))
    hh, ll, ss = colorsys.rgb_to_hls(r, g, b)

    ss = ss * (1.0 - sat_factor)

    ll = ll * (1.0 - light_factor)

    r2, g2, b2 = colorsys.hls_to_rgb(hh, ll, ss)
    return f"#{int(r2 * 255):02X}{int(g2 * 255):02X}{int(b2 * 255):02X}"
