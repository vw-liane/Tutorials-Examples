# figure - styling of plots (title, labels, axes, grids)
# output_file - how visualization is rendered (to HTML file)
# show - when plot is ready for output
from bokeh.plotting import figure, output_file, show
output_file('my_first_graph.html')    # recommended immed. after IMPORTS
# also can use <output_notebook>

# lists for x and y axes
x = [1, 3, 5, 7]
y = [2, 4, 6, 8]

p = figure()  # of type PLOT (hence 'p')

# plotting data with GLYPH METHOD (glyph = shapes added to plots)
# here passed DATA  styling arguments
p.circle(x, y, size=10, color='red', legend='circle')
p.line(x, y, color='blue', legend='line')
p.triangle(y, x, color='gold', size=10, legend='triangle')

# begin interactivity
# click on legend to show/hide that data-piece
p.legend.click_policy='hide'

# output to HTML file
show(p)

