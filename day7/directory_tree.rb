# frozen_string_literal: true

class DirectoryTree
  ROOT = '/'
  SMALL_FILE_SIZE = 100_000
  DISK_SPACE = 70_000_000
  SPACE_REQUIRED = 30_000_000

  attr_reader :terminal_output, :root

  # @param terminal_output [String] a list of commands and results from a terminal
  def initialize(terminal_output)
    @terminal_output = terminal_output.drop(1) # remove unnecessary navigation to root dir
    @root = Directory.new(ROOT)
    build_directories
    solve_pt1
    # solve_pt2
  end

  # rubocop:disable Metrics/AbcSize, Metrics/MethodLength
  def build_directories
    path = []
    current_dir = @root
    terminal_output.each do |cmd_line|
      line = cmd_line.split
      case line[0]
      when '$'
        case line[1]
        when 'cd'
          if line[2] == '..'
            path.pop
          else
            path << line[2]
          end
        when 'ls' then current_dir = find_dir(path)
        end
      when 'dir' then current_dir.add_child_dir(line[1])
      else current_dir.add_file(FileItem.new(line[1], line[0].to_i))
      end
    end
  end
  # rubocop:enable Metrics/AbcSize, Metrics/MethodLength

  def solve_pt1
    small_sum = sum_small_dirs
    puts "Sum of all directories less than #{SMALL_FILE_SIZE}: #{small_sum}"
  end

  def solve_pt2
    puts "Available Space: #{unused_space}
    Update Size: #{SPACE_REQUIRED}
    Space needed: #{SPACE_REQUIRED - unused_space}"
    rip_dir = directory_to_be_deleted(root, root)
    puts "The directory that will be deleted is Dir #{rip_dir.name}, which will clear #{rip_dir.size} space"
  end

  # private

  # Move to Directory class?
  def find_dir(path)
    return root if path.empty?

    current_dir = root
    path.each do |dir_name|
      current_dir = current_dir.find_child(dir_name)
    end
    current_dir
  end

  def sum_small_dirs(dir = @root)
    dir_size = dir.size
    sum = dir_size <= SMALL_FILE_SIZE ? dir_size : 0
    dir.children.each do |child_dir|
      sum += sum_small_dirs(child_dir)
    end
    sum
  end

  def reset_root
    @root = Directory.new(ROOT)
  end

  def change_input(terminal_output)
    @terminal_output = terminal_output
  end

  # -- PART 2 --
  def unused_space
    @unused_space ||= DISK_SPACE - root.size
  end

  def directory_to_be_deleted(root, candidate)
    dir_size = root.size
    candidate = root if dir_size < candidate.size && dir_size >= SPACE_REQUIRED - unused_space
    root.children.each do |child_dir|
      candidate = directory_to_be_deleted(child_dir, candidate)
    end
    candidate
  end
end
