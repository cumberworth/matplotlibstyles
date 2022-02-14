"""Function and settings for creating plots"""

import colorsys

import matplotlib as mpl
from matplotlib import cm
from matplotlib import colors
from matplotlib import pyplot as plt
import numpy as np


def set_default_style():

    # Lines
    plt.rcParams['lines.linewidth'] = 1.0
    plt.rcParams['lines.markeredgewidth'] = 1.0
    plt.rcParams['lines.markersize'] = 5

    # Fonts and symbols
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.serif'] = 'Times New Roman'
    plt.rcParams['font.weight'] = 'normal'
    plt.rcParams['font.size'] = 8
    plt.rcParams['axes.titlesize'] = 8
    plt.rcParams['axes.labelsize'] = 8
    plt.rcParams['xtick.labelsize'] = 8
    plt.rcParams['ytick.labelsize'] = 8
    plt.rcParams['legend.fontsize'] = 8
    plt.rcParams['text.usetex'] = False
    plt.rcParams['mathtext.rm'] = 'serif'
    plt.rcParams['mathtext.it'] = 'serif:italic'
    plt.rcParams['mathtext.fontset'] = 'stix'

    # Axes
    plt.rcParams['axes.linewidth'] = 0.8
    plt.rcParams['axes.spines.right'] = False
    plt.rcParams['axes.spines.top'] = False

    # Ticks
    plt.rcParams['xtick.color'] = (0.0, 0.0, 0.0)
    plt.rcParams['xtick.major.width'] = 0.8
    plt.rcParams['ytick.color'] = (0.0, 0.0, 0.0)
    plt.rcParams['ytick.major.width'] = 0.8

    # Errorbar plots
    plt.rcParams['errorbar.capsize'] = 2

    # Legend
    plt.rcParams['legend.frameon'] = False
    plt.rcParams['legend.framealpha'] = 0.0


def set_thin_style():

    # Lines
    plt.rcParams['lines.linewidth'] = 0.5
    plt.rcParams['lines.markeredgewidth'] = 0.7
    plt.rcParams['lines.markersize'] = 2.5

    # Fonts and symbols
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.serif'] = 'Times New Roman'
    plt.rcParams['font.weight'] = 'normal'
    plt.rcParams['font.size'] = 8
    plt.rcParams['axes.titlesize'] = 8
    plt.rcParams['axes.labelsize'] = 8
    plt.rcParams['xtick.labelsize'] = 8
    plt.rcParams['ytick.labelsize'] = 8
    plt.rcParams['legend.fontsize'] = 8
    plt.rcParams['text.usetex'] = False
    plt.rcParams['mathtext.rm'] = 'serif'
    plt.rcParams['mathtext.it'] = 'serif:italic'
    plt.rcParams['mathtext.fontset'] = 'stix'

    # Axes
    plt.rcParams['axes.edgecolor'] = (0.0, 0.0, 0.0)
    plt.rcParams['axes.linewidth'] = 0.5
    plt.rcParams['axes.spines.right'] = False
    plt.rcParams['axes.spines.top'] = False

    # Ticks
    plt.rcParams['xtick.color'] = (0.0, 0.0, 0.0)
    plt.rcParams['xtick.major.width'] = 0.5
    plt.rcParams['ytick.color'] = (0.0, 0.0, 0.0)
    plt.rcParams['ytick.major.width'] = 0.5

    # Errorbar plots
    plt.rcParams['errorbar.capsize'] = 1.0

    # Legend
    plt.rcParams['legend.frameon'] = False
    plt.rcParams['legend.framealpha'] = 0.0


