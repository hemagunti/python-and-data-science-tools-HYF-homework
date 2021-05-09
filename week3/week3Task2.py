{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'pd' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-1-d209c2116547>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mdf\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mpd\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mread_csv\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'SMSSpamCollection.txt'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mdelimiter\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m\"\\t\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mnames\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m's'\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m't'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m: name 'pd' is not defined"
     ]
    }
   ],
   "source": [
    "df = pd.read_csv('SMSSpamCollection.txt', delimiter = \"\\t\", names=['s','t'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv('SMSSpamCollection.txt', delimiter = \"\\t\", names=['s','t'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
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
       "      <th>s</th>\n",
       "      <th>t</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>ham</td>\n",
       "      <td>Go until jurong point, crazy.. Available only ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>ham</td>\n",
       "      <td>Ok lar... Joking wif u oni...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>spam</td>\n",
       "      <td>Free entry in 2 a wkly comp to win FA Cup fina...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>ham</td>\n",
       "      <td>U dun say so early hor... U c already then say...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>ham</td>\n",
       "      <td>Nah I don't think he goes to usf, he lives aro...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5567</th>\n",
       "      <td>spam</td>\n",
       "      <td>This is the 2nd time we have tried 2 contact u...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5568</th>\n",
       "      <td>ham</td>\n",
       "      <td>Will ü b going to esplanade fr home?</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5569</th>\n",
       "      <td>ham</td>\n",
       "      <td>Pity, * was in mood for that. So...any other s...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5570</th>\n",
       "      <td>ham</td>\n",
       "      <td>The guy did some bitching but I acted like i'd...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5571</th>\n",
       "      <td>ham</td>\n",
       "      <td>Rofl. Its true to its name</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5572 rows × 2 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "         s                                                  t\n",
       "0      ham  Go until jurong point, crazy.. Available only ...\n",
       "1      ham                      Ok lar... Joking wif u oni...\n",
       "2     spam  Free entry in 2 a wkly comp to win FA Cup fina...\n",
       "3      ham  U dun say so early hor... U c already then say...\n",
       "4      ham  Nah I don't think he goes to usf, he lives aro...\n",
       "...    ...                                                ...\n",
       "5567  spam  This is the 2nd time we have tried 2 contact u...\n",
       "5568   ham               Will ü b going to esplanade fr home?\n",
       "5569   ham  Pity, * was in mood for that. So...any other s...\n",
       "5570   ham  The guy did some bitching but I acted like i'd...\n",
       "5571   ham                         Rofl. Its true to its name\n",
       "\n",
       "[5572 rows x 2 columns]"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['s', 't']"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "import re\n",
    "df['l'] = df['t'].str.len()\n",
    "df['f'] = df.t.str.extract('([A-Z_]+)')\n",
    "df['fl'] = df['f'].str.len()\n",
    "df2 = df.t.str.extractall('([A-Z_]+)') # note that this is a data frame with hierarchical indexing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
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
       "      <th></th>\n",
       "      <th>0</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>text</th>\n",
       "      <th>no</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th rowspan=\"3\" valign=\"top\">0</th>\n",
       "      <th>0</th>\n",
       "      <td>G</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>A</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th rowspan=\"2\" valign=\"top\">1</th>\n",
       "      <th>0</th>\n",
       "      <td>O</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>J</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5569</th>\n",
       "      <th>1</th>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th rowspan=\"2\" valign=\"top\">5570</th>\n",
       "      <th>0</th>\n",
       "      <td>T</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>I</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th rowspan=\"2\" valign=\"top\">5571</th>\n",
       "      <th>0</th>\n",
       "      <td>R</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>I</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>19324 rows × 1 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "         0\n",
       "text no   \n",
       "0    0   G\n",
       "     1   A\n",
       "     2   C\n",
       "1    0   O\n",
       "     1   J\n",
       "...     ..\n",
       "5569 1   S\n",
       "5570 0   T\n",
       "     1   I\n",
       "5571 0   R\n",
       "     1   I\n",
       "\n",
       "[19324 rows x 1 columns]"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df2.index.names = ['text','no']\n",
    "df2\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "df['uc'] = df2.groupby(level=[0]).sum()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "df['ucl'] = df['uc'].str.len()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['s', 't', 'l', 'f', 'fl', 'uc', 'ucl']"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "list(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
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
       "      <th>s</th>\n",
       "      <th>t</th>\n",
       "      <th>l</th>\n",
       "      <th>f</th>\n",
       "      <th>fl</th>\n",
       "      <th>uc</th>\n",
       "      <th>ucl</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>ham</td>\n",
       "      <td>Go until jurong point, crazy.. Available only ...</td>\n",
       "      <td>111</td>\n",
       "      <td>G</td>\n",
       "      <td>1.0</td>\n",
       "      <td>GAC</td>\n",
       "      <td>3.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>ham</td>\n",
       "      <td>Ok lar... Joking wif u oni...</td>\n",
       "      <td>29</td>\n",
       "      <td>O</td>\n",
       "      <td>1.0</td>\n",
       "      <td>OJ</td>\n",
       "      <td>2.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>spam</td>\n",
       "      <td>Free entry in 2 a wkly comp to win FA Cup fina...</td>\n",
       "      <td>155</td>\n",
       "      <td>F</td>\n",
       "      <td>1.0</td>\n",
       "      <td>FFACMTFATC</td>\n",
       "      <td>10.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>ham</td>\n",
       "      <td>U dun say so early hor... U c already then say...</td>\n",
       "      <td>49</td>\n",
       "      <td>U</td>\n",
       "      <td>1.0</td>\n",
       "      <td>UU</td>\n",
       "      <td>2.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>ham</td>\n",
       "      <td>Nah I don't think he goes to usf, he lives aro...</td>\n",
       "      <td>61</td>\n",
       "      <td>N</td>\n",
       "      <td>1.0</td>\n",
       "      <td>NI</td>\n",
       "      <td>2.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5567</th>\n",
       "      <td>spam</td>\n",
       "      <td>This is the 2nd time we have tried 2 contact u...</td>\n",
       "      <td>160</td>\n",
       "      <td>T</td>\n",
       "      <td>1.0</td>\n",
       "      <td>TUPNOWOBT</td>\n",
       "      <td>9.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5568</th>\n",
       "      <td>ham</td>\n",
       "      <td>Will ü b going to esplanade fr home?</td>\n",
       "      <td>36</td>\n",
       "      <td>W</td>\n",
       "      <td>1.0</td>\n",
       "      <td>W</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5569</th>\n",
       "      <td>ham</td>\n",
       "      <td>Pity, * was in mood for that. So...any other s...</td>\n",
       "      <td>57</td>\n",
       "      <td>P</td>\n",
       "      <td>1.0</td>\n",
       "      <td>PS</td>\n",
       "      <td>2.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5570</th>\n",
       "      <td>ham</td>\n",
       "      <td>The guy did some bitching but I acted like i'd...</td>\n",
       "      <td>125</td>\n",
       "      <td>T</td>\n",
       "      <td>1.0</td>\n",
       "      <td>TI</td>\n",
       "      <td>2.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5571</th>\n",
       "      <td>ham</td>\n",
       "      <td>Rofl. Its true to its name</td>\n",
       "      <td>26</td>\n",
       "      <td>R</td>\n",
       "      <td>1.0</td>\n",
       "      <td>RI</td>\n",
       "      <td>2.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5572 rows × 7 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "         s                                                  t    l  f   fl  \\\n",
       "0      ham  Go until jurong point, crazy.. Available only ...  111  G  1.0   \n",
       "1      ham                      Ok lar... Joking wif u oni...   29  O  1.0   \n",
       "2     spam  Free entry in 2 a wkly comp to win FA Cup fina...  155  F  1.0   \n",
       "3      ham  U dun say so early hor... U c already then say...   49  U  1.0   \n",
       "4      ham  Nah I don't think he goes to usf, he lives aro...   61  N  1.0   \n",
       "...    ...                                                ...  ... ..  ...   \n",
       "5567  spam  This is the 2nd time we have tried 2 contact u...  160  T  1.0   \n",
       "5568   ham               Will ü b going to esplanade fr home?   36  W  1.0   \n",
       "5569   ham  Pity, * was in mood for that. So...any other s...   57  P  1.0   \n",
       "5570   ham  The guy did some bitching but I acted like i'd...  125  T  1.0   \n",
       "5571   ham                         Rofl. Its true to its name   26  R  1.0   \n",
       "\n",
       "              uc   ucl  \n",
       "0            GAC   3.0  \n",
       "1             OJ   2.0  \n",
       "2     FFACMTFATC  10.0  \n",
       "3             UU   2.0  \n",
       "4             NI   2.0  \n",
       "...          ...   ...  \n",
       "5567   TUPNOWOBT   9.0  \n",
       "5568           W   1.0  \n",
       "5569          PS   2.0  \n",
       "5570          TI   2.0  \n",
       "5571          RI   2.0  \n",
       "\n",
       "[5572 rows x 7 columns]"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "df['ucr'] = df['ucl'].div(df['l'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0       0.027027\n",
       "1       0.068966\n",
       "2       0.064516\n",
       "3       0.040816\n",
       "4       0.032787\n",
       "          ...   \n",
       "5567    0.056250\n",
       "5568    0.027778\n",
       "5569    0.035088\n",
       "5570    0.016000\n",
       "5571    0.076923\n",
       "Name: ucr, Length: 5572, dtype: float64"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['ucr']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
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
       "      <th>ucr</th>\n",
       "      <th>ucl</th>\n",
       "      <th>l</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0.027027</td>\n",
       "      <td>3.0</td>\n",
       "      <td>111</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0.068966</td>\n",
       "      <td>2.0</td>\n",
       "      <td>29</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0.064516</td>\n",
       "      <td>10.0</td>\n",
       "      <td>155</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0.040816</td>\n",
       "      <td>2.0</td>\n",
       "      <td>49</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0.032787</td>\n",
       "      <td>2.0</td>\n",
       "      <td>61</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5567</th>\n",
       "      <td>0.056250</td>\n",
       "      <td>9.0</td>\n",
       "      <td>160</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5568</th>\n",
       "      <td>0.027778</td>\n",
       "      <td>1.0</td>\n",
       "      <td>36</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5569</th>\n",
       "      <td>0.035088</td>\n",
       "      <td>2.0</td>\n",
       "      <td>57</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5570</th>\n",
       "      <td>0.016000</td>\n",
       "      <td>2.0</td>\n",
       "      <td>125</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5571</th>\n",
       "      <td>0.076923</td>\n",
       "      <td>2.0</td>\n",
       "      <td>26</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5572 rows × 3 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "           ucr   ucl    l\n",
       "0     0.027027   3.0  111\n",
       "1     0.068966   2.0   29\n",
       "2     0.064516  10.0  155\n",
       "3     0.040816   2.0   49\n",
       "4     0.032787   2.0   61\n",
       "...        ...   ...  ...\n",
       "5567  0.056250   9.0  160\n",
       "5568  0.027778   1.0   36\n",
       "5569  0.035088   2.0   57\n",
       "5570  0.016000   2.0  125\n",
       "5571  0.076923   2.0   26\n",
       "\n",
       "[5572 rows x 3 columns]"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[['ucr', 'ucl', 'l']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([<AxesSubplot:title={'center':'ham'}>,\n",
       "       <AxesSubplot:title={'center':'spam'}>], dtype=object)"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "%matplotlib inline\n",
    "df[df.l < 200].hist(column = 'l', bins = 50, by = 's')\n",
    "df[df.ucr < .35].hist(column = 'ucr', bins = 50, by = 's')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
