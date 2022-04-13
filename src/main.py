import tcod
from classes import Player
from engine import Engine
from navigator import Navigator

COLS, ROWS = 80, 24
WIDTH, HEIGHT = 8 * COLS, 8 * ROWS  # Window pixel resolution (when not maximized.)
FLAGS = tcod.context.SDL_WINDOW_RESIZABLE | tcod.context.SDL_WINDOW_MAXIMIZED
CHARMAP = tcod.tileset.CHARMAP_CP437


def main() -> None:
    # Taken from https://dwarffortresswiki.org/index.php/Tileset_repository, made by Zaratustra
    tileset = tcod.tileset.load_tilesheet(
        "assets/tilesets/Zaratustra_msx.png", 16, 16, CHARMAP,
    )
    player = Player(int(COLS/2), int(ROWS/2))
    navigator = Navigator()
    engine = Engine(player, start_scene=navigator.entry, navigator=navigator)

    with tcod.context.new(
        width=WIDTH, height=HEIGHT, sdl_window_flags=FLAGS, 
        tileset=tileset,
        title="CTM Demo",
        vsync=True
    ) as context:
        root_console = context.new_console(order="F")
        while True:
            engine.render(root_console, context)

            events = tcod.event.wait()

            new_console = engine.handle_events(events, context)

            if new_console:
                root_console = new_console



if __name__ == "__main__":
    main()