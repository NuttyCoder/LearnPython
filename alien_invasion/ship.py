import pygame

class Ship:
  """A class to manage the ship."""

def _init_(self, ai_game):
  """Initialize the ship and set its starting position"""
  self.scree = ai.game.screen
  self.screen_rect = ai_game.screen.get_rect()

  # Load ship image and get its rect.
  self.image = pygame.image.load('images/ship.bmp')
  self.rect = self.image.get_rect()

  # Start each new ship at the bottom center of the screen
  self.rect.midbottom = self.scree_rect.midbottom

def blitme(self):
  """Draw the ship at its current location."""
  self.screen.blit(self.image, self.rect)
