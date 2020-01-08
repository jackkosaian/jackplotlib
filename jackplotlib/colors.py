__all__ = ["get_color_wheel", "set_color_wheel", "color", "color_rgb",
           "set_color_wheel_qualitative"]


from cycler import cycler
import matplotlib as mpl

# Single-hue color map taken from http://colorbrewer2.org/#type=sequential,
# sequential with colorblind safe option set.
color_map = {
    "black": {
        2: ['#f0f0f0','#636363'],
        3: ['#f0f0f0','#bdbdbd','#636363'],
        4: ['#f7f7f7','#cccccc','#969696','#525252'],
        5: ['#f7f7f7','#cccccc','#969696','#636363','#252525'],
        6: ['#f7f7f7','#d9d9d9','#bdbdbd','#969696','#636363','#252525'],
        7: ['#f7f7f7','#d9d9d9','#bdbdbd','#969696','#737373','#525252','#252525'],
        8: ['#ffffff','#f0f0f0','#d9d9d9','#bdbdbd','#969696','#737373','#525252','#252525'],
        9: ['#ffffff','#f0f0f0','#d9d9d9','#bdbdbd','#969696','#737373','#525252','#252525','#000000']
    },
    "blue": {
        2: ['#deebf7','#3182bd'],
        3: ['#deebf7','#9ecae1','#3182bd'],
        4: ['#eff3ff','#bdd7e7','#6baed6','#2171b5'],
        5: ['#eff3ff','#bdd7e7','#6baed6','#3182bd','#08519c'],
        6: ['#eff3ff','#c6dbef','#9ecae1','#6baed6','#3182bd','#08519c'],
        7: ['#eff3ff','#c6dbef','#9ecae1','#6baed6','#4292c6','#2171b5','#084594'],
        8: ['#f7fbff','#deebf7','#c6dbef','#9ecae1','#6baed6','#4292c6','#2171b5','#084594'],
        9: ['#f7fbff','#deebf7','#c6dbef','#9ecae1','#6baed6','#4292c6','#2171b5','#08519c','#08306b']
    },
    "green": {
        2: ['#e5f5e0','#31a354'],
        3: ['#e5f5e0','#a1d99b','#31a354'],
        4: ['#edf8e9','#bae4b3','#74c476','#238b45'],
        5: ['#edf8e9','#bae4b3','#74c476','#31a354','#006d2c'],
        6: ['#edf8e9','#c7e9c0','#a1d99b','#74c476','#31a354','#006d2c'],
        7: ['#edf8e9','#c7e9c0','#a1d99b','#74c476','#41ab5d','#238b45','#005a32'],
        8: ['#f7fcf5','#e5f5e0','#c7e9c0','#a1d99b','#74c476','#41ab5d','#238b45','#005a32'],
        9: ['#f7fcf5','#e5f5e0','#c7e9c0','#a1d99b','#74c476','#41ab5d','#238b45','#006d2c','#00441b']
    },
    "orange": {
        2: ['#fee6ce','#e6550d'],
        3: ['#fee6ce','#fdae6b','#e6550d'],
        4: ['#feedde','#fdbe85','#fd8d3c','#d94701'],
        5: ['#feedde','#fdbe85','#fd8d3c','#e6550d','#a63603'],
        6: ['#feedde','#fdd0a2','#fdae6b','#fd8d3c','#e6550d','#a63603'],
        7: ['#feedde','#fdd0a2','#fdae6b','#fd8d3c','#f16913','#d94801','#8c2d04'],
        8: ['#fff5eb','#fee6ce','#fdd0a2','#fdae6b','#fd8d3c','#f16913','#d94801','#8c2d04'],
        9: ['#fff5eb','#fee6ce','#fdd0a2','#fdae6b','#fd8d3c','#f16913','#d94801','#a63603','#7f2704']
    },
    "purple": {
        2: ['#efedf5','#756bb1'],
        3: ['#efedf5','#bcbddc','#756bb1'],
        4: ['#f2f0f7','#cbc9e2','#9e9ac8','#6a51a3'],
        5: ['#f2f0f7','#cbc9e2','#9e9ac8','#756bb1','#54278f'],
        6: ['#f2f0f7','#dadaeb','#bcbddc','#9e9ac8','#756bb1','#54278f'],
        7: ['#f2f0f7','#dadaeb','#bcbddc','#9e9ac8','#807dba','#6a51a3','#4a1486'],
        8: ['#fcfbfd','#efedf5','#dadaeb','#bcbddc','#9e9ac8','#807dba','#6a51a3','#4a1486'],
        9: ['#fcfbfd','#efedf5','#dadaeb','#bcbddc','#9e9ac8','#807dba','#6a51a3','#54278f','#3f007d']
    },
    "red": {
        2: ['#fee0d2','#de2d26'],
        3: ['#fee0d2','#fc9272','#de2d26'],
        4: ['#fee5d9','#fcae91','#fb6a4a','#cb181d'],
        5: ['#fee5d9','#fcae91','#fb6a4a','#de2d26','#a50f15'],
        6: ['#fee5d9','#fcbba1','#fc9272','#fb6a4a','#de2d26','#a50f15'],
        7: ['#fee5d9','#fcbba1','#fc9272','#fb6a4a','#ef3b2c','#cb181d','#99000d'],
        8: ['#fff5f0','#fee0d2','#fcbba1','#fc9272','#fb6a4a','#ef3b2c','#cb181d','#99000d'],
        9: ['#fff5f0','#fee0d2','#fcbba1','#fc9272','#fb6a4a','#ef3b2c','#cb181d','#a50f15','#67000d']
    }
}


