#########################################
# Manages all the screens
#########################################
from .main_menu_screen import Main_menu_screen
from .classic_game_screen import Classic_Game_Screen
from .settings_screen import Settings_screen
from .game_over_screen import Game_over_screen
from .tutorial_screen import Tutorial_screen
from .credits_screen import Credits_screen
from .game_mode_screen import Game_Mode_Screen
from .game_introduction_screen import Game_Introduction_Screen
from .infinite_game_screen import Infinite_Game_Screen
from .one_v_one_game_screen import One_V_One_Game_Screen
from .ai_game_screen import AI_Game_Screen
from .hardcore_game_screen import Hardcore_Game_Screen
from .heist_game_screen import Heist_Game_Screen
from src.misc.game_enums import Game_mode
import sys


class Screens_Manager:
    def __init__(self, pygame, res, surface, size, game_clock, game_manager):
        self.pygame = pygame
        self.init_screens(pygame, res, surface, size, game_clock, game_manager)

    def init_screens(self, pygame, res, surface, size, game_clock, game_manager):
        ''' Init all the screen, based on params provided by main.py. '''
        self.main_menu_screen = Main_menu_screen(
            pygame, res, surface, size)

        self.classic_game_screen = Classic_Game_Screen(
            pygame, res, surface, size, game_clock, game_manager)

        self.settings_screen = Settings_screen(
            pygame, res, surface, size, game_manager)

        self.game_over_screen = Game_over_screen(
            pygame, res, surface, size, game_manager)

        self.tutorial_screen = Tutorial_screen(
            pygame, res, surface, size)

        self.credits_screen = Credits_screen(
            pygame, res, surface, size)

        self.game_mode_screen = Game_Mode_Screen(
            pygame, res, surface, size, game_manager)

        self.game_introduction_screen = Game_Introduction_Screen(
            pygame, res, surface, size, game_manager)

        self.infinite_game_screen = Infinite_Game_Screen(
            pygame, res, surface, size, game_clock, game_manager)

        self.one_v_one_game_screen = One_V_One_Game_Screen(
            pygame, res, surface, size, game_clock, game_manager)

        self.ai_game_screen = AI_Game_Screen(
            pygame, res, surface, size, game_clock, game_manager)

        self.hardcore_game_screen = Hardcore_Game_Screen(
            pygame, res, surface, size, game_clock, game_manager)

        self.heist_game_screen = Heist_Game_Screen(
            pygame, res, surface, size, game_clock, game_manager)

    def show(self, game_mode, events):
        ''' Show a screen based on game mode and will return the next game mode. '''
        return self.game_mode_to_screen(game_mode).update(events)

    def game_mode_to_screen(self, game_mode):
        if game_mode == Game_mode.MAIN_MENU:
            return self.main_menu_screen

        elif game_mode == Game_mode.CLASSIC:
            return self.classic_game_screen

        elif game_mode == Game_mode.SETTINGS:
            return self.settings_screen

        elif game_mode == Game_mode.GAME_OVER:
            return self.game_over_screen

        elif game_mode == Game_mode.TUTORIAL:
            return self.tutorial_screen

        elif game_mode == Game_mode.CREDITS:
            return self.credits_screen

        elif game_mode == Game_mode.GAME_MODE:
            return self.game_mode_screen

        elif game_mode == Game_mode.INTRODUCTION:
            return self.game_introduction_screen

        elif game_mode == Game_mode.INFINITE:
            return self.infinite_game_screen

        elif game_mode == Game_mode.ONE_V_ONE:
            return self.one_v_one_game_screen

        elif game_mode == Game_mode.AI:
            return self.ai_game_screen

        elif game_mode == Game_mode.HARDCORE:
            return self.hardcore_game_screen

        elif game_mode == Game_mode.HEIST:
            return self.heist_game_screen

        else:
            self.pygame.quit()
            sys.exit()
