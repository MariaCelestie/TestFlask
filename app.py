{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOAM8TjRSQcPsy7c7td7rA8",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/MariaCelestie/TestFlask/blob/main/app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0SAxqZF9r4c9",
        "outputId": "b03d99fc-2747-466c-ef13-f48760f52aac"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Requirement already satisfied: Flask in /usr/local/lib/python3.7/dist-packages (1.1.4)\n",
            "Collecting Flask\n",
            "  Downloading Flask-2.2.2-py3-none-any.whl (101 kB)\n",
            "\u001b[K     |████████████████████████████████| 101 kB 5.3 MB/s \n",
            "\u001b[?25hCollecting itsdangerous>=2.0\n",
            "  Downloading itsdangerous-2.1.2-py3-none-any.whl (15 kB)\n",
            "Requirement already satisfied: importlib-metadata>=3.6.0 in /usr/local/lib/python3.7/dist-packages (from Flask) (4.12.0)\n",
            "Collecting Werkzeug>=2.2.2\n",
            "  Downloading Werkzeug-2.2.2-py3-none-any.whl (232 kB)\n",
            "\u001b[K     |████████████████████████████████| 232 kB 40.8 MB/s \n",
            "\u001b[?25hCollecting Jinja2>=3.0\n",
            "  Downloading Jinja2-3.1.2-py3-none-any.whl (133 kB)\n",
            "\u001b[K     |████████████████████████████████| 133 kB 46.7 MB/s \n",
            "\u001b[?25hCollecting click>=8.0\n",
            "  Downloading click-8.1.3-py3-none-any.whl (96 kB)\n",
            "\u001b[K     |████████████████████████████████| 96 kB 7.5 MB/s \n",
            "\u001b[?25hRequirement already satisfied: zipp>=0.5 in /usr/local/lib/python3.7/dist-packages (from importlib-metadata>=3.6.0->Flask) (3.8.1)\n",
            "Requirement already satisfied: typing-extensions>=3.6.4 in /usr/local/lib/python3.7/dist-packages (from importlib-metadata>=3.6.0->Flask) (4.1.1)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.7/dist-packages (from Jinja2>=3.0->Flask) (2.0.1)\n",
            "Collecting MarkupSafe>=2.0\n",
            "  Downloading MarkupSafe-2.1.1-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (25 kB)\n",
            "Installing collected packages: MarkupSafe, Werkzeug, Jinja2, itsdangerous, click, Flask\n",
            "  Attempting uninstall: MarkupSafe\n",
            "    Found existing installation: MarkupSafe 2.0.1\n",
            "    Uninstalling MarkupSafe-2.0.1:\n",
            "      Successfully uninstalled MarkupSafe-2.0.1\n",
            "  Attempting uninstall: Werkzeug\n",
            "    Found existing installation: Werkzeug 1.0.1\n",
            "    Uninstalling Werkzeug-1.0.1:\n",
            "      Successfully uninstalled Werkzeug-1.0.1\n",
            "  Attempting uninstall: Jinja2\n",
            "    Found existing installation: Jinja2 2.11.3\n",
            "    Uninstalling Jinja2-2.11.3:\n",
            "      Successfully uninstalled Jinja2-2.11.3\n",
            "  Attempting uninstall: itsdangerous\n",
            "    Found existing installation: itsdangerous 1.1.0\n",
            "    Uninstalling itsdangerous-1.1.0:\n",
            "      Successfully uninstalled itsdangerous-1.1.0\n",
            "  Attempting uninstall: click\n",
            "    Found existing installation: click 7.1.2\n",
            "    Uninstalling click-7.1.2:\n",
            "      Successfully uninstalled click-7.1.2\n",
            "  Attempting uninstall: Flask\n",
            "    Found existing installation: Flask 1.1.4\n",
            "    Uninstalling Flask-1.1.4:\n",
            "      Successfully uninstalled Flask-1.1.4\n",
            "Successfully installed Flask-2.2.2 Jinja2-3.1.2 MarkupSafe-2.1.1 Werkzeug-2.2.2 click-8.1.3 itsdangerous-2.1.2\n"
          ]
        }
      ],
      "source": [
        "pip install -U Flask"
      ]
    }
  ]
}