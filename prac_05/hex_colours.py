"""
CP1404/CP5632 Practical - Suggested Solution
Hexadecimal colour lookup
"""

COLOUR_CODES = {"GO Green": "#00ab66", "Gray83": "#d4d4d4",
                "GhostWhite": "#f8f8ff", "HotPink2": "#ee6aa7",
                "International Orange": "#ff4f00", "Light Cornflower Blue": "#93ccea",
                "MediumPurple2": "#9f79ee", "aquamarine2": "#76eec6",
                "Yellow4": "#8b8b00", "azure1": "#f0ffff", "Wintergreen Dream": "#56887d",
                "azure3": "#c1cdcd", "Thistle1": "#ffe1ff",
                "beige": "#f5f5dc", "Teal Blue": "#36588"}

colour_name = input("Enter a colour name: ")
while colour_name != "":
    # Note: using the get dictionary method
    # means you will get None if the key is not found
    print(f"The code for \"{colour_name}\" is {COLOUR_CODES.get(colour_name)}")
    colour_name = input("Enter a colour name: ")