import pandas as pd

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

def csv_to_apc(input_file_path, output_file_path):
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
  '''
  reviews = pd.read_csv(input_file_path) 
  list_of_quotes = list(reviews['quote'])
  length = len(list_of_quotes)
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



if __name__ == '__main__':
    input_file_path = '/content/panda_readable_larger_dataset - unlabeled.csv'
    reviews = pd.read_csv(input_file_path)
    reviews.info()