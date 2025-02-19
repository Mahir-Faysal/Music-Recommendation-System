{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
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
      "source": [
        "# **Import libraries**"
      ],
      "metadata": {
        "id": "PzsoifFgIDD8"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install dash plotly pandas scikit-learn\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nxVeUBNtM_tc",
        "outputId": "bd8c734d-62c6-437d-c1f7-e92607b137aa"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: dash in /usr/local/lib/python3.11/dist-packages (2.18.2)\n",
            "Requirement already satisfied: plotly in /usr/local/lib/python3.11/dist-packages (5.24.1)\n",
            "Requirement already satisfied: pandas in /usr/local/lib/python3.11/dist-packages (2.2.2)\n",
            "Requirement already satisfied: scikit-learn in /usr/local/lib/python3.11/dist-packages (1.6.1)\n",
            "Requirement already satisfied: Flask<3.1,>=1.0.4 in /usr/local/lib/python3.11/dist-packages (from dash) (3.0.3)\n",
            "Requirement already satisfied: Werkzeug<3.1 in /usr/local/lib/python3.11/dist-packages (from dash) (3.0.6)\n",
            "Requirement already satisfied: dash-html-components==2.0.0 in /usr/local/lib/python3.11/dist-packages (from dash) (2.0.0)\n",
            "Requirement already satisfied: dash-core-components==2.0.0 in /usr/local/lib/python3.11/dist-packages (from dash) (2.0.0)\n",
            "Requirement already satisfied: dash-table==5.0.0 in /usr/local/lib/python3.11/dist-packages (from dash) (5.0.0)\n",
            "Requirement already satisfied: importlib-metadata in /usr/local/lib/python3.11/dist-packages (from dash) (8.6.1)\n",
            "Requirement already satisfied: typing-extensions>=4.1.1 in /usr/local/lib/python3.11/dist-packages (from dash) (4.12.2)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.11/dist-packages (from dash) (2.32.3)\n",
            "Requirement already satisfied: retrying in /usr/local/lib/python3.11/dist-packages (from dash) (1.3.4)\n",
            "Requirement already satisfied: nest-asyncio in /usr/local/lib/python3.11/dist-packages (from dash) (1.6.0)\n",
            "Requirement already satisfied: setuptools in /usr/local/lib/python3.11/dist-packages (from dash) (75.1.0)\n",
            "Requirement already satisfied: tenacity>=6.2.0 in /usr/local/lib/python3.11/dist-packages (from plotly) (9.0.0)\n",
            "Requirement already satisfied: packaging in /usr/local/lib/python3.11/dist-packages (from plotly) (24.2)\n",
            "Requirement already satisfied: numpy>=1.23.2 in /usr/local/lib/python3.11/dist-packages (from pandas) (1.26.4)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.11/dist-packages (from pandas) (2.8.2)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.11/dist-packages (from pandas) (2024.2)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.11/dist-packages (from pandas) (2025.1)\n",
            "Requirement already satisfied: scipy>=1.6.0 in /usr/local/lib/python3.11/dist-packages (from scikit-learn) (1.13.1)\n",
            "Requirement already satisfied: joblib>=1.2.0 in /usr/local/lib/python3.11/dist-packages (from scikit-learn) (1.4.2)\n",
            "Requirement already satisfied: threadpoolctl>=3.1.0 in /usr/local/lib/python3.11/dist-packages (from scikit-learn) (3.5.0)\n",
            "Requirement already satisfied: Jinja2>=3.1.2 in /usr/local/lib/python3.11/dist-packages (from Flask<3.1,>=1.0.4->dash) (3.1.5)\n",
            "Requirement already satisfied: itsdangerous>=2.1.2 in /usr/local/lib/python3.11/dist-packages (from Flask<3.1,>=1.0.4->dash) (2.2.0)\n",
            "Requirement already satisfied: click>=8.1.3 in /usr/local/lib/python3.11/dist-packages (from Flask<3.1,>=1.0.4->dash) (8.1.8)\n",
            "Requirement already satisfied: blinker>=1.6.2 in /usr/local/lib/python3.11/dist-packages (from Flask<3.1,>=1.0.4->dash) (1.9.0)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.11/dist-packages (from python-dateutil>=2.8.2->pandas) (1.17.0)\n",
            "Requirement already satisfied: MarkupSafe>=2.1.1 in /usr/local/lib/python3.11/dist-packages (from Werkzeug<3.1->dash) (3.0.2)\n",
            "Requirement already satisfied: zipp>=3.20 in /usr/local/lib/python3.11/dist-packages (from importlib-metadata->dash) (3.21.0)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests->dash) (3.4.1)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.11/dist-packages (from requests->dash) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests->dash) (2.3.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.11/dist-packages (from requests->dash) (2024.12.14)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "9nvzjBPzgB2y",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "4fd83c09-9b19-4af3-bc43-3f901526a842"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: dash in /usr/local/lib/python3.11/dist-packages (2.18.2)\n",
            "Requirement already satisfied: Flask<3.1,>=1.0.4 in /usr/local/lib/python3.11/dist-packages (from dash) (3.0.3)\n",
            "Requirement already satisfied: Werkzeug<3.1 in /usr/local/lib/python3.11/dist-packages (from dash) (3.0.6)\n",
            "Requirement already satisfied: plotly>=5.0.0 in /usr/local/lib/python3.11/dist-packages (from dash) (5.24.1)\n",
            "Requirement already satisfied: dash-html-components==2.0.0 in /usr/local/lib/python3.11/dist-packages (from dash) (2.0.0)\n",
            "Requirement already satisfied: dash-core-components==2.0.0 in /usr/local/lib/python3.11/dist-packages (from dash) (2.0.0)\n",
            "Requirement already satisfied: dash-table==5.0.0 in /usr/local/lib/python3.11/dist-packages (from dash) (5.0.0)\n",
            "Requirement already satisfied: importlib-metadata in /usr/local/lib/python3.11/dist-packages (from dash) (8.6.1)\n",
            "Requirement already satisfied: typing-extensions>=4.1.1 in /usr/local/lib/python3.11/dist-packages (from dash) (4.12.2)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.11/dist-packages (from dash) (2.32.3)\n",
            "Requirement already satisfied: retrying in /usr/local/lib/python3.11/dist-packages (from dash) (1.3.4)\n",
            "Requirement already satisfied: nest-asyncio in /usr/local/lib/python3.11/dist-packages (from dash) (1.6.0)\n",
            "Requirement already satisfied: setuptools in /usr/local/lib/python3.11/dist-packages (from dash) (75.1.0)\n",
            "Requirement already satisfied: Jinja2>=3.1.2 in /usr/local/lib/python3.11/dist-packages (from Flask<3.1,>=1.0.4->dash) (3.1.5)\n",
            "Requirement already satisfied: itsdangerous>=2.1.2 in /usr/local/lib/python3.11/dist-packages (from Flask<3.1,>=1.0.4->dash) (2.2.0)\n",
            "Requirement already satisfied: click>=8.1.3 in /usr/local/lib/python3.11/dist-packages (from Flask<3.1,>=1.0.4->dash) (8.1.8)\n",
            "Requirement already satisfied: blinker>=1.6.2 in /usr/local/lib/python3.11/dist-packages (from Flask<3.1,>=1.0.4->dash) (1.9.0)\n",
            "Requirement already satisfied: tenacity>=6.2.0 in /usr/local/lib/python3.11/dist-packages (from plotly>=5.0.0->dash) (9.0.0)\n",
            "Requirement already satisfied: packaging in /usr/local/lib/python3.11/dist-packages (from plotly>=5.0.0->dash) (24.2)\n",
            "Requirement already satisfied: MarkupSafe>=2.1.1 in /usr/local/lib/python3.11/dist-packages (from Werkzeug<3.1->dash) (3.0.2)\n",
            "Requirement already satisfied: zipp>=3.20 in /usr/local/lib/python3.11/dist-packages (from importlib-metadata->dash) (3.21.0)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests->dash) (3.4.1)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.11/dist-packages (from requests->dash) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests->dash) (2.3.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.11/dist-packages (from requests->dash) (2024.12.14)\n",
            "Requirement already satisfied: six>=1.7.0 in /usr/local/lib/python3.11/dist-packages (from retrying->dash) (1.17.0)\n",
            "Requirement already satisfied: pyngrok in /usr/local/lib/python3.11/dist-packages (7.2.3)\n",
            "Requirement already satisfied: PyYAML>=5.1 in /usr/local/lib/python3.11/dist-packages (from pyngrok) (6.0.2)\n"
          ]
        }
      ],
      "source": [
        "!pip install dash\n",
        "!pip install pyngrok"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Import additional libraries**"
      ],
      "metadata": {
        "id": "DQVroHluIRg5"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "import numpy as np\n",
        "import pandas as pd\n",
        "\n",
        "import seaborn as sns\n",
        "import plotly.express as px\n",
        "import matplotlib.pyplot as plt\n",
        "%matplotlib inline\n",
        "\n",
        "from sklearn.cluster import KMeans\n",
        "from sklearn.preprocessing import StandardScaler\n",
        "from sklearn.pipeline import Pipeline\n",
        "from sklearn.manifold import TSNE\n",
        "from sklearn.decomposition import PCA\n",
        "from sklearn.metrics import euclidean_distances\n",
        "from scipy.spatial.distance import cdist\n",
        "\n",
        "import warnings\n",
        "warnings.filterwarnings(\"ignore\")"
      ],
      "metadata": {
        "id": "lQx_9_Drrphf"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "jloqZPpwIXdB"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Load the dataset**"
      ],
      "metadata": {
        "id": "iNL2U1VGIZN3"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "data = pd.read_csv(\"/content/data.csv\")\n",
        "#genre_data = pd.read_csv('/content/data_w_genres.csv')\n",
        "year_data = pd.read_csv('/content/data_by_year.csv')"
      ],
      "metadata": {
        "id": "9yxpsx1lrs54"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Print the Dataset**"
      ],
      "metadata": {
        "id": "u93HAwgMIdjM"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "data.head()"
      ],
      "metadata": {
        "id": "Vzd6rXEvPIyY",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 504
        },
        "outputId": "ae049ebb-ec3b-4238-de45-959ec76edab8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   valence  year  acousticness  \\\n",
              "0   0.0594  1921         0.982   \n",
              "1   0.9630  1921         0.732   \n",
              "2   0.0394  1921         0.961   \n",
              "3   0.1650  1921         0.967   \n",
              "4   0.2530  1921         0.957   \n",
              "\n",
              "                                             artists  danceability  \\\n",
              "0  ['Sergei Rachmaninoff', 'James Levine', 'Berli...         0.279   \n",
              "1                                     ['Dennis Day']         0.819   \n",
              "2  ['KHP Kridhamardawa Karaton Ngayogyakarta Hadi...         0.328   \n",
              "3                                   ['Frank Parker']         0.275   \n",
              "4                                     ['Phil Regan']         0.418   \n",
              "\n",
              "   duration_ms  energy  explicit                      id  instrumentalness  \\\n",
              "0       831667   0.211         0  4BJqT0PrAfrxzMOxytFOIz          0.878000   \n",
              "1       180533   0.341         0  7xPhfUan2yNtyFG0cUWkt8          0.000000   \n",
              "2       500062   0.166         0  1o6I8BglA6ylDMrIELygv1          0.913000   \n",
              "3       210000   0.309         0  3ftBPsC5vPBKxYSee08FDH          0.000028   \n",
              "4       166693   0.193         0  4d6HGyGT8e121BsdKmw9v6          0.000002   \n",
              "\n",
              "   key  liveness  loudness  mode  \\\n",
              "0   10     0.665   -20.096     1   \n",
              "1    7     0.160   -12.441     1   \n",
              "2    3     0.101   -14.850     1   \n",
              "3    5     0.381    -9.316     1   \n",
              "4    3     0.229   -10.096     1   \n",
              "\n",
              "                                                name  popularity release_date  \\\n",
              "0  Piano Concerto No. 3 in D Minor, Op. 30: III. ...           4         1921   \n",
              "1                            Clancy Lowered the Boom           5         1921   \n",
              "2                                          Gati Bali           5         1921   \n",
              "3                                          Danny Boy           3         1921   \n",
              "4                        When Irish Eyes Are Smiling           2         1921   \n",
              "\n",
              "   speechiness    tempo  \n",
              "0       0.0366   80.954  \n",
              "1       0.4150   60.936  \n",
              "2       0.0339  110.339  \n",
              "3       0.0354  100.109  \n",
              "4       0.0380  101.665  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-6fdf0b80-3e4e-4229-ada1-4f4983a1fb18\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>valence</th>\n",
              "      <th>year</th>\n",
              "      <th>acousticness</th>\n",
              "      <th>artists</th>\n",
              "      <th>danceability</th>\n",
              "      <th>duration_ms</th>\n",
              "      <th>energy</th>\n",
              "      <th>explicit</th>\n",
              "      <th>id</th>\n",
              "      <th>instrumentalness</th>\n",
              "      <th>key</th>\n",
              "      <th>liveness</th>\n",
              "      <th>loudness</th>\n",
              "      <th>mode</th>\n",
              "      <th>name</th>\n",
              "      <th>popularity</th>\n",
              "      <th>release_date</th>\n",
              "      <th>speechiness</th>\n",
              "      <th>tempo</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>0.0594</td>\n",
              "      <td>1921</td>\n",
              "      <td>0.982</td>\n",
              "      <td>['Sergei Rachmaninoff', 'James Levine', 'Berli...</td>\n",
              "      <td>0.279</td>\n",
              "      <td>831667</td>\n",
              "      <td>0.211</td>\n",
              "      <td>0</td>\n",
              "      <td>4BJqT0PrAfrxzMOxytFOIz</td>\n",
              "      <td>0.878000</td>\n",
              "      <td>10</td>\n",
              "      <td>0.665</td>\n",
              "      <td>-20.096</td>\n",
              "      <td>1</td>\n",
              "      <td>Piano Concerto No. 3 in D Minor, Op. 30: III. ...</td>\n",
              "      <td>4</td>\n",
              "      <td>1921</td>\n",
              "      <td>0.0366</td>\n",
              "      <td>80.954</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>0.9630</td>\n",
              "      <td>1921</td>\n",
              "      <td>0.732</td>\n",
              "      <td>['Dennis Day']</td>\n",
              "      <td>0.819</td>\n",
              "      <td>180533</td>\n",
              "      <td>0.341</td>\n",
              "      <td>0</td>\n",
              "      <td>7xPhfUan2yNtyFG0cUWkt8</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>7</td>\n",
              "      <td>0.160</td>\n",
              "      <td>-12.441</td>\n",
              "      <td>1</td>\n",
              "      <td>Clancy Lowered the Boom</td>\n",
              "      <td>5</td>\n",
              "      <td>1921</td>\n",
              "      <td>0.4150</td>\n",
              "      <td>60.936</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>0.0394</td>\n",
              "      <td>1921</td>\n",
              "      <td>0.961</td>\n",
              "      <td>['KHP Kridhamardawa Karaton Ngayogyakarta Hadi...</td>\n",
              "      <td>0.328</td>\n",
              "      <td>500062</td>\n",
              "      <td>0.166</td>\n",
              "      <td>0</td>\n",
              "      <td>1o6I8BglA6ylDMrIELygv1</td>\n",
              "      <td>0.913000</td>\n",
              "      <td>3</td>\n",
              "      <td>0.101</td>\n",
              "      <td>-14.850</td>\n",
              "      <td>1</td>\n",
              "      <td>Gati Bali</td>\n",
              "      <td>5</td>\n",
              "      <td>1921</td>\n",
              "      <td>0.0339</td>\n",
              "      <td>110.339</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>0.1650</td>\n",
              "      <td>1921</td>\n",
              "      <td>0.967</td>\n",
              "      <td>['Frank Parker']</td>\n",
              "      <td>0.275</td>\n",
              "      <td>210000</td>\n",
              "      <td>0.309</td>\n",
              "      <td>0</td>\n",
              "      <td>3ftBPsC5vPBKxYSee08FDH</td>\n",
              "      <td>0.000028</td>\n",
              "      <td>5</td>\n",
              "      <td>0.381</td>\n",
              "      <td>-9.316</td>\n",
              "      <td>1</td>\n",
              "      <td>Danny Boy</td>\n",
              "      <td>3</td>\n",
              "      <td>1921</td>\n",
              "      <td>0.0354</td>\n",
              "      <td>100.109</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>0.2530</td>\n",
              "      <td>1921</td>\n",
              "      <td>0.957</td>\n",
              "      <td>['Phil Regan']</td>\n",
              "      <td>0.418</td>\n",
              "      <td>166693</td>\n",
              "      <td>0.193</td>\n",
              "      <td>0</td>\n",
              "      <td>4d6HGyGT8e121BsdKmw9v6</td>\n",
              "      <td>0.000002</td>\n",
              "      <td>3</td>\n",
              "      <td>0.229</td>\n",
              "      <td>-10.096</td>\n",
              "      <td>1</td>\n",
              "      <td>When Irish Eyes Are Smiling</td>\n",
              "      <td>2</td>\n",
              "      <td>1921</td>\n",
              "      <td>0.0380</td>\n",
              "      <td>101.665</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-6fdf0b80-3e4e-4229-ada1-4f4983a1fb18')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-6fdf0b80-3e4e-4229-ada1-4f4983a1fb18 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-6fdf0b80-3e4e-4229-ada1-4f4983a1fb18');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-fa4f35d0-d8c2-4339-ab5a-914453ffcdbf\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-fa4f35d0-d8c2-4339-ab5a-914453ffcdbf')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-fa4f35d0-d8c2-4339-ab5a-914453ffcdbf button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "data"
            }
          },
          "metadata": {},
          "execution_count": 15
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Data Preprocessing : Handeling Missing values**"
      ],
      "metadata": {
        "id": "tTRV5PJSIhGY"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "missing_values = data.isnull().sum()\n",
        "\n",
        "missing_values_df = missing_values.reset_index()\n",
        "\n",
        "missing_values_df.columns = ['Column', 'Missing Values']\n",
        "\n",
        "print(missing_values_df)\n"
      ],
      "metadata": {
        "id": "81WjBHSDkds_",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "19bbdb10-adc0-4cd1-9fe6-f3b511d8a260"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "              Column  Missing Values\n",
            "0            valence               0\n",
            "1               year               0\n",
            "2       acousticness               0\n",
            "3            artists               0\n",
            "4       danceability               0\n",
            "5        duration_ms               0\n",
            "6             energy               0\n",
            "7           explicit               0\n",
            "8                 id               0\n",
            "9   instrumentalness               0\n",
            "10               key               0\n",
            "11          liveness               0\n",
            "12          loudness               0\n",
            "13              mode               0\n",
            "14              name               0\n",
            "15        popularity               0\n",
            "16      release_date               0\n",
            "17       speechiness               0\n",
            "18             tempo               0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "data.duplicated().sum()"
      ],
      "metadata": {
        "id": "ROVyFdA5RVYR",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "06af4cb9-b6f4-427f-f2c6-66196f50862d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0"
            ]
          },
          "metadata": {},
          "execution_count": 17
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Count the numbers of columns and rows**"
      ],
      "metadata": {
        "id": "ZbfMIfUFIo5g"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "num_rows = len(data)\n",
        "\n",
        "num_columns = len(data.columns)\n",
        "\n",
        "print(f'Number of Rows: {num_rows}')\n",
        "print(f'Number of Columns: {num_columns}')\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KBekyN8gwEDC",
        "outputId": "9fca4394-781e-47b4-e68e-a89f09faf854"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Number of Rows: 170653\n",
            "Number of Columns: 19\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Data Visualization:Feature Correlation map**"
      ],
      "metadata": {
        "id": "Pln30RptIuvo"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from yellowbrick.target import FeatureCorrelation\n",
        "\n",
        "feature_names = ['acousticness', 'danceability', 'energy', 'instrumentalness',\n",
        "       'liveness', 'loudness', 'speechiness', 'tempo', 'valence','duration_ms','explicit','key','mode','popularity']\n",
        "\n",
        "X, y = data[feature_names], data['year']\n",
        "\n",
        "features = np.array(feature_names)\n",
        "\n",
        "visualizer = FeatureCorrelation(labels=features)\n",
        "\n",
        "plt.rcParams['figure.figsize']=(8,6)\n",
        "visualizer.fit(X, y)\n",
        "visualizer.show()"
      ],
      "metadata": {
        "id": "g94v1C-SYmy6",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 579
        },
        "outputId": "22ccdb78-4b8a-4764-b418-5162ee50f945"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 800x600 with 1 Axes>"
            ],
            "image/png": "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YcIEy/bBgwezZs0ahgwZwk8//YSXlxdffPGF1THS8/oZMWIEVapU4eeff6Z3796Eh4db3tQsXLgQFxcXXn/9dTZv3oynp+c9vWzYsCHnzp2757clK1as4OWXX6Zs2bKcPHmSrl27UqpUKcLDw1m8eDF+fn707NnTEvRvW7BgARUrVuSXX36hZMmS95wvPDyc4cOH89Zbb7Fy5Uq+++47smTJQseOHUlISLAaO378eLy9vVm0aBGffvopv/76K6NGjbrnmPDPm/y2bduyc+dOBg0axNKlSwkODqZ///6Eh4ffdx+RJ8IQEXkEoaGhRtWqVf91XGBgoPHWW29Zrdu/f7/h6upqLFmyxDAMw7hx44Zx6NAhIykpyTLm8OHDhqurq7FixQrDMAwjISHBcHV1NSZMmGAZM2HCBMPV1dVISEiwOr6rq6sxevRowzAMY9u2bYarq6sxYsQIqzEdOnQw6tSpYyQnJ1vWXbhwwShXrpwxZcoUwzAM45133jE6dOhgtd/Zs2eNAwcOPPB6Bw8ebPj6+lpdy/bt240+ffoYFy9eNHbt2mW4uroay5cvt9pvxowZhqurq3HmzBnDMAyjdevWxquvvmpcuXLFMiY6OtpwdXU13n//fat9P/30U8PT09O4du2aZV1CQoJRtWpVo3///lZ92LBhg2EYj6/n9erVM9555x2rei5cuGCUKVPGmDx5smEYhvHTTz8Zrq6uxg8//GAZk5SUZLz66qvG559/ft8+JiYmGh4eHsacOXMMwzCM69evG2XLljW++uor44033rCM6927t9G+ffv71tazZ0+jdu3a/9q/d955x6hXr9596zAMw5g/f77h6upqHD582LLu1q1bRqVKlSzHT0xMNLy8vIy+ffta7btq1SrD1dXV2Llzp2EY//zcuLq6Gn/99ZdlzI0bNwx3d3djyJAhhmEYxldffWW4ubkZJ06csDpWcHCw8b///e+h19KmTRsjJCTEMAzDiI+PN1599VVj1KhRVmOGDBliuLq6Gtu2bTMMI32vn7t/jvz9/Y333nvPsly1alUjNDT0gb1MSkoyqlSpYgwbNsyy7vr160a5cuWMr776ynLuw4cPGzdu3LCqx9XV1fj6668t61xdXY3GjRtbHf/2a+329+rq1avGwYMHrcZs2LDBcHV1NXbv3m11bZ9++qnVuE8++cSoWLGikZqa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E9mzZ+fHH39k1KhR2Nvb4+Pjw48//mj1jyQ5OTnx3nvv8dlnn3H06FHy58/PiBEjcHV1Bf757Mns2bMZM2YMnTt3Jj4+noIFC9K2bVvefffddNX+2WefMXDgQMvrr2bNmgwYMICOHTtaxjzK6+dBOnXqxLBhw2jZsiXDhw/n9ddfv++40qVL8+qrr7Jv3z569uxpte3tt9/m6NGjDBw4EBsbG2rXrs2oUaNYsGAB48eP58MPP+T7779PUz0DBw6kf//+tG3blly5ctGyZUs6depEbGwsM2bMwM7OzvKbntuPgf3888/JkiULwcHB99R2m729PTNnzmTMmDH07t2bq1evkjdvXoKCgqym8Yg8aTbG4/i9o4iIiPyrfv36sWnTJn7//feMLkVEngGaWiMiIiIiYkIK8iIiIiIiJqSpNSIiIiIiJqQ78iIiIiIiJqQgLyIiIiJiQgryIiIiIiImpOfIP2f+/PNPDMMga9asGV2KiIiIiNxHUlISNjY2eHp6PnSc7sg/ZwzDeCz/ZPnjqCMxMTFT1GIG6lf6qF/pp56lj/qVPupX+qln6fOs9SuteU135J8zt+/Eu7u7Z2gd8fHxREVF8dJLL1n9M+dyf+pX+qhf6aeepY/6lT7qV/qpZ+nzrPUrMjIyTeN0R15ERERExIQU5EVERERETEhBXkRERETEhBTkRURERERMSEFeRERERMSEFORFRERERExIQV5ERERExIQU5EVERERETEhBXkRERETEhBTkRURERERMSEFeRERERMSEFORFRERERExIQV5ERERExIQU5EVERERETEhBXkRERETEhBTkRURERERMSEFeRERERMSEFORFRERERExIQV5ERERExITsMroAERHJHCrN3g/sz+gyTEb9Sh/1K/3Us/R5cv1KGdvmiR37UemOvIiIiIiICSnIi4iIiIiYkIK8iIiIiIgJKciLiIiIiJiQgryIiIiIiAkpyIuIiIiImJCC/BNy6tQp3NzcOHLkyCPtHxYWRuvWrR9zVSIiIiLyrFCQz6S6du3KrFmzLMvffvstycnJGViRiIiIiGQmCvImcPnyZUaOHElKSkpGlyIiIiIimcQzH+RvT3H57bffCAoKonz58rRu3ZoLFy4AsGPHDpo1a4anpyd+fn6MGzeO1NRUAPr168dHH33E4MGD8fLyonLlysyePdtybH9/f+bMmWNZ3rhxI25ubvet4+TJk3To0AFfX198fX354IMPuHbtmlWNs2fPplKlSixbtoyJEyfSrFkzLl68SI0aNTAMA29vbyZNmsQrr7zCwYMHrY5ft25d5s2b91h7JyIiIiKZ1zMf5G+bNWsW33zzDZs2bcLGxoZBgwZx8eJFOnToQHBwMBEREUybNo2FCxdahfNff/2VV155hW3btjF06FAGDx7MgQMH0n3+/v37ky9fPjZt2sQvv/zCsWPHCAsLsxrzxx9/sHbtWoKCgizr8ubNy4wZM4B/3nR069YNHx8fli5dahkTFRVFTEwMgYGB6a5LRERERMzpuQnyrVq1In/+/OTKlYt27dqxceNGli5dSqFChXjrrbewt7enbNmyBAcH88svv1j2K1SoEM2aNcPe3p66detSpkwZ1q1bl+7zT5s2jUGDBmFvb4+LiwvVq1dn7969VmNCQkJwdnbGxsbmoccKCQlh+fLlGIYBwMqVK6lZsya5cuVKd10iIiIiYk7PTZAvWbKk5evChQuTmJjIyZMnKV26tNW44sWLc/r06fvuB/8E+/Pnz6f7/Hv37qVdu3Z4eXnh7u7O9OnTSUxMvOfYaREQEEBsbCw7duwAYNWqVTRs2DDdNYmIiIiIeT03Qf72vHfAcif77iB92513xO/+gKlhGA+8Y37nOe509epVOnbsiJeXFxs3biQyMpKOHTveM87W1vbhF/H/OTs7U6dOHZYuXcrx48eJiYmhdu3aadpXRERERJ4Nz02QP3nypOXr06dP4+joSMmSJTl69KjVuKNHj1K0aFHLcnR0tNX2M2fOUKBAAQDs7e1JSEi47znuPuaNGzfo0KEDzs7OAOzfv/8/XU9ISAirVq1i2bJl1KtXDwcHh/90PBERERExl+cmyM+ZM4eLFy9y5coVvvvuO2rWrMnrr79OdHQ08+bNIzk5mT179vDzzz/TuHFjy36nT58mPDycpKQkVq1axYEDB6hVqxYAJUqUYP369SQkJHDixAmrD6DeqVChQmTJkoU///yT+Ph4Zs6cycWLF7l48WKang3v6OgIwLFjx4iPjwegatWq2Nra8u2332pajYiIiMhz6LkJ8o0aNaJt27ZUr14dgIEDB1K4cGEmTZrEvHnz8PHxoU+fPvTo0YOQkBDLfjVq1ODPP/+kcuXKDBgwgEGDBuHq6gpAz549uXz5Mr6+voSGhtKhQ4f7njt//vx88MEHfPzxx9SuXZurV68yZswYEhMTadWq1b/WXqZMGTw9PXnzzTctT9SxtbWlYcOGODk54evr+x+7IyIiIiJmY2PcnjD+jDp16hR16tRhxYoV93yw9d/069ePW7duMW7cuCdU3X8TGhpKwYIF6dmzZ5r3iYyMBMDd3f0JVZU28fHxREVFUaZMGZycnDK0FjNQv9JH/Uq/+Ph4cgz4KaPLEBHJtFLGtnlq50prXrN7GsXI47dmzRrWr1/PsmXLMroUEREREckACvImFBgYSGJiIqNGjeLFF1/M6HJEREREJAM880G+SJEiHDx48JH2HTFixGOu5vH49ddfM7oEEREREclgz82HXUVEREREniUK8iIiIiIiJvTMT60REZG0+aNVWT3pJ430ZKT0Ub/STz1Ln+e1X7ojLyIiIiJiQgryIiIiIiImpCAvIiIiImJCCvIiIiIiIiakIC8iIiIiYkJ6ao2IyDPItvcP6d7nj1Zln0AlIiLypOiOvIiIiIiICSnIi4iIiIiYkIK8iIiIiIgJKciLiIiIiJiQgryIiIiIiAkpyIuIiIiImJCCfCZ369Yt3NzciIiIyOhSRERERCQTUZAXERERETEhBXkRERERERNSkH8M3NzcWL58OU2aNKF8+fJ07NiRmJgYOnTogKenJ02aNOHUqVOW8atXr6ZRo0Z4eHjg7+/P999/b9kWHx/PBx98gLe3N3Xr1mXt2rVW57py5Qoffvghfn5+eHp60qVLF86dO/fUrlVEREREMgcF+cdk7ty5TJ06lSVLlrB161beffddevfuzaZNm0hJSeHbb78F4MCBA/To0YPu3buzfft2hg0bxtixY9mwYQMAU6dO5cCBAyxfvpyFCxfy66+/Wp2nX79+JCQksHz5cjZt2oSTkxMfffTRU79eEREREclYCvKPSVBQEPny5aNEiRKUKlUKd3d3ypYti7OzM5UqVeL48eMA/PTTT1SpUoW6deuSNWtWqlSpQq1atVixYgUAq1atomXLluTPn5/cuXPz7rvvWs5x6dIl1q1bR69evciVKxfOzs58+OGH/P7771y4cCEjLltEREREMohdRhfwrChYsKDlawcHB/Lnz2+1nJiYCMCpU6coXbq01b7Fixdn165dAMTExFCkSBHLthIlSli+jo6OBiAkJMRqf1tbW86ePcuLL774WK5FRERERDI/BfnHxMbGxmo5S5b7/7LjdqB/0P5JSUmkpKRY1huGYfna0dERgI0bN5InT57/VK+IiIiImJum1jxlxYoV4+jRo1brjh49StGiRQHIly8fZ8+etWw7fPiw5evChQuTJUsWDh48aFmXlJSkD7uKiIiIPIcU5J+yRo0a8fvvv7Nu3TqSk5PZtGkT69evt0yXqV69OvPnz+fChQtcvnyZ6dOnW/bNkSMH9evXZ8yYMcTExJCQkMAXX3xB+/btre7ci4iIiMizT0H+KfP09LQ8qcbHx4dRo0YxZswYKlWqBECfPn0oWbIkgYGBvPnmmzRu3Bg7u/+bATVgwACKFy9OUFAQ1atX5/Dhw4SFhd0ztUdEREREnm2aI/8Y3DnVBWD+/PlWyx9++KHVcuPGjWncuPF9j+Xs7MyECROs1u3bt8/yde7cuRk7dux/KVdEREREngG6Iy8iIiIiYkIK8iIiIiIiJqQgLyIiIiJiQgryIiIiIiImpCAvIiIiImJCCvIiIiIiIiakx0+KiDyDUsa2Sdf4+Ph4oqKinlA1IiLyJOiOvIiIiIiICSnIi4iIiIiYkIK8iIiIiIgJKciLiIiIiJiQgryIiIiIiAkpyIuICACVZu8nx4CfMroMERFJIwV5ERERERETUpAXERERETEhBXkRERERERNSkBcRERERMSEFeRERERERE1KQFxERERExIQX5DHLq1Cnc3Nw4cuRIRpciIiIiIiakIC8iIiIiYkIK8iIiIiIiJqQgn0mcPn2aqlWr8tNPP3H69Gk6d+6Mr68vPj4+9O3bl7i4OG7evImXlxdr16612rdt27Z88cUXGVS5iIiIiGQEBflM4MaNG3Tu3JnmzZvTpEkTunbtSsGCBVm/fj2//vor586dY+TIkWTLlo2AgACWLl1q2Tc2Npbt27fTqFGjDLwCEREREXnaFOQzmGEYfPjhh7zyyiv06NGDyMhI/v77b/r06UO2bNl44YUXeP/991myZAmGYRAcHMzatWuJi4sDYM2aNbi6uvLSSy9l8JWIiIiIyNNkl9EFPO/Gjx/Pli1b+P333wGIjo4mJSUFX19fq3EpKSnExsbi6+uLi4sLq1evJiQkhFWrVtGwYcOMKF1EREREMpDuyGewmJgYihUrxqRJkwBwcHDAycmJyMhIqz/79+/HxcUFGxsbGjVqxNKlS4mLiyMiIoIGDRpk8FWIiIiIyNOmO/IZbPjw4SQnJ9OsWTPq1KlDsWLFiI+PJzo6mqJFiwIQFxdHUlISefLkASA4OJgZM2awaNEiKlSoQP78+TPyEkREREQkA+iOfAbLkiULZcqUoXPnzoSGhlKoUCE8PT0ZNmwYly9f5tq1awwcOJC+ffta9ilVqhRlypThyy+/1LQaERERkeeUgnwm0alTJ1xcXBg+fDhjx47FMAzq1KnDa6+9RkpKCiNGjLAaHxISQmJiIgEBARlUsYiIiIhkJE2tySBFihTh4MGDlmU7OzsWLlxoWf7qq68euv+lS5cIDAwkR44cT6xGEREREcm8FORN6K+//uKHH37ghx9+yOhSRERERCSDKMibTIcOHTh48CChoaG88sorGV2OiIiIiGQQBXmTmTFjRkaXICIiIiKZgD7sKiIiIiJiQgryIiIiIiImpKk1IiICwB+tylKmTJmMLkNERNJId+RFRERERExIQV5ERERExIQU5EVERERETEhBXkRERETEhBTkRURERERMSE+tERERACrN3g/sz+gyTObB/UoZ2+Yp1iEizyPdkRcRERERMSEFeRERERERE1KQFxERERExIQV5ERERERETUpAXERERETEhBXkRERERERNSkM9A/fr1o1evXgCEhYXRunXrf90nPDwcf3//J12aiIiIiGRyCvKZRNeuXZk1a9a/jgsJCWHt2rWW5YULF3L58uUnWZqIiIiIZEIK8iaWkpLCiBEjiI2NzehSREREROQpU5BPo9OnT9O5c2d8fX3x8fGhb9++xMXF0bt3b7p3724Zt2nTJry8vDhz5gyLFi3itddeY8GCBVSvXh0PDw8+/fRTkpOT7zn+xIkTadasmWV58+bNNGrUCA8PD4KDg9m6dSsAixYtolq1agBUqlSJ69evExwczKRJk55wB0REREQkM1GQTwPDMOjatSsFCxZk/fr1/Prrr5w7d46RI0fy8ccfExERwbZt20hKSuLzzz+nd+/eFCpUCIBz584RGRnJypUr+emnn1i7di0//vjjQ8937tw53n//fTp37sz27dtp27Yt7733HleuXLEat3jxYst/u3Xr9kSuXUREREQyJwX5NIiMjOTvv/+mT58+ZMuWjRdeeIH333+fJUuW4OLiQmhoKMOGDeO7774jd+7ctGrVyrLvrVu36Nmz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vOjduzfLli3j0KFDHDhw4KnWISIiIiIZK1MH+QoVKpArVy6mT59OYmIiO3bsYN26dQAUL16cGzdusHnzZhITE/nqq68wDOOBx3JxccHJyYm//vqLW7dusXTpUqKiooiLi+PGjRvAP28OTpw4QVxcnNW+7u7ulC5dmrFjxxIfH8+5c+eYMmUKQUFBT31u+rBhwwgNDeXy5csYhsG+fftITU2lUKFCT7UOEREREclYmTrIOzo6MnnyZNasWYOPjw+TJk2iffv2AJQrV4527drRq1cvatSogZ2dHZ6eng88lp2dHYMGDWLatGlUrVqV7du3M3HiRAoUKEC9evUAaNGiBaNGjaJPnz5W+9rY2BAWFsb58+epVasWzZo1o0KFCnz66adP7uIfoHfv3mTJkoWAgAC8vLwYNmwYY8eOtfyWQURERESeDzbGw25jyzMnMjIS+Oe3DBkpPj6eqKgoypQpg5OTU4bWYgbqV/qoX+kXHx9PjgE/Zci5U8a2yZDz/hd6jaWP+pV+6ln6PGv9Smtey9R35EVERERE5P4y9eMnnwWdO3fm999/f+D2IUOGEBIS8vQKEhEREZFngoL8EzZ16tSMLkFEREREnkGaWiMiIiIiYkK6Iy8iIgD80arsM/NBMRGR54HuyIuIiIiImJCCvIiIiIiICSnIi4iIiIiYkIK8iIiIiIgJKciLiIiIiJiQnlojIvIMs+39Q5rH/tGq7BOsREREHjfdkRcRERERMSEFeRERERERE1KQFxERERExIQV5ERERERETUpAXERERETEhBXkRERERERNSkH8MFi1aRLVq1TK6DBERERF5jijIi4iIiIiYkIK8iIiIiIgJKcjfoWnTpkyaNMlq3dChQ+nQoQORkZG0atUKb29vqlatysCBA0lKSrrvcQ4cOEDbtm3x9vamcuXKDB061DJ20aJFNGrUiPDwcPz9/fH09KRXr16W7SkpKYwZM4Zq1arh4+NDjx49uHLlCgCpqalMmDCBunXrUqFCBd544w127tz55BoiIiIiIpmWgvwdAgMDWb16tdW6NWvWEBQURK9evahcuTIREREsXLiQdevWMXfu3HuOcfPmTd555x2qVq3Kli1bWLBgAREREcyYMcMy5vTp0+zdu5dly5Yxf/58Vq9ezapVqwD44YcfWLVqFfPmzWP9+vXcvHmTIUOGAPDdd9+xfPly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Ghr6yMd+4403GDNmDDt37qRAgQJMmjQJW1tb4J8n5QwZMoRatWqRLVs26taty4cffvi4LktERERETEJB/hF9/PHHfPzxx5blWbNm3XdckyZNaNKkiWW5dOnSHDx40GrM77//brX8wgsv8O233973eCVKlLB6tKWIiIiIPJ80tUZERERExIQU5EVERERETEhTazKZtWvXZnQJIiIiImICuiMvIiIiImJCCvIiIiIiIiakqTUiIgLAH63KUqZMGZycnDK6FBERSQPdkRcRERERMSEFeRERERERE1KQFxERERExIQV5ERERERETUpAXERERETEhPbVGROT/s+39Q0aXkKH+aFU2o0sQEZF00B15ERERERETUpAXERERETEhBXkRERERERNSkBcRERERMSEFeRERERERE1KQFxERERExIQX5dPD392fOnDn33bZ9+3bc3d1JTEx8ylWJiIiIyPNIz5F/THx8fIiMjMzoMkRERETkOaE78iIiIiIiJpSpg/y0adOoXbs2FSpUICAggMWLFxMREcGrr77KunXrqFOnDuXLl6dbt27cuHHDst+KFSsIDg7Gw8ODOnXqMG/ePMu21NRUJkyYQN26dalQoQJvvPEGO3futGy/fPky3bt3p2LFivj5+fHFF19gGIZl+40bN+jevTseHh7Url2biIgIACIiInBzc+PWrVsAuLm5sXLlSlq2bImHhwcNGzZk//79luNs3bqV5s2b4+npSfXq1Zk8ebJl27Fjx2jXrh3e3t74+PjQrVs3YmNjAdi9ezfNmjXD09MTX19fPvnkExISEh5z50VEREQks8u0QX7Xrl18//33/Pjjj/z1118MGDCAQYMGcenSJZKTkwkPD2fRokWsWrWKo0eP8uWXXwIQGRnJJ598Qp8+fdi5cycjR45kxIgR7Nq1C4DvvvuO5cuXM336dLZv305ISAhdunQhPj4egP79+wOwYcMG5s6dy5IlS1iwYIGlroULF/LOO+8QERGBt7c3Q4cOfeA1TJ8+nWHDhrF161by5cvHuHHjAIiJiaFr1660bNmSHTt2MH36dObOncvSpUsBGDJkCF5eXmzbto3Vq1eTnJzMlClTAOjbty9NmzZl586dLF26lIMHD1q9URERERGR50OmDfLXr18nS5YsODo6YmNjg5+fHzt37uSFF14AoEOHDuTKlYv8+fPTokUL1q9fD8CiRYuoVasWfn5+2Nra4u3tzeuvv87ixYuBf4J4u3btKFGiBPb29rRp04acOXOyfv16YmNjWbduHZ07d8bZ2ZkiRYowbtw4ypQpY6nL39+f8uXL4+DgQL169Th27NgDryE4OJhSpUqRLVs2/P39OXLkCADLli3j5ZdfJiQkBFtbW9zc3GjRooWlxmvXruHo6IidnR25cuUiLCyMjz/+2LLNycmJLFmykC9fPubPn0/btm0fe/9FREREJHPLtB92rVKlCmXLlsXf358qVapQo0YNgoODLdtLlSpl+bpQoUKcP38egJMnT7J161bc3d0t2w3DwM/Pz7J92LBhfP7555btqampnD17llOnTpGamkqRIkUs2zw9Pa3qunObg4MDSUlJD7yGO8dmy5bNMu3m5MmTREZG3lNjyZIlAejWrRt9+vQhPDwcPz8/GjRoQPny5QH44IMP+Pjjj5kxYwZ+fn4EBwdTunTpB9YgIiIiIs+mTBvk7e3tmTp1KgcOHGDNmjX8+OOPfPPNN4SGhgKQkpJiNd7GxgYAR0dHWrZsyYABA+57XEdHR4YOHUpAQMA92/bt2wf8E+wf5PZ50uJBYx0dHalZsyZTp0697/ZatWqxfv16NmzYwJo1a2jdujV9+/aldevWNG3alLp167J27VrWrFlDSEgI48aNo27dummuS0RERETML9NOrUlKSiIuLo5XXnmF9957j/DwcGxsbCwB/uTJk5axp0+fJn/+/AAUK1aMgwcPWh0rJibGsl/RokXv2X7q1CkAChcuTJYsWaymy2zbto21a9c+1msrVqwYhw4dsvoQ7YULFyzPoI+NjSV79uzUr1+fsWPH8tlnn1nmwcfGxpInTx7eeOMNwsLC6NSpEwsXLnys9YmIiIhI5pdpg/w333zDu+++S0xMDABHjhzh6tWrnD17FoCZM2dy/fp1YmJimDdvHrVr1wbgzTffZNeuXfz0008kJiYSFRVF06ZN+e233wBo0aKF5QO0KSkprFixggYNGnDmzBly585NnTp1mDx5MleuXOHMmTMMGDCAc+fOPdZrCwoK4sqVK4SFhZGQkEB0dDTt27fnu+++IyEhwfKEnuTkZBISEti3bx/FihUjJiYGf39/Nm/eTGpqKtevX+fQoUMUK1bssdYnIiIiIplfpp1a87///Y8zZ84QEhJCQkICBQsW5MMPP7SE1jp16hASEsL58+epWbMm3bt3B6B06dKMHTuWCRMm8Nlnn5EvXz46dOhA/fr1gX+C/tmzZ+nWrRtxcXGUKlWKSZMmUahQIQCGDx/OJ598Qu3atXF2diYkJITmzZs/1mvLkycPYWFhjBo1iqlTp+Li4kJwcDDt27fH1taWL7/8klGjRjFw4EAcHR3x9vbm008/JX/+/AwbNoxhw4Zx5swZnJ2dqVGjhuXaRUREROT5YWPcOb/DBCIiInj77bfZs2cPDg4OGV2O6dz+12fv/KBtRoiPjycqKooyZcrg5OSUobWYgfqVPo/aL9vePzzBqjK/P1qV1WssjfQzmT7qV/qpZ+nzrPUrrXkt006tERERERGRB1OQFxERERExoUw7R/5BfH1973nqjIiIiIjI80Z35EVERERETEhBXkRERETEhEw3tUZE5ElJGdsmo0vIMLef+CAiIuahO/IiIiIiIiakIC8iIiIiYkIK8iIiIiIiJqQgLyIiIiJiQgryIiIiIiImpKfWiIgIAJVm7wf2Z3QZJqN+pU/G9+t5fjqVPHt0R15ERERExIQU5EVERERETEhBXkRERETEhBTkRURERERMSEFeRERERMSEFORFREREREzouQvyp06dws3NjSNHjjz2Yzdr1oyJEyc+9uOKiIiIiNztuQvyIiIiIiLPAgV5ERERERETeq6D/NWrV+nbty9+fn54enrSsWNHTp06BUBERARubm7cunXLMr5Xr17069fPsjx58mT8/Pzw9fVl8uTJVsfu168fQ4YMYfjw4VSqVInKlSvz9ddfW7ZfuXKFDz/80HLuLl26cO7cOQBSU1MZMWIEfn5+eHh40KhRIzZt2gTAzZs3CQ0NpUqVKnh6etKiRQv27t37xHokIiIiIpnTcx3k+/fvz4ULF1iyZAmbNm3C0dGRnj17pmnfzZs3M23aNL788ks2btyIYRgcOnTIasyyZct45ZVX+P333+nTpw/jxo3j/PnzwD9BPyEhgeXLl7Np0yacnJz46KOPAFi+fDlbtmxhyZIl7Ny5k7Zt2xIaGkpSUhLfffcdFy9eZNWqVURERFC9enUGDBjwWPsiIiIiIpnfcxvkr169yqpVq+jZsycuLi44OzvTvXt3IiMjiY6O/tf9V61aRY0aNahYsSIODg506tQJe3t7qzFFihShcePGZM2alfr165OSksLx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yJ07NwcPHrQaf+rUqTQdt1ixYhw6dMhqPv2FCxdITEwEIDY2luzZs1O/fn3Gjh3LZ599ZpkHHxsbS548eXjjjTcICwujU6dOLFy48HFcroiIiIiYhIJ8GgQGBjJjxgwMw6BSpUqW9S1atGDKlCkcOXKEpKQkZs6cyZtvvsnNmzf/9ZhBQUFcuXKFsLAwEhISiI6Opn379nz33XckJCQQEBDA4sWLSU5OJiEhgX379lGsWDFiYmLw9/dn8+bNpKamcv36dQ4dOkSxYsWeZAtEREREJJNRkE+DwMBAduzYQWBgILa2tpb1Xbt2pXr16rRq1QpfX19WrVrF119/TbZs2f71mHny5CEsLIw1a9bg4+ND69atqV27Nu3bt8fR0ZEvv/ySmTNn4u3tTa1atYiJieHTTz+lQIECDBs2jGHDhuHp6UlgYCDZs2ene/fuT7IFIiIiIpLJaI78/1ekSBHLNJm7p8uUK1funnUADg4ODBw4kIEDB973mHfv06RJE5o0aWJZrly5MosWLbrvvlWqVOHnn3++77b69etbpviIiIiIyPNJd+RFRERERExIQV5ERERExIQU5EVERERETEhBXkRERETEhBTkRURERERMSE+tERExmZSxbR77MePj44mKinrsxxURkSdHd+RFRERERExIQV5ERERExIQU5EVERERETEhBXkRERETEhBTkRURERERMSE+tEZGnxrb3D0/5jPuf8vnM7Y9WZTO6BBERSQfdkRcRERERMSEFeRERERERE1KQFxERERExIQV5ERERERETUpAXERERETEhBXkRERERERNKV5A/ffo07u7uHDt27EnVY2oRERG4ublx69atjC5FRERERJ5x6QryhQsXJjIykpIlS/6nk3777bckJyf/p2M8Lfv27WPLli0ZXYaIiIiIiJWnPrXm8uXLjBw5kpSUlKd96kfy008/KciLiIiISKaTriB/6tQp3NzcOHLkCP7+/ixYsICOHTvi6elJ3bp12bx5MwCpqamMGDECPz8/PDw8aNSoEZs2beLixYvUqFEDwzDw9vZm0aJFLFq0iAYNGjBixAg8PDw4d+4cbdq0YcyYMZbzHjlyBDc3N06dOgWAv78/c+bMoU2bNlSoUIEWLVpw9uxZevfujaenJwEBAezdu9ey/9atW2nevDmenp5Ur16dyZMnW7ZNnDiRLl268PXXX1OtWjV8fHwYOnQoAEOGDGH27Nl88803vPbaawCcPHmSDh064Ovri6+vLx988AHXrl27b7/c3NxYuXIlLVu2xMPDg4YNG7J////9S5MPq+vYsWO0a9cOb29vfHx86NatG7GxsQDs3r2bZs2a4enpia+vL5988gkJCQnp+VaKiIiIiMn9pzvyM2bMoFu3bkRERFCpUiU+//xzAJYvX86WLVtYsmQJO3fupG3btoSGhpIrVy5mzJgBwI4dO2jSpAkA58+fx8HBge3bt5M/f/40nXv27NkMHjyYNWvWcOrUKd566y2aNGnCtm3bKFq0KJMmTQIgJiaGrl270rJlS3bs2MH06dOZO3cuS5cutRxr165dJCcns27dOiZMmMAPP/zAnj17GDBgAD4+PrRv355Vq1YB0L9/f/Lly8emTZv45ZdfOHbsGGFhYQ+sc/r06QwbNoytW7eSL18+xo0bl6a6hgwZgpeXF9u2bWP16tUkJyczZcoUAPr27UvTpk3ZuXMnS5cu5eDBg8ybNy/N3zcRERERMT+7/7Jz7dq1KV++PAABAQGEh4eTmprKtWvXsLOzI1u2bNja2vLGG2/QuHFjsmS5//uG69ev8+6775I1a9Y0n7tWrVqWufrly5fnxo0bVKtWDQA/Pz/mzp0LwLJly3j55ZcJCQkB/rlL3qJFCxYvXkzDhg0BsLW1pVOnTmTJkoUqVarg4uLCkSNHLNd2p2nTpmFjY4O9vT0uLi5Ur16dXbt2PbDO4OBgSpUqBfzzm4Tbb2T+ra5r167h6OiInZ0duXLlIiwszNK/a9eu4eTkRJYsWciXLx/z589/YG9FRERE5Nn0n4J8kSJFLF87OjqSkpJCUlISQUFBLF68mBo1alCtWjVq1apFUFDQA8Nmzpw5cXZ2Tte5CxQoYPnawcHBan8HBwcSExOBf6bCREZG4u7ubtluGIbVB3YLFSpkVVu2bNkeOFVl7969jB07loMHD5KUlERKSgrlypV7YJ139ihbtmyWJ9r8W13dunWjT58+hIeH4+fnR4MGDSxvLD744AM+/vhjZsyYgZ+fH8HBwZQuXfoh3RIRERGRZ81/uo37oGCeO3du5s+fz1dffUXRokWZMGECrVu3fuCTauzsHv5+IjU19V/P/aBaHB0dqVmzJpGRkZY/e/futZpak9a72VevXqVjx454eXmxceNGIiMj6dix40P3sbGxeaS6atWqxfr16+nWrRuXLl2idevWzJo1C4CmTZuyfv163nrrLQ4fPkxISAirV69O0zWIiIiIyLPhiczHuHXrFjdv3sTLy4vevXuzbNkyDh06xIEDB9K0v729vdUd8ZMnTz5yLcWKFePQoUMYhmFZd+HCBcsd+/Q4evQoN27coEOHDpbfANz54dXHWVdsbCzZs2enfv36jB07ls8++8wyDz42NpY8efLwxhtvEBYWRqdOnVi4cOEj1SEiIiIi5vREgvywYcMIDQ3l8uXLGIbBvn37SE1NpVChQjg6OgL/PJUlPj7+vvuXKFGCrVu3cvXqVS5cuGCZ7/4ogoKCuHLlCmFhYSQkJBAdHU379u357rvv0rS/g4MDp06d4urVq5YpOH/++Sfx8fHMnDmTixcvcvHixXQ/F/9hdSUkJBAQEMDixYtJTk4mISGBffv2UaxYMWJiYvD392fz5s2kpqZy/fp1Dh06RLFixR6lPSIiIiJiUk8kyPfu3ZssWbIQEBCAl5cXw4YNY+zYsbi4uFCmTBk8PT158803mTNnzn3379ChAzly5KBGjRq0b9+etm3bPnItefLkISwsjDVr1uDj40Pr1q2pXbs27du3T9P+TZo0YePGjdSrV4+8efNa5qfXrl2bq1evMmbMGBITE2nVqtVjq8vR0ZEvv/ySmTNn4u3tTa1atYiJieHTTz+lQIECDBs2jGHDhuHp6UlgYCDZs2ene/fuj9IeERERETEpG+POuR3yzIuMjASw+pBtRoiPjycqKooyZcrg5OSUobWYwbPSL9veP2R0CfIQf7Qqa/rX2NPyrPxMPi3qV/qpZ+nzrPUrrXlNzywUERERETEhBXkRERERERNSkBcRERERMSEFeRERERERE1KQFxERERExoYf/k6oiIo9Rytg2T+U8z9rTC56G2z0TERHz0B15ERERERETUpAXERERETEhBXkRERERERNSkBcRERERMSEFeRERERERE1KQFxERERExIT1+UkREAKg0ez+wP6PLMBn1K33M36+n9RhdkbTQHXkRERERERNSkBcRERERMSEFeRERERERE1KQFxERERExIQV5ERERERETUpAXERERETEhBXkRERERERNSkBcRERERMSEFeRERERERE1KQT6PTp0/TuXNnfH198fHxoW/fvsTFxREREUHFihXZuHEjgYGBeHh40KFDB65evWrZd9asWbz++utUqFCBoKAgVq9ebdnWpk0bRo8eTcOGDenYsSMAe/bsISAggAoVKtC5c2dmzZqFv78/N2/exMvLi7Vr11rV1rZtW7744oun0wgRERERyRQU5NPAMAy6du1KwYIFWb9+Pb/++ivnzp1j5MiRANy8eZPly5czb948fv31Vw4ePMj8+fMBWLlyJZMmTWL06NHs3LmTHj160LNnT86cOWM5/vLlyxk2bBhfffUViYmJdO7cmdq1axMREUHLli2ZMmUKANmyZSMgIIClS5da9o2NjWX79u00atToKXZERERERDKagnwaREZG8vfff9OnTx+yZcvGCy+8wPvvv8+SJUswDIOUlBTeeecdcuXKRYECBahYsSJHjx4FYOHChbz55puUK1cOOzs76tWrR8WKFVm2bJnl+OXLl6d8+fLY2NgQGRnJ5cuX6dKlC46OjtSsWZPKlStbxgYHB7N27Vri4uIAWLNmDa6urrz00ktPtykiIiIikqHsMroAM4iOjiYlJQVfX1+r9SkpKcTGxgJQpEgRy/ps2bKRkJAAwMmTJ/n999/57rvvLNsNw7AK3oULF7Z8feHCBZydncmVK5dlnbu7O3/++ScAvr6+uLi4sHr1akJCQli1ahUNGzZ8jFcrIiIiImagIJ8GDg4OODk5WcL0nSIiIgDIkuX+v9xwdHSkd+/etG/f/oHHt7W1tXydmpqKnZ31t8XGxsbq60aNGrF06VLq1q1LREQEgwcPTtf1iIiIiIj5aWpNGhQrVoz4+Hiio6Mt6+Li4ix34/9t34MHD1qtO3PmDIZh3Hf8Cy+8wNWrVy1TZ+CfqT13Cg4OJiIigkWLFlGhQgXy58+fnssRERERkWeAgnwauLq64unpybBhw7h8+TLXrl1j4MCB9O3b91/3bd68OStWrGD9+vUkJyezbds2GjRowO7du+87vly5cmTLlo2vv/6axMRENm7cyB9//GE1plSpUpQpU4Yvv/xS02pEREREnlMK8mk0duxYDMOgTp06vPbaa6SkpDBixIh/3a9atWqEhoYyePBgvLy8GDx4MIMGDcLDw+O+47Nnz8748eMJDw/H19eXxYsX065dO6vpNQAhISEkJiYSEBDwOC5PRERERExGc+TTqHDhwnz11Vf3rH/hhRfumTpzd8Bv3bo1rVu3vu9xf/jhh3vWVatWjbVr11rmzk+YMOGe6TOXLl0iMDCQHDlypOs6REREROTZoDvymYxhGAQGBjJu3DiSkpI4ceIE4eHh1KxZ0zLmr7/+4ocffqBDhw4ZWKmIiIiIZCTdkc9kbGxsGDduHMOGDaNSpUrkyJGDgIAA/ve//wHQoUMHDh48SGhoKK+88koGVysiIiIiGUVBPhMqV64cc+bMue+2GTNmPOVqRERERCQz0tQaERERERETUpAXERERETEhTa0REREA/mhVljJlyuDk5JTRpWR68fHxREVFqV9ppH6JPBm6Iy8iIiIiYkIK8iIiIiIiJqQgLyIiIiJiQgryIiIiIiImpCAvIiIiImJCemqNiIgAUGn2fmB/RpeRaaWMbZPRJYiIWNEdeRERERERE1KQFxERERExIQV5ERERERETUpAXERERETEhBXkRERERERNSkBcRERERMSFTB/k5c+bg7++f0WU80KJFi6hWrdoDt/fv35++ffsCMHHiRJo1awZAeHh4pr4uEREREcl4eo58Bho6dOh914eEhBASEmJZXrhwIf7+/ri4uDylykREREQkszP1HfnnQUpKCiNGjCA2NjajSxERERGRTMRUQX737t00atQIDw8P/ve//3Hp0iXLtiVLllC/fn08PT3x9/dn9uzZlm0TJ06kS5cufP3111SrVg0fHx+ru+E3b95kwIAB+Pr6UrlyZQYMGEBiYiIACQkJDB48mFq1auHh4UGbNm04fPiwZd/IyEhatWqFt7c3VatWZeDAgSQlJVnV/dNPP1GjRg0qVapkdex+/frRq1eve67zzik5lSpV4vr16wQHBzNp0iS8vLxYu3at1fi2bdvyxRdfPGpbRURERMSETBPkU1JS6N69O35+fkRERNCzZ0/mz58PQHR0NKGhofTv359du3YxbNgwhgwZwoEDByz779q1i+TkZNatW8eECRP44Ycf2LNnDwBffPEFhw8f5pdffmHFihXs27ePyZMnAzBmzBj279/PvHnz2LZtG+7u7nTr1g3DMADo1asXlStXJiIigoULF7Ju3Trmzp1rOe+1a9f4888/WbFiBbNnz2bNmjV8//33ab7uxYsXW/7brVs3AgICWLp0qWV7bGws27dvp1GjRo/YWRERERExI9ME+b1793L+/Hm6dOmCg4MDFSpU4LXXXgOgSJEibNu2japVq2JjY0OVKlV44YUX2Ldvn2V/W1tbOnXqhL29PVWqVMHFxYUjR45gGAbh4eG0b98eFxcXXFxc+Pzzz6lWrRqpqaksWrSIrl27kj9/fhwdHenZsydnzpyxvAkIDw+nc+fO2NraUqhQIXx8fNi7d6/lvImJiXTv3h1nZ2deeuklGjRowIYNGx65D8HBwaxdu5a4uDgA1qxZg6urKy+99NIjH1NEREREzMc0H3aNiYkhZ86c5MiRw7KuRIkSANjY2DBnzhwWLlzI+fPnMQyDxMREyxQWgEKFCpEly/+9b8mWLRsJCQnExsZy7do1ihQpYtn2yiuvAHDhwgVu3LhB165dsbGxsWxPTU3l7NmzVKhQgW3btjF58mSOHz9OcnIyycnJBAYGWsbmypWLfPnyWZaLFSv2n4K8r68vLi4urF69mpCQEFatWkXDhg0f+XgiIiIiYk6mCfKJiYmkpKRYrUtNTQVgwYIFTJs2jbCwMHx8fLC1taVmzZpWY+8M8fdbf/tYd3J0dARg7ty5lCtX7p7tR44coUePHoSGhtKsWTMcHR3p06cPycnJljF3vgEAMAwDe3v7f7vcB7KxsaFRo0YsXbqUunXrEhERweDBgx/5eCIiIiJiTqaZWpMvXz7i4uK4fv26Zd2RI0eAfz5w6u3tTeXKlbG1teXChQucP38+TcfNnTs3OXPm5NixY5Z1+/btY/HixeTIkYPcuXNz8OBBq31OnToFQFRUFPb29rz99ts4OjpiGAZRUVFWY69evcrly5ctyydPniR//vzpu/i7BAcHExERwaJFi6hQocJ/Pp6IiIiImI9pgnyFChXIlSsX06dPJzExkR07drBu3ToAChcuzNGjR7l69SqnT59m6NChFCpUiHPnzqXp2E2aNGH69OmcO3eO2NhYhgwZwt9//w1AixYtmDJlCkeOHCEpKYmZM2fy5ptvcvPmTQoXLkxCQgJRUVFcvXqV0aNHY29vb5neA2Bvb8+kSZNISEjg6NGjrFixwjK3Py1u/1bg+PHjlnnxpUqVokyZMnz55ZeaViMiIiLynDJNkHd0dGTy5MmsWbMGHx8fJk2aRPv27QFo2bIlxYsXp2bNmnTs2JHWrVvTunVrvv32W3788cd/PXbv3r0pX7489evXp379+rz88st069YNgK5du1K9enVatWqFr68vq1at4uuvvyZbtmx4enry1ltv0bp1a4KCgihcuDAff/wxhw4dsjxW8sUXX6RMmTLUrVuXli1bEhAQwBtvvJHm686bNy8BAQH06NGD8ePHW9aHhISQmJhIQEBAOrooIiIiIs8KG+P2rWMxlQkTJhAdHc3o0aPTtV9kZCQA7u7uT6KsNIuPjycqKooyZcrg5OSUobWYgfqVPupX+sXHx5NjwE8ZXUamljK2jeVrvcbSR/1KP/UsfZ61fqU1r5nmw67yf/766y9++OEHfvjhh4wuRUREREQyiIK8yXTo0IGDBw8SGhpqeUymiIiIiDx/FORNZsaMGRldgoiIiIhkAqb5sKuIiIiIiPwfBXkRERERERPS1BoREQHgj1Zln5knPoiIPA90R15ERERExIQU5EVERERETEhBXkRERETEhBTkRURERERMSEFeRERERMSE9NQaeeJse//wkK37n1odzwb1K33Ur/T4o1XZjC5BRETSQXfkRURERERMSEFeRERERMSEFORFRERERExIQV5ERERExIQU5EVERERETEhBXkRERETEhBTkRURERERMSEE+nU6fPo27uzvHjh3L6FJERERE5DmmfxAqDbZu3YqzszPu7u4ULlyYyMjIjC5JRERERJ5zuiOfBjNnzmTv3r0ZXYaIiIiIiEWmDPKRkZG0atUKb29vqlatysCBA0lKSgJg8+bNNGrUCA8PD4KDg9m6datlvx07dtCsWTM8PT3x8/Nj3LhxpKamAtCvXz969eplGXvr1i3c3NyIiIgAYP369TRs2NCy7+jRo0lNTaVz586sX7+eoUOH0rZtW06dOoWbmxtHjhwB4PLly3Tv3p2KFSvi5+fHF198gWEYAPj7+7NgwQI6duyIp6cndevWZfPmzZYaDhw4QNu2bfH29qZy5coMHTrUcp0XL17kvffew9fXFy8vL9q1a0d0dDQAx44do127dnh7e+Pj40O3bt2IjY19Ut8OEREREcmEMmWQ79WrF5UrVyYiIoKFCxeybt065s6dy7lz53j//ffp3Lkz27dvp23btrz33ntcuXKFixcv0qFDB4KDg4mIiGDatGksXLiQOXPm/Ov5kpKS6NWrFx999BG7du1i1qxZ/Pbbb6xdu5apU6dSuHBh+vfvz3fffXfPvv379wdgw4YNzJ07lyVLlrBgwQLL9hkzZtCtWzciIiKoVKkSn3/+OQA3b97knXfeoWrVqmzZsoUFCxYQERHBjBkzAPjyyy/JlSsXGzduZPPmzRQrVoyRI0cCMGTIELy8vNi2bRurV68mOTmZKVOm/Oe+i4iIiIh5ZMo58uHh4djb22Nra0uhQoXw8fFh7969pKSkULRoUerXrw9AkyZNcHBwIDU1lWXLllGoUCHeeustAMqWLUtwcDC//PKLZd2D3Lp1i4SEBJycnLCxsaFEiRKsXLmSLFke/j4nNjaWdevW8dNPP+Hs7IyzszPjxo3Dzu7/2lq7dm3Kly8PQEBAAOHh4aSmprJ+/XoMw6BTp04AFC1alA4dOvDVV1/RuXNnrl27Ru7cubG3t8fGxoZBgwZZ6rl27RqOjo7Y2dmRK1cuwsLC/rVWEREREXm2ZMogv23bNiZPnszx48dJTk4mOTmZwMBATp48SZEiRazGBgUFAXDq1ClKly5tta148eL88ssv/3o+Z2dn3nvvPVq3bk358uWpVq0aTZo0oWDBgg/d79SpU6SmplrV5OnpaTXmzm2Ojo6kpKSQlJREdHQ0ly5dwt3d3bLdMAzs7e0BeOedd+jSpQubNm3Cz8+P119/nSpVqgDQrVs3+vTpQ3h4OH5+fjRo0MDyZkFEREREng+Z7jbukSNH6NGjB40bN2br1q1ERkbSoEEDALJkyWKZ8363xMTE+663sbG57/qUlBSr5W7durFmzRqCgoLYsWMH9evXZ8+ePQ+t9fZd8AfVdOeYuzk4OPDyyy8TGRlp+bN371527doFgLu7O2vXruWTTz7BMAy6detmmVpTq1Yt1q9fT7du3bh06RKtW7dm1qxZD61VRERERJ4tmS7IR0VFYW9vz9tvv42joyOGYRAVFQX8c3f77ue3z5o1i+joaIoVK8bRo0etth09epSiRYsCYG9vz82bNy3bTp48aTX2ypUr5M+fn7feeotvv/2WwMBAFi9e/NBaCxcuTJYsWaxq2rZtG2vXrv3X6yxWrBjR0dHcuHHDsi42Npa4uDhLPVmzZqVOnToMGTKEKVOmMHfuXMu47NmzU79+fcaOHctnn33GvHnz/vWcIiIiIvLsyHRBvnDhwiQkJBAVFcXVq1cZPXo09vb2nD9/ngYNGnD27Fnmz59PYmIiy5cv54svviB79uy8/vrrREdHM2/ePJKTk9mzZw8///wzjRs3BqBEiRLs3r2bmJgYrl+/zjfffIOtrS0Af/75J6+//jp79uzBMAwuXbrEsWPHKFasGPDP3fOTJ09y/fp1q1pz585NnTp1mDx5MleuXOHMmTMMGDCAc+fO/et1+vn54eLiwsiRI4mLi+PChQv06NGDMWPGANCiRQu+/vprbt26RVJSErt376Z48eIkJCQQEBDA4sWLSU5OJiEhgX379llqFREREZHnQ6YL8p6enrz11lu0bt2aoKAgChcuzMcff8yhQ4cYOnQoM2bMYObMmfj4+DBt2jQmT56Mi4sLhQsXZtKkScybNw8fHx/69OlDjx49CAkJAeDNN9/k1VdfJTAwkDfeeIMGDRrg6OhoOWeXLl3o2bMnFSpUoHHjxlSoUMHyIdlmzZoxe/ZsWrdufU+9w4cPx8nJidq1a9O8eXMCAwNp3rz5v15n1qxZCQsL4+jRo1SrVo2QkBBKlChBaGgoAOPHj2fdunVUrlyZqlWrsnXrVsaMGYOjoyNffvklM2fOxNvbm1q1ahETE8Onn376mL4DIiIiImIGNsbth57Lc+H2v0p754dsnzTb3j88tXOJyKP7o1VZypQpg5OTU0aXkunFx8cTFRWlfqWR+pV+6ln6PGv9Smtey3R35EVERERE5N8pyIuIiIiImJCCvIiIiIiICSnIi4iIiIiYkIK8iIiIiIgJ2WV0AfLsSxnb5p51z9qny5809St91K/0u90zERExD92RFxERERExIQV5ERERERETUpAXERERETEhBXkRERERERNSkBcRERERMSEFeRERERERE1KQFxERERExIQV5ERERERETUpAXERERETEhBXkRERERERNSkBcRERERMSEFeRERERERE1KQFxERERExIQV5ERERERETUpAXERERETEhBXkRERERERNSkBcRERERMSEFeRERERERE1KQFxERERExIRvDMIyMLkKenl27dmEYBvb29hlah2EYJCUlkTVrVmxsbDK0FjNQv9JH/Uo/9Sx91K/0Ub/STz1Ln2etX4mJidjY2ODl5fXQcXZPqR7JJDLLi9vGxibD30yYifqVPupX+qln6aN+pY/6lX7qWfo8a/2ysbFJU2bTHXkRERERERPSHHkRERERERNSkBcRERERMSEFeRERERERE1KQFxERERExIQV5ERERERETUpAXERERETEhBXkRERERERNSkBcRERERMSEFeRERERERE1KQl6fiypUr9OzZk6pVq+Ln58cn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Pnx4RpeYJhMnTmTv3r0ZXYaImJyCvIjIM6RQoUJ88sknxMbGsmvXLgBu3brFyJEjqVu3LuXLl6devXp8//33VvstXryYhg0bUr58eapUqUKvXr24dOmSZbu/vz8TJ06kefPm+Pr6AhAVFUXbtm3x8fHB09OTFi1asGPHDss+Bw8epEOHDlSuXBlPT0/atm1rFV79/f355ptvGDp0KJUrV8bHx4c+ffpw69at+15bamoq/fr1w8PDg5EjR1KiRAlsbGzIkycPb731FiNHjiRLliwkJSUBcObMGd5//338/PyoUKECzZo14/fff7ccr02bNgwaNIhOnTrh4eHBpUuX6NevH127duWTTz7B09OTPXv2ALBq1SqaNm2Kl5cXvr6+9OnTh8uXL9+3zpSUFMaNG0eNGjVwd3enVq1ajB07ltTUVACqVavGvn37GDp0KP7+/pZejBkzxnKMVatW0aRJE8v5PvzwQ8v5Tp06hZubG5s2baJjx454eXlRvXp1vv766we+LkTkGWWIiIgptW7d2ujZs+c960+ePGm4uroav//+u2EYhtG3b1+jUaNGxpEjR4zk5GRjy5YthoeHhzF//nzDMAxjz549hqurq7Fs2TIjNTXViImJMRo0aGB17Nq1axs1atQwtmzZYqSkpBiGYRiBgYHGF198Ydy6dctISEgwpk6datSsWdNITk42rly5Yvj4+BiDBg0yrl+/bly/ft3o16+fUalSJePKlSuWY/r5+RkrVqwwEhMTjd27dxtlypQxZs2add/r3bt3r+Hq6mps2bLlX3uTlJRk1KtXz3jvvfeMS5cuGTdv3jS++OIL49VXXzWOHTtm6V/lypWNJUuWGMnJyYZhGEZoaKhRuXJl46uvvjISExON1NRUY8uWLUa5cuWMZcuWGUlJScbZs2eNt99+22jZsqXlfK6ursbs2bMNwzCMGTNmGN7e3sbff/9tGIZh7N692yhfvrxl+93jb/di9OjRhmEYRkREhOHm5mb8/PPPxq1bt4zo6GijcePGRps2bQzDMIzo6GjD1dXVaNKkiREZGWkkJycb3377reHq6mocOnToX3sjIs8O3ZEXEXlGGIbBqVOnGDZsGCVKlMDLy4srV66wZMkSevToQalSpbC1taVKlSo0btyY8PBwAMqVK8fWrVsJCgrCxsaG/PnzU6tWLXbv3m11/LJly1Kl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\n"
          },
          "metadata": {}
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<Axes: title={'center': 'Features correlation with dependent variable'}, xlabel='Pearson Correlation'>"
            ]
          },
          "metadata": {},
          "execution_count": 19
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **A dashboard for interactive visualization**"
      ],
      "metadata": {
        "id": "Otfww8OWI352"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from dash import Dash, html, dash_table, dcc, callback, Output, Input\n",
        "from pyngrok import ngrok\n",
        "\n",
        "\n",
        "ngrok.set_auth_token(\"2ra68T1PexqPW4YHpFxTAE0G2bg_4v1Qyo8uBBzYbqkU3tADr\")\n",
        "\n",
        "\n",
        "app = Dash()\n",
        "\n",
        "\n",
        "app.layout = html.Div([\n",
        "\n",
        "    dcc.Dropdown(\n",
        "        id='scatter-dropdown',\n",
        "        options=[\n",
        "            {'label': 'Valence vs. Energy', 'value': 'valence_energy'},\n",
        "            {'label': 'Acousticness vs. Danceability', 'value': 'acousticness_danceability'},\n",
        "            {'label': 'Loudness vs. Popularity', 'value': 'loudness_popularity'}\n",
        "        ],\n",
        "        value='valence_energy',\n",
        "        style={'width': '50%'}\n",
        "    ),\n",
        "\n",
        "    dcc.Graph(id='scatter-plot')\n",
        "])\n",
        "\n",
        "\n",
        "@app.callback(\n",
        "    Output('scatter-plot', 'figure'),\n",
        "    [Input('scatter-dropdown', 'value')]\n",
        ")\n",
        "def update_scatter(selected_value):\n",
        "    if selected_value == 'valence_energy':\n",
        "        fig = px.scatter(data, x='valence', y='energy', title='Valence vs. Energy')\n",
        "    elif selected_value == 'acousticness_danceability':\n",
        "        fig = px.scatter(data, x='acousticness', y='danceability', title='Acousticness vs. Danceability')\n",
        "    elif selected_value == 'loudness_popularity':\n",
        "        fig = px.scatter(data, x='loudness', y='popularity', title='Loudness vs. Popularity')\n",
        "\n",
        "    return fig\n",
        "\n",
        "\n",
        "public_url = ngrok.connect(8040)\n",
        "print(\"Dash app is running at:\", public_url)\n",
        "\n",
        "app.run_server(debug=False)\n"
      ],
      "metadata": {
        "id": "6wUJCcdcsEs-",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 688
        },
        "outputId": "7df8a102-e449-4dcc-cbf6-8e1e3205ece7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Dash app is running at: NgrokTunnel: \"https://8b4a-34-31-121-86.ngrok-free.app\" -> \"http://localhost:8040\"\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ],
            "application/javascript": [
              "(async (port, path, width, height, cache, element) => {\n",
              "    if (!google.colab.kernel.accessAllowed && !cache) {\n",
              "      return;\n",
              "    }\n",
              "    element.appendChild(document.createTextNode(''));\n",
              "    const url = await google.colab.kernel.proxyPort(port, {cache});\n",
              "    const iframe = document.createElement('iframe');\n",
              "    iframe.src = new URL(path, url).toString();\n",
              "    iframe.height = height;\n",
              "    iframe.width = width;\n",
              "    iframe.style.border = 0;\n",
              "    iframe.allow = [\n",
              "        'accelerometer',\n",
              "        'autoplay',\n",
              "        'camera',\n",
              "        'clipboard-read',\n",
              "        'clipboard-write',\n",
              "        'gyroscope',\n",
              "        'magnetometer',\n",
              "        'microphone',\n",
              "        'serial',\n",
              "        'usb',\n",
              "        'xr-spatial-tracking',\n",
              "    ].join('; ');\n",
              "    element.appendChild(iframe);\n",
              "  })(8050, \"/\", \"100%\", 650, false, window.element)"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Data visualization : Histogram**"
      ],
      "metadata": {
        "id": "OTaO0a25JHbq"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "data['decade'] = (data['year'] // 10) * 10\n",
        "\n",
        "count = data.groupby('decade')['year'].count().reset_index()\n",
        "\n",
        "plt.figure(figsize=(8, 6))\n",
        "sns.barplot(x='decade', y='year', data=count)\n",
        "\n",
        "plt.title('Number of Songs Count by Decade')\n",
        "plt.xlabel('Decade')\n",
        "plt.ylabel('Number of songs')\n",
        "\n",
        "plt.show()"
      ],
      "metadata": {
        "id": "SbTSGQh75o3B",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 562
        },
        "outputId": "448a07be-0469-48d8-ef98-1983f2f3cf39"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 800x600 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAsQAAAIhCAYAAABJ3KyyAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAY89JREFUeJzt3XlYVGXjxvEbEVBEQNTcMjUXQhaXNNQsXFLLStPceEsztVxDyX0LNc3XcimXNK1cWpTXJTXTNNf2XCpFQg3MXHKX0UBkkfP7w4v5NQnKKOuc7+e6uJLznHPmuWfGvDk8M+NkGIYhAAAAwKSK5PcEAAAAgPxEIQYAAICpUYgBAABgahRiAAAAmBqFGAAAAKZGIQYAAICpUYgBAABgahRiAAAAmBqFGAAAAKZGIQZMbtSoUfL19dXcuXMzHe/evbtGjRqVJ3Pp3r27unTpkie3ZQ/DMDRq1CjVr19fbdu2zXK/pKQkvf/+++rQoYMaNmyogIAAhYSEaPjw4Tp16lQezjjnnD17VpMnT1arVq0UGBio4OBgdenSRR9//LHS0tLye3q3tGbNGvn6+iouLi7Hz92iRQv5+vpav+rWrasnnnhCEydO1B9//JHjt3e3pk+fLl9f3/yeBlBgUYgByNnZWYsWLSq0pS23RUVF6bPPPtMLL7ygxYsXZ7lf//79tXjxYvXo0UNr1qzRxo0bNXr0aP366696/vnndeXKlTyc9d07cOCA2rVrp4MHD2r06NHatGmTPvjgAz3yyCN688031bt3b6WmpubL3E6cOJHvBa9ly5b69ttv9e2332rdunUaMmSI4uLi1L59e23cuDFf5wbAPkXzewIA8l/dunWVkJCgadOmafbs2fk9nQLn8uXLkqRGjRqpXLlyme4TFxenH374QZMnT1aHDh2s2++77z5VrVpVI0eOVHR0tBo3bpwnc75bycnJGjx4sO6//34tXbpUrq6ukqR7771XAQEB8vf3V//+/bV+/Xo9++yzeT6/X375Jc9v89/c3NxUtmxZ6/dVqlRR69atFRERoREjRsjX11fVq1fPxxkCyC6uEAOQs7Ozxo0bp82bN+uHH3645b4tWrRQeHi4zbZ//2p61KhReuqpp7Rr1y61bdtWgYGBeuaZZxQTE6MffvhB7du3V506dfTss8/q0KFDN93Gpk2b1KZNGwUEBOjxxx/Xjh07bMb379+v3r17q0mTJqpbt66ee+45/fzzz9bxn376Sb6+vtq0aZOefvrpW5bQlJQUzZgxQy1atFBAQICaNGmiUaNG6eLFi5KkOXPmqE+fPpKkHj16qEWLFpme59q1a9bz/dsDDzygdevW2cwjLi5O/fr1U4MGDRQQEKC2bdvqo48+sjnO19dXS5Ys0Zw5c/TII4+oXr166tGjh44dO2bdJzU1VZMnT1ZwcLDq1aungQMHKiYmRr6+vlqzZo11Tv/973/VokULBQYG6uGHH9bIkSMVHx+f5f2yadMm/fXXXxo+fLi1DP9TixYttHXrVpsy/Msvv+iFF15QvXr1FBQUpA4dOuiLL76wjp88eVK+vr5avny5zblGjRqlhx9+2ObcU6ZM0SeffKKWLVuqbt266tSpkw4cOCDpxmMyfPhw6310uyU9Z86cUe/evVW3bl0FBwdrypQpun79ui5duqTAwEDNmTPnpmN69+6tzp073/K8mXFyctLIkSNVvHhxm98mJCQk6PXXX1ebNm0UGBioxx57TAsXLpRhGNZ90tPT9eGHH6p169YKCgrS448/rmXLltmcf/369erQoYMCAwP14IMPKjQ0VLt377bZJy4uTs8//7wCAwPVtGlTvfPOOza3k2HdunXq3Lmz6tevr4ceekjh4eE6e/as3ZkBR0AhBiBJeuihh/TEE09oypQpObI2ND4+Xh999JFmzJihjz/+WJcuXdKIESP07rvvavLkyfroo490/vx5TZkyxea4U6dOKTIyUm+99ZZWr16tSpUqKSwsTKdPn5Yk/fHHH3rhhRd0/fp1LVq0SJGRkSpfvrx69ep101rRBQsWaPDgwfrss8+ynOe4ceP06aefKiwsTBs3btTUqVP1008/6aWXXpJhGOrVq5dmzJgh6UYRW7VqVabnqVmzpipUqKCpU6dq1qxZOnLkSKYlRJIuXryo5557ThaLRQsXLtSGDRvUvn17TZky5aYCtGLFCiUlJWnp0qWaP3++Dh8+rNdff906PmfOHH366acaMGCA1qxZo4YNG2ro0KE253j33Xf1xRdfaMqUKdqyZYveeecd/fbbb9ZSmZndu3fLy8tL9evXz3KfypUrW/8cGxurF154Qe7u7vr444/12Wef6cEHH9Srr76qrVu3ZnmOrHzzzTfav3+/FixYoGXLluny5csaMWKEJKlX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x6VLl7Rnzx4999xzkv6/kC9duvSmci7dWPZx4cIFSbe+Ar5+/XrVrVtXEyZMsLmtf8oowklJSdZlJZLtczzj8ejZs2em66T/XaYBM2DJBICbtGrVSo0bN9bkyZNvKi+enp43/SP866+/5tht//nnnzavdD958qQuX76smjVrSrqxhOCPP/5QhQoVVKVKFeuXYRg3LUG4nYCAABUpUkR79uyx2b5v3z5JUmBgYLbPNXnyZDVv3jzTMpqSkqKzZ89a37ItKChIJ06cuOkV/fv27VP16tVveZXwn3x8fOTl5WV994UM/1wDmp6eri1btlgLuKurq5o1a6awsDCdOnUqywLWqlUrValSRW+++WamRXfXrl0aPXq0vvzyS0lSnTp1FBUVpeTkZOs+hmHo559/tt6PGT8s/PP5k5aWpoMHD2Yrb2ayc8X4n+uDpRtLYf55ZdzT01NPPPGEvvjiC23YsEGdOnW64/mkp6dr4sSJcnZ2Vo8ePSTJugzi3LlzNs9ZT09PFS9eXO7u7qpQoYJKlix503PxnXfe0ejRoyXdeMHcv9cCZyz1yLgf7r//fkmyeU4YhmF9Tks3rhbXqlVLf/zxh818qlSpopSUFJUuXfqO8wOFFYUYQKbGjh2r6Ojom8puUFCQfv75Z23dulXHjx/XkiVLblq7eze8vb01ZswYRUdH69ChQxo3bpzc3d3Vpk0bSTfe+iwxMVFDhw5VVFSUTpw4of/973965plnFBkZaddtlS1bVh06dLC+08OJEye0bds2TZ06VcHBwQoKCsr2ubp3765ixYrp+eef14YNGxQXF6cTJ07o66+/Vp8+fXTt2jX17t1bktSxY0d5e3srPDxcBw4c0B9//KHZs2fr66+/1ssvv2xXhscff1zbtm3TqlWr9Oeff+qjjz6yKT9FihTR+++/ryFDhmjv3r06ffq0oqOjtWLFCtWqVUve3t6ZntfFxUWzZs3SuXPn1KVLF23cuFEnTpzQoUOHNHfuXL3yyit66qmnrL+u7969u5KTkzV06FAdPnxYsbGxioiI0NGjR625S5YsqapVq2rdunU6cOCAYmNjNX78eOuVbntklOutW7da1wNn5fPPP9eXX36pP//8U++//752796tjh072uwTGhqq7777TocOHVL79u2zNYfk5GSdP39e58+f119//aVdu3bphRde0I4dOzR9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rzb7li9fXqdOnbLZdujQIeuf77vvPhUtWlTR0dE2+5w5c0YpKSl3HhQAchGFGAAKobS0NP3888/q2bOnkpKS9Nprr+n+++9XSEiI3nzzTcXFxen69ev67rvv1K5dO23atEmSFBoaqp9++kkbNmxQSkqKfvnlF40aNUoJCQmqVKmSihYtqj179igtLU2//PKLFi1aJE9PT50+fVqS1KpVKx05ckTr169XamqqfvnlF5u1we7u7urSpYveffdd7d+/X9evX1dUVJS6du2qxYsX58ddBQC35WRk9bszAECB8e8P5nByclKlSpXUqlUr9enTR56enpKk+Ph4TZs2TTt27FBiYqIqVaqkXr16qWvXrtZzbd68WTNnztTp06dVoUIF9ejRQ88995wkKTIyUnPnzlVCQoLq1Kmj119/Xf/73/+0dOlSvfjiiwoPD9eSJUu0bNkyXbx4UUFBQerUqZNGjBihbdu26d5779W1a9c0Y8YMbdq0SRaLRWXLllXXrl318ssvq0gRrsMAKHgoxAAAADA1flQHAACAqVGIAQAAYGoUYgAAAJgahRgAAACmRiEGAACAqVGIAQAAYGoUYgAAAJgahRgAAACmRiEGAACAqVGIAQAAYGoUYgAAAJja/wECslPx1ri8swAAAABJRU5ErkJggg==\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import seaborn as sns\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "\n",
        "data['decade'] = (data['year'] // 10) * 10\n",
        "\n",
        "decade_popularity = data.groupby('decade')['acousticness'].mean().reset_index()\n",
        "\n",
        "\n",
        "plt.figure(figsize=(8, 6))\n",
        "sns.barplot(x='decade', y='acousticness', data=decade_popularity)\n",
        "\n",
        "plt.title('Average Acoustickness by Decade')\n",
        "plt.xlabel('Decade')\n",
        "plt.ylabel('Average Acousticness')\n",
        "\n",
        "\n",
        "plt.show()\n"
      ],
      "metadata": {
        "id": "TtYFa1hJ2JJ7",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 562
        },
        "outputId": "b67803dd-b410-451d-e818-d4ad889f358f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 800x600 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAArAAAAIhCAYAAAC2folQAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAU+9JREFUeJzt3Xt8z/X///H722xOc1pEoXzCFjswpzmFOSuHnCkkIYeEEKpF5NDHoUIfURGlCJEQQkipSJjDyJxmlMO2GHawPX9/+O399TZsbzbvvdbterm45P18PV+v9+Pxfr+z+17v5/v1thljjAAAAACLyOHqAgAAAABnEGABAABgKQRYAAAAWAoBFgAAAJZCgAUAAIClEGABAABgKQRYAAAAWAoBFgAAAJZCgAUAAIClEGCBbGTmzJny8fHR4MGDXV2KS40aNUo+Pj6aPHmyq0u5Kz4+PpoyZUq65zdo0EBDhgzJxIoyV2bV//XXX8vHx8f+p3z58qpRo4aef/55LVu2TElJSRl+n/ciPj5ePj4+mjFjhqtLAbI8AiyQTRhj7D+wN27cqJiYGFeX5BKxsbFau3atfHx89M0332S5kHKziIgI+fj4OIxt27ZN/fr1c1FF2c/ChQu1bds2bd68WXPmzFGVKlU0YcIEPffcc7p8+bKrywNwFwiwQDbx888/KzIyUhMmTJDNZtO3337r6pJcYs2aNUpOTtaECRN07tw5bdmyxdUl3dEff/yRaqxo0aLKly+fC6rJngoXLqyiRYuqWLFiCggI0EsvvaSvvvpKYWFheuutt1xdHoC7QIAFsoklS5YoMDBQfn5+aty4sZYtW2bfZoxRcHCwhg4dmmq/N998U0FBQUpMTJQkbd26VV27dlX16tVVuXJl9e7dW+Hh4fb5KWd5t2zZooYNG6pdu3aSpGvXrun9999Xw4YN5evrq9q1a+vll1/WqVOnHO5vw4YNat68ufz9/dWiRQtt2bJFL7zwgrp162afk5CQoPfff19PPfWUAgICVK9ePU2ZMkUJCQnpehwaNWokPz8/BQYGOjwOKZKTkzV37lw1adJEAQEBatasmRYsWOAw548//tBzzz2nwMBABQQEqE2bNlq9erV9+6lTp+Tj46Mvv/zSYb+RI0eqdu3a9tu//fabunbtqmrVqqlSpUoOx5kxY4aGDx8u6fqygZEjR9r/fuMSgrNnz2ro0KGqXr26qlSpoh49eig0NPS2j0F0dLSaNm2q7t27KyEhQTNmzFDVqlV16NAhPfPMM6pUqZLq16+vOXPmOOx37tw5vfrqq2rQoIH8/f311FNPaenSpQ5zvv/+e7Vr106VK1dW5cqV1blzZ/3888/27WFhYerdu7dq1KihgIAAPfnkk/rss89uW+uNFi5cqODgYPn5+alt27bavXu3JOmdd95RYGBgqrOlu3fvtr8WnVWmTBn17NlTK1eu1JkzZ+zjab3+Jeno0aPq27evKleurKCgIPXv31/Hjx+3bz937pxGjhypmjVrys/PTw0aNNCkSZMUFxfncJwPPvhAderUUUBAgLp06aJDhw6lqjM9zwnwr2QAWF5UVJTx9fU1X331lTHGmJ9//tl4e3ub/fv32+dMnjzZBAYGmri4OPtYYmKiCQoKMm+99ZYxxphff/3VPP7442bIkCHmzz//NHv37jXdu3c3NWrUMBcuXDDGGLNs2TLj7e1tunTpYn755Rdz9uxZY4wxM2bMML6+vua7774zp0+fNnv27DFt27Y1bdq0sd/f4cOHTYUKFUyfPn3MwYMHzfbt203Lli1NvXr1TNeuXe3zXnvtNePv728WL15sTpw4YVavXm2qV69uRo4cecfHISwszHh7e5uff/7ZGGPMV199ZXx9fc358+cd5s2aNctUrFjRLF++3Jw4ccIsWbLElC9f3nz++efGGGP+/PNP4+/vb/r27Wv27dtnjhw5YsaNG2e8vb3N999/b4wxJiIiwnh7e5svvvjC4dgjRowwtWrVMsYYc/HiRVOpUiUzbtw4c/ToUXPixAkza9Ys4+PjY/744w8TGxtrxo4da7y9vc3Zs2fNxYsXjTHGeHt7m8mTJxtjjImPjzctWrQw7du3N7t27TJHjhwxL7/8sqlatar566+/jDHGBAcHm8GDBxtjjLl69arp1KmTadOmjbl06ZIxxpjp06ebihUrmq5du5pt27aZEydOmDfeeMN4e3ubP/74w34/zZs3Nw0aNDBbtmwxx44dM7NnzzY+Pj5m+fLlxhhjjh49aipUqGBmz55tTp48aX9cfH19zenTp40xxtSrV88MHjzYHD582ERERJjFixcbX19fs3r16ts+b8HBwaZu3bpm4MCB5uDBg2bv3r3m6aefNjVq1DCXL182R48eNT4+PmbZsmUO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fpm1F154wVSqVMlUr17d9O3b1xw/fty+ffny5SY4ONgEBASY9u3bm507d5rw8HBTr149U6lSJfPnn3+apKQkM2XKFFOjRg3j5+dnOnXqZA4ePGj8/Pycfk6AfyObMbd53woAMkFUVJTy589vP3t27do11a5dW08++aRGjx7t4uqQ1fXt21fGGM2ePdvVpQBwIT7EBeC+CQ8PV6tWrdSqVSv16tVLkjR//nxdvHgxXR9owr9TQkKCzp07p8WLF2vbtm0OS2IA/DtxBhbAffXjjz/qgw8+0OHDh5UjRw6VLVtW/fv3V926dV1dGrKonTt3qlu3bipdurRGjhypevXqubokAC5GgAUAAIClcBUCAAAAWAoBFgAAAJZCgAUAAICl/GuuQvDHH3/IGJPuC18DAADg/kpMTJTNZlNgYOAd5/1rAqwx5rZf1QgAAADXS29W+9cE2JQzrynfYw4AAICsJTQ0NF3zWAMLAAAASyHAAgAAwFIIsAAAALAUAiwAAAAshQALAAAASyHAAgAAwFIIsAAAALAUAiwAAAAshQALAAAASyHAAgAAwFIIsAAAALAUAiwAAAAshQALAAAASyHAAgAAwFIIsAAAALAUAiwAAAAshQALAAAASyHAAgAAwFIIsAAAALAUAiwAAAAsJaerCwDuVbEB77q6BKf9/cEQV5cAAIBlEWD/BQh4AAAgO2EJAQAAACyFAAsAAABLIcACAADAUgiwAAAAsBQCLAAAACyFAAsAAABLIcACAADAUgiwAAAAsBQCLAAAACyFAAsAAABLIcACAADAUgiwAAAAsBQCLAAAACwlp6sLAHBnxQa86+oSnPb3B0NcXQIAIBvjDCwAAAAshQALAAAASyHAAgAAwFIIsAAAALAUAiwAAAAshQALAAAASyHAAgAAwFIIsAAAALAUAiwAAAAshQALAAAASyHAAgAAwFIIsAAAALAUAiwAAAAshQALAAAASyHAAgAAwFIIsAAAALAUlwbYyMhI9enTR0FBQQoODtbkyZOVnJycal5ycrKmT5+uBg0aKDAwUC1bttSaNWtcUDEAAABcLacr73zgwIHy9fXVhg0bdOHCBb344osqUqSInn/+eYd5X375pZYsWaL58+fr0Ucf1datW/XSSy/pscce0+OPP+6i6gEAAOAKLjsDGxoaqrCwMA0bNkz58+dX6dKl1aNHDy1evDjV3P3796tKlSp67LHH5ObmpuDgYBUqVEiHDh1yQeUAAABwJZedgd2/f79KlCihggUL2sd8fX117NgxxcbGytPT0z5ev359jRkzRgcPHlSZMmX0448/6urVq6pevbpT92mM0ZUrVxzG/jN89r014gLHJr/o6hIy3c3PU3ZDfwAApGaMkc1mS3OeywJsTEyMChQo4DCWEmajo6MdAmyTJk108OBBPf3005KkPHny6J133tFDDz3k1H0mJibq4MGD91Z4FpAdekhLdu+R/gAAuDUPD48057h0DawxJl3zVqxYoRUrVmjJkiXy8fHR9u3bNXToUD300EMKCAhI9/25u7urbNmyN41udaLirKF8+fJO7pHde6S/rMb51ygAANKRI0fSNc9lAdbLy0sxMTEOYzExMbLZbPLy8nIY//zzz9WpUyd7WK1fv75q1KihlStXOhVgbTab8ubNe8+1u1p26CEt2b1H+gMAILX0LB+QXPghLj8/P505c0ZRUVH2sdDQUJUtW1b58uVzmJucnKykpCSHsYSEhPtSJwAAALIWlwXYChUqyN/fX1OnTlVsbKzCw8M1b948denSRZLUrFkz7dy5U5LUoEEDLV26VGFhYbp27Zq2bdum7du3q2HDhq4qHwAAAC7i0jWw06dPV0hIiGrXri1PT0917txZzzzzjCTp2LFj9k8yv/jii7p27ZoGDBigqKgolShRQm+//bZq1qzpyvIBAADgAi4NsMWLF9dHH310y203XuPV3d1dgwcP1uDBg+9TZQAAAMiqXPpVsgAAAICzCLAAAACwFAIsAAAALIUACwAAAEshwAIAAMBSCLAAAACwFAIsAAAALIUACwAAAEshwAIAAMBSCLAAAACwFAIsAAAALIUACwAAAEshwAIAAMBSCLAAAACwFAIsAAAALIUACwAAAEshwAIAAMBSCLAAAACwFAIsAAAALIUACwAAAEshwAIAAMBSCLAAAACwFAIsAAAALIUACwAAAEshwAIAAMBSCLAAAACwFAIsAAAALIUACwAAAEshwAIAAMBSCLAAAACwFAIsAAAALIUACwAAAEshwAIAAMBSCLAAAACwFAIsAAAALIUACwAAAEshwAIAAMBSCLAAAACwFAIsAAAALIUACwAAAEshwAIAAMBSCLAAAACwFAIsAAAALIUACwAAAEshwAIAAMBSCLAAAACwFAIsAAAALIUACwAAAEshwAIAAMBSCLAAAACwFAIsAAAALIUACwAAAEshwAIAAMBSCLAAAACwFAIsAAAALIUACwAAAEshwAIAAMBSCLAAAACwFAIsAAAALIUACwAAAEshwAIAAMBSCLAAAACwFAIsAAAALIUACwAAAEshwAIAAMBSCLAAAACwFAIsAAAALIUACwAAAEshwAIAAMBSCLAAAACwFAIsAAAALIUACwAAAEshwAIAAMBSCLAAAACwFAIsAAAALIUACwAAAEshwAIAAMBSCLAAAACwFAIsAAAALIUACwAAAEshwAIAAMBScrq6AAAoNuBdV5fgtL8/GOLqEgDgX4szsAAAALAUAiwAAAAshQALAAAASyHAAgAAwFIIsAAAALAUAiwAAAAshQALAAAASyHAAgAAwFJcGmAjIyPVp08fBQUFKTg4WJMnT1ZycvIt54aHh6tbt26qWLGi6tWrp08//fT+FgsAAIAswaUBduDAgSpWrJg2bNigefPmacOGDZo/f36qeXFxcerVq5fq1aunX375RTNmzNDSpUsVHh7ugqoBAADgSi4LsKGhoQoLC9OwYcOUP39+lS5dWj169NDixYtTzf3uu+/k6empXr16KU+ePAoICNCqVatUpkwZF1QOAAAAV8rp7A6xsbH66KOPNGTI9e8B/+qrr7Rw4UKVKVNGISEhKly4cLqOs3//fpUoUUIFCxa0j/n6+urYsWOKjY2Vp6enffz333+Xt7e3Ro0ape+//15FihRR//791apVK6dqN8boypUrTu2TFWWHHtKS3XukP+v7N/QIAPebMUY2my3NeU4H2PHjx+vEiROSrq9LHTt2rHr37q3Dhw/rnXfe0aRJk9J1nJiYGBUoUMBhLCXMRkdHOwTYv/76Szt37tS4ceP05ptvau3atRoxYoTKli2rChUqpLv2xMREHTx4MN3zs6rs0ENasnuP9Gd9/4YeAcAVPDw80pzjdIDdunWrli9fLklatWqVateurUGDBikmJkYtW7Z06ljGmHTP8/X1tR+/TZs2WrRokdauXetUgHV3d1fZsmVvGt2a7v2zivLlyzu5R3bvkf6yGl6jAIC7ceTIkXTNczrAXrlyRQ8++KAkafv27Xr66aclSYUKFdKlS5fSfRwvLy/FxMQ4jMXExMhms8nLy8thvGjRoqnmlihRQufOnXOqdpvN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uaV6+3ncuHF6+umndenSJY0ePVo//PCD3N3d1aJFC40cOVIeHh73qz1J99ZjdHS0Jk6cqE2bNskYo8cff1zDhw9XpUqVJF3/AE1ISIh+++03eXp6qnPnznrppZfu6/qte+nvZg0aNNDEiRMVFBQkKWv0J91bj6dPn9aECRO0Y8cOJSQkqGbNmho9erT906VZocd7fQ4XLlyojz76SBcuXFBAQIAmTJhgv9xRdujvjz/+UOfOnbV9+/ZUb5tnhf6ke+vx/PnzmjRpkn755RfFx8fLx8dHw4cPt5/dyQo93uu/oyNHjtRvv/2mvHnzqkuXLhowYIC9/sOHD2v06NHat2+fihQpot69e+uZZ565b71J0s6dO/Xss8/e8ufT2rVrdfny5TvWuH79ek2dOlWRkZEqW7asXn/9dVWrVk3S9TPqM2bM0KJFi3T58mUFBQXd8d/hrNbfihUrFBISIklKSEiQu7u7bDabWrdurbffflsJCQmaOHGiVq9erWvXrik4OFhjxoy541UrslqPr732mpYvX57qBFu1atXsX3jwxRdfaM6cObpw4YL8/f01ZswYeXt7Z1o/BFgAAABYCksIAAAAYCkEWAAAAFgKARYAAACWQoAFAACApRBgAQAAYCkEWAAAAFgKARYAAACWQoAFAACApRBgAeBfaOvWrfLx8dGpU6dcXQoAOC1n2lMAAHejW7du2rlzp/3rF93d3fWf//xHwcHBeu655+77V0kCQHbBGVgAyETNmjVTaGioQkNDtXHjRg0fPly//vqrWrVqxdlPALhLBFgAuE8KFy6sGjVqaO7cuSpatKjefPNNSdI///yj119/XfXr11fFihXVsmVLrV692mHfVatWqWXLlqpUqZKaNm2qL7/80r7t/PnzGjp0qKpXr65KlSrpqaee0sqVKx32//LLL9W4cWNVqlRJzz33nE6fPu2wPT4+Xu+8844aNWqkgIAANWnSRAsWLMikRwIA7g1LCADgPnN3d9cLL7ygQYMG6e+//9bQoUPl4eGhRYsW6YEHHtD333+v4cOHq3DhwqpVq5Z++uknjRo1StOnT9cTTzyh33//Xb1791ahQoXUvHlzvfHGG4qOjtb69euVP39+ffXVVxoxYoQqVKigsmXLateuXRozZowmTpyoli1b6uDBgxo2bJhDTW+++abCwsI0Z84cPfroo/rtt9/Uv39/5cmTRx06dHDRIwUAt8YZWABwgbJly8oYoxMnTmjHjh0aMWKEihcvLnd3dz355JOqU6eOVqxYIUn64osvVLt2bQUHBytnzpwKCgrSzJkz9eijj0qS3nvvPX3yyScqVKiQ3Nzc1K5dOyUnJ2vv3r2Srp+9LVeunNq2bSt3d3cFBASoXbt29lpiYmK0cuVKDRo0SI899pjc3NxUs2ZNtWnTxl4DAGQlnIEFABe4du2aJOm3336TJLVv395huzFGlSpVkiSdOHFCNWvWdNhet25d+9+PHj2qd999V3v37tXly5dls9kkXV8WIEmnT59WyZIlHfYvV66c/e8nTpxQcnKyXn75Zfu+KTUULVr0XtoEgExBgAUAFwgNDVWOHDnswXLLli3y8vK65dwcOXLIGHPLbbGxsXr++ecVFBSkb775RsWLF1dSUpIqVKhgn5OQkCAPDw+H/ZKTk+1/z5Url6TrZ3oDAgLuqS8AuB9YQgAA91lCQoLmz5+vhg0b2gPjvn37HOZERkYqKSlJklS6dGmFh4c7bF+/fr22bNmiI0eOKCYmRr169VLx4sUlSbt373aYW7x4cUVGRjqMhYWF2f/+yCOPKGfOnNq/f7/DnL/++ksJCQl33ygAZBICLADcJ9euXdOuXbvUo0cPXb16VW+++aYee+wx1atXT//9738VHh6upKQk/fTTT2rVqpW+++47SVKXLl3066+/atWqVUpISNAff/yhkSNHKjY2ViVKlFDOnDm1Y8cOXbt2TX/88Yc++ugjFShQQGfOnJEkNW7cWIcPH9bKlSuVmJioP/74w2Fta968edWxY0f973//0549e5SUlKTQ0FB16tRJ8+bNc8VDBQB3ZDO3e18KAHBPbv4iA5vNphIlSqhx48bq1auXChQoIEmKjo7WO++8ox9++EGXL19WiRIl1LNnT3Xq1Ml+rHXr1mnatGk6c+aMHnroIXXv3l3PPvusJGnx4sWaOXOmYmNjVbFiRY0bN05fffWV5s+fr+eff15DhgzRp59+qgULFujChQsKCAhQ+/bt9eqrr2rjxo0qWbKk4uLiNHXqVH333XeKiYlR0aJF1alTJ/Xp00c5cnCuA0DWQoAFAACApfBrNQAAACyFAAsAAABLIcACAADAUgiwAAAAsBQCLAAAACyFAAsAAABLIcACAADAUgiwAAAAsBQCLAAAACyFAAsAAABLIcACAADAUv4fvs427TmsqMwAAAAASUVORK5CYII=\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Data Visualization from interactive Dashboard**"
      ],
      "metadata": {
        "id": "8-EOZU1ZJlyz"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import plotly.graph_objects as go\n",
        "import dash\n",
        "from dash import dcc, html\n",
        "from dash.dependencies import Input, Output\n",
        "\n",
        "data['decade'] = (data['year'] // 10) * 10\n",
        "\n",
        "decade_stats = data.groupby('decade').agg(\n",
        "    average_popularity=('popularity', 'mean'),\n",
        "    song_count=('year', 'count')\n",
        ").reset_index()\n",
        "\n",
        "\n",
        "app = dash.Dash(__name__)\n",
        "\n",
        "\n",
        "app.layout = html.Div([\n",
        "    html.H1(\"Decade vs Popularity/Count of Songs\"),\n",
        "\n",
        "\n",
        "    dcc.Dropdown(\n",
        "        id='y-axis-dropdown',\n",
        "        options=[\n",
        "            {'label': 'Average Popularity', 'value': 'average_popularity'},\n",
        "            {'label': 'Count of Songs', 'value': 'song_count'}\n",
        "\n",
        "        ],\n",
        "        value='average_popularity',\n",
        "        style={'width': '50%'}\n",
        "    ),\n",
        "\n",
        "    dcc.Graph(id='decade-bar-plot'),\n",
        "\n",
        "#     html.Div([\n",
        "#     html.H1(\"Scatter Plot\"),\n",
        "#     # Dropdown menu for selecting scatter plot\n",
        "#     dcc.Dropdown(\n",
        "#         id='scatter-dropdown',\n",
        "#         options=[\n",
        "#             {'label': 'Valence vs. Energy', 'value': 'valence_energy'},\n",
        "#             {'label': 'Acousticness vs. Danceability', 'value': 'acousticness_danceability'},\n",
        "#             {'label': 'Loudness vs. Popularity', 'value': 'loudness_popularity'}\n",
        "#         ],\n",
        "#         value='valence_energy',  # Default value\n",
        "#         style={'width': '50%'}\n",
        "#     ),\n",
        "\n",
        "#     # Graph to display the selected scatter plot\n",
        "#     dcc.Graph(id='scatter-plot')\n",
        "# ])\n",
        "    ])\n",
        "\n",
        "\n",
        "@app.callback(\n",
        "    Output('decade-bar-plot', 'figure'),\n",
        "    [Input('y-axis-dropdown', 'value')]\n",
        ")\n",
        "def update_graph(y_axis_value):\n",
        "\n",
        "    fig = go.Figure()\n",
        "\n",
        "\n",
        "    fig.add_trace(go.Bar(\n",
        "        x=decade_stats['decade'],\n",
        "        y=decade_stats[y_axis_value],\n",
        "        marker_color='indianred' if y_axis_value == 'average_popularity' else 'lightblue',\n",
        "        name=y_axis_value\n",
        "    ))\n",
        "\n",
        "\n",
        "    fig.update_layout(\n",
        "        title=f'{y_axis_value.replace(\"_\", \" \").title()} by Decade',\n",
        "        xaxis_title=\"Decade\",\n",
        "        yaxis_title=y_axis_value.replace(\"_\", \" \").title(),\n",
        "        template='plotly_dark'\n",
        "    )\n",
        "\n",
        "    return fig\n",
        "\n",
        "# Step 6: Run the app\n",
        "if __name__ == '__main__':\n",
        "    app.run_server(debug=True)\n"
      ],
      "metadata": {
        "id": "mEq5EptB7lvK",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 671
        },
        "outputId": "a814b6df-1539-4f4a-a4ce-d4bee36ddac9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ],
            "application/javascript": [
              "(async (port, path, width, height, cache, element) => {\n",
              "    if (!google.colab.kernel.accessAllowed && !cache) {\n",
              "      return;\n",
              "    }\n",
              "    element.appendChild(document.createTextNode(''));\n",
              "    const url = await google.colab.kernel.proxyPort(port, {cache});\n",
              "    const iframe = document.createElement('iframe');\n",
              "    iframe.src = new URL(path, url).toString();\n",
              "    iframe.height = height;\n",
              "    iframe.width = width;\n",
              "    iframe.style.border = 0;\n",
              "    iframe.allow = [\n",
              "        'accelerometer',\n",
              "        'autoplay',\n",
              "        'camera',\n",
              "        'clipboard-read',\n",
              "        'clipboard-write',\n",
              "        'gyroscope',\n",
              "        'magnetometer',\n",
              "        'microphone',\n",
              "        'serial',\n",
              "        'usb',\n",
              "        'xr-spatial-tracking',\n",
              "    ].join('; ');\n",
              "    element.appendChild(iframe);\n",
              "  })(8050, \"/\", \"100%\", 650, false, window.element)"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Draft : Cosine similarity (problem)**"
      ],
      "metadata": {
        "id": "IsQO8e8SJv3N"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "from sklearn.preprocessing import StandardScaler\n",
        "from sklearn.metrics.pairwise import cosine_similarity\n",
        "\n",
        "data1 = data.head(10000)\n",
        "\n",
        "\n",
        "features = data1[['acousticness', 'danceability', 'energy', 'loudness', 'tempo', 'valence']]\n",
        "\n",
        "\n",
        "scaler = StandardScaler()\n",
        "features_scaled = scaler.fit_transform(features)\n",
        "\n",
        "\n",
        "cosine_sim = cosine_similarity(features_scaled)\n",
        "\n",
        "\n",
        "cosine_sim_df = pd.DataFrame(cosine_sim, index=data1['name'], columns=data1['name'])\n",
        "\n",
        "def recommend_songs(name, cosine_sim_df, top_n=10):\n",
        "\n",
        "    similar_songs = cosine_sim_df[name].sort_values(ascending=False).iloc[1:top_n+1]\n",
        "\n",
        "    return similar_songs\n",
        "\n",
        "song_name = input(\"Enter the name of the song you want recommendations for: \")\n",
        "\n",
        "recommendations = recommend_songs(song_name, cosine_sim_df, top_n=5)\n",
        "\n",
        "print(\"Recommended songs:\")\n",
        "print(recommendations)"
      ],
      "metadata": {
        "id": "7fTQHASamFD9",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 599
        },
        "outputId": "0150b014-308d-4974-a68f-47f889cc40cf"
      },
      "execution_count": null,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Enter the name of the song you want recommendations for: Who Am I\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "KeyError",
          "evalue": "'Who Am I'",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/pandas/core/indexes/base.py\u001b[0m in \u001b[0;36mget_loc\u001b[0;34m(self, key)\u001b[0m\n\u001b[1;32m   3804\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 3805\u001b[0;31m             \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_engine\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget_loc\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcasted_key\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   3806\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mKeyError\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0merr\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32mindex.pyx\u001b[0m in \u001b[0;36mpandas._libs.index.IndexEngine.get_loc\u001b[0;34m()\u001b[0m\n",
            "\u001b[0;32mindex.pyx\u001b[0m in \u001b[0;36mpandas._libs.index.IndexEngine.get_loc\u001b[0;34m()\u001b[0m\n",
            "\u001b[0;32mindex.pyx\u001b[0m in \u001b[0;36mpandas._libs.index.IndexEngine._get_loc_duplicates\u001b[0;34m()\u001b[0m\n",
            "\u001b[0;32mindex.pyx\u001b[0m in \u001b[0;36mpandas._libs.index.IndexEngine._maybe_get_bool_indexer\u001b[0;34m()\u001b[0m\n",
            "\u001b[0;32mindex.pyx\u001b[0m in \u001b[0;36mpandas._libs.index._unpack_bool_indexer\u001b[0;34m()\u001b[0m\n",
            "\u001b[0;31mKeyError\u001b[0m: 'Who Am I'",
            "\nThe above exception was the direct cause of the following exception:\n",
            "\u001b[0;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-24-ae56f4878dc8>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     26\u001b[0m \u001b[0msong_name\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0minput\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Enter the name of the song you want recommendations for: \"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     27\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 28\u001b[0;31m \u001b[0mrecommendations\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mrecommend_songs\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0msong_name\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcosine_sim_df\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtop_n\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;36m5\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     29\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     30\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Recommended songs:\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m<ipython-input-24-ae56f4878dc8>\u001b[0m in \u001b[0;36mrecommend_songs\u001b[0;34m(name, cosine_sim_df, top_n)\u001b[0m\n\u001b[1;32m     20\u001b[0m \u001b[0;32mdef\u001b[0m \u001b[0mrecommend_songs\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mname\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcosine_sim_df\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtop_n\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;36m10\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     21\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 22\u001b[0;31m     \u001b[0msimilar_songs\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mcosine_sim_df\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mname\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msort_values\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mascending\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mFalse\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0miloc\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0mtop_n\u001b[0m\u001b[0;34m+\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     23\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     24\u001b[0m     \u001b[0;32mreturn\u001b[0m \u001b[0msimilar_songs\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/pandas/core/frame.py\u001b[0m in \u001b[0;36m__getitem__\u001b[0;34m(self, key)\u001b[0m\n\u001b[1;32m   4100\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcolumns\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mnlevels\u001b[0m \u001b[0;34m>\u001b[0m \u001b[0;36m1\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   4101\u001b[0m                 \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_getitem_multilevel\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 4102\u001b[0;31m             \u001b[0mindexer\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcolumns\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget_loc\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   4103\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0mis_integer\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mindexer\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   4104\u001b[0m                 \u001b[0mindexer\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m[\u001b[0m\u001b[0mindexer\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/pandas/core/indexes/base.py\u001b[0m in \u001b[0;36mget_loc\u001b[0;34m(self, key)\u001b[0m\n\u001b[1;32m   3810\u001b[0m             ):\n\u001b[1;32m   3811\u001b[0m                 \u001b[0;32mraise\u001b[0m \u001b[0mInvalidIndexError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 3812\u001b[0;31m             \u001b[0;32mraise\u001b[0m \u001b[0mKeyError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0merr\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   3813\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mTypeError\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   3814\u001b[0m             \u001b[0;31m# If we have a listlike key, _check_indexing_error will raise\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mKeyError\u001b[0m: 'Who Am I'"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "data1 = data"
      ],
      "metadata": {
        "id": "UdwWLItnNgLK"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.decomposition import PCA\n",
        "from sklearn.preprocessing import StandardScaler\n",
        "\n",
        "# Assume 'data1' contains your feature columns: 'acousticness', 'danceability', etc.\n",
        "features = data1[['acousticness', 'danceability', 'energy', 'loudness', 'tempo', 'valence']]\n",
        "\n",
        "# Standardize the features\n",
        "scaler = StandardScaler()\n",
        "features_scaled = scaler.fit_transform(features)\n",
        "\n",
        "# Apply PCA to reduce the dimensions to 2 components (for example)\n",
        "pca = PCA(n_components=2)\n",
        "features_reduced = pca.fit_transform(features_scaled)\n",
        "\n",
        "# Now 'features_reduced' contains the reduced 2-dimensional data\n"
      ],
      "metadata": {
        "id": "MOHZAbQiSFpf"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "from sklearn.decomposition import PCA\n",
        "from sklearn.preprocessing import StandardScaler\n",
        "from sklearn.neighbors import NearestNeighbors\n",
        "from sklearn.metrics.pairwise import cosine_similarity\n",
        "from scipy.sparse import csr_matrix\n",
        "\n",
        "\n",
        "dataa = data\n",
        "\n",
        "\n",
        "features = dataa[['acousticness', 'danceability', 'energy', 'loudness', 'tempo', 'valence']]\n",
        "\n",
        "\n",
        "scaler = StandardScaler()\n",
        "features_scaled = scaler.fit_transform(features)\n",
        "\n",
        "\n",
        "pca = PCA(n_components=6)\n",
        "features_reduced = pca.fit_transform(features_scaled)\n",
        "\n",
        "\n",
        "features_sparse = csr_matrix(features_reduced)\n",
        "\n",
        "\n",
        "knn = NearestNeighbors(metric='cosine', algorithm='auto', n_neighbors=10)\n",
        "knn.fit(features_sparse)\n",
        "\n",
        "\n",
        "def recommend_song(song_name, data, knn_model):\n",
        "\n",
        "    song_idx = dataa[data['name'] == song_name].index[0]\n",
        "\n",
        "\n",
        "    song_features = features_sparse[song_idx].reshape(1, -1)\n",
        "\n",
        "\n",
        "    distances, indices = knn_model.kneighbors(song_features, n_neighbors=11)\n",
        "\n",
        "\n",
        "    recommended_song_names = dataa.iloc[indices.flatten()[1:]]['name'].tolist()\n",
        "\n",
        "    return recommended_song_names\n",
        "\n",
        "\n",
        "song_to_recommend = \"Little Rock\"\n",
        "recommended_songs = recommend_song(song_to_recommend, data, knn)\n",
        "\n",
        "print(f\"Recommended songs similar to '\\n{song_to_recommend}':\")\n",
        "print(recommended_songs)\n"
      ],
      "metadata": {
        "id": "lZ178bjXUgCa"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import dash\n",
        "import dash_core_components as dcc\n",
        "import dash_html_components as html\n",
        "from dash.dependencies import Input, Output\n",
        "import pandas as pd\n",
        "import numpy as np\n",
        "from sklearn.decomposition import PCA\n",
        "from sklearn.preprocessing import StandardScaler\n",
        "from sklearn.neighbors import NearestNeighbors\n",
        "from sklearn.metrics.pairwise import cosine_similarity\n",
        "from scipy.sparse import csr_matrix\n",
        "\n",
        "\n",
        "dataa = data\n",
        "song_name=['Little Rock', 'Are You With Me', 'Earth Song', 'Earth Song - Radio Edit', 'Please Forgive Me', 'Pagan Poetry']\n",
        "\n",
        "features = dataa[['acousticness', 'danceability', 'energy', 'loudness', 'tempo', 'valence']]\n",
        "\n",
        "\n",
        "scaler = StandardScaler()\n",
        "features_scaled = scaler.fit_transform(features)\n",
        "\n",
        "\n",
        "pca = PCA(n_components=6)\n",
        "features_reduced = pca.fit_transform(features_scaled)\n",
        "\n",
        "\n",
        "features_sparse = csr_matrix(features_reduced)\n",
        "\n",
        "\n",
        "knn = NearestNeighbors(metric='cosine', algorithm='auto', n_neighbors=10)\n",
        "knn.fit(features_sparse)\n",
        "\n",
        "\n",
        "def recommend_song(song_name, data, knn_model):\n",
        "\n",
        "    song_idx = dataa[data['name'] == song_name].index[0]\n",
        "\n",
        "\n",
        "    song_features = features_sparse[song_idx].reshape(1, -1)\n",
        "\n",
        "\n",
        "    distances, indices = knn_model.kneighbors(song_features, n_neighbors=11)\n",
        "\n",
        "\n",
        "    recommended_song_names = dataa.iloc[indices.flatten()[1:]]['name'].tolist()\n",
        "\n",
        "    return recommended_song_names\n",
        "\n",
        "\n",
        "#song_to_recommend = \"Who Am I\"\n",
        "#recommended_songs = recommend_song(song_to_recommend, data, knn)\n",
        "\n",
        "\n",
        "app = dash.Dash(__name__)\n",
        "\n",
        "app.layout = html.Div([\n",
        "\n",
        "       html.Div([\n",
        "        html.H1(\"Music Recommendation System\",\n",
        "                style={\n",
        "                    'textAlign': 'center',\n",
        "                    'color': 'white',\n",
        "                    'padding': '20px',\n",
        "                    'fontFamily': 'Arial, sans-serif'\n",
        "                }),\n",
        "\n",
        "\n",
        "        html.Div([\n",
        "            dcc.Dropdown(\n",
        "                id='song-dropdown',\n",
        "                options=[{'label': song, 'value': song} for song in song_name],\n",
        "                #options=[{'label': song, 'value': song} for song in dataa['name']],\n",
        "                value='Earth Song',\n",
        "                style={\n",
        "                    'width': '300px',\n",
        "                    'margin': '0 auto',\n",
        "                    'fontFamily': 'Arial, sans-serif'\n",
        "                }\n",
        "            )\n",
        "        ], style={'display': 'flex', 'justifyContent': 'center', 'marginBottom': '20px'}),\n",
        "\n",
        "\n",
        "        html.Div(id='recommendations-output',\n",
        "                 style={\n",
        "                     'textAlign': 'center',\n",
        "                     'color': 'white',\n",
        "                     'fontFamily': 'Arial, sans-serif'\n",
        "                 })\n",
        "    ], style={\n",
        "        'backgroundColor': 'rgba(0,0,0,0.7)',\n",
        "        'maxWidth': '600px',\n",
        "        'margin': '0 auto',\n",
        "        'borderRadius': '10px',\n",
        "        'padding': '20px'\n",
        "    })\n",
        "])\n",
        "\n",
        "\n",
        "@app.callback(\n",
        "    Output('recommendations-output', 'children'),\n",
        "    [Input('song-dropdown', 'value')]\n",
        ")\n",
        "def update_recommendations(selected_song):\n",
        "\n",
        "    recommended_songs = recommend_song(selected_song, dataa, knn)\n",
        "\n",
        "    song_list = [html.Div(f\"{i + 1}. {song}\") for i, song in enumerate(recommended_songs)]\n",
        "\n",
        "    return [html.Div(f\"Recommended songs for '{selected_song}':\"), *song_list]\n",
        "\n",
        "if __name__ == '__main__':\n",
        "    app.run_server(debug=True)\n"
      ],
      "metadata": {
        "id": "ZbZ8bq0TK7dV"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}