# Minecraft Education Code Builder (Python)
# Build-only script for creating a large warehouse and section map.

ORIGIN_X = 100
ORIGIN_Y = 4
ORIGIN_Z = 100

sections = [
    {"name": "Loading_Bay", "minX": 102, "maxX": 118, "minY": 4, "maxY": 12, "minZ": 102, "maxZ": 116},
    {"name": "Storage_Area_A", "minX": 122, "maxX": 158, "minY": 4, "maxY": 12, "minZ": 102, "maxZ": 128},
    {"name": "Storage_Area_B", "minX": 122, "maxX": 158, "minY": 4, "maxY": 12, "minZ": 130, "maxZ": 144},
    {"name": "Packing_Station", "minX": 102, "maxX": 118, "minY": 4, "maxY": 12, "minZ": 118, "maxZ": 128},
    {"name": "Forbidden_Zone", "minX": 102, "maxX": 118, "minY": 4, "maxY": 12, "minZ": 130, "maxZ": 144},
    {"name": "Control_Office", "minX": 160, "maxX": 170, "minY": 4, "maxY": 12, "minZ": 102, "maxZ": 114}
]


def rel(dx, dy, dz):
    return world(ORIGIN_X + dx, ORIGIN_Y + dy, ORIGIN_Z + dz)


def build_shell():
    blocks.fill(GRAY_CONCRETE, rel(0, 0, 0), rel(72, 0, 48), FillOperation.REPLACE)
    blocks.fill(LIGHT_GRAY_CONCRETE, rel(0, 12, 0), rel(72, 12, 48), FillOperation.REPLACE)

    blocks.fill(BLACK_CONCRETE, rel(0, 1, 0), rel(72, 11, 0), FillOperation.REPLACE)
    blocks.fill(BLACK_CONCRETE, rel(0, 1, 48), rel(72, 11, 48), FillOperation.REPLACE)
    blocks.fill(BLACK_CONCRETE, rel(0, 1, 0), rel(0, 11, 48), FillOperation.REPLACE)
    blocks.fill(BLACK_CONCRETE, rel(72, 1, 0), rel(72, 11, 48), FillOperation.REPLACE)

    blocks.fill(AIR, rel(0, 1, 6), rel(0, 6, 14), FillOperation.REPLACE)

    blocks.fill(SEA_LANTERN, rel(6, 11, 6), rel(66, 11, 6), FillOperation.REPLACE)
    blocks.fill(SEA_LANTERN, rel(6, 11, 24), rel(66, 11, 24), FillOperation.REPLACE)
    blocks.fill(SEA_LANTERN, rel(6, 11, 42), rel(66, 11, 42), FillOperation.REPLACE)


def build_sections():
    blocks.fill(WHITE_CONCRETE, rel(2, 0, 2), rel(18, 0, 16), FillOperation.REPLACE)
    blocks.fill(YELLOW_CONCRETE, rel(2, 0, 2), rel(18, 0, 2), FillOperation.REPLACE)

    blocks.fill(ORANGE_CONCRETE, rel(2, 0, 18), rel(18, 0, 28), FillOperation.REPLACE)

    blocks.fill(GREEN_CONCRETE, rel(22, 0, 2), rel(58, 0, 28), FillOperation.REPLACE)
    blocks.fill(LIME_CONCRETE, rel(22, 0, 30), rel(58, 0, 44), FillOperation.REPLACE)

    blocks.fill(RED_CONCRETE, rel(2, 0, 30), rel(18, 0, 44), FillOperation.REPLACE)
    blocks.fill(IRON_BARS, rel(2, 1, 30), rel(18, 5, 30), FillOperation.REPLACE)
    blocks.fill(IRON_BARS, rel(2, 1, 44), rel(18, 5, 44), FillOperation.REPLACE)
    blocks.fill(IRON_BARS, rel(2, 1, 30), rel(2, 5, 44), FillOperation.REPLACE)
    blocks.fill(IRON_BARS, rel(18, 1, 30), rel(18, 5, 44), FillOperation.REPLACE)

    blocks.fill(WHITE_CONCRETE, rel(60, 1, 2), rel(70, 7, 14), FillOperation.REPLACE)
    blocks.fill(AIR, rel(61, 2, 3), rel(69, 6, 13), FillOperation.REPLACE)
    blocks.fill(GLASS_PANE, rel(60, 3, 5), rel(60, 5, 11), FillOperation.REPLACE)

    blocks.fill(YELLOW_CONCRETE, rel(20, 0, 2), rel(20, 0, 44), FillOperation.REPLACE)
    blocks.fill(YELLOW_CONCRETE, rel(2, 0, 29), rel(58, 0, 29), FillOperation.REPLACE)


def build_racks_and_pallets():
    x = 24
    while x <= 56:
        blocks.fill(IRON_BLOCK, rel(x, 1, 4), rel(x, 6, 26), FillOperation.REPLACE)
        blocks.fill(OAK_PLANKS, rel(x, 2, 4), rel(x + 4, 2, 26), FillOperation.REPLACE)
        blocks.fill(OAK_PLANKS, rel(x, 4, 4), rel(x + 4, 4, 26), FillOperation.REPLACE)
        x += 8

    x2 = 24
    while x2 <= 56:
        blocks.fill(IRON_BLOCK, rel(x2, 1, 32), rel(x2, 6, 42), FillOperation.REPLACE)
        blocks.fill(OAK_PLANKS, rel(x2, 2, 32), rel(x2 + 4, 2, 42), FillOperation.REPLACE)
        blocks.fill(OAK_PLANKS, rel(x2, 4, 32), rel(x2 + 4, 4, 42), FillOperation.REPLACE)
        x2 += 8

    blocks.place(CHEST, rel(6, 1, 10))
    blocks.place(BARREL, rel(10, 1, 10))
    blocks.place(HAY_BLOCK, rel(14, 1, 10))


def log_section_coordinates():
    player.say("Warehouse section coordinates:")
    i = 0
    while i < len(sections):
        s = sections[i]
        player.say(
            s["name"] +
            " X:" + str(s["minX"]) + "-" + str(s["maxX"]) +
            " Y:" + str(s["minY"]) + "-" + str(s["maxY"]) +
            " Z:" + str(s["minZ"]) + "-" + str(s["maxZ"])
        )
        i += 1


def on_build_warehouse():
    build_shell()
    build_sections()
    build_racks_and_pallets()
    player.teleport(rel(8, 2, -6))
    log_section_coordinates()
    player.say("Warehouse built at origin X:" + str(ORIGIN_X) + " Y:" + str(ORIGIN_Y) + " Z:" + str(ORIGIN_Z))


def on_show_coords():
    log_section_coordinates()


player.on_chat("build_warehouse", on_build_warehouse)
player.on_chat("show_coords", on_show_coords)
