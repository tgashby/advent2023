class Day2
  def initialize

  end

  def processPuzzle
    idTotal = 0

    Dir.chdir(File.dirname(__FILE__))
    File.foreach("puzzle.input") do |line|
      captures = line.match(/Game (\d+)/)
      marbles = /((\d+) (red|green|blue))(,|;|)/

      # if (!self.gameIsImpossible(line.scan(marbles))) then
      #   puts line
      #   idTotal += captures[1].to_i
      # end

      minColors = minMarbles(line.scan(marbles))

      idTotal += (minColors[:red] * minColors[:green] * minColors[:blue])
    end

    return idTotal
  end

  def gameIsImpossible(marbles)
    colors = {red: 0, green: 0, blue: 0}

    marbles.to_a.each do | marble_data |
      total = marble_data[1].to_i
      color = marble_data[2]
      semi_colon = marble_data[3] == ';' || marble_data[3] == ''

      colors[color.to_sym] += total
      if (semi_colon) then
        if colors[:red] > 12 or colors[:green] > 13 or colors[:blue] > 14 then
          return true
        end

        colors = {red: 0, green: 0, blue: 0}
      end
    end

    return false
  end

  def minMarbles(marbles)
    minColors = {red: 0, green: 0, blue: 0}

    colors = {red: 0, green: 0, blue: 0}
    marbles.to_a.each do | marble_data |
      total = marble_data[1].to_i
      color = marble_data[2]
      semi_colon = marble_data[3] == ';' || marble_data[3] == ''

      colors[color.to_sym] += total
      if (semi_colon) then
        if colors[:red] > minColors[:red] then
          minColors[:red] = colors[:red]
        end

        if colors[:green] > minColors[:green] then
          minColors[:green] = colors[:green]
        end

        if colors[:blue] > minColors[:blue] then
          minColors[:blue] = colors[:blue]
        end

        colors = {red: 0, green: 0, blue: 0}
      end
    end

    return minColors
  end
end

day2 = Day2.new()

puts day2.processPuzzle()
