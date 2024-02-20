import json

colors_file = "/home/polter/.cache/wal/colors.json"
with open(colors_file, "r") as f:
    colors = json.load(f)

custom = {
    "background": colors['special']['background'],
    "foreground": colors["special"]["foreground"],
    "color1": colors["colors"]["color2"],
    "color2": colors["colors"]["color3"],
    "color3": colors["colors"]["color4"],
}

rose_pine = {
    'Base': "#191724",
    'Surface': "#1f1d2e",
    'Overlay': "#26233a",
    'Muted': "#6e6a86",
    'Subtle': "#908caa",
    'Text': "#e0def4",
    'Love': "#eb6f92",
    'Gold': "#f6c177",
    'Rose': "#ebbcba",
    'Pine': "#31748f",
    'Foam': "#9ccfd8",
    'Iris': "#c4a7e7",
    'HighlightLow': "#bf88bc",
    'HighlightMed': "#403d52",
    'HighlightHigh': "#524f67",
}

rose_pine_moon = {
    'Base': "#232136",
    'Surface': "#2a273f",
    'Overlay': "#393552",
    'Muted': "#6e6a86",
    'Subtle': "#908caa",
    'Text': "#e0def4",
    'Love': "#eb6f92",
    'Gold': "#f6c177",
    'Rose': "#ea9a97",
    'Pine': "#3e8fb0",
    'Foam': "#9ccfd8",
    'Iris': "#c4a7e7",
    'HighlightLow': "#2a283e",
    'HighlightMed': "#44415a",
    'HighlightHigh': "#56526e",
}

rose_pine_dawn = {
    'Base': "#faf4ed",
    'Surface': "#fffaf3",
    'Overlay': "#f2e9e1",
    'Muted': "#9893a5",
    'Subtle': "#797593",
    'Text': "#575279",
    'Love': "#b4637a",
    'Gold': "#ea9d34",
    'Rose': "#d7827e",
    'Pine': "#286983",
    'Foam': "#56949f",
    'Iris': "#907aa9",
    'HighlightLow': "#f4ede8",
    'HighlightMed': "#dfdad9",
    'HighlightHigh': "#cecacd",
}