def set_default_latex_style():
    mpl.use('pgf')

    plt.rcParams['lines.linewidth'] = 1.0
    plt.rcParams['lines.markeredgewidth'] = 1.0
    plt.rcParams['lines.markersize'] = 2.5

    # Fonts and symbols
    plt.rcParams['pgf.texsystem'] = 'lualatex'
    plt.rcParams['pgf.rcfonts'] = False
    plt.rcParams['text.usetex'] = True
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.serif'] = ['STIX Two Text']
    plt.rcParams['text.color'] = 'black'
    plt.rcParams['font.size'] = 8
    plt.rcParams['axes.titlesize'] = 8
    plt.rcParams['axes.labelsize'] = 8
    plt.rcParams['xtick.labelsize'] = 8
    plt.rcParams['ytick.labelsize'] = 8
    plt.rcParams['legend.fontsize'] = 8
    plt.rcParams['pgf.preamble'] = '\n'.join([
        r'\usepackage{fontspec}',
        r'\usepackage[RGB]{xcolor}',
        r'\usepackage{unicode-math}',
        r'\setmainfont{STIX Two Text}',
        r'\setmathfont{STIX Two Math}',
        r'\usepackage{nicefrac}',
        r'\usepackage{siunitx}',
        r'\DeclareSIUnit{\molar}{M}',
        r'\DeclareSIUnit{\kb}{\ensuremath{k_\textrm{B}}}',
        r'\DeclareSIUnit{\kbT}{\ensuremath{k_\textrm{B} T}}'])

    # Axes
    plt.rcParams['axes.edgecolor'] = 'black'
    plt.rcParams['axes.labelcolor'] = 'black'
    plt.rcParams['axes.linewidth'] = 0.8
    plt.rcParams['axes.spines.right'] = False
    plt.rcParams['axes.spines.top'] = False

    # Ticks
    plt.rcParams['xtick.color'] = 'black'
    plt.rcParams['xtick.major.width'] = 0.8
    plt.rcParams['ytick.color'] = 'black'
    plt.rcParams['ytick.major.width'] = 0.8

    # Errorbar plots
    plt.rcParams['errorbar.capsize'] = 2

    # Legend
    plt.rcParams['legend.frameon'] = False
    plt.rcParams['legend.framealpha'] = 0.0


def set_thin_latex_style():
    mpl.use('pgf')

    plt.rcParams['lines.linewidth'] = 0.5
    plt.rcParams['lines.markeredgewidth'] = 0.7
    plt.rcParams['lines.markersize'] = 2.5

    # Fonts and symbols
    plt.rcParams['pgf.texsystem'] = 'lualatex'
    plt.rcParams['pgf.rcfonts'] = False
    plt.rcParams['text.usetex'] = True
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.serif'] = ['STIX Two Text']
    plt.rcParams['text.color'] = '#231f20'
    plt.rcParams['font.size'] = 8
    plt.rcParams['axes.titlesize'] = 8
    plt.rcParams['axes.labelsize'] = 8
    plt.rcParams['xtick.labelsize'] = 8
    plt.rcParams['ytick.labelsize'] = 8
    plt.rcParams['legend.fontsize'] = 8
    plt.rcParams['pgf.preamble'] = '\n'.join([
        r'\usepackage{fontspec}',
        r'\usepackage[RGB]{xcolor}',
        r'\usepackage{unicode-math}',
        r'\setmainfont{STIX Two Text}',
        r'\setmathfont{STIX Two Math}',
        r'\usepackage{nicefrac}',
        r'\usepackage{siunitx}',
        r'\DeclareSIUnit{\molar}{M}',
        r'\DeclareSIUnit{\kb}{\ensuremath{k_\textrm{B}}}',
        r'\DeclareSIUnit{\kbT}{\ensuremath{k_\textrm{B} T}}'])

    # Axes
    plt.rcParams['axes.edgecolor'] = '#231f20'
    plt.rcParams['axes.labelcolor'] = '#231f20'
    plt.rcParams['axes.linewidth'] = 0.5
    plt.rcParams['axes.spines.right'] = False
    plt.rcParams['axes.spines.top'] = False

    # Ticks
    plt.rcParams['xtick.color'] = '#231f20'
    plt.rcParams['xtick.major.width'] = 0.5
    plt.rcParams['ytick.color'] = '#231f20'
    plt.rcParams['ytick.major.width'] = 0.5

    # Errorbar plots
    plt.rcParams['errorbar.capsize'] = 1.0

    # Legend
    plt.rcParams['legend.frameon'] = False
    plt.rcParams['legend.framealpha'] = 0.0


