"""Function and settings for creating plots"""

import matplotlib.pyplot as plt


def set_default_style():

    plt.rcParams['lines.linewidth'] = 1.0
    plt.rcParams['lines.markeredgewidth'] = 1.0
    plt.rcParams['lines.markersize'] = 2.5

    # Fonts and symbols
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.serif'] = 'Times New Roman'
    plt.rcParams['font.weight'] = 'normal'
    plt.rcParams['font.size'] = '8'
    plt.rcParams['text.usetex'] = False
    plt.rcParams['mathtext.rm'] = 'serif'
    plt.rcParams['mathtext.it'] = 'serif:italic'
    plt.rcParams['mathtext.fontset'] = 'stix'

    # Axes
    plt.rcParams['axes.edgecolor'] = (0.0, 0.0, 0.0)
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


def set_thin_style():

    plt.rcParams['lines.linewidth'] = 0.5
    plt.rcParams['lines.markeredgewidth'] = 0.5
    plt.rcParams['lines.markersize'] = 1.0

    # Fonts and symbols
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.serif'] = 'Times New Roman'
    plt.rcParams['font.weight'] = 'normal'
    plt.rcParams['font.size'] = '8'
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


def set_default_latex_style():

    plt.rcParams['lines.linewidth'] = 1.0
    plt.rcParams['lines.markeredgewidth'] = 1.0
    plt.rcParams['lines.markersize'] = 2.5

    # Fonts and symbols
    plt.rcParams['text.usetex'] = True
    plt.rcParams['text.latex.preamble'] = r'\usepackage{newpxtext}'
    r'\usepackage{siunitx}\n'
    r'\DeclareSIUnit\Molar{M}\n'
    r'\DeclareSIUnit\kb{\ensuremath{k_\textrm{B}}}\n'
    r'\usepackage{newpxmath}'
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.size'] = '9'

    # Axes
    plt.rcParams['axes.edgecolor'] = (0.0, 0.0, 0.0)
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
