

```python
# Dependencies
import pandas as pd
import numpy as np
```


```python
# Files to Load 
measure_load = "resources/hawaii_measurements.csv"
station_load = "resources/hawaii_stations.csv"

# Read Data Files and store into Pandas Data Frames
measure_df = pd.read_csv(measure_load)
station_df = pd.read_csv(station_load)
```


```python
measure_df.head(20)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>station</th>
      <th>date</th>
      <th>prcp</th>
      <th>tobs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>USC00519397</td>
      <td>2010-01-01</td>
      <td>0.08</td>
      <td>65</td>
    </tr>
    <tr>
      <th>1</th>
      <td>USC00519397</td>
      <td>2010-01-02</td>
      <td>0.00</td>
      <td>63</td>
    </tr>
    <tr>
      <th>2</th>
      <td>USC00519397</td>
      <td>2010-01-03</td>
      <td>0.00</td>
      <td>74</td>
    </tr>
    <tr>
      <th>3</th>
      <td>USC00519397</td>
      <td>2010-01-04</td>
      <td>0.00</td>
      <td>76</td>
    </tr>
    <tr>
      <th>4</th>
      <td>USC00519397</td>
      <td>2010-01-06</td>
      <td>NaN</td>
      <td>73</td>
    </tr>
    <tr>
      <th>5</th>
      <td>USC00519397</td>
      <td>2010-01-07</td>
      <td>0.06</td>
      <td>70</td>
    </tr>
    <tr>
      <th>6</th>
      <td>USC00519397</td>
      <td>2010-01-08</td>
      <td>0.00</td>
      <td>64</td>
    </tr>
    <tr>
      <th>7</th>
      <td>USC00519397</td>
      <td>2010-01-09</td>
      <td>0.00</td>
      <td>68</td>
    </tr>
    <tr>
      <th>8</th>
      <td>USC00519397</td>
      <td>2010-01-10</td>
      <td>0.00</td>
      <td>73</td>
    </tr>
    <tr>
      <th>9</th>
      <td>USC00519397</td>
      <td>2010-01-11</td>
      <td>0.01</td>
      <td>64</td>
    </tr>
    <tr>
      <th>10</th>
      <td>USC00519397</td>
      <td>2010-01-12</td>
      <td>0.00</td>
      <td>61</td>
    </tr>
    <tr>
      <th>11</th>
      <td>USC00519397</td>
      <td>2010-01-14</td>
      <td>0.00</td>
      <td>66</td>
    </tr>
    <tr>
      <th>12</th>
      <td>USC00519397</td>
      <td>2010-01-15</td>
      <td>0.00</td>
      <td>65</td>
    </tr>
    <tr>
      <th>13</th>
      <td>USC00519397</td>
      <td>2010-01-16</td>
      <td>0.00</td>
      <td>68</td>
    </tr>
    <tr>
      <th>14</th>
      <td>USC00519397</td>
      <td>2010-01-17</td>
      <td>0.00</td>
      <td>64</td>
    </tr>
    <tr>
      <th>15</th>
      <td>USC00519397</td>
      <td>2010-01-18</td>
      <td>0.00</td>
      <td>72</td>
    </tr>
    <tr>
      <th>16</th>
      <td>USC00519397</td>
      <td>2010-01-19</td>
      <td>0.00</td>
      <td>66</td>
    </tr>
    <tr>
      <th>17</th>
      <td>USC00519397</td>
      <td>2010-01-20</td>
      <td>0.00</td>
      <td>66</td>
    </tr>
    <tr>
      <th>18</th>
      <td>USC00519397</td>
      <td>2010-01-21</td>
      <td>0.00</td>
      <td>69</td>
    </tr>
    <tr>
      <th>19</th>
      <td>USC00519397</td>
      <td>2010-01-22</td>
      <td>0.00</td>
      <td>67</td>
    </tr>
  </tbody>
</table>
</div>




```python
measure_df.count()
```




    station    19550
    date       19550
    prcp       18103
    tobs       19550
    dtype: int64




```python
# drop any rows containing NaN (1447 rows is < 10%) and avoid making up data
measure_clean = measure_df.dropna()

