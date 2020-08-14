import pandas as pd
import os


def badwords(working_dir, search_terms):
    # read in excel with words to be searched in other datasets
    search_terms = pd.read_excel(working_dir + search_terms, usecols=[0])
    return search_terms


def files(infolder):
    # yield files from a folder of .xlsx type, one at a time
    for file in os.listdir(infolder):
        if file.endswith(".xlsx"):
            yield file


def remove_bad_cols(browser_search, working_dir, search_terms, terms_col, output_dir, terms_removed, terms_found):
    # function to return excel file with searchterms found and excel file with rows with search terms removed
    for path in files(browser_search):
        print(f'FILENAMES: ', path, '\n')
        search_df = pd.read_excel(browser_search + '/' + path, usecols=['Title', 'URL']).fillna(value='--- N/A ---')
        # search_df.drop_duplicates(inplace = True)
        list_words = []
        search_terms = badwords(working_dir, search_terms)
        for word in search_terms[terms_col]:
            for i in range(len(search_df)):
                for wordList in search_df.iloc[i, :]:
                    if word in wordList:
                        list_words.append(wordList)
        all_data = pd.DataFrame(list_words)
        headers = all_data.iloc[:, 0]  # Adds header to Badwords_Found.xlsx - all_data DataFrame revised
        new_df = pd.DataFrame({'search_terms': headers})  # Adds header to Badwords_Found.xlsx
        merged = df.merge(new_df, left_on='Title', right_on='search_terms')
        mod_df = merged.drop_duplicates(subset=['Title'], keep=False)
        mod_df.to_excel(output_dir + terms_removed, index=False)
        
        with pd.ExcelWriter(output_dir + terms_found, engine='xlsxwriter') as writer:
            merged.to_excel(writer, sheet_name='BadWords', startrow=1, header=False, index=False)
            workbook = writer.book
            worksheet = writer.sheets['BadWords']
            headers = workbook.add_format({  # Adds header formating to Badwords_Found.xlsx
                'bold': True,
                'text_wrap': True,
                'valign': 'top',
                'font_color': 'black',
                'fg_color': '#D7E4BC',
                'border': 1})
            for col_number, value in enumerate(
                    merged.columns.values):  # Iterates over / Writes format to Badwords_Found.xlsx
                worksheet.write(0, col_number + 0, value, headers)
            return writer.save()  # Saves .xlsx files as output


if __name__ == '__main__':
    