def get_color_wheel(color, num_modes, reverse=False, rgb=False, decimal=True):
    """
    Args:
        color: (str) name of color to get
        num_modes: (int) number of shades of `color` to get
        reverse: (bool) whether to reverse the order of the colors
        rgb: (bool) whether to return colors as tuples of RGB values
        decimal: (bool) whether to return RGB colors as decimals. Only relevent
                 if `rgb` is set to True.
    """
    assert color in color_map, "Unrecognized color '{}'".format(color)
    min_color = min(color_map[color])
    max_color = max(color_map[color])
    assert num_modes in color_map[color], "Argument `num_modes` of {} is not within the valid range [{}, {}]".format(num_modes, min_color, max_color)
    colors = color_map[color][num_modes]
    if reverse:
        colors = reversed(colors)

    if rgb:
        div_factor = 255. if decimal else 1.
        colors = [tuple(y / div_factor for y in _hex_to_rgb(x)) for x in colors]
    return colors


def set_color_wheel(color, num_modes, reverse=False):
    assert color in color_map, "Unrecognized color '{}'".format(color)
    min_color = min(color_map[color])
    max_color = max(color_map[color])
    assert num_modes in color_map[color], "Argument `num_modes` of {} is not within the valid range [{}, {}]".format(num_modes, min_color, max_color)
    colors = color_map[color][num_modes]
    if reverse:
        colors = reversed(colors)
    mpl.rcParams['axes.prop_cycle'] = cycler(color=colors)


def color(color, shade="dark"):
    assert color in color_map, "Unrecognized color '{}'".format(color)
    return color_map[color][3][_get_shade(shade)]


def set_color_wheel_qualitative(shade="dark", num=None):
    colors = ["blue", "orange", "green", "purple", "red", "black"]
    if num is not None:
        assert num <= 6
        colors = colors[:num]
    shade_idx = _get_shade(shade)
    cycle_colors = [color_map[c][3][shade_idx] for c in colors]
    mpl.rcParams['axes.prop_cycle'] = cycler(color=cycle_colors)


def _get_shade(shade):
    assert shade in ["dark", "medium", "light"], "Unrecognized shade '{}'".format(color)
    if shade == "dark":
        return 2
    elif shade == "medium":
        return 1
    else:
        return 0


def _hex_to_rgb(hex):
    # Adapted from: https://gist.github.com/matthewkremer/3295567
    hex = hex.lstrip('#')
    hlen = len(hex)
    return tuple(int(hex[i:i + hlen // 3], 16) for i in range(0, hlen, hlen // 3))


def color_rgb(color_name, shade="dark", decimal=False):
    hex_color = color(color_name, shade)
    rgb_tuple = _hex_to_rgb(hex_color)

    if decimal:
        return tuple(x / 255 for x in rgb_tuple)

    return rgb_tuple
