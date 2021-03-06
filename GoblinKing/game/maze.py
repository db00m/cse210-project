#!/usr/bin/env python3

import random
import arcade
import timeit
import os

NATIVE_SPRITE_SIZE = 128
SPRITE_SCALING = 0.25
SPRITE_SIZE = NATIVE_SPRITE_SIZE * SPRITE_SCALING
SCREEN_WIDTH = 1000
height = 700
SCREEN_TITLE = "Maze Depth First Example"
MOVEMENT_SPEED = 8
TILE_EMPTY = 0
TILE_CRATE = 1
MERGE_SPRITES = True
VIEWPORT_MARGIN = 200


class Maze(arcade.SpriteList):
    def __init__(self, width, height):
        super().__init__()
        self.setup(width, height)

    def setup(self, width, height):
        # Create the maze
        maze = self.make_maze_depth_first(width, height)

        # Create sprites based on 2D grid
        if not MERGE_SPRITES:
            # This is the simple-to-understand method. Each grid location
            # is a sprite.
            for row in range(height):
                for column in range(width):
                    if maze[row][column] == 1:
                        wall = arcade.Sprite(
                            "local_resources/brick.png", SPRITE_SCALING
                        )
                        wall.center_x = column * SPRITE_SIZE + SPRITE_SIZE / 2
                        wall.center_y = row * SPRITE_SIZE + SPRITE_SIZE / 2
                        self.append(wall)
        else:
            for row in range(height):
                column = 0
                while column < len(maze):
                    while column < len(maze) and maze[row][column] == 0:
                        column += 1
                    start_column = column
                    while column < len(maze) and maze[row][column] == 1:
                        column += 1
                    end_column = column - 1

                    column_count = end_column - start_column + 1
                    column_mid = (start_column + end_column) / 2

                    wall = arcade.Sprite(
                        "local_resources/brick.png",
                        SPRITE_SCALING,
                        repeat_count_x=column_count,
                    )
                    wall.center_x = column_mid * SPRITE_SIZE + SPRITE_SIZE / 2
                    wall.center_y = row * SPRITE_SIZE + SPRITE_SIZE / 2
                    wall.width = SPRITE_SIZE * column_count
                    self.append(wall)

    def _create_grid_with_cells(self, width, height):
        """Create a grid with empty cells on odd row/column combinations."""
        grid = []
        for row in range(height):
            grid.append([])
            for column in range(width):
                if column % 2 == 1 and row % 2 == 1:
                    grid[row].append(TILE_EMPTY)
                elif (
                    column == 0 or row == 0 or column == width - 1 or row == height - 1
                ):
                    grid[row].append(TILE_CRATE)
                else:
                    grid[row].append(TILE_CRATE)
        grid[-2][-3] = TILE_EMPTY
        grid[1][0] = TILE_EMPTY
        return grid

    def make_maze_depth_first(self, maze_width, maze_height):
        maze = self._create_grid_with_cells(maze_width, maze_height)

        w = (len(maze[0]) - 1) // 2
        h = (len(maze) - 1) // 2
        vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]

        def walk(x: int, y: int):
            vis[y][x] = 1

            d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
            random.shuffle(d)
            for (xx, yy) in d:
                if vis[yy][xx]:
                    continue
                if xx == x:
                    maze[max(y, yy) * 2][x * 2 + 1] = TILE_EMPTY
                if yy == y:
                    maze[y * 2 + 1][max(x, xx) * 2] = TILE_EMPTY

                walk(xx, yy)

        walk(random.randrange(w), random.randrange(h))

        return maze
