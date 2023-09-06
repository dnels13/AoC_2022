# frozen_string_literal: true

class FileItem
  attr_reader :name, :size

  def initialize(name, size)
    @name = name
    @size = size
  end
end
