import pandas as pd
import numpy as np

# Specify the input CSV file path
sim_file = 'totalseries.csv'
# Specify the observation CSV file path
obs_file='observation.csv'
# Specify the filtered CSV file path
output_file='filtered_data.csv'
def filterdata(sim_file):
    """
    Reads a CSV file ('totalseries.csv'), filters the data based on the first and tenth columns,
    converts the 'Time' column which is integer, and saves the filtered data to a new CSV file ('filtered_data.csv').

    Returns:
    filtered_df

    """
    df = pd.read_csv(sim_file, usecols=[0, 10], skiprows=1) 
    df['Time'] = pd.to_numeric(df['Time'])  # Convert values in 'Column1' to numeric
    filtered_df= df[df['Time'].astype(int) == df['Time']]  # Filter rows with integer values in first column
    filtered_df.to_csv('filtered_data.csv', index=False)
    return filtered_df

def nse(obs_file):
    obs_df = pd.read_csv(obs_file)
    output_df = pd.read_csv(output_file)
    

    # Calculate the Nash-Sutcliffe Efficiency
    nse = 1 - np.sum((output_df.Channels - obs_df.Channels) ** 2) / np.sum((obs_df.Channels - obs_df.Channels.mean()) ** 2)

    print('Nash-Sutcliffe Efficiency:', nse)
    return nse

filterdata(sim_file)
nse(obs_file)

    