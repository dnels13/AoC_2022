# frozen_string_literal: true

class TreeGrid
  attr_reader :grid

  def initialize(grid_input)
    @grid = build_grid(grid_input)
  end

  def build_grid(grid_input)
    grid_txt = grid_input.split("\n")
    grid_proto = []
    grid_txt.each do |row|
      grid_proto << row.split('').map(&:to_i)
    end
    grid_proto
  end

  def solve_pt1
    visible_trees = count_visible_trees + perimeter_trees
    puts "Number of visible trees: #{visible_trees}"
  end

  def count_visible_trees
    count = 0
    (1..grid.size - 2).each do |i|
      (1..grid[i].size - 2).each do |j|
        count += 1 if tree_visible?(j, i)
      end
    end
    count
  end

  def perimeter_trees
    grid.size * 2 + ((grid.first.size - 2) * 2)
  end

  def tree_visible?(tree_x, tree_y)
    tree_visible_from_north?(tree_x, tree_y) ||
      tree_visible_from_east?(tree_x, tree_y) ||
      tree_visible_from_south?(tree_x, tree_y) ||
      tree_visible_from_west?(tree_x, tree_y)
  end

  def tree_visible_from_north?(tree_x, tree_y)
    tree_size = grid[tree_y][tree_x]
    visible = true
    (0..tree_y - 1).each do |i|
      visible &&= tree_size > grid[i][tree_x]
    end
    visible
  end

  def tree_visible_from_east?(tree_x, tree_y)
    tree_size = grid[tree_y][tree_x]
    visible = true
    (tree_x + 1..grid.first.size - 1).each do |i|
      visible &&= tree_size > grid[tree_y][i]
    end
    visible
  end

  def tree_visible_from_south?(tree_x, tree_y)
    tree_size = grid[tree_y][tree_x]
    visible = true
    (tree_y + 1..grid.size - 1).each do |i|
      visible &&= tree_size > grid[i][tree_x]
    end
    visible
  end

  def tree_visible_from_west?(tree_x, tree_y)
    tree_size = grid[tree_y][tree_x]
    visible = true
    (0..tree_x - 1).each do |i|
      visible &&= tree_size > grid[tree_y][i]
    end
    visible
  end
end
