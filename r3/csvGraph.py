import csv 
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
plt.ion()  # Enable interactive mode
matplotlib.use("TkAgg")

def plot_data_chatgpt(csv_file):
    import pandas as pd
    import matplotlib.pyplot as plt

    # Read the CSV file
    df = pd.read_csv(csv_file, sep=';')

    # Convert timestamp to datetime format
    # df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Separate data for each product
    products = df['product'].unique()

    for product in products:
        product_data = df[df['product'] == product]
        
        # Plot mid price
        plt.figure(figsize=(10, 5))
        plt.plot(product_data['timestamp'], product_data['mid_price'], label='Mid Price')
        plt.xlabel('Timestamp')
        plt.ylabel('Mid Price')
        plt.title(f'{product} Mid Price')
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.ion()  # Enable interactive mode
        plt.show()
        plt.savefig(f'mid_price_plot_{product}1.png')  # Save the plot to a file
        
        # Plot histograms for mid price, bid prices, and ask prices
        plt.figure(figsize=(12, 6))
        plt.hist(product_data['mid_price'], bins=30, alpha=0.5, label='Mid Price')
        plt.hist(product_data[['bid_price_1', 'bid_price_2', 'bid_price_3']].values.flatten(), bins=30, alpha=0.5, label='Bid Prices')
        plt.hist(product_data[['ask_price_1', 'ask_price_2', 'ask_price_3']].values.flatten(), bins=30, alpha=0.5, label='Ask Prices')
        plt.xlabel('Price')
        plt.ylabel('Frequency')
        plt.title(f'{product} Price Histograms')
        plt.legend()
        plt.tight_layout()
        plt.ion()  # Enable interactive mode
        plt.show()
        plt.savefig(f'mid_price_plot_{product}2.png')  # Save the plot to a file


def plot_data(csv_file):
    """
    Reads a CSV file, plots separate graphs for each product,
    and creates a histogram using midprice, bid prices, and ask prices.

    Args:
        csv_file (str): Path to the CSV file.
    """

    try:
        # Read the CSV file using pandas
        data = pd.read_csv(csv_file, sep = ';')
        print(data, type(data))
        print(data.product)
        # Create separate graphs for each product
        unique_products = data['product'].unique()
        for product in unique_products:
            product_data = data[data['product'] == product]
            plt.figure(figsize=(10, 6))  # Set appropriate figure size
            plt.plot(product_data['timestamp'], product_data['bid_price_1'], label='Bid Price 1')
            plt.plot(product_data['timestamp'], product_data['bid_price_2'], label='Bid Price 2')
            plt.plot(product_data['timestamp'], product_data['bid_price_3'], label='Bid Price 3')
            plt.plot(product_data['timestamp'], product_data['ask_price_1'], label='Ask Price 1')
            plt.plot(product_data['timestamp'], product_data['ask_price_2'], label='Ask Price 2')
            plt.plot(product_data['timestamp'], product_data['ask_price_3'], label='Ask Price 3')
            plt.plot(product_data['timestamp'], product_data['mid_price'], label='Mid Price')
            plt.title(f"Price Trends for Product: {product}")
            plt.xlabel('Timestamp')
            plt.ylabel('Price')
            plt.legend()
            plt.grid(True)
            plt.ion()  # Enable interactive mode
            plt.show()
            plt.savefig(f'mid_price_plot_{product}_3.png')  # Save the plot to a file

        # Create a histogram using midprice, bid prices, and ask prices
        plt.figure(figsize=(12, 6))  # Adjust figure size for better readability
        plt.hist(data['mid_price'], bins=20, alpha=0.7, label='Mid Price')
        plt.hist(data['bid_price_1'], bins=20, alpha=0.5, label='Bid Price 1')
        plt.hist(data['bid_price_2'], bins=20, alpha=0.5, label='Bid Price 2')
        plt.hist(data['bid_price_3'], bins=20, alpha=0.5, label='Bid Price 3')
        plt.hist(data['ask_price_1'], bins=20, alpha=0.5, label='Ask Price 1')
        plt.hist(data['ask_price_2'], bins=20, alpha=0.5, label='Ask Price 2')
        plt.hist(data['ask_price_3'], bins=20, alpha=0.5, label='Ask Price 3')
        plt.title('Distribution of Prices')
        plt.xlabel('Price')
        plt.ylabel('Frequency')
        plt.legend()
        plt.grid(True)
        plt.ion()  # Enable interactive mode
        plt.show()
        plt.savefig(f'mid_price_plot_{product}_4.png')  # Save the plot to a file

    except FileNotFoundError:
        print("Error: CSV file not found. Please check the file path.")

if __name__ == "__main__":
    csv_file = "/home/puneeth/Downloads/773dbdf0-e4f0-4a60-83f2-05d2d1bfa564.csv"  # Replace with the actual path to your CSV file
    plot_data(csv_file)
    plot_data_chatgpt(csv_file)
    # plot_3(csv_file)
    # plot_4(csv_file)




# import pandas as pd

# def parse_data(data_string):
#   # Split the data string by semicolons
#   data_list = data_string.split(';')
#   # Create a dictionary to store data points
#   data_dict = {}
#   # Assuming there are 18 features (modify based on your actual number)
#   for i in range(18):
#     data_dict[f"feature_{i+1}"] = data_list[i]
#   return data_dict

# def plot_4(csv_file):
#     # Read the entire CSV file content (assuming it's a small file)
#     with open(csv_file, 'r') as f:
#         csv_data = f.read()

#         # Skip the header row if present (adjust index if needed)
#         lines = csv_data.splitlines()
#         parsed_data = []
#         for line in lines[1:]:  # Skip the header row
#             parsed_data.append(parse_data(line))

#         # Create a DataFrame from the parsed data
#         df = pd.DataFrame(parsed_data)

#         # Now you can access data by column names (e.g., df['feature_3'] for "product")
#         print(df.head())  # Display the first few rows

# def plot_3(csv_file):
#     import pandas as pd
#     from matplotlib import pyplot as plt
#     plt.rcParams["figure.figsize"] = [7.00, 3.50]
#     plt.rcParams["figure.autolayout"] = True
#     columns = ['day', 'timestamp', 'product', 'bid_price_1', 'bid_volume_1', 'bid_price_2', 'bid_volume_2', 'bid_price_3', 'bid_volume_3', 'ask_price_1', 'ask_volume_1', 'ask_price_2', 'ask_volume_2', 'ask_price_3', 'ask_volume_3', 'mid_price', 'profit_and_loss']
#     df = pd.read_csv(csv_file, header=None, sep = ';')
#     print("Contents in csv file:\n", df[0])
#     df.columns = df.iloc[0]
#     df = df[1:]
#     print("Contents in csv file:", df)
#     plt.plot(df.day, df.timestamp)
#     plt.ion()  # Enable interactive mode
#     plt.show()
#     plt.savefig('mid_price_plot5.png')  # Save the plot to a file
