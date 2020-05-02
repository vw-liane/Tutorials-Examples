from bokeh.plotting import figure, output_file, show
output_file('basic_plot.html')

# blank figure with labels
p = figure(plot_width = 600, plot_height = 600,
           title = 'Example Glyphs',
           x_axis_label = 'X', y_axis_label = 'Y')

# random data
squares_x = [1, 3, 4, 5, 8]
squares_y = [8, 7, 3, 1, 10]
circles_x = [9, 12, 4, 3, 15]
circles_y = [8, 4, 11, 6, 10]

# add squares glyph
p.square(squares_x, squares_y, size = 12, color = 'navy', alpha = 0.6)
# add circles glyp
p.circle(circles_x, circles_y, size = 12, color = 'red')

show(p)