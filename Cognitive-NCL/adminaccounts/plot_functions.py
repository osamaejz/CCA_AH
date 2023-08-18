
from PIL import Image
import os
import sys
import matplotlib
from matplotlib import cm
from matplotlib import pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Wedge, Rectangle
# import emoji
# print(emoji.emojize('Python is :thumbs_up:'))
# em_1 = emoji.emojize(':smiling_face_with_smiling_eyes:')
# em_2 = emoji.emojize(':Slightly_smiling_face:')
# em_3 = emoji.emojize(':neutral_face:')
# em_4 = emoji.emojize(':disappointed_face:')
# em_5 = emoji.emojize(':worried_face:')

em_1 = 'Extr. Severe'
em_2 = 'Severe'
em_3 = 'Moderate'
em_4 = 'Mild'
em_5 = 'Normal'


em_1, em_2, em_3, em_4, em_5


def degree_range(n):
    start = np.linspace(0, 180, n+1, endpoint=True)[0:-1]
    end = np.linspace(0, 180, n+1, endpoint=True)[1::]
    mid_points = start + ((end-start)/2.)
    return np.c_[start, end], mid_points


def rot_text(ang):
    rotation = np.degrees(np.radians(ang) * np.pi / np.pi - np.radians(90))
    return rotation


def gauge(labels,
          colors=['red', 'orangered', 'orange', 'lightgreen', 'lime'],
          arrow="",
          title="",
          fname=False):
    """
    some sanity checks first

    """

    N = len(labels)

    if arrow > N:
        raise Exception("\n\nThe category ({}) is greated than \
        the length\nof the labels ({})".format(arrow, N))

    """
    begins the plotting
    """

    fig, ax = plt.subplots(figsize=(5, 5))
    fig.subplots_adjust(0, 0, 2, 1)

    ang_range, mid_points = degree_range(N)

    labels = labels[::-1]

    """
    plots the sectors and the arcs
    """
    patches = []
    for ang, c in zip(ang_range, colors):
        # sectors
        patches.append(Wedge((0., 0.), .4, *ang, facecolor='w', lw=2))
        # arcs
        patches.append(Wedge((0., 0.), .4, *ang, width=0.2,
                       facecolor=c, lw=2, alpha=0.5,))

    [ax.add_patch(p) for p in patches]

    """
    set the labels
    """

    for mid, lab in zip(mid_points, labels):

        ax.text(0.42 * np.cos(np.radians(mid)), 0.42 * np.sin(np.radians(mid)), lab,
                horizontalalignment='center', verticalalignment='center', fontsize=20,
                fontweight='bold', rotation=rot_text(mid))

    """
    set the bottom banner and the title
    """

    r = Rectangle((-0.4, -0.1), 0.8, 0.1, facecolor='w', lw=2)
    ax.add_patch(r)

    ax.text(0, -0.1, title, horizontalalignment='center',
            verticalalignment='center', fontsize=30, fontweight='bold')

    """
    plots the arrow now
    """

    pos = mid_points[abs(arrow - N)]

    ax.arrow(0, 0, 0.225 * np.cos(np.radians(pos)), 0.225 * np.sin(np.radians(pos)),
             width=0.04, head_width=0.09, head_length=0.1, fc='k', ec='k')

    ax.add_patch(Circle((0, 0), radius=0.02, facecolor='k'))
    ax.add_patch(Circle((0, 0), radius=0.01, facecolor='w', zorder=11))

    """
    removes frame and ticks, and makes axis equal and tight
    """

    ax.set_frame_on(False)
    ax.axes.set_xticks([])
    ax.axes.set_yticks([])
    ax.axis('equal')


#     plt.tight_layout()
    if fname:
        fig.savefig(fname, dpi='figure', bbox_inches='tight')


# gauge(title= ("Depression: " + str(95) + "%"), arrow = 5)


def concatenate_images(images, direction='horizontal'):
    # Determine the dimensions of the final image
    if direction == 'horizontal':
        width = sum(image.width for image in images)
        height = max(image.height for image in images)
    else:
        width = max(image.width for image in images)
        height = sum(image.height for image in images)

    # Create a new blank image with the calculated dimensions
    result_image = Image.new('RGB', (width, height))

    # Paste each image onto the result image
    offset = 0
    for image in images:
        if direction == 'horizontal':
            result_image.paste(image, (offset, 0))
            offset += image.width
        else:
            result_image.paste(image, (0, offset))
            offset += image.height

    return result_image
