import PySimpleGUI as sg


def frame(title, layout, expand_y=True, expand_x=True, **kwargs):
    return sg.Frame(title, layout, expand_y=expand_y, expand_x=expand_x, **kwargs)


def column(layout, expand_y=True, expand_x=True):
    return sg.Column(layout, expand_y=expand_y, expand_x=expand_x)


def button(text):
    return sg.Button(button_text=text, key=f'button_{text}')


# DEFAULT THEME #
sg.theme('DarkGrey11')

# GUI Frames #

# LEFT COL #
viewer_x_size = 750
viewer_y_size = 550
viewer_canvas_size = (viewer_x_size, viewer_y_size)
viewer_bottom_left = (0, viewer_y_size)
viewer_top_right = (viewer_x_size, 0)

jigsaw_viewer = sg.Graph(
    canvas_size=viewer_canvas_size,
    graph_bottom_left=viewer_bottom_left,
    graph_top_right=viewer_top_right,
    key='viewer',
    enable_events=True
)
jigsaw_viewer_frame = frame('Jigsaw Viewer', [[jigsaw_viewer]])

# RIGHT COL #
piece_viewer = sg.Graph(
    background_color='white',
    canvas_size=(150, 150),
    graph_bottom_left=(0, 50),
    graph_top_right=(50, 0),
    key='piece_viewer',
    enable_events=True
)
piece_viewer_frame = frame('Piece Viewer', [[piece_viewer]], expand_y=False)

input_frame = frame('Input', [
    [sg.T('Load Jigsaw'), sg.In(key='input_image', enable_events=True), sg.FileBrowse()],
    [sg.T('Original size'), sg.T(k='original_img_height'), sg.T('X'), sg.T(k='original_img_width')],
    [sg.T('Resized size'), sg.T(k='new_img_width'), sg.T('X'), sg.T(k='new_img_height')],
    [sg.HorizontalSeparator()],
    [sg.T('Search Piece'), sg.In(key='input_piece', enable_events=True), sg.FileBrowse()],
    [sg.T('Height pieces:'), sg.In(default_text=24, k='height_pieces', size=5), sg.T('Width pieces:'), sg.In(default_text=50, k='width_pieces', size=5)],
    [sg.T('Height(cm):    '), sg.In(default_text=50, k='height_cm', size=5), sg.T('Width(cm):    '), sg.In(default_text=70, k='width_cm', size=5)],
    [sg.T('Total pieces:'), sg.T(text='1000', k='total_pieces'), sg.T('Piece width:'), sg.T(
        text='30(px)', k='piece_width'), sg.T('Piece height:'), sg.T(text='30(px)', k='piece_height')],
], expand_y=False)

actions_frame = sg.Frame('Actions', [
    [button('crop'), button('grid')]
])
log_frame = frame('Log', [
    [sg.Multiline(key='log', expand_y=True, expand_x=True, echo_stdout_stderr=True, autoscroll=True, reroute_stdout=True)]
], expand_y=True)

# GUI COLs #
viewer_col = column([[jigsaw_viewer_frame]])
editor_col = column([[input_frame], [actions_frame], [piece_viewer_frame], [log_frame]])
