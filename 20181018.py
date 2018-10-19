{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 23,
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
       "      <th>年　齢</th>\n",
       "      <th>身長(男)</th>\n",
       "      <th>体重(男)</th>\n",
       "      <th>身長(女)</th>\n",
       "      <th>体重(女)</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>77.8</td>\n",
       "      <td>10.1</td>\n",
       "      <td>78.4</td>\n",
       "      <td>10.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>88.7</td>\n",
       "      <td>12.5</td>\n",
       "      <td>87.2</td>\n",
       "      <td>12.1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>96.7</td>\n",
       "      <td>14.3</td>\n",
       "      <td>96.2</td>\n",
       "      <td>14.1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>103.2</td>\n",
       "      <td>16.6</td>\n",
       "      <td>101.2</td>\n",
       "      <td>15.6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>110.9</td>\n",
       "      <td>18.7</td>\n",
       "      <td>108.3</td>\n",
       "      <td>17.2</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  年　齢  身長(男)  体重(男)  身長(女)  体重(女)\n",
       "0   1   77.8   10.1   78.4   10.0\n",
       "1   2   88.7   12.5   87.2   12.1\n",
       "2   3   96.7   14.3   96.2   14.1\n",
       "3   4  103.2   16.6  101.2   15.6\n",
       "4   5  110.9   18.7  108.3   17.2"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "%matplotlib inline\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "from scipy import signal\n",
    "import pandas as pd\n",
    "df = pd.read_csv('20181018.csv',encoding='utf-8')\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "Must pass DataFrame with boolean values only",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-30-e62f398bae5b>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mdf_height_man\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mdf\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mdf\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0miloc\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[0mdf_weight_man\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mdf\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0miloc\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[0mdf_height_woman\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mdf\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0miloc\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m3\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[0mdf_weight_woman\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mdf\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0miloc\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m4\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\AppData\\Local\\Continuum\\anaconda3\\lib\\site-packages\\pandas\\core\\frame.py\u001b[0m in \u001b[0;36m__getitem__\u001b[1;34m(self, key)\u001b[0m\n\u001b[0;32m   2679\u001b[0m             \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_getitem_array\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   2680\u001b[0m         \u001b[1;32melif\u001b[0m \u001b[0misinstance\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mDataFrame\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 2681\u001b[1;33m             \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_getitem_frame\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   2682\u001b[0m         \u001b[1;32melif\u001b[0m \u001b[0mis_mi_columns\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   2683\u001b[0m             \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_getitem_multilevel\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\AppData\\Local\\Continuum\\anaconda3\\lib\\site-packages\\pandas\\core\\frame.py\u001b[0m in \u001b[0;36m_getitem_frame\u001b[1;34m(self, key)\u001b[0m\n\u001b[0;32m   2762\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0m_getitem_frame\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mkey\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   2763\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mkey\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mvalues\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msize\u001b[0m \u001b[1;32mand\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[0mis_bool_dtype\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mvalues\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 2764\u001b[1;33m             \u001b[1;32mraise\u001b[0m \u001b[0mValueError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'Must pass DataFrame with boolean values only'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   2765\u001b[0m         \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mwhere\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   2766\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mValueError\u001b[0m: Must pass DataFrame with boolean values only"
     ]
    }
   ],
   "source": [
    "df_height_man = df[df.iloc[:,0:1]]\n",
    "df_weight_man = df.iloc[:,[0,2]]\n",
    "df_height_woman = df.iloc[:,[0,3]]\n",
    "df_weight_woman = df.iloc[:,[0,4]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "Empty 'DataFrame': no numeric data to plot",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-31-1b8395572d86>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mdf_height_man\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mplot\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mkind\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m'bar'\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0msubplots\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mTrue\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mlayout\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mfigsize\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m20\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m10\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m;\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m~\\AppData\\Local\\Continuum\\anaconda3\\lib\\site-packages\\pandas\\plotting\\_core.py\u001b[0m in \u001b[0;36m__call__\u001b[1;34m(self, x, y, kind, ax, subplots, sharex, sharey, layout, figsize, use_index, title, grid, legend, style, logx, logy, loglog, xticks, yticks, xlim, ylim, rot, fontsize, colormap, table, yerr, xerr, secondary_y, sort_columns, **kwds)\u001b[0m\n\u001b[0;32m   2939\u001b[0m                           \u001b[0mfontsize\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mfontsize\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mcolormap\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mcolormap\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mtable\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mtable\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   2940\u001b[0m                           \u001b[0myerr\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0myerr\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mxerr\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mxerr\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0msecondary_y\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0msecondary_y\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 2941\u001b[1;33m                           sort_columns=sort_columns, **kwds)\n\u001b[0m\u001b[0;32m   2942\u001b[0m     \u001b[0m__call__\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m__doc__\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mplot_frame\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m__doc__\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   2943\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\AppData\\Local\\Continuum\\anaconda3\\lib\\site-packages\\pandas\\plotting\\_core.py\u001b[0m in \u001b[0;36mplot_frame\u001b[1;34m(data, x, y, kind, ax, subplots, sharex, sharey, layout, figsize, use_index, title, grid, legend, style, logx, logy, loglog, xticks, yticks, xlim, ylim, rot, fontsize, colormap, table, yerr, xerr, secondary_y, sort_columns, **kwds)\u001b[0m\n\u001b[0;32m   1975\u001b[0m                  \u001b[0myerr\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0myerr\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mxerr\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mxerr\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1976\u001b[0m                  \u001b[0msecondary_y\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0msecondary_y\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0msort_columns\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0msort_columns\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1977\u001b[1;33m                  **kwds)\n\u001b[0m\u001b[0;32m   1978\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1979\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\AppData\\Local\\Continuum\\anaconda3\\lib\\site-packages\\pandas\\plotting\\_core.py\u001b[0m in \u001b[0;36m_plot\u001b[1;34m(data, x, y, subplots, ax, kind, **kwds)\u001b[0m\n\u001b[0;32m   1802\u001b[0m         \u001b[0mplot_obj\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mklass\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdata\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0msubplots\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0msubplots\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0max\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0max\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mkind\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mkind\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwds\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1803\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1804\u001b[1;33m     \u001b[0mplot_obj\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mgenerate\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1805\u001b[0m     \u001b[0mplot_obj\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdraw\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1806\u001b[0m     \u001b[1;32mreturn\u001b[0m \u001b[0mplot_obj\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mresult\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\AppData\\Local\\Continuum\\anaconda3\\lib\\site-packages\\pandas\\plotting\\_core.py\u001b[0m in \u001b[0;36mgenerate\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m    256\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mgenerate\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    257\u001b[0m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_args_adjust\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 258\u001b[1;33m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_compute_plot_data\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    259\u001b[0m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_setup_subplots\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    260\u001b[0m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_make_plot\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\AppData\\Local\\Continuum\\anaconda3\\lib\\site-packages\\pandas\\plotting\\_core.py\u001b[0m in \u001b[0;36m_compute_plot_data\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m    371\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mis_empty\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    372\u001b[0m             raise TypeError('Empty {0!r}: no numeric data to '\n\u001b[1;32m--> 373\u001b[1;33m                             'plot'.format(numeric_data.__class__.__name__))\n\u001b[0m\u001b[0;32m    374\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    375\u001b[0m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdata\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mnumeric_data\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mTypeError\u001b[0m: Empty 'DataFrame': no numeric data to plot"
     ]
    }
   ],
   "source": [
    "df_height_man.plot(kind='bar',subplots=True,layout=(2,2),figsize=(20,10));"
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
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
