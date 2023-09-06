# frozen_string_literal: true

class Directory
  attr_reader :contents, :name, :children

  def initialize(name, contents = [], children = [])
    @name = name
    @contents = contents
    @children = children
  end

  def add_file(file)
    @contents << file
  end

  def add_child_dir(child_name)
    @children << Directory.new(child_name)
  end

  def size
    total_size = contents_size
    children.each do |dir|
      total_size += dir.size
    end
    total_size
  end

  def contents_size
    total_size = 0
    contents.each do |file| # FileItem
      total_size += file.size
    end
    total_size
  end

  def find_child(dir_name)
    @children.each do |child|
      return child if child.name == dir_name
    end
  end
end