measure_clean.head(15)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>station</th>
      <th>date</th>
      <th>prcp</th>
      <th>tobs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>USC00519397</td>
      <td>2010-01-01</td>
      <td>0.08</td>
      <td>65</td>
    </tr>
    <tr>
      <th>1</th>
      <td>USC00519397</td>
      <td>2010-01-02</td>
      <td>0.00</td>
      <td>63</td>
    </tr>
    <tr>
      <th>2</th>
      <td>USC00519397</td>
      <td>2010-01-03</td>
      <td>0.00</td>
      <td>74</td>
    </tr>
    <tr>
      <th>3</th>
      <td>USC00519397</td>
      <td>2010-01-04</td>
      <td>0.00</td>
      <td>76</td>
    </tr>
    <tr>
      <th>5</th>
      <td>USC00519397</td>
      <td>2010-01-07</td>
      <td>0.06</td>
      <td>70</td>
    </tr>
    <tr>
      <th>6</th>
      <td>USC00519397</td>
      <td>2010-01-08</td>
      <td>0.00</td>
      <td>64</td>
    </tr>
    <tr>
      <th>7</th>
      <td>USC00519397</td>
      <td>2010-01-09</td>
      <td>0.00</td>
      <td>68</td>
    </tr>
    <tr>
      <th>8</th>
      <td>USC00519397</td>
      <td>2010-01-10</td>
      <td>0.00</td>
      <td>73</td>
    </tr>
    <tr>
      <th>9</th>
      <td>USC00519397</td>
      <td>2010-01-11</td>
      <td>0.01</td>
      <td>64</td>
    </tr>
    <tr>
      <th>10</th>
      <td>USC00519397</td>
      <td>2010-01-12</td>
      <td>0.00</td>
      <td>61</td>
    </tr>
    <tr>
      <th>11</th>
      <td>USC00519397</td>
      <td>2010-01-14</td>
      <td>0.00</td>
      <td>66</td>
    </tr>
    <tr>
      <th>12</th>
      <td>USC00519397</td>
      <td>2010-01-15</td>
      <td>0.00</td>
      <td>65</td>
    </tr>
    <tr>
      <th>13</th>
      <td>USC00519397</td>
      <td>2010-01-16</td>
      <td>0.00</td>
      <td>68</td>
    </tr>
    <tr>
      <th>14</th>
      <td>USC00519397</td>
      <td>2010-01-17</td>
      <td>0.00</td>
      <td>64</td>
    </tr>
    <tr>
      <th>15</th>
      <td>USC00519397</td>
      <td>2010-01-18</td>
      <td>0.00</td>
      <td>72</td>
    </tr>
  </tbody>
</table>
</div>




```python
measure_clean.count()
```




    station    18103
    date       18103
    prcp       18103
    tobs       18103
    dtype: int64




```python
station_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>station</th>
      <th>name</th>
      <th>latitude</th>
      <th>longitude</th>
      <th>elevation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>USC00519397</td>
      <td>WAIKIKI 717.2, HI US</td>
      <td>21.27160</td>
      <td>-157.81680</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>USC00513117</td>
      <td>KANEOHE 838.1, HI US</td>
      <td>21.42340</td>
      <td>-157.80150</td>
      <td>14.6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>USC00514830</td>
      <td>KUALOA RANCH HEADQUARTERS 886.9, HI US</td>
      <td>21.52130</td>
      <td>-157.83740</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>USC00517948</td>
      <td>PEARL CITY, HI US</td>
      <td>21.39340</td>
      <td>-157.97510</td>
      <td>11.9</td>
    </tr>
    <tr>
      <th>4</th>
      <td>USC00518838</td>
      <td>UPPER WAHIAWA 874.3, HI US</td>
      <td>21.49920</td>
      <td>-158.01110</td>
      <td>306.6</td>
    </tr>
    <tr>
      <th>5</th>
      <td>USC00519523</td>
      <td>WAIMANALO EXPERIMENTAL FARM, HI US</td>
      <td>21.33556</td>
      <td>-157.71139</td>
      <td>19.5</td>
    </tr>
    <tr>
      <th>6</th>
      <td>USC00519281</td>
      <td>WAIHEE 837.5, HI US</td>
      <td>21.45167</td>
      <td>-157.84889</td>
      <td>32.9</td>
    </tr>
    <tr>
      <th>7</th>
      <td>USC00511918</td>
      <td>HONOLULU OBSERVATORY 702.2, HI US</td>
      <td>21.31520</td>
      <td>-157.99920</td>
      <td>0.9</td>
    </tr>
    <tr>
      <th>8</th>
      <td>USC00516128</td>
      <td>MANOA LYON ARBO 785.2, HI US</td>
      <td>21.33310</td>
      <td>-157.80250</td>
      <td>152.4</td>
    </tr>
  </tbody>
</table>
</div>




```python
# save cleaned data to csv
measure_clean.to_csv("resources/clean_hawaii_measurements.csv", index=False)
station_df.to_csv("resources/clean_hawaii_stations.csv", index=False)
```
