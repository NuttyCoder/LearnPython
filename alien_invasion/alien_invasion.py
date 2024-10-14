import sys
import pygame


class AlienInvasion:
  """Overall class to manage game assets and behaviors."""

  def_init_(self):
    """Initialize the game, and create game resources."""
    pygame.init()
    self.clock = pygame.time.Clock() # Class Clock, making the clock tick at the end of the while loop
    
    self.screen = pygame.display.set_mode((1200,800))
    # self.screen  is called the surface, while 1200, 800 is a tuple in this case the alien or the ship will have its own surface
    pygame.display.set_caption("Alien Invasion")
    # entire game window
    # set the background color
    self.bg_color = (230, 230,230)
def run_game(self):
             """Start the main loop for the game."""
              # Here run_game() is a method that contains a while loop which contains and event loop, an event is an action that the user performs while playing.
             while True:
               # Watch for keyboard and mouse events. Event loop listens for events.
               for event in pygame.event.get(); # this function returns a list of events
                 if event.type == pygame.QUIT: # Event that allows the player to quit.
                  sys.exit()
              # Redraw the screen during each pass through thr loop  
              self.screen.fill(self.bg_color)

              # Make the most recently drawn screen visible.
              pygame.display.flip()
              self.clock.tick(60)
if_name_ == ' _main_ ':
  # make a game instance, and run the game.
  ai = AlienInvasion()
  ai.run_game()


