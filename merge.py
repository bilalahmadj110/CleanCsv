import pandas as pd
import os
import time

# config
INPUT_PATH = r"C:\Users\Bilal Ahmad\Documents\Fiverr\ttmedia_agency\inputs"
OUTPUT_PATH = r"C:\Users\Bilal Ahmad\Documents\Fiverr\ttmedia_agency\outputs"
# columns position maping to name
# Florian	Fischer	http://www.linkedin.com/in/fischerfl	SlopeLift	slopelift.com	Austria	florian.fischer@slopelift.com	http://www.linkedin.com/company/slopelift

COLUMNS = ["First Name", "Last Name", "Linkedin", "Company", "Website", "Country", "Email", "Linkedin Company"]

# if output folder does not exist, create it
if not os.path.exists(OUTPUT_PATH):
    print("Creating output folder...")
    os.makedirs(OUTPUT_PATH)
    

def list(input_path):
    """Returns a list of all files in the input folder"""
    files = os.listdir(input_path)
    files = filter(lambda x: x.endswith('.csv'), files)
    return files


def remove_duplicate(df: pd.DataFrame):
    """Remove duplicate rows from dataframe over `Company` column"""
    # replace nan with empty string
    df['Company'] = df['Company'].fillna('')
    # split the company column by - and take the first part
    df['Company'] = df['Company'].apply(lambda x: x.split('-')[0])
    # drop duplicates and keep first
    df = df.drop_duplicates(subset=['Company'], keep='first')
    return df

def process():
    for file in list(INPUT_PATH):
        print("Processing file: {}".format(file))
        # read csv file, since it has no header, we will provide the column names
        df = pd.read_csv(os.path.join(INPUT_PATH, file), names=COLUMNS)
        # remove duplicate rows
        df = remove_duplicate(df)
        # save to csv
        df.to_csv(os.path.join(OUTPUT_PATH, file), index=False)
        print("File saved: {}".format(file))
        
if __name__ == "__main__":
    # start counter
    start = time.time()
    process()
    end = time.time()
    print("Done! Time taken: {}".format(end-start))