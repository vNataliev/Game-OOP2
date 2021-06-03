import pygame as pg

from utils import Dimension, Icons, Position
from utils import ContextPopup
from world import World

import pickle


class Game:
    icon_size = 30  # px
    world_size = 20

    window_size = (1000, 600)

    white = (255, 255, 255)
    green = (153, 208, 144)
    black = (0, 0, 0)

    header_font_size = 30
    text_font_size = 10
    info_font_size = 13

    potion_position = (window_size[0] - icon_size - 20, window_size[1] - icon_size - 20)

    def __init__(self):
        self.icons = Icons(Dimension(Game.icon_size, Game.icon_size))
        self.world = World(Dimension(Game.world_size, Game.world_size))
        self.popup = ContextPopup(self.icons, (self.world.dims.x * Game.icon_size + 20, 400))
        self.popup.on_click_listener = self.create_and_add_organism

        self.last_clicked_pos = None

        pg.init()
        pg.font.init()

        self.header_font = pg.font.SysFont('Bookman Old Style', Game.header_font_size)
        self.text_font = pg.font.SysFont('Bookman Old Style', Game.text_font_size)
        self.info_font = pg.font.SysFont('Bookman Old Style', Game.info_font_size)

        self.screen = pg.display.set_mode(Game.window_size)

        pg.display.set_caption("World Simulator - Natalia Brzozka 180457")
        # icon source: https://www.flaticon.com/free-icon/planet-earth_1598196

        pg.display.set_icon(self.icons['bar'])

    def draw_grid(self, spacing):
        width, height = self.world.dims.as_tuple()
        for i in range(height + 1):  # horizontal
            y = i * spacing
            pg.draw.line(self.screen, Game.white, (0, y), (width * spacing, y))
        for i in range(width + 1):  # vertical
            x = i * spacing
            pg.draw.line(self.screen, Game.white, (x, 0), (x, height * spacing))

    def start(self):
        self.world.fill_world()
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit(0)
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP or event.key == pg.K_LEFT or event.key == pg.K_DOWN or event.key == pg.K_RIGHT:
                        self.world.make_turn(event)
                        self.popup.is_active = False
                    elif event.key == pg.K_p:
                        if self.world.human is not None:
                            self.world.human.activate_special_ability()
                    elif event.key == pg.K_s:
                        self.save_world('game_file.save')
                    elif event.key == pg.K_l:
                        self.load_world('game_file.save')
                elif event.type == pg.MOUSEBUTTONDOWN:
                    if self.handle_click_event_on_world():
                        self.popup.activate()
                    elif self.popup.is_active:
                        self.popup.handle_event()

                self.screen.fill(Game.green)
                self.render_text(self.header_font, 'Report:', (self.world.dims.x * Game.icon_size + 20, 0))
                self.render_text(self.info_font, 'TURN - {}'.format(self.world.turn_counter), (self.window_size[0] -
                                                                                               Game.icon_size - 45,
                                                                                               0.4 * Game.icon_size))
                self.draw_grid(Game.icon_size)
                self.draw_organisms()
                self.draw_info()
                self.draw_potion()
                self.draw_instructions()
                if self.popup.is_active:
                    self.popup.blit(self.screen)
                pg.display.update()

    def create_and_add_organism(self, constructor):
        pos = self.last_clicked_pos
        org = constructor(self.world, Position(pos[0], pos[1]))
        self.world.add_organism(org)

    def draw_organisms(self):
        for org in self.world.organisms:
            self.screen.blit(
                self.icons[org.get_name()], tuple(x * Game.icon_size for x in org.position.as_tuple())
            )

    def draw_potion(self):
        human = self.world.human
        if human is not None:
            if human.ability_activation:
                self.screen.blit(
                    self.icons['potion'], Game.potion_position
                )
                self.render_text(
                    self.text_font, 'AVAILABLE - press "p"', (Game.potion_position[0] - Game.icon_size * 4,
                                                              Game.potion_position[1] + 0.5 * Game.icon_size)
                )
            elif human.activated:
                self.screen.blit(
                    self.icons['potion'], Game.potion_position
                )
                self.render_text(
                    self.text_font, 'ACTIVATED',
                    (Game.potion_position[0] - Game.icon_size * 2.5, Game.potion_position[1] + 0.5 * Game.icon_size)
                )
            else:
                self.render_text(
                    self.text_font, 'NOT AVAILABLE YET',
                    (Game.potion_position[0] - Game.icon_size * 2.5, Game.potion_position[1] + 0.5 * Game.icon_size)
                )

    def render_text(self, font, text, pos):
        start_x, start_y = pos
        rendered = font.render(text, False, Game.black)
        text_rect = rendered.get_rect()
        text_rect.left = start_x
        text_rect.top = start_y
        self.screen.blit(rendered, text_rect)

    def draw_info(self):
        report_list = self.world.info_box.report
        for i, line in enumerate(report_list):
            self.render_text(self.text_font, line,
                             (self.world.dims.x * Game.icon_size + 20, Game.text_font_size * i + 40))

    def draw_instructions(self):
        self.render_text(self.info_font, 'To move use arrow keys',
                         (self.world.dims.x * Game.icon_size + 20, 450))
        self.render_text(self.info_font, 'To save game press "s"',
                         (self.world.dims.x * Game.icon_size + 20, Game.info_font_size + 450))
        self.render_text(self.info_font, 'To load last saved game press "l"',
                         (self.world.dims.x * Game.icon_size + 20, 2 * Game.info_font_size + 450))

    def save_world(self, filename):
        with open(filename, 'wb') as world_file:
            pickle.dump(self.world, world_file)

    def load_world(self, filename):
        with open(filename, 'rb') as world_file:
            self.world = pickle.load(world_file)

    def handle_click_event_on_world(self) -> bool:
        pos = list(pg.mouse.get_pos())
        pos[0] //= Game.icon_size
        pos[1] //= Game.icon_size

        if self.world.test_position(Position(pos[0], pos[1])):
            self.last_clicked_pos = pos
            return True
        return False
