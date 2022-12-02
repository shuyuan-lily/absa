import pandas as pd
from findfile import find_files, find_cwd_file, find_cwd_files

def float_to_sent(n):
  '''
  Converts a floating point value in the spreadsheet entry
  to its corresponding sentiment.
  1 - negative
  2 - neutral
  3 - positive
  4 - conflict
  '''
  if n == 1.:
    return 'Negative'
  if n == 2.:
    return 'Neutral'
  if n == 3.:
    return 'Positive'
  if n == 4.:
    return 'Conflict'
  elif pd.isna(n) or pd.isnull(n):
    raise Exception("The sentiment is missing for this entity!")
  else:
    raise Exception("Sorry, no numbers other than 1, 2, 3, 4")

def csv_to_apc(input_file_path):
  '''
  1. Converts the csv file directly drawn from the quotations_with_entity spreadsheet
  into a readable ascii file that is suitable for training the Aspect Polarity 
  Classification (APC) task.
  2. Format: 
      sentence (with masked aspect term. mask: $T$)
      aspect
      sentiment
    example: 
      This situation spells disaster for the farmers and $T$.
      Swaziland Cotton Board
      Negative

  ** Note: this code may need to be improved. If there are multiple occurrences of the same 
     entity in the quotation, the code will not be able to handle this case, since it only 
     replaces the entity *once*. Either do some manual checking or improve the code. **

  ** We ignore 'conflict' class for the time being. This may be something to improve on. **
  '''
  reviews = pd.read_csv(input_file_path) 
  list_of_quotes = list(reviews['quote'])
  length = len(list_of_quotes)
  output_file_path = input_file_path.replace('apc_datasets', 'csv')

  with open(output_file_path, mode='w+') as dataset_file:
    for i in range(length):
      if pd.notna(reviews['entity 1'][i]):
        s = reviews['quote'][i].replace(reviews['entity 1'][i], '$T$')
        dataset_file.write(f"{s}\n{reviews['entity 1'][i]}\n{float_to_sent(reviews['sentiment 1'][i])}\n")
        if pd.notna(reviews['entity 2'][i]):
          s = reviews['quote'][i].replace(reviews['entity 2'][i], '$T$')
          dataset_file.write(f"{s}\n{reviews['entity 2'][i]}\n{float_to_sent(reviews['sentiment 2'][i])}\n")
          if pd.notna(reviews['entity 3'][i]):
            s = reviews['quote'][i].replace(reviews['entity 3'][i], '$T$')
            dataset_file.write(f"{s}\n{reviews['entity 3'][i]}\n{float_to_sent(reviews['sentiment 3'][i])}\n")
            if pd.notna(reviews['entity 4'][i]):
                s = reviews['quote'][i].replace(reviews['entity 4'][i], '$T$')
                dataset_file.write(f"{s}\n{reviews['entity 4'][i]}\n{float_to_sent(reviews['sentiment 4'][i])}\n")



if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="csv_to_apc")
    parser.add_argument('--input_csv_path', required=True, help='path to source csv data file')
    parser.add_argument('--verbose', action='store_true', help='if true, print the detailed information for debugging purpose')
    opt, unknown = parser.parse_known_args()

    if opt.verbose print(opt)

    input_csv_path = opt.input_csv_path
    # This line may look like:
    ##   input_csv_path = 'datasets/csv/001.larger_mbio/larger_mbio.train.csv'
    df = pd.read_csv(input_csv_path)
    if opt.verbose print(df.info())

    list_of_quotes = list(df['quote'])
    if opt.verbose print(list_of_quotes)

    csv_to_apc(input_csv_path)
