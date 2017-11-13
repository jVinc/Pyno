from pyno import html as H, TreeNode, TreeSub
def linspace(first, last, n):
    """ returns a linear range from first to last with n elements"""
    return [(last-first)*x/(n-1)+first for x in range(n)]

# Setting default parameters to be added to svg elements
TreeNode.defaults['svg'] = {'version': '1.1', 'xmlns:xlink': "http://www.w3.org/1999/xlink", 'xmlns': "http://www.w3.org/2000/svg"}


def rescale_fun(box_from, box_to):
    """ Carries out a linear rescaling from coorindates defined by box_from in the
    format [[x1,y1],[x2,y2] to box_to in the same format. """
    scale_x = lambda x: (x-box_from[0][0])/(box_from[1][0]-box_from[0][0])*(box_to[1][0]-box_to[0][0])+box_to[0][0]
    scale_y = lambda y: (y-box_from[0][1])/(box_from[1][1]-box_from[0][1])*(box_to[1][1]-box_to[0][1])+box_to[0][1]
    return lambda xy: [scale_x(xy[0]), scale_y(xy[1])]



def svg_plot(data_outside, data_region=None, labels=('', ''), marked_location=None, prolog=(), epilog=()):
    if data_region is None:
        # If not defined is set to a 10% margin of data range.
        min_x = min(el[0] for el in data_outside)
        min_y = min(el[1] for el in data_outside)
        max_x = max(el[0] for el in data_outside)
        max_y = max(el[1] for el in data_outside)
        data_region = (
            (min_x-0.1*(max_x-min_x), min_y-0.1*(max_y-min_y)),
            (max_x+0.1*(max_x-min_x), max_y+0.1*(max_y-min_y))
        )

    y_axis_label = labels[1]
    x_axis_label = labels[0]

    cfg = {'width': 800, 'height': 450, 'ticks_x': 9, 'ticks_y': 7,
                      'ticks_offset_x': 26,
                      'ticks_offset_y': 14,
                      'vertical_align_hard': 5,
                      'ticks_x_height': 10,
                      'ticks_y_width': 20,
                      'margin': (60, 60, 80, 120) #Margin follows css standard so top, right, bottom, left
                      }

    canvas_region = [[cfg['margin'][3], cfg['height']-cfg['margin'][2]],
                     [cfg['width']-cfg['margin'][1], cfg['margin'][0]]]  # These are the pixel locations of origin and upper right corner.


    point_data = list(map(rescale_fun(data_region, canvas_region), data_outside))
    point_data_x = [xy[0] for xy in point_data]
    point_data_y = [xy[1] for xy in point_data]

    point_data_value = [xy[1] for xy in data_outside]

    dots = H.g((H.circle('', cx=x, cy=y, data_value=v, r=5)
                    for x, y, v in zip(point_data_x, point_data_y, point_data_value)),
                Class='first_set points', data_setname='Our first data set')

    x_ticks = linspace(canvas_region[0][0], canvas_region[1][0], cfg['ticks_x'])
    y_ticks = linspace(canvas_region[0][1], canvas_region[1][1], cfg['ticks_y'])

    xlines = (H.line('', x1=x, x2=x, y1=min(y_ticks), y2=max(y_ticks)+cfg['ticks_offset_x']/2) for x in x_ticks)
    groupx = H.g(xlines, Class='grid x-grid', id='xGrid')

    ylines = (H.line('', x1=min(x_ticks)-cfg['ticks_offset_y']/2, x2=max(x_ticks), y1=y, y2=y) for y in y_ticks)
    groupy = H.g(ylines, nodeClass='grid y-grid', id='yGrid')

    label_treatment = lambda labels: [round(x, 2) for x in labels] # todo, figure out highest non similar and round to that.
    x_labels = label_treatment(linspace(data_region[0][0], data_region[1][0], cfg['ticks_x']))
    y_labels = label_treatment(linspace(data_region[0][1], data_region[1][1], cfg['ticks_y']))

    h_x_labels = H.g([H.text(label, x=x, y=cfg['height']-cfg['margin'][2]+cfg['ticks_offset_x'])
        for x, label in zip(x_ticks, x_labels)]+[H.text(x_axis_label, x=cfg['width']/2, y=cfg['height']-(cfg['margin'][2]-cfg['ticks_offset_x']-cfg['ticks_x_height'])/2, Class='x_axis_label')],
            Class='labels x-labels')

    y_x_positions = [cfg['margin'][3]-cfg['ticks_offset_y']]*len(y_labels)
    y_positions = [y+cfg['vertical_align_hard'] for y in y_ticks]

    distance_y_label_to_axis = (cfg['margin'][3] - cfg['ticks_offset_y']-cfg['ticks_y_width'])/2
    distance_y_label_center = cfg['height']/2

    h_y_labels = H.g([H.text(label, x=x, y=y)
                          for x, y, label in zip(y_x_positions, y_positions, y_labels)] +
                            [H.text(y_axis_label, x=0, y=0,
                                  transform="translate("+str(distance_y_label_to_axis)+","+str(distance_y_label_center)+") rotate(-90)", Class='y_axis_label')],
                             Class='labels y-labels')

    # surface = H.g(H.path('', nodeClass='first_set', d=fill_surface_d(point_data, y_ticks[0])), Class='surfaces')

    use_tags = H.g([H.use('', nodeClass='grid double', **{'xlink:href': '#xGrid'}),
                    H.use('', nodeClass='grid double', **{'xlink:href': '#yGrid'})])
    # print(canvas_region, data_region)

    # todo Insert svg based canvas scaling
    content = H.svg(prolog, groupx, groupy, use_tags, dots, h_x_labels, h_y_labels, epilog, Class='graph',
        width=str(cfg['width'])+'px',
        height=str(cfg['height'])+'px')

    return content

from pyno import browser_preview

if __name__ == '__main__':
    browser_preview(svg_plot([[1, 2], [2, 3], [3, 2.3], [4, 2.4]]))