def setup_shared_axis(ax):
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_color('none')
    ax.spines['left'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.tick_params(
        labelcolor='none', top=False, bottom=False, left=False, right=False)

    # The above does not work with pgf backend
    ax.set_xticklabels([])
    ax.set_yticklabels([])


def cm_to_inches(cm):
    return cm/2.54


def pt_to_inches(pt):
    return pt*0.01389


def create_truncated_colormap(left, right, name='viridis', N=256):
    cmap = cm.get_cmap(name, 2*N)

    return colors.ListedColormap(cmap(np.linspace(left, right, N)))


def create_log_mappable(cmap, vmin, vmax):
    norm = mpl.colors.LogNorm(vmin=vmin, vmax=vmax)
    mappable = cm.ScalarMappable(norm=norm, cmap=cmap)

    return mappable


def create_linear_mappable(cmap, vmin, vmax):
    norm = mpl.colors.Normalize(vmin=vmin, vmax=vmax)
    mappable = cm.ScalarMappable(norm=norm, cmap=cmap)

    return mappable


def create_segmented_colormap(cmap, values, increment):
    bmin = values[0] - increment/2
    bmax = values[-1] + 3*increment/2
    boundaries = np.arange(bmin, bmax, increment)
    norm = mpl.colors.BoundaryNorm(boundaries, len(values) + 1)
    norm2 = mpl.colors.Normalize(vmin=0, vmax=len(values))
    norm3 = mpl.colors.BoundaryNorm(
        np.arange(-0.5, len(values) + 0.5, 1), len(values) + 1)
    colors = cmap(norm2(norm(values + [values[-1] + increment])))
    cmap = mpl.colors.ListedColormap(colors, 'hate')

    return cmap, norm3, colors


def plot_segmented_colorbar(f, ax, cmap, norm, label, ticklabels, orientation):
    mappable = mpl.cm.ScalarMappable(norm=norm, cmap=cmap)
    cbar = f.colorbar(mappable, ax=ax, orientation=orientation,
                      ticks=list(range(0, len(ticklabels) + 1)), aspect=40)
    cbar.set_label(label)
    ticklabels += ['0.0']
    cbar.set_ticklabels(ticklabels)


#def plot_segmented_colorbar(f, mappable, ncolors, vmin, vmax):
#    mappable.set_clim(0, ncolors)
#    colorbar = f.colorbar(mappable)
#    colorbar.set_ticks(np.linspace(0.5, ncolors - 0.5, ncolors))
#    colorbar.set_ticklabels(range(vmin, vmax + 1))
#
#    return colorbar


def darken_color(color, factor):
    darkcolor = colorsys.rgb_to_hls(*color)
    darkcolor = (darkcolor[0], darkcolor[1]*factor, darkcolor[2])

    return colorsys.hls_to_rgb(*darkcolor)


def set_line_labels_by_pos(line, ax, xpos, ha, va, label, ypos=None, yshift=0):
    xdata = line.get_xdata()
    if ypos is None:
        ypos = line.get_ydata()[np.abs(xdata - xpos).argmin()]
    ax.text(
        xpos, ypos + yshift, label, color=line.get_color(),
        horizontalalignment=ha, verticalalignment=va)


def set_line_labels_by_index(
        line, ax, index, ha, va, label, xshift=0, yshift=0):
    xpos = line.get_xdata()[index]
    ypos = line.get_ydata()[index]
    ax.text(
        xpos + xshift, ypos + yshift, label, color=line.get_color(),
        horizontalalignment=ha, verticalalignment=va)
